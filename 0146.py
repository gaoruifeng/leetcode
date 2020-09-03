from collections import OrderedDict

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.od = OrderedDict()

    def get(self, key: int) -> int:
        if key in self.od:
            self.od.move_to_end(key)
        return self.od.get(key, -1)

    def put(self, key: int, value: int) -> None:
        if key in self.od:
            self.od.move_to_end(key)
        elif len(self.od) == self.capacity:
        # key is new and od is full, remove first item
            first_key = next(iter(self.od.keys()))
            del self.od[first_key]
        self.od[key] = value

    def __repr__(self):
        return str(self.od)


if __name__ == '__main__':
    lru = LRUCache(2)
    lru.put(1,1)
    lru.put(2,2)
    print(lru.get(1))
    lru.put(3,3)
    print(lru.get(2))
    lru.put(4,4)
    print(lru.get(1))
    print(lru.get(3))
    print(lru.get(4))
    print(lru)
