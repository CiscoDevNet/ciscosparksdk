# -*- coding: utf-8 -*-
"""ciscosparksdk exception classes."""


# Use future for Python v2 and v3 compatibility
from __future__ import (
    absolute_import,
    division,
    print_function,
    unicode_literals,
)


__author__ = "Chris Lunsford"
__author_email__ = "chrlunsf@cisco.com"
__copyright__ = "Copyright (c) 2017 Cisco Systems, Inc."
__license__ = "MIT"


from builtins import *
from past.builtins import basestring


class CiscoSparkSdkException(Exception):
    """Base class for all ciscosparksdk package exceptions."""
    pass


class AccessTokenError(CiscoSparkSdkException):
    """Raised when an invalid access token has been provided."""
    pass
