# -*- coding: utf-8 -*-
"""CiscoSparkClient licenses interface."""


from __future__ import (
    absolute_import,
    division,
    print_function,
    unicode_literals,
)
from builtins import *


__copyright__ = "Copyright (c) 2016-2018 Cisco Systems, Inc."
__license__ = "MIT"


import functools
import weakref

import ciscosparkapi

from ..utils import filter_by_attribute


class Licenses(object):
    """CiscoSparkClient licenses interface."""

    def __init__(self, client):
        """Initialize the client licenses interface.

        Args:
            client(CiscoSparkClient): The parent client object.

        """
        self.client = weakref.proxy(client)

    def __call__(self, where=None, equals=None, starts_with=None,
                 contains=None, ends_with=None, case_sensitive=True,
                 **request_parameters):
        """Filter the returned licenses.

        Args:
            where(basestring): The attribute name to filter on.
            equals(basestring): The attribute value must match this string
                exactly.
            starts_with(basestring): The attribute value must start with this
                prefix.
            contains(basestring): The attribute value must contain this
                substring.
            ends_with(basestring): The attribute value must end with this
                suffix.
            case_sensitive(bool): Matches should be case sensitive.
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            GeneratorContainer: A GeneratorContainer yielding all of the
                matched licenses.

        Raises:
            TypeError: If the parameter types are incorrect.

        """
        licenses = self.client.api.licenses.list(
            **request_parameters
        )
        if where:
            return filter_by_attribute(
                licenses, where=where, equals=equals,
                starts_with=starts_with, contains=contains,
                ends_with=ends_with, case_sensitive=case_sensitive
            )
        else:
            return licenses

    def __iter__(self):
        """Default `licenses` iterable."""
        return iter(self.client.api.licenses.list())

    def __getitem__(self, item):
        """Make default `licenses` iterable subscriptable."""
        return self.client.api.licenses.list()[item]

    @functools.wraps(ciscosparkapi.api.licenses.LicensesAPI.get)
    def get(self, *args, **kwargs):
        """Expose the get() method."""
        return self.client.api.licenses.get(*args, **kwargs)
