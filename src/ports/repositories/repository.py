from abc import abstractmethod
from asyncio import Task
from typing import Any, Generic, TypeVar

T = TypeVar('T')

class Repository(Generic[T]):
    def __init__(self, data_type: T):
        self.type = data_type

    @abstractmethod
    async def get_all_async(self, **filters: Any) -> list[T] | None:
        pass

    @abstractmethod
    async def get_async(self, bid: T) -> T | None:
        pass

    @abstractmethod
    async def add_async(self, bid: T) -> None:
        pass

    @abstractmethod
    async def edit_async(self, bid: T) ->  None:
        pass

    @abstractmethod
    async def remove_async(self, bid: T) -> None:
        pass
