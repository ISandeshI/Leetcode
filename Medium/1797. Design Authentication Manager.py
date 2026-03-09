# 1797. Design Authentication Manager
# Medium
# Topics
# premium lock icon
# Companies
# Hint
# There is an authentication system that works with authentication tokens. For each session, the user will receive a new authentication token that will expire timeToLive seconds after the currentTime. If the token is renewed, the expiry time will be extended to expire timeToLive seconds after the (potentially different) currentTime.

# Implement the AuthenticationManager class:

# AuthenticationManager(int timeToLive) constructs the AuthenticationManager and sets the timeToLive.
# generate(string tokenId, int currentTime) generates a new token with the given tokenId at the given currentTime in seconds.
# renew(string tokenId, int currentTime) renews the unexpired token with the given tokenId at the given currentTime in seconds. If there are no unexpired tokens with the given tokenId, the request is ignored, and nothing happens.
# countUnexpiredTokens(int currentTime) returns the number of unexpired tokens at the given currentTime.
# Note that if a token expires at time t, and another action happens on time t (renew or countUnexpiredTokens), the expiration takes place before the other actions.

 

# Example 1:


# Input
# ["AuthenticationManager", "renew", "generate", "countUnexpiredTokens", "generate", "renew", "renew", "countUnexpiredTokens"]
# [[5], ["aaa", 1], ["aaa", 2], [6], ["bbb", 7], ["aaa", 8], ["bbb", 10], [15]]
# Output
# [null, null, null, 1, null, null, null, 0]

# Explanation
# AuthenticationManager authenticationManager = new AuthenticationManager(5); // Constructs the AuthenticationManager with timeToLive = 5 seconds.
# authenticationManager.renew("aaa", 1); // No token exists with tokenId "aaa" at time 1, so nothing happens.
# authenticationManager.generate("aaa", 2); // Generates a new token with tokenId "aaa" at time 2.
# authenticationManager.countUnexpiredTokens(6); // The token with tokenId "aaa" is the only unexpired one at time 6, so return 1.
# authenticationManager.generate("bbb", 7); // Generates a new token with tokenId "bbb" at time 7.
# authenticationManager.renew("aaa", 8); // The token with tokenId "aaa" expired at time 7, and 8 >= 7, so at time 8 the renew request is ignored, and nothing happens.
# authenticationManager.renew("bbb", 10); // The token with tokenId "bbb" is unexpired at time 10, so the renew request is fulfilled and now the token will expire at time 15.
# authenticationManager.countUnexpiredTokens(15); // The token with tokenId "bbb" expires at time 15, and the token with tokenId "aaa" expired at time 7, so currently no token is unexpired, so return 0.
 

# Constraints:

# 1 <= timeToLive <= 108
# 1 <= currentTime <= 108
# 1 <= tokenId.length <= 5
# tokenId consists only of lowercase letters.
# All calls to generate will contain unique values of tokenId.
# The values of currentTime across all the function calls will be strictly increasing.
# At most 2000 calls will be made to all functions combined.

class Node:
    def __init__(self, tokenId, expiryTime):
        self.tokenId = tokenId
        self.expiryTime = expiryTime
        self.next = None
        self.prev = None

class AuthenticationManager:

    def __init__(self, timeToLive: int):
        self.hashMap = {}
        self.timeToLive =  timeToLive
        self.head = Node(None, None)
        self.tail = Node(None, None)

        self.head.next = self.tail
        self.tail.prev = self.head
        # just like LRU problem we are making dummy end nodes. In future doubly linked list looks like:
        #(Head)<->("aaa",2)<->("bb":6)<->......<->("cccccc":12)<->(Tail)

    def removeNode(self, Node1):
        prevNode = Node1.prev
        frontNode = Node1.next
        prevNode.next = frontNode
        frontNode.prev = prevNode

    def addToTail(self, Node2):
        lastNode = self.tail.prev
        lastNode.next = Node2
        Node2.prev = lastNode
        Node2.next = self.tail
        self.tail.prev = Node2

    def linkedListUpdation(self, currentTime):
        while self.head.next != self.tail and self.head.next.expiryTime <= currentTime:
            del self.hashMap[self.head.next.tokenId]
            self.removeNode(self.head.next)

    def generate(self, tokenId: str, currentTime: int) -> None:
        self.linkedListUpdation(currentTime)
        Node3 = Node(tokenId, currentTime + self.timeToLive)
        self.hashMap[tokenId] = Node3
        self.addToTail(Node3)

    def renew(self, tokenId: str, currentTime: int) -> None:
        self.linkedListUpdation(currentTime)
        if tokenId in self.hashMap:
            Node4 = self.hashMap[tokenId]
            self.removeNode(Node4)
            Node4.expiryTime = currentTime + self.timeToLive
            self.addToTail(Node4)

    def countUnexpiredTokens(self, currentTime: int) -> int:
        self.linkedListUpdation(currentTime)
        return len(self.hashMap)


# Your AuthenticationManager object will be instantiated and called as such:
# obj = AuthenticationManager(timeToLive)
# obj.generate(tokenId,currentTime)
# obj.renew(tokenId,currentTime)
# param_3 = obj.countUnexpiredTokens(currentTime)

"""
runtime is 8ms and beating 95% + solutions and in memory beating only 8% + solutions.
I used AI since begining to understand approach and for code as well.
This problem could have been solved using only hashmap. Because there are max 2000 calls.
There is another way of using deque(), which is just like linkedlist and readymade by python 
no need code heavy.

If size is big then combo of "hashmap + linkedlist" is best as per time complexity.
Operations
Operation	Time Complexity
generate	O(1)
renew	O(1)
countUnexpiredTokens	O(1) (after cleanup)

Core idea:
1. Created a Node structure containing tokenId, expiry, prev, and next to store token information in a doubly linked list.
2. Maintained a HashMap (tokenId → node) for O(1) lookup of tokens when performing renew().
3. Used a Doubly Linked List to keep tokens ordered by expiry time, with the earliest expiry near the head.
4.Used dummy head and tail nodes to simplify insertion and deletion operations in the linked list.
5. Implemented generate(tokenId, currentTime):
Create a new node with expiry = currentTime + TTL
Add it to the tail of the linked list
Store the node in the hashmap.
6. Implemented renew(tokenId, currentTime):
First remove expired tokens (cleanup)
If the token exists, remove the node from its current position
Update its expiry
Insert it again at the tail.
7. Implemented cleanup(currentTime):
Continuously remove nodes from the head while expiry <= currentTime
Also delete those tokens from the hashmap.
8. Implemented countUnexpiredTokens(currentTime):
Call cleanup(currentTime)
Return len(hashmap).
9. Linked list operations used:
remove(node) → unlink node from list
add_to_tail(node) → insert node before tail.

"""