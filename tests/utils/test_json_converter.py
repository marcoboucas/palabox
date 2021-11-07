"""Test json_converter."""

from datetime import datetime
from typing import Any

import pytest

from palabox.utils import json_converter

TESTS = [
    ("hello", "hello"),
    (1, "1"),
    (1.0, "1.0"),
    (datetime(2021, 11, 1, 1, 1, 1, 0), "2021-11-01 01:01:01"),
]


@pytest.mark.parametrize(
    "test_input,expected",
    TESTS,
)
def test_json_converter(test_input: Any, expected: str) -> None:
    """Test json_converter."""
    value = json_converter(test_input)
    assert isinstance(value, str)
    assert value == expected
