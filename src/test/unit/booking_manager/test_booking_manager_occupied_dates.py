from datetime import datetime, timedelta
from typing import List
from unittest.mock import AsyncMock, Mock
import pytest
from src.domain import entities
from src.test.unit.booking_manager.booking_manger_parametrize_data import FUTURE_DATES_RESERVED, START_DATE_IN_FUTURE, \
    START_DATE_HIGHER_THAN_END_DATE
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
async def test__fully_occupied__dates_in_range__list_of_dates(start_date, end_date, booking_repository, room_repository, booking_manager):
    _result = await booking_manager.get_fully_ocupied_dates(start_date=start_date, end_date=end_date)

    assert len(_result) is not 0
    assert _result.__contains__(start_date.date())
    assert room_repository.get_all_async.call_count == 1
    assert booking_repository.get_all_async.call_count == 1

@pytest.mark.asyncio
async def test__fully_occupied_dates__inside_outside_date_in_range__dates_in_range(booking_repository, room_repository, booking_manager):
    _expected = [
        (datetime.now() + timedelta(days=19)).date(),
        (datetime.now() + timedelta(days=20)).date(),
    ]

    _start_date = datetime.now() + timedelta(days=19)
    _end_date = datetime.now() + timedelta(days=30)

    _result = await booking_manager.get_fully_ocupied_dates(start_date=_start_date, end_date=_end_date)


    assert len(_result) is not 0
    assert _result == _expected
    assert _result.__contains__(_start_date.date())
    assert room_repository.get_all_async.call_count == 1
    assert booking_repository.get_all_async.call_count == 1

@pytest.mark.asyncio
@pytest.mark.parametrize(
    "start_date, end_date", START_DATE_IN_FUTURE
)
async def test__fully_occupied_dates__outside_date_range__empty(start_date, end_date, booking_repository, room_repository, booking_manager):

    _result = await booking_manager.get_fully_ocupied_dates(start_date=start_date, end_date=end_date)

    assert len(_result) is 0
    assert room_repository.get_all_async.call_count == 1
    assert booking_repository.get_all_async.call_count == 1

@pytest.mark.asyncio
@pytest.mark.parametrize(
    "start_date, end_date", START_DATE_HIGHER_THAN_END_DATE
)
async def test_dully_occupied_dates__dates_in_past__exception(start_date, end_date, booking_repository, room_repository, booking_manager):

    with pytest.raises(ValueError):
        await booking_manager.get_fully_ocupied_dates(start_date=start_date, end_date=end_date)

    assert room_repository.get_all_async.call_count == 0
    assert booking_repository.get_all_async.call_count == 0
