from abc import abstractmethod
from asyncio import Task
from typing import Any, Generic, TypeVar

T = TypeVar('T')


class Repository(Generic[T]):
    def __init__(self, type: T):
        self.type = type

    @abstractmethod
    async def get_all_async(self, **filters: Any) -> Task[list[T] | None]:
        pass

    @abstractmethod
    async def get_async(self, bid: T) -> Task[T | None]:
        pass

    @abstractmethod
    async def add_async(self, bid: T) -> Task:
        pass

    @abstractmethod
    async def edit_async(self, bid: T) -> Task:
        pass

    @abstractmethod
    async def remove_async(self, bid: T) -> Task:
        pass


"""
    Task<IEnumerable<T>> GetAllAsync();
    Task<T> GetAsync(int id);
    Task AddAsync(T entity);
    Task EditAsync(T entity);
    Task RemoveAsync(int id);
"""
