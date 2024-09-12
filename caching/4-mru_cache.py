#!/usr/bin/python3
"""MRU cache"""

BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    """MRU cache"""

    def put(self, key, item):
        """Add an item in the cache"""
        if key is None or item is None:
            return
        # Split the long condition into multiple lines
        if (key not in self.cache_data and
                len(self.cache_data) >= BaseCaching.MAX_ITEMS):
            discard = next(reversed(self.cache_data))
            print("DISCARD: {}".format(discard))
            del self.cache_data[discard]
        if key in self.cache_data:
            del self.cache_data[key]
        self.cache_data[key] = item

    def get(self, key):
        """Get an item in the cache"""
        if key is None or key not in self.cache_data:
            return None
        item = self.cache_data[key]
        del self.cache_data[key]
        self.cache_data[key] = item
        return item
