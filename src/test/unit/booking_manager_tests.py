
from datetime import datetime, timedelta
from unittest.mock import AsyncMock, Mock
import pytest
from src.domain import entities
from src.use_cases import BookingManager

# ================================= SET-UP =================================

@pytest.fixture
def room_repository():
    room_repository = Mock()
    room_repository.get_async = AsyncMock(return_value=entities.Room(id=19, description="Less popular room"))
    room_repository.get_all_async = AsyncMock(return_value=[
            entities.Room(id=19,description="Less popular room"),
            entities.Room(id=15,description="Some room"),
            entities.Room(id=12,description="Best room")
        ])


    return room_repository
@pytest.fixture
def booking_repository():
    booking_repository = Mock()

    booking_repository.get_async = AsyncMock(return_value=entities.Booking(id=117,start_date=datetime.now(),end_date=datetime.now(), is_active=False, customer_id=12,room_id=19))
    booking_repository.get_all_async = AsyncMock(return_value=[entities.Booking(id=117, start_date=datetime.now(), end_date=datetime.now(), is_active=False,
                             customer_id=12, room_id=19),
            entities.Booking(id=118, start_date=datetime.now(), end_date=datetime.now(), is_active=False,
                             customer_id=22, room_id=15),
            entities.Booking(id=119, start_date=datetime.now(), end_date=datetime.now(), is_active=False,
                             customer_id=15, room_id=12)])
    return booking_repository


@pytest.fixture
def booking_manager(room_repository, booking_repository) -> BookingManager:
    return  BookingManager(room_repository=room_repository, booking_repository=booking_repository)


# ================================= TEST =================================

@pytest.mark.asyncio
@pytest.mark.parametrize(
    "start_date, end_date",
    [
        (datetime.now() + timedelta(days=1), datetime.now() + timedelta(days=10)),
        (datetime.now() + timedelta(days=2), datetime.now() + timedelta(days=5)),
        (datetime.now() + timedelta(days=20), datetime.now() + timedelta(days=22)),
        (datetime.now() + timedelta(days=32), datetime.now() + timedelta(days=35)),
    ]
)
async def test__find_available_rooms__not_none(start_date,end_date,booking_manager, room_repository, booking_repository):
    _start_date = start_date
    _end_date = end_date

    result = await booking_manager.find_available_room(start_date=_start_date, end_date=_end_date)
    assert result is not None
    assert room_repository.get_all_async.call_count == 1
    assert booking_repository.get_all_async.call_count == 1
