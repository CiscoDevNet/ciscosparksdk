# -*- coding: utf-8 -*-
"""CiscoSparkClient `Message` enhanced data model."""


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


class Message(ciscosparkapi.Message):
    """CiscoSparkClient `Message` enhanced data model."""

    def __init__(self, client, json):
        """Initialize a Message object from a dictionary or JSON string.

        Args:
            client(CiscoSparkClient): The associated Spark client object.
            json(dict, basestring): Input dictionary or JSON string.

        Raises:
            TypeError: If the input object is not a dictionary or string.

        """
        self._client = weakref.proxy(client)
        super(Message, self).__init__(json)

        self._mentionedPeople = None

    def delete(self):
        """Delete this message (aka. remove this person from the room).

        Raises:
            SparkApiError: If the Cisco Spark cloud returns an error.

        """
        self._client.api.messages.delete(messageId=self.id)

    # Enhanced Properties
    @property
    def created(self):
        """The date and time the message was created."""
        return SparkDateTime.strptime(super(Message, self).created())

    @property
    def mentionedPeople(self):
        """The list of people mentioned in this message."""
        if self._mentionedPeople is None:
            ids = super(Message, self).mentionedPeople()
            self._mentionedPeople = tuple(self._client.people.get_people(ids))

        return self._mentionedPeople

    # Rooms
    @property
    def room(self):
        """The room where this message is posted."""
        return self._client.rooms.get(roomId=self.roomId)

    # People
    @property
    def person(self):
        """The person who posted this message."""
        return self._client.people.get(personId=self.personId)
