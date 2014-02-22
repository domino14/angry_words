"""Utility library for responses."""
import json
from django.http import HttpResponse


class HTTP_STATUS:

    """Defines different HTTP stati."""

    OK = 200
    BAD_REQUEST = 400
    UNAUTHORIZED = 401
    FORBIDDEN = 403
    NOT_FOUND = 404
    METHOD_NOT_ALLOWED = 405
    INTERNAL_ERROR = 500
    NOT_IMPLEMENTED = 501

CONTENT_TYPE = 'application/javascript; charset=utf-8'


def response(obj, status=HTTP_STATUS.OK):
    """
    Return an HttpResponse.

    :param obj The object to return; it is JSON dumped.
    :param status The HTTP status, defaults to 200 (OK).

    """
    resp = HttpResponse(json.dumps(obj, ensure_ascii=False),
                        content_type=CONTENT_TYPE,
                        status=status)
    return resp


def error_response(msg, status=HTTP_STATUS.BAD_REQUEST):
    """
    Return an error HTTP response.

    :param msg A string with the error message.
    :param status The HTTP status.

    """
    resp = HttpResponse(json.dumps({'error': msg}),
                        content_type=CONTENT_TYPE,
                        status=status)
    return resp
