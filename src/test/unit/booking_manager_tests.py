
from datetime import datetime, timedelta
import pytest

from src.domain import entities
from src.adapters.repositories import FakeBookingRepository, FakeRoomRepository
from src.use_cases import BookingManager


@pytest.fixture
def booking_manager() -> BookingManager:
    return  BookingManager(room_repository=FakeBookingRepository(), booking_repository=FakeRoomRepository())




def test__fina_available_rooms__not_none(booking_manager):
    _start_date = datetime.now()
    _end_date = datetime.now() + timedelta(days=3)

    result = booking_manager.find_available_room(start_date=_start_date, end_date=_end_date)

    assert result is not None
