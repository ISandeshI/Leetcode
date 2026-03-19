# Print N-bit binary numbers having more 1s than 0s
# recursion included
# Difficulty: MediumAccuracy: 56.08%Submissions: 51K+Points: 4
# Given a positive integer n. Your task is to generate a string list of all n-bit binary numbers where, for any prefix of the number, there are more or an equal number of 1's than 0's. The numbers should be sorted in decreasing order of magnitude.

# Example 1:

# Input:  
# n = 2
# Output: 
# {"11", "10"}
# Explanation: Valid numbers are those where each prefix has more 1s than 0s:
# 11: all its prefixes (1 and 11) have more 1s than 0s.
# 10: all its prefixes (1 and 10) have more 1s than 0s.
# So, the output is "11, 10".
# Example 2:

# Input:  
# n = 3
# Output: 
# {"111", "110", "101"}
# Explanation: Valid numbers are those where each prefix has more 1s than 0s.
# 111: all its prefixes (1, 11, and 111) have more 1s than 0s.
# 110: all its prefixes (1, 11, and 110) have more 1s than 0s.
# 101: all its prefixes (1, 10, and 101) have more 1s than 0s.
# So, the output is "111, 110, 101".
# User Task:
# Your task is to complete the function NBitBinary() which takes a single integer n as input and returns the list of strings in decreasing order. You need not take any input or print anything.

# Expected Time Complexity: O(|2n|)
# Expected Auxiliary Space: O(2n)

# Constraints:
# 1 <= n <= 15

#User function Template for python3
class Solution:
	def NBitBinary(self, n):
        fixedHalf = "1"
        remainingLength = n - 1
        zeroMaxCount = remainingLength // 2
        ans = []

        def recursion(currentIndex, currentString):
            if currentIndex == remainingLength:
                  ans.append(fixedHalf + currentString)
                  return
            
            recursion(currentIndex + 1, currentString + "1")                
            if currentString.count("1") >= currentString.count("0"):
                  recursion(currentIndex + 1, currentString + "0") 
            

        recursion(0, "")
        return ans
      


"""
Above solution is way much over-engineered. Do not refer it.
Following is much simpler version, It has same logic of Leetcode 22, parenthesis problem, we just using
1's and 0's, condition is same starting has to be 1, and then balance further combinations. Just like
"(" and ")":


class Solution:
	def NBitBinary(self, n):
        ans = []

        def recursion(currentIndex, currentString):
            if currentIndex == n:
                  ans.append(currentString)
                  return
            
            recursion(currentIndex + 1, currentString + "1")                
            if currentString.count("1") > currentString.count("0"):
                  recursion(currentIndex + 1, currentString + "0") 
            
        recursion(0, "")
        return ans

"""