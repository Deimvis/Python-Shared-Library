from abc import ABC, abstractmethod
from typing import Any, Hashable


class CacheBase(ABC):

    @abstractmethod
    def get(self, key: Hashable) -> Any:
        pass

    @abstractmethod
    def has(self, key: Hashable) -> bool:
        pass

    @abstractmethod
    def set(self, key: Hashable, value: Any) -> None:
        pass

    @property
    @abstractmethod
    def size(self):
        pass
