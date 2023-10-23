"""Tests  for etl.utils.preprocesser"""

import pytest

from  etl.utils.preprocesser import transform_date, chop


def test_transform_date():
    test_date = "31/1/1991"

    assert transform_date(test_date) == "1991-01-31"

def test_chop_length():
    test_text = "I  am a test text."

    assert len(chop(test_text)) == 1

def test_chop_type():
    test_text = "I am a test text."
    
    assert type(chop(test_text)) == list
