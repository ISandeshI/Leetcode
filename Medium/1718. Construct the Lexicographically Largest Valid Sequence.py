# 1718. Construct the Lexicographically Largest Valid Sequence
# recursion included
# Medium
# Topics
# premium lock icon
# Companies
# Hint
# Given an integer n, find a sequence with elements in the range [1, n] that satisfies all of the following:

# The integer 1 occurs once in the sequence.
# Each integer between 2 and n occurs twice in the sequence.
# For every integer i between 2 and n, the distance between the two occurrences of i is exactly i.
# The distance between two numbers on the sequence, a[i] and a[j], is the absolute difference of their indices, |j - i|.

# Return the lexicographically largest sequence. It is guaranteed that under the given constraints, there is always a solution.

# A sequence a is lexicographically larger than a sequence b (of the same length) if in the first position where a and b differ, sequence a has a number greater than the corresponding number in b. For example, [0,1,9,0] is lexicographically larger than [0,1,5,6] because the first position they differ is at the third number, and 9 is greater than 5.

 

# Example 1:

# Input: n = 3
# Output: [3,1,2,3,2]
# Explanation: [2,3,2,1,3] is also a valid sequence, but [3,1,2,3,2] is the lexicographically largest valid sequence.
# Example 2:

# Input: n = 5
# Output: [5,3,1,4,3,5,2,4,2]
 

# Constraints:

# 1 <= n <= 20

class Solution:
    def constructDistancedSequence(self, n: int) -> List[int]:
        m = ((n * 2) - 1)
        ans = [0] * m
        usedNumber = set()
        
        def backtrack (currIndex):
            if currIndex == m:
                return True
            
            for num in range(n, 0, -1):
                if num in usedNumber:
                    continue
                
                if num > 1 and ((currIndex + num) >= m or ans[currIndex + num]):
                    continue
                
                usedNumber.add(num)
                
                ans[currIndex] = num 
                if num > 1:
                    ans[currIndex + num] = num 
                
                j = currIndex + 1
                while j < m and ans[j]:
                    j += 1
                
                if backtrack(j):
                    return True
                    
                usedNumber.remove(num)
                
                ans[currIndex] = 0 
                if num > 1:
                    ans[currIndex + num] = 0
                    
            return False
            
            
        backtrack (0)
        return ans