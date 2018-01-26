# -*- coding: utf-8 -*-
"""Package Exceptions."""


from __future__ import (
    absolute_import,
    division,
    print_function,
    unicode_literals,
)
from builtins import *


__copyright__ = "Copyright (c) 2016-2018 Cisco and/or its affiliates."
__license__ = "MIT"


class CiscoSparkSdkException(Exception):
    """Base class for all ciscosparksdk package exceptions."""
    pass


class AccessTokenError(CiscoSparkSdkException):
    """Raised when an incorrect Cisco Spark Access Token has been provided."""
    pass
