from pytest_bdd import given, when, then, parsers, scenarios
from datetime import datetime, timedelta
from unittest.mock import AsyncMock, Mock
import pytest
import asyncio
from src.domain import entities
from src.use_cases import BookingManager

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

@pytest.fixture
def context():
    return {}

#=====================================================================================================================

scenarios("booking_manager_create_booking.feature")

@given(parsers.parse("A booking starting on {start_date:d}"))
def starting_on(context, start_date: int):
    _start_date = datetime.now() + timedelta(days=start_date)
    context["start_date"] = _start_date

@given(parsers.parse("Ending on {end_date:d}"))
def ending_on(context, end_date: int):
    _end_date = datetime.now() + timedelta(days=end_date)
    context["end_date"] = _end_date

@when("The booking is created")
def booking_is_created(context):
    _booking = entities.Booking(start_date=context["start_date"], end_date=context["end_date"], is_active=False, customer_id=None,
                                room_id=None, id=None)
    context["booking"] = _booking

@then("The booking should be created successfully")
def booking_should_be_created_successfully(context, booking_repository, room_repository, booking_manager):
    result = asyncio.run(booking_manager.create_booking(booking=context["booking"]))

    assert result is not None
    assert room_repository.get_all_async.call_count == 1
    assert booking_repository.get_all_async.call_count == 1

@when("the booking fails to be created")
def booking_creation_fails(context, booking_repository, room_repository, booking_manager):
    try:
        _booking = entities.Booking(start_date=context["start_date"], end_date=context["end_date"], is_active=False, customer_id=None,
                                    room_id=None, id=None)
        result = asyncio.run(booking_manager.create_booking(booking=_booking))
        print(result)
    except Exception as e:
        context["exception"] = e
        print(e)

@then("there should be an error message indicating invalid dates")
def booking_should_not_be_created(context, booking_repository, room_repository):
    print(context)
    exception = context["exception"]
    assert exception is not None
    assert room_repository.get_all_async.call_count == 0
    assert booking_repository.get_all_async.call_count == 0
    assert booking_repository.add_async.call_count == 0

@then("The booking should not be be created due to full occupancy")
def booking_should_not_be_created_due_to_full_occupancy(context, booking_repository, room_repository, booking_manager):
    result = asyncio.run(booking_manager.create_booking(booking=context["booking"]))
    assert result is not None
    assert result is False
    assert room_repository.get_all_async.call_count == 1
    assert booking_repository.get_all_async.call_count == 1
    assert booking_repository.add_async.call_count == 0