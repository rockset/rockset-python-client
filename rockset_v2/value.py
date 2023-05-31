import collections

_CustomEncoder = collections.namedtuple("_CustomEncoder", ["type_id", "encoder"])

_CustomDecoder = collections.namedtuple("_CustomDecoder", ["py_type", "decoder"])

_standard_types = frozenset((bool, int, float, str, bytes, list, dict))


class ValueCodec(object):
    def __init__(self):
        self._decoders = {
            None: (lambda x: type(None), lambda x: None),
            "bool_value": (lambda x: bool, lambda x: x.bool_value),
            "int_value": (lambda x: int, lambda x: x.int_value),
            "float_value": (lambda x: float, lambda x: x.float_value),
            "string_value": (lambda x: str, lambda x: x.string_value),
            "bytes_value": (lambda x: bytes, lambda x: x.bytes_value),
            "array_value": (lambda x: list, self._decode_array),
            "object_value": (lambda x: dict, self._decode_object),
            "custom_value": (self._py_type_custom, self._decode_custom),
            "null_value": (lambda x: type(None), lambda x: None),
        }
        self._custom_encoders = {}
        self._custom_decoders = {}

    def add_custom(self, type_id, py_type, encoder, decoder):
        if not isinstance(py_type, type):
            raise TypeError(
                "Custom types must be standard Python types "
                "(metaclasses not supported)"
            )
        if py_type in _standard_types:
            raise TypeError(
                "May not register custom type for Python standard "
                "type {}".format(py_type)
            )
        if not isinstance(type_id, int):
            raise TypeError("Type ids must be integers")
        if py_type in self._custom_encoders:
            raise KeyError("Duplicate entry for Python type {}".format(py_type))
        if type_id in self._custom_decoders:
            raise KeyError("Duplicate entry for type id {}".format(type_id))

        self._custom_encoders[py_type] = _CustomEncoder(
            type_id=type_id, encoder=encoder
        )

        self._custom_decoders[type_id] = _CustomDecoder(
            py_type=py_type, decoder=decoder
        )

    def _decode_array(self, x):
        return [self.decode(v) for v in x.array_value.value]

    def _decode_object(self, x):
        return {v.key: self.decode(v.value) for v in x.object_value.fields}

    def _decode_custom(self, x):
        cv = x.custom_value
        dec = self._custom_decoders.get(cv.type)
        if not dec:
            raise KeyError(
                "No custom decoder registered for type id " "{}".format(cv.type)
            )
        obj = dec.decoder(cv.encoded)
        if type(obj) != dec.py_type:
            raise TypeError(
                "Custom decoder produced a Python object of type "
                "{}, expecting {}".format(type(obj), dec.py_type)
            )
        return obj

    def _py_type_custom(self, x):
        cv = x.custom_value
        dec = self._custom_decoders.get(cv.type)
        if not dec:
            raise KeyError(
                "No custom decoder registered for type id " "{}".format(cv.type)
            )
        return dec.py_type

    def decode(self, x):
        # if isinstance(x, Value):
        #     return self._decoders[x.WhichOneof("value_union")][1](x)
        return x

    def py_type(self, x):
        # if isinstance(x, Value):
        #     return self._decoders[x.WhichOneof("value_union")][0](x)
        return type(x)


_default_codec = ValueCodec()


def decode(x):
    return _default_codec.decode(x)


def py_type(x):
    return _default_codec.py_type(x)


__all__ = [
    "ValueCodec",
    "encode",
    "decode",
    "py_type",
]
