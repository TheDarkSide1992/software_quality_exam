from datetime import datetime, timedelta
from typing import List

from src.ports.repositories.repository import Repository
from src.domain import entities


class BookingManager:
    def __init__(self, booking_repository: Repository[entities.Booking], room_repository: Repository[entities.Room]):
        self.booking_repository = booking_repository
        self.room_repository = room_repository

    async def create_booking(self, booking: entities.Booking) -> bool:
        room_id: int = await self.find_available_room(start_date=booking.start_date, end_date=booking.end_date)

        if room_id is None or  room_id <= 0: return False

        booking.RoomId = room_id
        booking.is_active = True
        await self.booking_repository.add_async(booking)

        return True

    async def find_available_room(self, start_date: datetime, end_date: datetime) -> int:
        if start_date <= datetime.today() or start_date > end_date:
            raise ValueError("The start date cannot be in the past or later than the end date.")

        bookings: List[entities.Booking] = await self.booking_repository.get_all_async()
        active_bookings = [b for b in bookings if b.is_active]
        rooms: List[entities.Room] = await self.room_repository.get_all_async()

        for room in rooms:
            active_bookings_for_current_room = [b for b in active_bookings if b.room_id == room.id]

            if all(start_date < b.start_date and end_date < b.start_date or start_date > b.end_date and end_date > b.end_date for b in active_bookings_for_current_room):
                return room.id

        return -1

    async def get_fully_ocupied_dates(self, start_date: datetime, end_date: datetime) -> List[datetime]:
        if start_date > end_date:
            raise ValueError("The start date cannot be later than the end date.")

        fully_occupied_dates: List[datetime] = []
        rooms: List[entities.Room] = await self.room_repository.get_all_async()
        no_of_rooms = len(rooms)
        bookings: List[entities.Booking] = await self.booking_repository.get_all_async()


        if bookings:
            current = start_date
            while current <= end_date:
                no_of_bookings = [
                    b for b in bookings if b.is_active and b.start_date <= current <= b.end_date
                ]
                if len(no_of_bookings) >= no_of_rooms:
                    fully_occupied_dates.append(current)
                current += timedelta(days=1)

        return fully_occupied_dates