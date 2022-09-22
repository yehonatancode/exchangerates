import json

import pytest

from src.APICall import api_call
from src.savetojson import usedata
from src.specific_convert import generaterates


def test_dev():
    # Arrange output that should match our use of data
    expected_data = ""

    # Act
    output = generaterates()
    with open('data.json') as json_file:
        data = json.load(json_file)
        expected_data = data

    # Assert
    assert output == expected_data

