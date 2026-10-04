from collections import OrderedDict


class LRUCache:
    """
    LRU Cache => Cache eviction policy where the cache has a fixed size. If we
    exceed that size, we must evict the *least-recently used* keys first.
    """

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = OrderedDict()

    def get(self, key: int) -> int:
        try:
            value = self.cache[key]
            self.cache.move_to_end(key)
            return value
        except KeyError:
            return -1

    def put(self, key: int, value: int) -> None:
        if key not in self.cache and len(self.cache) >= self.capacity:
            self.cache.popitem(last=False)

        self.cache[key] = value

        # The above inserts at the end, but if we only updated a value, we must
        # move it to the end manually.
        self.cache.move_to_end(key)