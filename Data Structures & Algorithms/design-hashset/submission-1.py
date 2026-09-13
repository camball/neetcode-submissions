class MyHashSet:
    """
    Underlying store: array (top-level) of arrays ("buckets").

    Trading storage for lookup speed. Increase in speed is proportional
    to an increase in `NUM_BUCKETS`.

    Write path: When we want to add a value to the set, we compute the
    hash of the value, which is the index of the top-level array. We then
    append the value to the bucket, thus inserting it into our HashSet.
    
    Read path: Compute hash of the item to find the bucket, then perform a
    linear scan of the bucket until we find the item.
    """

    NUM_BUCKETS = 100_000
    """At most a search of 10 keys per bucket, based on constraint `0 <= key <= 1,000,000`"""

    def myHash(self, key: int):
        return key % self.NUM_BUCKETS

    def __init__(self):
        self.buckets = [[]] * self.NUM_BUCKETS

    def add(self, key: int) -> None:
        bucket_id = self.myHash(key)
        for item in self.buckets[bucket_id]:
            if item == key:
                return
        else:
            self.buckets[bucket_id].append(key)

    def remove(self, key: int) -> None:
        bucket_id = self.myHash(key)
        for item in self.buckets[bucket_id]:
            if item == key:
                self.buckets[bucket_id].remove(key)

    def contains(self, key: int) -> bool:
        bucket_id = self.myHash(key)
        for item in self.buckets[bucket_id]:
            if item == key:
                return True
        else:
            return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)