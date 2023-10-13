from collections import OrderedDict
from typing import Any, Hashable, Mapping
from .base import CacheBase


class LRUCache(CacheBase):
    MAX_SIZE = 64

    def __init__(self, max_size: int = MAX_SIZE):
        self._max_size: int = max_size
        self._data: Mapping[Hashable, Any] = OrderedDict()

    def get(self, key: Hashable) -> Any:
        self._data.move_to_end(key)
        return self._data[key]

    def has(self, key: Hashable) -> bool:
        return key in self._data

    def set(self, key: Hashable, value: Any) -> None:
        if self.has(key):
            self._data.move_to_end(key)
        elif self.size == self._max_size:
            self._data.popitem(last=False)
        self._data[key] = value

    @property
    def size(self):
        return len(self._data)
