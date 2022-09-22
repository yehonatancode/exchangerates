import pytest

from src.savetojson import usedata
from src.specific_convert import generaterates


def test_dev():
    #Arrange output that should match our use of mock data
    expected_data = usedata()

    #Act
    output = generaterates()

    #Assert
    assert output == expected_data

