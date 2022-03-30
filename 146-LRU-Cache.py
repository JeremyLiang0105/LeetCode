class ListNode:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None
        
class LRUCache:

    def __init__(self, capacity: int):
        self.space = capacity
        self.lookup = {}
        self.left = ListNode(0, 0)
        self.right = ListNode(0, 0)
        self.left.next = self.right
        self.right.prev = self.left
        
    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next = nxt
        nxt.prev = prev
        
    def insert(self, node):
        node.next = self.right
        node.prev = self.right.prev
        self.right.prev.next = node
        self.right.prev = node
        
        
    def get(self, key: int) -> int:
        if key in self.lookup:
            self.remove(self.lookup[key])
            self.insert(self.lookup[key])
            return self.lookup[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.lookup:
            self.remove(self.lookup[key])
        self.lookup[key] = ListNode(key, value)
        self.insert(self.lookup[key])
        
        if len(self.lookup) > self.space:
            lru = self.left.next
            self.remove(lru)
            del self.lookup[lru.key]
            

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
