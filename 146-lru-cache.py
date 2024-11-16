# https://leetcode.com/problems/lru-cache/?envType=company&envId=facebook&favoriteSlug=facebook-thirty-days&role=full-stack&status=TO_DO%2CATTEMPTED&difficulty=MEDIUM

######################################
# Linked List, Hash table
######################################


class Node:
    def __init__(self, key: int, value: int, next = None, previous = None):
        self.value = value
        self.key = key
        self.next = next
        self.previous = previous

class LRUCache:

    def __init__(self, capacity: int):
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.previous = self.head
        self.capacity = capacity
        self.cache = {}

    def add(self, node):
        prev_tail = self.tail.previous
        prev_tail.next = node
        node.previous = prev_tail
        node.next = self.tail
        self.tail.previous = node

    def remove(self, node):
        node.previous.next = node.next
        node.next.previous = node.previous
        
    def get(self, key: int) -> int:
        node = self.cache.get(key, None)

        if not node:
            return -1
        
        self.remove(node)
        self.add(node)

        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            old_node = self.cache[key]
            self.remove(old_node)

        node = Node(key, value)
        self.cache[key] = node
        self.add(node)

        if len(self.cache) > self.capacity:
            remove_node = self.head.next
            self.remove(remove_node)
            del self.cache[remove_node.key]

lRUCache = LRUCache(2)
lRUCache.put(2, 1)
lRUCache.put(1, 1)
lRUCache.put(2, 3)
lRUCache.put(4, 1)
print(lRUCache.get(1))
print(lRUCache.get(2))

print("Next case")


lRUCache = LRUCache(2)
lRUCache.put(1, 1) # cache is {1=1}
lRUCache.put(2, 2) # cache is {1=1, 2=2}
print(lRUCache.get(1))    # return 1
lRUCache.put(3, 3) # LRU key was 2, evicts key 2, cache is {1=1, 3=3}
print(lRUCache.get(2))    # returns -1 (not found)
lRUCache.put(4, 4) # LRU key was 1, evicts key 1, cache is {4=4, 3=3}
print(lRUCache.get(1))    # return -1 (not found)
print(lRUCache.get(3))    # return 3
print(lRUCache.get(4))    # return 4

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)