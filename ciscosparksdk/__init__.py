# -*- coding: utf-8 -*-
"""Batteries added, community developed Python SDK for Cisco Spark."""


# Use future for Python v2 and v3 compatibility
from __future__ import (
    absolute_import,
    division,
    print_function,
    unicode_literals,
)
from builtins import *
from past.builtins import basestring

from ciscosparksdk.exceptions import ciscosparksdkException


# Versioneer version control
from ._version import get_versions
__version__ = get_versions()['version']
del get_versions


# Metadata, license and copyright
__author__ = "Chris Lunsford"
__author_email__ = "chrlunsf@cisco.com"
__copyright__ = "Copyright (c) 2017 Cisco Systems, Inc."
__license__ = "MIT"
