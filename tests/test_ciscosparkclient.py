# -*- coding: utf-8 -*-
"""Test suite for the CiscoSparkClient top-level class interfaces."""


import os
import random

import pytest

from .context import ciscosparksdk


# Fixtures
@pytest.fixture(scope="session")
def access_token():
    """The Cisco Spark Access Token to be used for all API calls."""
    return os.environ.get(ciscosparksdk.ACCESS_TOKEN_ENVIRONMENT_VARIABLE)


@pytest.fixture
def unset_access_token(access_token):
    """Temporarily unset the Access Token environment variable."""
    del os.environ[ciscosparksdk.ACCESS_TOKEN_ENVIRONMENT_VARIABLE]
    yield access_token
    os.environ[ciscosparksdk.ACCESS_TOKEN_ENVIRONMENT_VARIABLE] = access_token


@pytest.fixture(scope="session")
def client():
    """The CiscoSparkClient instance to be used by the test suite."""
    return ciscosparksdk.CiscoSparkClient()


# Tests
def test_creating_a_client_instance_with_no_parameters():
    """The initializer should use default values and environment variables.

    This should succeed as long as the necessary environment variables have
    been provided.

    """
    ciscosparksdk.CiscoSparkClient()


def test_creating_a_client_with_access_token_parameter(unset_access_token):
    """Create a client by providing the access token as a parameter."""
    ciscosparksdk.CiscoSparkClient(access_token=unset_access_token)


def test_not_providing_an_access_token_raises_an_error(unset_access_token):
    """Not providing an access token should raise an error."""
    with pytest.raises(ciscosparksdk.AccessTokenError):
        ciscosparksdk.CiscoSparkClient()


def test_default_base_url(client):
    """The client should use the package default."""
    assert client.base_url == ciscosparksdk.DEFAULT_BASE_URL


def test_custom_base_url():
    """The client should use the provided value."""
    custom_url = "https://spark.cmlccie.com/v1/"
    assert custom_url != ciscosparksdk.DEFAULT_BASE_URL

    client = ciscosparksdk.CiscoSparkClient(base_url=custom_url)
    assert client.base_url == custom_url


def test_default_single_request_timeout(client):
    """The client should use the package default."""
    assert client.single_request_timeout == \
           ciscosparksdk.DEFAULT_SINGLE_REQUEST_TIMEOUT


def test_custom_single_request_timeout():
    """The client should use the provided value."""
    default_timeout = ciscosparksdk.DEFAULT_SINGLE_REQUEST_TIMEOUT
    custom_timeout = random.randint(default_timeout+1, 86400)
    assert custom_timeout != default_timeout

    client = ciscosparksdk.CiscoSparkClient(single_request_timeout=custom_timeout)
    assert client.single_request_timeout == custom_timeout


def test_default_wait_on_rate_limit(client):
    """The client should use the package default."""
    assert client.wait_on_rate_limit == \
           ciscosparksdk.DEFAULT_WAIT_ON_RATE_LIMIT


def test_non_default_wait_on_rate_limit():
    """The client should use the provided value."""
    client = ciscosparksdk.CiscoSparkClient(
            wait_on_rate_limit=not ciscosparksdk.DEFAULT_WAIT_ON_RATE_LIMIT,
    )
    assert client.wait_on_rate_limit != \
           ciscosparksdk.DEFAULT_WAIT_ON_RATE_LIMIT
