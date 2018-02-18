# -*- coding: utf-8 -*-
"""CiscoSparkClient `Membership` enhanced data model."""


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

from ...utils import SparkDateTime


class Membership(ciscosparkapi.Membership):
    """CiscoSparkClient `Membership` enhanced data model."""

    def __init__(self, client, json):
        """Initialize a Membership object from a dictionary or JSON string.

        Args:
            client(CiscoSparkClient): The associated Spark client object.
            json(dict, basestring): Input dictionary or JSON string.

        Raises:
            TypeError: If the input object is not a dictionary or string.

        """
        self._client = weakref.proxy(client)
        super(Membership, self).__init__(json)

    def update(self, isModerator=None, **request_parameters):
        """Update attributes for this membership.

        Args:
            isModerator(bool): Set to True to make the person a room moderator.
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            Membership: A Membership object with the updated details.

        Raises:
            TypeError: If the parameter types are incorrect.
            SparkApiError: If the Cisco Spark cloud returns an error.

        """
        return self._client.api.memberships.update(
            membershipId=self.id, isModerator=isModerator, **request_parameters
        )

    def delete(self):
        """Delete this membership (aka. remove this person from the room).

        Raises:
            SparkApiError: If the Cisco Spark cloud returns an error.

        """
        self._client.api.memberships.delete(membershipId=self.id)

    # Enhanced Properties
    @property
    def created(self):
        """The date and time the message was created."""
        return SparkDateTime.strptime(super(Membership, self).created())

    # Organizations
    @property
    def organization(self):
        """The organization this membership is associated with."""
        return self._client.organizations.get(orgId=self.personOrgId)

    # Rooms
    @property
    def room(self):
        """The room this membership is associated with."""
        return self._client.rooms.get(roomId=self.roomId)

    # People
    @property
    def person(self):
        """The person this membership is associated with."""
        return self._client.people.get(personId=self.personId)
