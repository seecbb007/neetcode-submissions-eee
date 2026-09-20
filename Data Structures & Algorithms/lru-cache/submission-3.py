class DoubleLList:
    def __init__(self, key,value):
        self.key = key
        self.value = value

        self.prev = None
        self.next = None
class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity

        self.head = DoubleLList(0,0)
        self.tail = DoubleLList(0,0)

        self.head.next = self.tail
        self.tail.prev = self.head
    def add(self, node):
        temp = self.head.next

        node.prev = self.head
        self.head.next = node

        node.next = temp
        temp.prev = node

    def remove(self,node):
        temp = node.prev
        nxt = node.next

        temp.next = nxt
        nxt.prev = temp

    
    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        node = self.cache[key]
        self.remove(node)
        self.add(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        newnode = DoubleLList(key,value)
        self.cache[key] = newnode
        self.add(newnode)

        if len(self.cache) > self.capacity:
            lrunode = self.tail.prev
            self.remove(lrunode)
            del self.cache[lrunode.key]
        
