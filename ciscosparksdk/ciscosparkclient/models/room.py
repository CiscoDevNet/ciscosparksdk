# -*- coding: utf-8 -*-
"""CiscoSparkClient `Room` enhanced data model."""


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

from ...utils import check_type
from .person import Person


class Room(ciscosparkapi.Room):
    """CiscoSparkClient `Room` enhanced data model."""

    def __init__(self, client, json):
        """Initialize a Room data object from a dictionary or JSON string.

        Args:
            client(CiscoSparkClient): The associated Spark client object.
            json(dict, basestring): Input dictionary or JSON string.

        Raises:
            TypeError: If the input object is not a dictionary or string.

        """
        self._client = weakref.proxy(client)
        super(Room, self).__init__(json)

    def update(self, title=None, **request_parameters):
        """Update the attributes of this room.

        Args:
            title(basestring): A user-friendly name for the room.
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            Room: A Room object with the updated Spark room details.

        Raises:
            TypeError: If the parameter types are incorrect.
            SparkApiError: If the Cisco Spark cloud returns an error.

        """
        return self._client.api.rooms.update(
            roomId=self.id, title=title, **request_parameters
        )

    def delete(self):
        """Delete this room.

        Raises:
            SparkApiError: If the Cisco Spark cloud returns an error.

        """
        self._client.api.rooms.delete(roomId=self.id)

    # Memberships
    @property
    def memberships(self):
        """GeneratorContainer yielding the memberships for this room."""
        return self._client.api.memberships.list(roomId=self.id)

    def list_memberships(self, personId=None, personEmail=None,
                         **request_parameters):
        """List room memberships.

        Use query parameters to filter the response.

        Use either `personId` or `personEmail` to filter the results.

        This method supports Cisco Spark's implementation of RFC5988 Web
        Linking to provide pagination support.  It returns a generator
        container that incrementally yields all memberships returned by the
        query.  The generator will automatically request additional 'pages' of
        responses from Spark as needed until all responses have been returned.
        The container makes the generator safe for reuse.  A new API call will
        be made, using the same parameters that were specified when the
        generator was created, every time a new iterator is requested from the
        container.

        Args:
            personId(basestring): Limit results to a specific person, by ID.
            personEmail(basestring): Limit results to a specific person, by
                email address.
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            GeneratorContainer: A GeneratorContainer which, when iterated,
                yields the memberships returned by the Cisco Spark query.

        Raises:
            TypeError: If the parameter types are incorrect.
            SparkApiError: If the Cisco Spark cloud returns an error.

        """
        self._client.api.memberships.list(
            roomId=self.id, personId=personId, personEmail=personEmail,
            **request_parameters
        )

    def add_person(self, person=None, personId=None, personEmail=None,
                   isModerator=False, **request_parameters):
        """Add a person to the room.

        Args:
            person(Person): The person to be added to the room.
            personId(basestring): The ID of the person to be added to the room.
            personEmail(basestring): The e-mail address of the person to be
                added to the room.
            isModerator(bool): Set to True to make the person a room moderator.
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            Membership: The Membership object of the newly created room
                membership.

        Raises:
            TypeError: If the parameter types are incorrect, or if a required
                parameter has been omitted.
            SparkApiError: If the Cisco Spark cloud returns an error.

        """
        check_type(person, Person)

        if person:
            personId = person.id

        if personId:
            return self._client.api.memberships.create(
                roomId=self.id, personId=personId, isModerator=isModerator,
                **request_parameters
            )
        elif personEmail:
            return self._client.api.memberships.create(
                roomId=self.id, personEmail=personEmail,
                isModerator=isModerator, **request_parameters
            )
        else:
            raise TypeError(
                "You must provide the person object, ID or e-mail address of "
                "the person to be added to the room."
            )

    # Messages
    @property
    def messages(self):
        """GeneratorContainer yielding the messages in this room."""
        return self._client.api.messages.list(roomId=self.id)

    def list_messages(self, mentionedPeople=None, before=None,
                      beforeMessage=None, **request_parameters):
        """Lists messages in this room.

        The list API sorts the messages in descending order by creation date.

        This method supports Cisco Spark's implementation of RFC5988 Web
        Linking to provide pagination support.  It returns a generator
        container that incrementally yields all messages returned by the
        query.  The generator will automatically request additional 'pages' of
        responses from Spark as needed until all responses have been returned.
        The container makes the generator safe for reuse.  A new API call will
        be made, using the same parameters that were specified when the
        generator was created, every time a new iterator is requested from the
        container.

        Args:
            mentionedPeople(basestring): List messages where the caller is
                mentioned by specifying "me" or the caller `personId`.
            before(basestring): List messages sent before a date and time, in
                ISO8601 format.
            beforeMessage(basestring): List messages sent before a message,
                by ID.
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            GeneratorContainer: A GeneratorContainer which, when iterated,
                yields the messages returned by the Cisco Spark query.

        Raises:
            TypeError: If the parameter types are incorrect.
            SparkApiError: If the Cisco Spark cloud returns an error.

        """
        return self._client.api.messages.list(
            roomId=self.id, mentionedPeople=mentionedPeople, before=before,
            beforeMessage=beforeMessage, **request_parameters
        )

    def post_message(self, text=None, markdown=None, files=None,
                     **request_parameters):
        """Post a message, and optionally a attachment, to this room.

        The files parameter is a list, which accepts multiple values to allow
        for future expansion, but currently only one file may be included with
        the message.

        Args:
            text(basestring): The message, in plain text. If `markdown` is
                specified this parameter may be optionally used to provide
                alternate text for UI clients that do not support rich text.
            markdown(basestring): The message, in markdown format.
            files(list): A list of public URL(s) or local path(s) to files to
                be posted into the room. Only one file is allowed per message.
                Uploaded files are automatically converted into a format that
                all Spark clients can render.
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            Message: A Message object with the details of the created message.

        Raises:
            TypeError: If the parameter types are incorrect.
            SparkApiError: If the Cisco Spark cloud returns an error.
            ValueError: If the files parameter is a list of length > 1, or if
                the string in the list (the only element in the list) does not
                contain a valid URL or path to a local file.

        """
        return self._client.api.messages.create(
            roomId=self.id, text=text, markdown=markdown, files=files,
            **request_parameters
        )
