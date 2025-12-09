
import pytest

from src.ports.repositories import Repository
from src.domain import entities

@pytest.fixture
def room_repository() -> Repository[entities.Room]:
    return None

def booking_repository() -> Repository[entities.Booking]:
    return None


"""
mock test is written for testing mock library and should not be used in actuality
"""
def mock_Test(): #TODO remove this
    return 4
def test_mock(): #TODO remove this
    assert mock_Test() == 4
def test_mock2(): #TODO remove this
    assert mock_Test() != 5
