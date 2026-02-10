# 434. Number of Segments in a String
# Easy
# Topics
# premium lock icon
# Companies
# Given a string s, return the number of segments in the string.

# A segment is defined to be a contiguous sequence of non-space characters.

 

# Example 1:

# Input: s = "Hello, my name is John"
# Output: 5
# Explanation: The five segments are ["Hello,", "my", "name", "is", "John"]
# Example 2:

# Input: s = "Hello"
# Output: 1
 

# Constraints:

# 0 <= s.length <= 300
# s consists of lowercase and uppercase English letters, digits, or one of the following characters "!@#$%^&*()_+-=',.:".
# The only space character in s is ' '.

class Solution:
    def countSegments(self, s: str) -> int:
        list1 = s.split()
        return len(list1)
    
"""
This runs in 0ms.
initialy i wrote:
list1 = s.split(" ")
return len(list1)

here  space in split function as an argument cause huge problem.
whenever s = '' (empty) or there are multiple spaces it will count each as single count and will create
'' in list1. and this increase list1's length.

Split function without any argument will convert into list with ignoring on 
any whitespace (spaces, tabs, newlines).
---------------------------------------------------------------------------

Following is manual way of checking:
class Solution:
    def countSegments(self, s: str) -> int:
        count = 0
        in_word = False

        for ch in s:
            if ch != " " and not in_word:
                count += 1
                in_word = True
            elif ch == " ":
                in_word = False

        return count

"""