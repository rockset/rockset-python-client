load("@py_deps//:requirements.bzl", "requirement")

py_library(
    name="client",
    srcs=glob(["**/*.py"]),
    visibility=["//visibility:public"],
    deps=[requirement("setuptools"), requirement("six"), requirement("certifi"), requirement("python_dateutil"), requirement("urllib3")],
    imports=["."],
)