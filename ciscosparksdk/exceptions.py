# -*- coding: utf-8 -*-
"""ciscosparksdk exception classes."""


# Use future for Python v2 and v3 compatibility
from __future__ import (
    absolute_import,
    division,
    print_function,
    unicode_literals,
)
from builtins import *
from past.builtins import basestring


# Metadata, license and copyright
__author__ = "Chris Lunsford"
__author_email__ = "chrlunsf@cisco.com"
__copyright__ = "Copyright (c) 2017 Cisco Systems, Inc."
__license__ = "MIT"


class ciscosparksdkException(Exception):
    """Base class for all ciscosparksdk package exceptions."""

    def __init__(self, *args, **kwargs):
        super(ciscosparksdkException, self).__init__(*args, **kwargs)
