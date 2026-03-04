# 146. LRU Cache
# Medium
# Topics
# premium lock icon
# Companies
# Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

# Implement the LRUCache class:

# LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
# int get(int key) Return the value of the key if the key exists, otherwise return -1.
# void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.
# The functions get and put must each run in O(1) average time complexity.

 

# Example 1:

# Input
# ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
# [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
# Output
# [null, null, null, 1, null, -1, null, -1, 3, 4]

# Explanation
# LRUCache lRUCache = new LRUCache(2);
# lRUCache.put(1, 1); // cache is {1=1}
# lRUCache.put(2, 2); // cache is {1=1, 2=2}
# lRUCache.get(1);    // return 1
# lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
# lRUCache.get(2);    // returns -1 (not found)
# lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
# lRUCache.get(1);    // return -1 (not found)
# lRUCache.get(3);    // return 3
# lRUCache.get(4);    // return 4
 

# Constraints:

# 1 <= capacity <= 3000
# 0 <= key <= 104
# 0 <= value <= 105
# At most 2 * 105 calls will be made to get and put.


class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.hashMap = {}
        self.capacity = capacity

        self.head = Node(0,0)
        self.tail = Node(0,0)
        # Tail and Head are dummy nodes to keep the track of length as well latest used key value pair

        self.head.prev = self.tail
        self.tail.next = self.head

        #in future our linked list will look like:
        #(Tail)<->(1:3)<->(3:6)<->......<->(54:3)<->(Head)

    def removeNode(self, Node1):
        prevNode = Node1.prev
        nextNode = Node1.next

        prevNode.next = nextNode
        nextNode.prev = prevNode

    def insertNode(self, Node2):
        Node2.next = self.head
        Node2.prev = self.head.prev

        self.head.prev.next = Node2
        self.head.prev = Node2

    def get(self, key: int) -> int:
        if key in self.hashMap:
            Node4 = self.hashMap[key]
            self.removeNode(Node4)
            self.insertNode(Node4)
            return Node4.value
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.hashMap:
            self.removeNode(self.hashMap[key])
        
        node3 = Node(key, value)
        self.hashMap[key] = node3
        self.insertNode(self.hashMap[key])

        if len(self.hashMap) > self.capacity:
            current = self.tail.next
            del self.hashMap[current.key]
            self.removeNode(current)



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)


"""
I used AI for whole help, understand the code and wrote line by line. Ans i stil sucks.
Runtime is 163ms and beating only 15% + solutions and in memory beating only 26% + solutions.
Although i checked space complexity is O(n) and time complexity is O(1).
This code is slow because while put()
we are always removing node, creating one then inserting it again even if it exists inside hashMap.
In this case if it exists then just update the value in hashMap and then update linked list.
code:

def put(self, key: int, value: int) -> None:
        if key in self.hashMap:
            node3 = self.hashMap[key]
            node3.value = value
            self.removeNode(self.hashMap[key])
            self.insertNode(self.hashMap[key])
            return
        node3 = Node(key, value)
        self.hashMap[key] = node3
        self.insertNode(self.hashMap[key])   

        if len(self.hashMap) > self.capacity:
            current = self.tail.next
            del self.hashMap[current.key]
            self.removeNode(current)

this made runtime 111ms and beating 74% + solutions.
"""