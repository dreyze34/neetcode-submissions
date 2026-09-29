class Node:
    def __init__(self, key = None, value = None):
        self.key = key
        self.val = value
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity
        self.left, self.right = Node(), Node()
        self.left.next, self.right.prev = self.right, self.left

    def push_front(self, node):
        node.prev.next, node.next.prev = node.next, node.prev
        self.right.prev.next, node.prev = node, self.right.prev
        node.next, self.right.prev = self.right, node

    def get(self, key: int) -> int:
        if key in self.cache:
            self.push_front(self.cache[key])
            return self.cache[key].val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache[key].val = value

            curr = self.cache[key]
            self.push_front(curr)
        
        else:
            new_node = Node(key, value)
            self.cache[key] = new_node
            self.right.prev.next, new_node.prev = new_node, self.right.prev
            new_node.next, self.right.prev = self.right, new_node

            if len(self.cache) > self.capacity:
                del self.cache[self.left.next.key]
                self.left.next = self.left.next.next
                self.left.next.prev = self.left



            

        
