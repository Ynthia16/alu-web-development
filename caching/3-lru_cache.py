from collections import OrderedDict

class BaseCaching:
    MAX_ITEMS = 6

    def __init__(self):
        self.cache_data = OrderedDict()

    def print_cache(self):
        print("Current cache:")
        for key, value in self.cache_data.items():
            print(f"{key}: {value}")


class LRUCache(BaseCaching):
    def __init__(self):
        super().__init__()

    def put(self, key, item):
        if key is None or item is None:
            return
        self.cache_data[key] = item
        if len(self.cache_data) > self.MAX_ITEMS:
            lru_key, _ = self.cache_data.popitem(last=False)
            print(f"DISCARD: {lru_key}")

    def get(self, key):
        if key is None or key not in self.cache_data:
            return None
        value = self.cache_data.pop(key)
        self.cache_data[key] = value  # Move to the end to mark as recently used
        return value

