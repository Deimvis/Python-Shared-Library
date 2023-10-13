from typing import Dict

from .base import ConsumerBase

class DummyConsumer(ConsumerBase):

    def recv(self, data: Dict) -> None:
        pass
