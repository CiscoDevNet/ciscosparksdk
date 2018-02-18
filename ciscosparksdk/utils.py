# -*- coding: utf-8 -*-
"""Package helper functions and classes."""


from __future__ import (
    absolute_import,
    division,
    print_function,
    unicode_literals,
)
from builtins import *
from past.builtins import basestring


__copyright__ = "Copyright (c) 2016-2018 Cisco and/or its affiliates."
__license__ = "MIT"


from datetime import datetime, timedelta, tzinfo
import re

from ciscosparkapi.utils import check_type, dict_from_items_with_values
from ciscosparkapi.generator_containers import (
    GeneratorContainer,
    generator_container,
)


SPARK_DATETIME_FORMAT = "%Y-%m-%dT%H:%M:%S.%fZ"


@generator_container
def filter_by_attribute(iterable, where, equals=None, starts_with=None,
                        contains=None, ends_with=None, case_sensitive=True):
    """Filter an iterable sequence of objects by attribute value.

     Filter an iterable sequence of objects where the specified attribute
     matches the parameters.

    Args:
        where(basestring): The object attribute name to match on.
        equals(basestring): The attribute value must match this string exactly.
        starts_with(basestring): The attribute value must start with this
            prefix.
        contains(basestring): The attribute value must contain this substring.
        ends_with(basestring): The attribute value must end with this suffix.
        case_sensitive(bool): Matches should be case sensitive.

    Returns:
        Generator: A generator yielding all of the matched objects.

    Raises:
        TypeError: If the parameter types are incorrect.

    """
    check_type(where, basestring, may_be_none=False)
    check_type(equals, basestring)
    check_type(starts_with, basestring)
    check_type(contains, basestring)
    check_type(ends_with, basestring)
    check_type(case_sensitive, bool, may_be_none=False)

    attribute_name = where

    if not any((equals, starts_with, contains, ends_with)):
        raise TypeError(
            "You must supply at least one matching parameter."
        )

    # Compile the regular expression
    exact_match = "(?=^{}$)".format(equals) if equals else ""

    starts_with_match = "(?=^{}.*)".format(starts_with) \
        if starts_with else ""

    contains_match = "(?=^.*{}.*$)".format(contains) if contains else ""

    ends_with_match = "(?=.*{}$)".format(ends_with) if ends_with else ""

    match_string = "".join(
        (exact_match, starts_with_match, contains_match, ends_with_match)
    )

    flags = 0 if not case_sensitive else re.IGNORECASE
    regex = re.compile(match_string, flags=flags)

    # Find and yield matching objects
    for object in iterable:
        attribute_value = getattr(object, attribute_name, None)
        if attribute_value is not None and regex.match(str(attribute_value)):
            yield object


def first(iterable):
    """Return the first item from the iterable."""
    return next(iter(iterable), None)


class ZuluTimeZone(tzinfo):
    """Zulu Time Zone."""

    def tzname(self, dt):
        """Time Zone Name."""
        return "Z"

    def utcoffset(self, dt):
        """UTC Offset."""
        return timedelta(0)

    def dst(self, dt):
        """Daylight Savings Time Offset."""
        return timedelta(0)


class SparkDateTime(datetime):
    """Cisco Spark formatted datetime."""

    @classmethod
    def strptime(cls, date_string, format=SPARK_DATETIME_FORMAT):
        """strptime with the Spark DateTime format as the default."""
        return super(SparkDateTime, cls).strptime(
            date_string, format
        ).replace(tzinfo=ZuluTimeZone())

    def strftime(self, fmt=SPARK_DATETIME_FORMAT):
        """strftime with the Spark DateTime format as the default."""
        return super(SparkDateTime, self).strftime(fmt)

    def __str__(self):
        """Human readable string representation of this SparkDateTime."""
        dt = self.astimezone(ZuluTimeZone())
        return dt.strftime("%Y-%m-%dT%H:%M:%S.{:0=3}%Z").format(
            self.microsecond // 1000
        )
