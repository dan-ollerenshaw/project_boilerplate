"""Dummy unit tests file."""

import pytest

import src.analysis


def test_invalid_data():
    with pytest.raises(AssertionError):
        src.analysis.analyse(None)
