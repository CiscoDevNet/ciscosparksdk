# -*- coding: utf-8 -*-
"""CiscoSparkClient `Person` enhanced data model."""


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


import weakref

import ciscosparkapi

from ...utils import dict_from_items_with_values, SparkDateTime


class Person(ciscosparkapi.Person):
    """CiscoSparkClient `Person` enhanced data model."""

    def __init__(self, client, json):
        """Initialize a Person data object from a dictionary or JSON string.

        Args:
            client(CiscoSparkClient): The associated Spark client object.
            json(dict, basestring): Input dictionary or JSON string.

        Raises:
            TypeError: If the input object is not a dictionary or string.

        """
        self._client = weakref.proxy(client)
        super(Person, self).__init__(json)

    def update(self, displayName=None, firstName=None, lastName=None,
               avatar=None, orgId=None, roles=None, licenses=None,
               **request_parameters):
        """Update attributes for this person.

        Only an admin can update a person's details.

        Args:
            displayName(basestring): Full name of the person.
            firstName(basestring): First name of the person.
            lastName(basestring): Last name of the person.
            avatar(basestring): URL to the person's avatar in PNG format.
            orgId(basestring): ID of the organization to which this
                person belongs.
            roles(list): Roles of the person (list of strings containing
                the role IDs to be assigned to the person).
            licenses(list): Licenses allocated to the person (list of
                strings - containing the license IDs to be allocated to the
                person).
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            Person: A Person object with the updated details.

        Raises:
            TypeError: If the parameter types are incorrect.
            SparkApiError: If the Cisco Spark cloud returns an error.

        """
        person_details = self.json_data
        updates = dict_from_items_with_values(
            request_parameters,
            displayName=displayName,
            firstName=firstName,
            lastName=lastName,
            avatar=avatar,
            orgId=orgId,
            roles=roles,
            licenses=licenses,
        )

        person_details.update(updates)

        return self._client.api.people.update(
            personId=self.id, **person_details
        )

    def delete(self):
        """Remove this person from the system.

        Only an admin can remove a person.

        Raises:
            SparkApiError: If the Cisco Spark cloud returns an error.

        """
        self._client.api.people.delete(personId=self.id)

    # Enhanced Properties
    @property
    def created(self):
        """The date and time the message was created."""
        return SparkDateTime.strptime(super(Person, self).created())
