# -*- coding: utf-8 -*-
"""Batteries added, community developed Python SDK for Cisco Spark."""


from __future__ import (
    absolute_import,
    division,
    print_function,
    unicode_literals,
)
from builtins import *
from past.builtins import basestring


__copyright__ = "Copyright (c) 2016-2018 Cisco Systems, Inc."
__license__ = "MIT"


from ._metadata import *
from ._version import get_versions
from .exceptions import *


__version__ = get_versions()['version']
