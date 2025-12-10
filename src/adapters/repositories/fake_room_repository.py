from datetime import datetime
from src.ports.repositories import Repository
from src.domain import entities


class FakeRoomRepository(Repository):

    def __init__(self):
        super().__init__(Repository[entities.Room])

    async def get_all_async(self) -> list[entities.Room] | None:
        return [
            entities.Room(id=19,description="Less popular room"),
            entities.Room(id=15,description="Some room"),
            entities.Room(id=12,description="Best room")
        ]
    async def get_async(self, id: int) -> entities.Room | None:
        print("TODO")

        if id == 117: return entities.Room(id=19, description="Less popular room")
    async def add_async(self, entity: entities.Room) -> None:
        print("Booking added")

        if entity is None or entity.id is None or entity.customer_id is None: raise ValueError("Invalid entity")
    async def edit_async(self, entity: entities.Room) ->  None:
        print("booking edited")
        if entity is None or entity.id is None or entity.customer_id is None: raise ValueError("Invalid entity")
    async def remove_async(self, entity: entities.Room) -> None:
        print("Booking removed")
        if entity is None or entity.id is None or entity.customer_id is None: raise ValueError("Invalid entity")