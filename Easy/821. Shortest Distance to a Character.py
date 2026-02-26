# 821. Shortest Distance to a Character
# Easy
# Topics
# premium lock icon
# Companies
# Given a string s and a character c that occurs in s, return an array of integers answer where answer.length == s.length and answer[i] is the distance from index i to the closest occurrence of character c in s.

# The distance between two indices i and j is abs(i - j), where abs is the absolute value function.

 

# Example 1:

# Input: s = "loveleetcode", c = "e"
# Output: [3,2,1,0,1,0,0,1,2,2,1,0]
# Explanation: The character 'e' appears at indices 3, 5, 6, and 11 (0-indexed).
# The closest occurrence of 'e' for index 0 is at index 3, so the distance is abs(0 - 3) = 3.
# The closest occurrence of 'e' for index 1 is at index 3, so the distance is abs(1 - 3) = 2.
# For index 4, there is a tie between the 'e' at index 3 and the 'e' at index 5, but the distance is still the same: abs(4 - 3) == abs(4 - 5) = 1.
# The closest occurrence of 'e' for index 8 is at index 6, so the distance is abs(8 - 6) = 2.
# Example 2:

# Input: s = "aaab", c = "b"
# Output: [3,2,1,0]
 

# Constraints:

# 1 <= s.length <= 104
# s[i] and c are lowercase English letters.
# It is guaranteed that c occurs at least once in s.

class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        prevLocation = len(s) - 1
        nextLocation = len(s) - 1
        ans = []
        distance = 0

        j = 0
        for i in range(len(s)):
            while j < len(s) and distance == 0 and s[j] != c:
                j += 1
            if j >= len(s):
                nextLocation = prevLocation
            else:
                nextLocation = j
            distance = min(abs(i - prevLocation), abs(i - nextLocation))
            ans.append(distance)

            if distance == 0:
                prevLocation = j
                j += 1

        return ans


"""
This code has runtime of 0ms and beating only 30% + solutions in memory.
i added a lot of edge case handling and a bit complex code that no one can understand. So never thought 
this will work fine. But sometimes you get surprises. I am sure i won't be able to explain my own code 
in future because all this logic and thinking happened just in my mind and I built this code.

before there was only one line:
nextLocation = j

inplace of 43- 47 lines. This caused error. because this way nextLocation for last occurence will be 
len(s). one more than last index. this gives wrong calculations and so does wrong answers.
So i have to check condition for this case as well.

There is another approach where we compare minimum of :
distance from nearest left 'c'
vs
distance from nearest right 'c'

code:

class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        n = len(s)
        result = [0] * n
        
        # First pass: Left → Right
        prev = float('-inf')
        for i in range(n):
            if s[i] == c:
                prev = i
            result[i] = i - prev
        
        # Second pass: Right → Left
        prev = float('inf')
        for i in range(n - 1, -1, -1):
            if s[i] == c:
                prev = i
            result[i] = min(result[i], prev - i)
        
        return result

check distance from left side and then from right side of occurence and then conclude your answer.

example:

Input
s = "loveleetcode"
c = "e"

Result After First Pass:
(ignoring very large values conceptually)
[∞, ∞, ∞, 0, 1, 0, 0, 1, 2, 3, 4, 0]

Final Result after second loop:
[3, 2, 1, 0, 1, 0, 0, 1, 2, 2, 1, 0]
"""