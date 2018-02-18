# -*- coding: utf-8 -*-
"""CiscoSparkClient people interface."""


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
from itertools import islice
import weakref

import ciscosparkapi

from ..utils import filter_by_attribute


MAX_PEOPLE_IDS_PER_REQUEST = 85


class People(object):
    """CiscoSparkClient people interface."""

    def __init__(self, client):
        """Initialize the client people interface.

        Args:
            client(CiscoSparkClient): The parent client object.

        """
        self._client = weakref.proxy(client)

    def __call__(self, where=None, equals=None, starts_with=None,
                 contains=None, ends_with=None, case_sensitive=True,
                 **request_parameters):
        """Filter the returned people.

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
                matched people.

        Raises:
            TypeError: If the parameter types are incorrect.

        """
        people = self._client.api.people.list(
            **request_parameters
        )
        if where:
            return filter_by_attribute(
                people, where=where, equals=equals,
                starts_with=starts_with, contains=contains,
                ends_with=ends_with, case_sensitive=case_sensitive
            )
        else:
            return people

    def __iter__(self):
        """Default `people` iterable."""
        return iter(self._client.api.people.list())

    def __getitem__(self, item):
        """Make default `people` iterable subscriptable."""
        return self._client.api.people.list()[item]

    @property
    def me(self):
        """The details of the person accessing the API."""
        return self._client.api.people.me()

    @functools.wraps(ciscosparkapi.api.people.PeopleAPI.create)
    def create(self, *args, **kwargs):
        """Expose the create() method."""
        return self._client.api.people.create(*args, **kwargs)

    @functools.wraps(ciscosparkapi.api.people.PeopleAPI.get)
    def get(self, *args, **kwargs):
        """Expose the get() method."""
        return self._client.api.people.get(*args, **kwargs)

    def get_people(self, ids_iterable):
        """Get the people objects for each of the IDs in the iterable.

        Args:
            ids_iterable(iterable): An iterable containing the person IDs of
                the people objects to be retrieved.

        Raises:
            SparkApiError: If the Cisco Spark cloud returns an error.

        """
        # Get people objects in batches of size MAX_PEOPLE_IDS_PER_REQUEST
        i = iter(ids_iterable)
        batch = tuple(islice(i, stop=MAX_PEOPLE_IDS_PER_REQUEST))
        while batch:
            for person in self._client.people.get(id=",".join(batch)):
                yield person
            batch = tuple(islice(i, stop=MAX_PEOPLE_IDS_PER_REQUEST))
