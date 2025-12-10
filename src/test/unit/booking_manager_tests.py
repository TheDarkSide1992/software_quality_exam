
import pytest

from src.ports.repositories import Repository
from src.domain import entities
from src.adapters.repositories import FakeBookingRepository, FakeRoomRepository


@pytest.fixture
def room_repository() -> Repository[entities.Room]:
    return FakeRoomRepository()

def booking_repository() -> Repository[entities.Room]:
    return FakeBookingRepository()


"""
mock test is written for testing mock library and should not be used in actuality
"""
def mock_Test(): #TODO remove this
    return 4
def test_mock(): #TODO remove this
    assert mock_Test() == 4
def test_mock2(): #TODO remove this
    _booking_repository = booking_repository()

    _booking_repository.get_async(id=2)
    assert mock_Test() != 5
