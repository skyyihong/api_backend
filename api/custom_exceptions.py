from rest_framework.views import exception_handler
from rest_framework.response import Response


def custom_exception_handler(exc, context):
    res = exception_handler(exc, context)
    if res is None:
        if isinstance(exc, ZeroDivisionError):
            res = Response({'detail': "0不能为除数"})
        elif isinstance(exc, Exception):
            res = Response({'detail': exc.__str__()})
    return res
