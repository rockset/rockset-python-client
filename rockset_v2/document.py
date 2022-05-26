import datetime
import geojson

# all Rockset data types
DATATYPE_META = "__rockset_type"
DATATYPE_INT = "int"
DATATYPE_FLOAT = "float"
DATATYPE_BOOL = "bool"
DATATYPE_STRING = "string"
DATATYPE_BYTES = "bytes"
DATATYPE_NULL = "null"
DATATYPE_NULL_TYPE = "null_type"
DATATYPE_ARRAY = "array"
DATATYPE_OBJECT = "object"
DATATYPE_DATE = "date"
DATATYPE_DATETIME = "datetime"
DATATYPE_TIME = "time"
DATATYPE_TIMESTAMP = "timestamp"
DATATYPE_MONTH_INTERVAL = "month_interval"
DATATYPE_MICROSECOND_INTERVAL = "microsecond_interval"
DATATYPE_GEOGRAPHY = "geography"


def _date_fromisoformat(s):
    dt = datetime.datetime.strptime(s, "%Y-%m-%d")
    return dt.date()


def _time_fromisoformat(s):
    try:
        dt = datetime.datetime.strptime(s, "%H:%M:%S.%f")
    except ValueError:
        dt = datetime.datetime.strptime(s, "%H:%M:%S")
    return datetime.time(
        hour=dt.hour, minute=dt.minute, second=dt.second, microsecond=dt.microsecond
    )


def _datetime_fromisoformat(s):
    try:
        dt = datetime.datetime.strptime(s, "%Y-%m-%dT%H:%M:%S.%f")
    except ValueError:
        dt = datetime.datetime.strptime(s, "%Y-%m-%dT%H:%M:%S")
    return dt


def _timedelta_from_microseconds(us):
    return datetime.timedelta(microseconds=us)


class Document(dict):
    """Represents a single record or row in query results.

    This is a sub-class of dict. So, treat this object as a dict
    for all practical purposes.

    Only the constructor is overridden to handle the type adaptations
    shown in the table above.
    """

    def __init__(self, *args, **kwargs):
        super(Document, self).__init__(*args, **kwargs)
        for k in self.keys():
            if not isinstance(self[k], dict):
                continue
            if DATATYPE_META not in self[k]:
                continue
            t = self[k][DATATYPE_META].lower()
            v = self[k]["value"]
            if t == DATATYPE_DATE:
                self[k] = _date_fromisoformat(v)
            elif t == DATATYPE_TIME:
                self[k] = _time_fromisoformat(v)
            elif t == DATATYPE_DATETIME:
                self[k] = _datetime_fromisoformat(v)
            elif t == DATATYPE_MICROSECOND_INTERVAL:
                self[k] = _timedelta_from_microseconds(v)
            elif t == DATATYPE_GEOGRAPHY:
                self[k] = geojson.GeoJSON.to_instance(v)

    def _py_type_to_rs_type(self, v):
        if isinstance(v, bool):
            # check for bool before int, since bools are ints too
            return DATATYPE_BOOL
        elif isinstance(v, int):
            return DATATYPE_INT
        elif isinstance(v, float):
            return DATATYPE_FLOAT
        elif isinstance(v, str):
            return DATATYPE_STRING
        elif isinstance(v, bytes):
            return DATATYPE_BYTES
        elif isinstance(v, type(None)):
            return DATATYPE_NULL
        elif isinstance(v, list):
            return DATATYPE_ARRAY
        elif isinstance(v, datetime.datetime):
            # check for datetime first, since datetimes are dates too
            return DATATYPE_DATETIME
        elif isinstance(v, datetime.date):
            return DATATYPE_DATE
        elif isinstance(v, datetime.time):
            return DATATYPE_TIME
        elif isinstance(v, datetime.timedelta):
            return DATATYPE_MICROSECOND_INTERVAL
        elif isinstance(v, geojson.GeoJSON):
            return DATATYPE_GEOGRAPHY
        elif isinstance(v, dict):  # keep this in the end
            if DATATYPE_META not in v:
                return DATATYPE_OBJECT
            return v[DATATYPE_META].lower()

    def fields(self, columns=None):
        columns = columns or sorted(self)
        return [
            {"name": c, "type": self._py_type_to_rs_type(self.get(c, type(None)))}
            for c in columns
        ]
