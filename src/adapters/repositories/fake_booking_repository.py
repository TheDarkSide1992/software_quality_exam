from datetime import datetime
from src.ports.repositories import Repository
from src.domain import entities


class FakeBookingRepository(Repository):
    def __init__(self):
        super().__init__(Repository[entities.Booking])

    async def get_all_async(self) -> list[entities.Booking] | None:
        return [
            entities.Booking(id=117, start_date=datetime.now(), end_date=datetime.now(), is_active=False,
                             customer_id=12, room_id=19),
            entities.Booking(id=118, start_date=datetime.now(), end_date=datetime.now(), is_active=False,
                             customer_id=22, room_id=15),
            entities.Booking(id=119, start_date=datetime.now(), end_date=datetime.now(), is_active=False,
                             customer_id=15, room_id=12)
        ]
    async def get_async(self, id: int) -> entities.Booking | None:
        if id == 117: return entities.Booking(id=117,start_date=datetime.now(),end_date=datetime.now(), is_active=False, customer_id=12,room_id=19)
    async def add_async(self, entity: entities.Booking) -> None:
        if entity is None or entity.id is None or entity.customer_id is None: raise ValueError("Invalid entity")
    async def edit_async(self, entity: entities.Booking) ->  None:
        if entity is None or entity.id is None or entity.customer_id is None: raise ValueError("Invalid entity")
    async def remove_async(self, entity: entities.Booking) -> None:
        if entity is None or entity.id is None or entity.customer_id is None: raise ValueError("Invalid entity")