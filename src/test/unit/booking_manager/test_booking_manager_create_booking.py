from datetime import datetime, timedelta
from unittest.mock import AsyncMock, Mock
import pytest
from src.domain import entities
from src.test.unit.booking_manager.booking_manger_parametrize_data import FUTURE_DATES_RESERVED, START_DATE_IN_FUTURE, \
    START_DATE_HIGHER_THAN_END_DATE, START_DATE_NOT_IN_FUTURE
from src.use_cases import BookingManager


# ================================= SET-UP =================================

@pytest.fixture
def room_repository():
    room_repository = Mock()
    room_repository.get_async = AsyncMock(
        entities.Room(id=1, description="A"),
    )
    room_repository.get_all_async = AsyncMock(return_value=[
        entities.Room(id=1, description="A"),
        entities.Room(id=2, description="B"),
    ])
    return room_repository


@pytest.fixture
def booking_repository():
    booking_repository = Mock()
    _start_date = datetime.now() + timedelta(days=10)
    _end_date = datetime.now() + timedelta(days=20)

    booking_repository.get = AsyncMock(return_value=
                                       entities.Booking(id=1, start_date=_start_date, end_date=_end_date,
                                                        is_active=True, customer_id=1, room_id=1)
                                       )
    booking_repository.get_all_async = AsyncMock(return_value=[
        entities.Booking(id=1, start_date=_start_date, end_date=_end_date, is_active=True, customer_id=1, room_id=1),
        entities.Booking(id=2, start_date=_start_date, end_date=_end_date, is_active=True, customer_id=2, room_id=2),
    ])
    booking_repository.add_async = AsyncMock()
    return booking_repository


@pytest.fixture
def booking_manager(room_repository, booking_repository) -> BookingManager:
    return BookingManager(room_repository=room_repository, booking_repository=booking_repository)


# ================================= TEST =================================

@pytest.mark.asyncio
@pytest.mark.parametrize(
    "start_date, end_date", FUTURE_DATES_RESERVED
)
async def test_create_booking__fully_occupied__false(start_date, end_date, booking_repository, booking_manager):
    _booking = entities.Booking(start_date=start_date, end_date=end_date, is_active=False, customer_id=None, room_id=None, id=None)

    result = await booking_manager.create_booking(_booking)

    assert result == False
    assert booking_repository.get_all_async.call_count == 1

@pytest.mark.asyncio
@pytest.mark.parametrize(
    "start_date, end_date", START_DATE_IN_FUTURE
)
async def test__create_booking__not_fully_occupied__true(start_date, end_date, booking_repository, booking_manager):
    _booking = entities.Booking(start_date=start_date, end_date=end_date, is_active=False, customer_id=None,
                                room_id=None, id=None)

    result = await booking_manager.create_booking(booking=_booking)

    assert result == True
    assert booking_repository.get_all_async.call_count == 1

@pytest.mark.asyncio
@pytest.mark.parametrize(
    "start_date, end_date", START_DATE_HIGHER_THAN_END_DATE
)
async def test__create_booking__start_date_higher_than_end_date__exception(start_date, end_date, booking_repository, booking_manager):
    _booking = entities.Booking(start_date=start_date, end_date=end_date, is_active=False, customer_id=None,
                                room_id=None, id=None)
    with pytest.raises(ValueError):
        await booking_manager.create_booking(booking=_booking)
    assert booking_repository.call_count == 0


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "start_date, end_date", START_DATE_NOT_IN_FUTURE
)
async def test__create_booking__start_date_biger_than_end_date__exception(start_date, end_date, booking_repository, room_repository, booking_manager):
    _booking = entities.Booking(start_date=start_date, end_date=end_date, is_active=False, customer_id=None,
                                room_id=None, id=None)
    with pytest.raises(ValueError):
        await booking_manager.create_booking(booking=_booking)
