# 131. Palindrome Partitioning
# recursion included
# Medium
# Topics
# premium lock icon
# Companies
# Given a string s, partition s such that every substring of the partition is a palindrome. Return all possible palindrome partitioning of s.

 

# Example 1:

# Input: s = "aab"
# Output: [["a","a","b"],["aa","b"]]
# Example 2:

# Input: s = "a"
# Output: [["a"]]
 

# Constraints:

# 1 <= s.length <= 16
# s contains only lowercase English letters.

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans = []
        currentList = []
        end = len(s)

        def recursion(currentIndex):
            if currentIndex == end:
                ans.append(currentList.copy())
                return
            
            for endPartition in range(currentIndex, end):
                if self.isPalindrome(s, currentIndex, endPartition):
                    currentList.append(s[currentIndex: endPartition + 1])
                    recursion(endPartition + 1)
                    currentList.pop()
                    
        recursion(0)
        return ans


    def isPalindrome(self, s, left, right):
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1

        return True
    
"""
Runtime 39ms Beating 79.52% + solutions ans in Memory beating 96.63% + solutions.

I didn't do a shit. Neetcode guy did this. He's genious. I still didn't understand by myself. 
I can explain the code but if you asked me to create it from scratch randomly then i am a blank.
"""