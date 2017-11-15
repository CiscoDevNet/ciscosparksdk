# -*- coding: utf-8 -*-
"""Python Spark Client."""


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
__all__ = ["SparkClient"]


from builtins import *
from past.builtins import basestring

import os
import weakref

from ciscosparkapi import (
    ACCESS_TOKEN_ENVIRONMENT_VARIABLE,
    CiscoSparkAPI,
    ciscosparkapiException,
    DEFAULT_BASE_URL,
    DEFAULT_SINGLE_REQUEST_TIMEOUT,
    DEFAULT_WAIT_ON_RATE_LIMIT,
)

from ciscosparkapi.utils import check_type

from .exceptions import AccessTokenError


class _Rooms(object):
    """Python Spark Client | Rooms Interface."""

    def __init__(self, client):
        """Initialize the rooms interface object."""
        self._client = weakref.proxy(client)

    # Convenience iterators / generators
    def __iter__(self):
        """All Rooms - Iterate through all (group and direct) rooms."""
        return iter(self._client.api.rooms.list())

    @property
    def group_rooms(self):
        """Group Rooms - Iterate through all the group rooms."""
        return self._client.api.rooms.list(type='group')

    @property
    def direct_rooms(self):
        """Direct Rooms - Iterate through all the direct rooms."""
        return self._client.api.rooms.list(type='direct')


class SparkClient(object):
    """Python Spark Client."""

    def __init__(self, access_token=None, base_url=DEFAULT_BASE_URL,
                 single_request_timeout=DEFAULT_SINGLE_REQUEST_TIMEOUT,
                 wait_on_rate_limit=DEFAULT_WAIT_ON_RATE_LIMIT):
        """Initialize a new Spark Client object.

        An access token must be used when interacting with the Cisco Spark API.
        This package supports two methods for you to provide that access token:

          1. You may manually specify the access token via the access_token
             argument, when creating a new CiscoSparkAPI object.

          2. If an access_token argument is not supplied, the package checks
             for a SPARK_ACCESS_TOKEN environment variable.

        An AccessTokenError is raised if an access token is not provided via
        one of these two methods.

        Args:
            access_token(basestring): The access token to be used for API
                calls to the Cisco Spark service.  Defaults to checking for a
                SPARK_ACCESS_TOKEN environment variable.
            base_url(basestring): The base URL to be prefixed to the
                individual API endpoint suffixes.
                Defaults to ciscosparkapi.DEFAULT_BASE_URL.
            single_request_timeout(int): Timeout (in seconds) for RESTful HTTP
                requests. Defaults to
                ciscosparkapi.DEFAULT_SINGLE_REQUEST_TIMEOUT.
            wait_on_rate_limit(bool): Enables or disables automatic rate-limit
                handling. Defaults to ciscosparkapi.DEFAULT_WAIT_ON_RATE_LIMIT.

        Returns:
            CiscoSparkAPI: A new CiscoSparkAPI object.

        Raises:
            TypeError: If the parameter types are incorrect.
            AccessTokenError: If an access token is not provided via the
                access_token argument or SPARK_ACCESS_TOKEN environment
                variable.

        """
        check_type(access_token, basestring)
        check_type(base_url, basestring)
        # check_type(single_request_timeout, int)
        check_type(wait_on_rate_limit, bool)

        env_access_token = os.environ.get(ACCESS_TOKEN_ENVIRONMENT_VARIABLE)
        access_token = access_token or env_access_token
        if not access_token:
            error_message = "You must provide an Spark access token to " \
                            "interact with the Cisco Spark APIs, either via " \
                            "a SPARK_ACCESS_TOKEN environment variable " \
                            "or via the access_token argument."
            raise AccessTokenError(error_message)

        self.api = CiscoSparkAPI(
            access_token=access_token,
            base_url=base_url,
            single_request_timeout=single_request_timeout,
            wait_on_rate_limit=wait_on_rate_limit,
        )

        self.rooms = _Rooms(self)
