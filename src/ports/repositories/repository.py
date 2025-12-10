from abc import abstractmethod, ABC
from typing import Generic, TypeVar

T = TypeVar('T')

class Repository(ABC, Generic[T]):
    def __init__(self, data_type: T) -> None:
        self.type = data_type

    @abstractmethod
    async def get_all_async(self) -> list[T] | None:
        pass

    @abstractmethod
    async def get_async(self, id: int) -> T | None:
        pass

    @abstractmethod
    async def add_async(self, entity: T) -> None:
        pass

    @abstractmethod
    async def edit_async(self, entity: T) ->  None:
        pass

    @abstractmethod
    async def remove_async(self, entity: T) -> None:
        pass
