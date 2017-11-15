# -*- coding: utf-8 -*-
"""Batteries added, community developed Python SDK for Cisco Spark."""


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

from .exceptions import AccessTokenError, CiscoSparkSdkException

from .sparkclient import SparkClient

# Versioneer version control
from ._version import get_versions
__version__ = get_versions()['version']
del get_versions
