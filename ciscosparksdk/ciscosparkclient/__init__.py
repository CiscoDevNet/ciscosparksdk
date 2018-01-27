# -*- coding: utf-8 -*-
"""The community developed 🐍 CiscoSparkClient."""


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


import os

from ciscosparkapi import (
    ACCESS_TOKEN_ENVIRONMENT_VARIABLE,
    DEFAULT_BASE_URL,
    DEFAULT_SINGLE_REQUEST_TIMEOUT,
    DEFAULT_WAIT_ON_RATE_LIMIT,
    CiscoSparkAPI,
)

from ..exceptions import AccessTokenError
from ..utils import check_type
from .rooms import Rooms


class CiscoSparkClient(object):
    """The community developed 🐍 CiscoSparkClient."""

    def __init__(self, access_token=None, base_url=DEFAULT_BASE_URL,
                 single_request_timeout=DEFAULT_SINGLE_REQUEST_TIMEOUT,
                 wait_on_rate_limit=DEFAULT_WAIT_ON_RATE_LIMIT):
        """Initialize a new CiscoSparkClient.

        An access token must be used when interacting with the Cisco Spark
        APIs. The client supports two methods for you to provide that access
        token:

          1. You may manually specify the access token via the access_token
             parameter, when creating a new CiscoSparkAPI object.

          2. If an access_token argument is not supplied, the client checks
             for a SPARK_ACCESS_TOKEN environment variable.

        An AccessTokenError is raised if an access token is not provided via
        one of these two methods.

        Args:
            access_token(basestring): The access token to be used for API
                calls to the Cisco Spark service.  Defaults to checking for a
                SPARK_ACCESS_TOKEN environment variable.
            base_url(basestring): The base URL to be prefixed to the
                individual API endpoint suffixes.
                Defaults to DEFAULT_BASE_URL.
            single_request_timeout(int): Timeout (in seconds) for RESTful HTTP
                requests. Defaults to DEFAULT_SINGLE_REQUEST_TIMEOUT.
            wait_on_rate_limit(bool): Enables or disables automatic rate-limit
                handling. Defaults to DEFAULT_WAIT_ON_RATE_LIMIT.

        Returns:
            CiscoSparkClient: A new CiscoSparkClient object.

        Raises:
            TypeError: If the parameter types are incorrect.
            AccessTokenError: If an access token is not provided via the
                access_token argument or SPARK_ACCESS_TOKEN environment
                variable.

        """
        check_type(access_token, basestring)
        check_type(base_url, basestring)
        check_type(single_request_timeout, int)
        check_type(wait_on_rate_limit, bool)

        env_access_token = os.environ.get(ACCESS_TOKEN_ENVIRONMENT_VARIABLE)
        access_token = access_token or env_access_token
        if not access_token:
            raise AccessTokenError(
                "You must provide an Spark access token to interact with the "
                "Cisco Spark APIs, either via a SPARK_ACCESS_TOKEN "
                "environment variable or via the access_token argument."
            )

        self.api = CiscoSparkAPI(
            access_token=access_token,
            base_url=base_url,
            single_request_timeout=single_request_timeout,
            wait_on_rate_limit=wait_on_rate_limit,
        )

        self.rooms = Rooms(client=self)

    @property
    def access_token(self):
        """The access token used for API calls to the Cisco Spark service."""
        return self.api.access_token

    @property
    def base_url(self):
        """The base URL prefixed to the individual API endpoint suffixes."""
        return self.api.base_url

    @property
    def single_request_timeout(self):
        """Timeout (in seconds) for an single HTTP request."""
        return self.api.single_request_timeout

    @property
    def wait_on_rate_limit(self):
        """Automatic rate-limit handling enabled / disabled."""
        return self.api.wait_on_rate_limit
