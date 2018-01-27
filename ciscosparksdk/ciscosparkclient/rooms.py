# -*- coding: utf-8 -*-
"""CiscoSparkClient rooms interface."""


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


class Rooms(object):
    """CiscoSparkClient rooms interface."""

    def __init__(self, client):
        """Initialize the client rooms interface.

        Args:
            client(CiscoSparkClient): The parent client object.

        """
        self.client = weakref.proxy(client)

    def __call__(self, where=None, equals=None, starts_with=None,
                 contains=None, ends_with=None, case_sensitive=True,
                 sortBy='lastactivity', **request_parameters):
        """Filter and sort the returned rooms.

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
            sortBy(basestring): Sort results by room ID (`id`), most recent
                activity (`lastactivity`), or most recently created
                (`created`).
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            GeneratorContainer: A GeneratorContainer yielding all of the
                matched rooms.

        Raises:
            TypeError: If the parameter types are incorrect.

        """
        rooms = self.client.api.rooms.list(sortBy=sortBy, **request_parameters)
        if where is not None:
            return filter_by_attribute(
                rooms, where=where, equals=equals, starts_with=starts_with,
                contains=contains, ends_with=ends_with,
                case_sensitive=case_sensitive
            )
        else:
            return rooms

    def __iter__(self):
        """Default `rooms` iterable.

        Iterate through all rooms sorted by by lastActivity.

        """
        return iter(self.client.api.rooms.list(sortBy='lastactivity'))

    def __getitem__(self, item):
        """Make default `rooms` iterable subscriptable."""
        return self.client.api.rooms.list(sortBy='lastactivity')[item]

    @property
    def direct(self):
        """Direct rooms iterable; sorted by last activity."""
        return self.client.api.rooms.list(type='direct', sortBy='lastactivity')

    @property
    def group(self):
        """Group rooms iterable; sorted by last activity."""
        return self.client.api.rooms.list(type='group', sortBy='lastactivity')

    @functools.wraps(ciscosparkapi.api.rooms.RoomsAPI.create)
    def create(self, *args, **kwargs):
        """Expose the create() method."""
        return self.client.api.rooms.create(*args, **kwargs)

    @functools.wraps(ciscosparkapi.api.rooms.RoomsAPI.get)
    def get(self, *args, **kwargs):
        """Expose the get() method."""
        return self.client.api.rooms.get(*args, **kwargs)
