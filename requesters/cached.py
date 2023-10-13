import requests
from typing import Hashable, Protocol
from lib.requesters.base import RequesterBase
from lib.storages.cache import CacheBase


class RequestHashFunction(Protocol):
    def __call__(self, method, url, **kwargs) -> Hashable: ...


class CachedRequester(RequesterBase):
    DEFAULT_CACHE_HASH: RequestHashFunction = lambda method, url, **kwargs: (method, url)

    def __init__(self, requester: RequesterBase, cache: CacheBase, cache_hash: RequestHashFunction = DEFAULT_CACHE_HASH):
        self._requester = requester
        self._cache = cache
        self._cache_hash = cache_hash

    def request(self, method, url, **kwargs) -> requests.Response:
        hash_key = self._cache_hash(method, url, **kwargs)
        if not self._cache.has(hash_key):
            self._cache.set(hash_key, self._requester.request(method, url, **kwargs))
        return self._cache.get(hash_key)

    def request_force(self, method, url, **kwargs) -> requests.Response:
        return self._requester.request(method, url, **kwargs)
