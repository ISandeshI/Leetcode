# 784. Letter Case Permutation
# recursion included
# Medium
# Topics
# premium lock icon
# Companies
# Given a string s, you can transform every letter individually to be lowercase or uppercase to create another string.

# Return a list of all possible strings we could create. Return the output in any order.

 

# Example 1:

# Input: s = "a1b2"
# Output: ["a1b2","a1B2","A1b2","A1B2"]
# Example 2:

# Input: s = "3z4"
# Output: ["3z4","3Z4"]
 

# Constraints:

# 1 <= s.length <= 12
# s consists of lowercase English letters, uppercase English letters, and digits.

class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        ans = []
        
        def recursion(currentIndex, stringTillNow):
            if currentIndex == len(s):
                ans.append(stringTillNow)
                return
            
            if s[currentIndex].isalpha():
                recursion(currentIndex + 1, stringTillNow + s[currentIndex].lower())
                recursion(currentIndex + 1, stringTillNow + s[currentIndex].upper())

            else:
                recursion(currentIndex + 1, stringTillNow + s[currentIndex])

        recursion(0, "")
        return ans
    
"""
Runtime is 7ms and beating only 46% + solutions and in memory beating only 62% + solutions.
Not many complications, You just have to have a knowledge of some string functions.
Logic using recursion:
1. chck if character is alphabet then check all further backtracking of when current character is in 
uppercase and then for lower case
2. if character is an integer, then just check backtracking for further string characters.

There is another function swapcase() in strings. it just converts current character in opposite case.
if lower then to upper and
if upper then to lower.

then code becomes on line 38 -39:

                recursion(currentIndex + 1, stringTillNow + s[currentIndex].swapcase())
                recursion(currentIndex + 1, stringTillNow + s[currentIndex])

this makes code runtime 3ms and beating 90% + solutions.

"""