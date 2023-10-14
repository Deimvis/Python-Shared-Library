from abc import ABC, abstractmethod
from typing import Any, Iterable, Sequence


class BufferBase(ABC):
    @abstractmethod
    def write(self, data: Any) -> None:
        pass

    @abstractmethod
    def read(self) -> Any:
        pass

    @property
    @abstractmethod
    def size(self) -> int:
        pass

    @property
    @abstractmethod
    def empty(self) -> bool:
        pass

    @property
    @abstractmethod
    def full(self) -> bool:
        pass

    def read_all(self) -> Sequence[Any]:
        return [v for v in self.read_all_stream()]

    def read_all_stream(self) -> Iterable[Any]:
        while not self.empty:
            yield self.read()
