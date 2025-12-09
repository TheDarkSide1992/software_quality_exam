from asyncio import Task
from datetime import datetime
from typing import List
from xmlrpc.client import DateTime

from src.ports.repositories.repository import Repository
from src.domain import entities


class BookingManager:
    def __init__(self, booking_repository: Repository[entities.Booking], room_repository: Repository[entities.Room]):
        self.booking_repository = booking_repository
        self.room_repository = room_repository

    async def create_booking(self, booking: entities.Booking) -> bool:
        print("DOO SOMETHING")

        room_id: int = await self.find_available_room(start_date=booking.StartDate, end_date=booking.EndDate)

        if room_id is None or  room_id < 0: return False

        booking.RoomId = room_id
        booking.is_active = True
        await self.booking_repository.add_async(booking)

        return True

    async def find_available_room(self, start_date: datetime, end_date: datetime) -> int:
        print("DOO SOMETHING")
        # TODO implement this.

        return 0

    async def get_fully_ocupied_dates(self, start_date: datetime, end_date: datetime) -> List[DateTime]:
        print("DOO SOMETHING")

        return []
        # TODO implement this


"""
public async Task<bool> CreateBooking(Booking booking)
        {
            int roomId = await FindAvailableRoom(booking.StartDate, booking.EndDate);

            if (roomId >= 0)
            {
                booking.RoomId = roomId;
                booking.IsActive = true;
                await bookingRepository.AddAsync(booking);
                return true;
            }
            else
            {
                return false;
            }
        }

        public async Task<int> FindAvailableRoom(DateTime startDate, DateTime endDate)
        {
            if (startDate <= DateTime.Today || startDate > endDate)
                throw new ArgumentException("The start date cannot be in the past or later than the end date.");

            var bookings = await bookingRepository.GetAllAsync();
            var activeBookings = bookings.Where(b => b.IsActive);
            var rooms = await roomRepository.GetAllAsync();
            foreach (var room in rooms)
            {
                var activeBookingsForCurrentRoom = activeBookings.Where(b => b.RoomId == room.Id);
                if (activeBookingsForCurrentRoom.All(b => startDate < b.StartDate &&
                    endDate < b.StartDate || startDate > b.EndDate && endDate > b.EndDate))
                {
                    return room.Id;
                }
            }
            return -1;
        }

        public async Task<List<DateTime>> GetFullyOccupiedDates(DateTime startDate, DateTime endDate)
        {
            if (startDate > endDate)
                throw new ArgumentException("The start date cannot be later than the end date.");

            List<DateTime> fullyOccupiedDates = new List<DateTime>();
            var rooms = await roomRepository.GetAllAsync();
            int noOfRooms = rooms.Count();
            var bookings = await bookingRepository.GetAllAsync();

            if (bookings.Any())
            {
                for (DateTime d = startDate; d <= endDate; d = d.AddDays(1))
                {
                    var noOfBookings = from b in bookings
                                       where b.IsActive && d >= b.StartDate && d <= b.EndDate
                                       select b;
                    if (noOfBookings.Count() >= noOfRooms)
                        fullyOccupiedDates.Add(d);
                }
            }
            return fullyOccupiedDates;
        }

    }
"""
