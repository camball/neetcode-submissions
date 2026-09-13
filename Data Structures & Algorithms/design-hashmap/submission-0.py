class MyHashMap:
    """
    Underlying store: array (top-level) of arrays ("buckets").

    Trading storage for lookup speed. Increase in speed is proportional
    to an increase in `NUM_BUCKETS`.

    Write path: When we want to add a value to the hashmap, we compute the
    hash of the key, which is the index of the top-level array. We then
    append the k/v pair ("item") to the bucket, thus inserting it.
    
    Read path: Compute hash of the key to find the bucket, then perform a
    linear scan of the bucket until we find the item.
    """

    NUM_BUCKETS = 100_000
    """At most a search of 10 keys per bucket, based on constraint `0 <= key <= 1,000,000`"""

    def myHash(self, key: int):
        return key % self.NUM_BUCKETS

    def __init__(self):
        self.buckets = [[]] * self.NUM_BUCKETS

    def put(self, key: int, value: int) -> None:
        bucket_id = self.myHash(key)
        for idx, (k, _) in enumerate(self.buckets[bucket_id]):
            if k == key:
                self.buckets[bucket_id][idx] = (key, value)
                return
        else:
            self.buckets[bucket_id].append((key, value))

    def get(self, key: int) -> int:
        bucket_id = self.myHash(key)
        for k, v in self.buckets[bucket_id]:
            if k == key:
                return v
        else:
            return -1

    def remove(self, key: int) -> None:
        bucket_id = self.myHash(key)
        for k, v in self.buckets[bucket_id]:
            if k == key:
                self.buckets[bucket_id].remove((k, v))

 
# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)