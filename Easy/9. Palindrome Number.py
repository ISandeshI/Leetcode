# 9. Palindrome Number
# Solved
# Easy
# Topics
# premium lock icon
# Companies
# Hint
# Given an integer x, return true if x is a palindrome, and false otherwise.

 

# Example 1:

# Input: x = 121
# Output: true
# Explanation: 121 reads as 121 from left to right and from right to left.
# Example 2:

# Input: x = -121
# Output: false
# Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
# Example 3:

# Input: x = 10
# Output: false
# Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
 

# Constraints:

# -231 <= x <= 231 - 1


class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x >= 0 and x < 10:
            return True
        elif x > 0:
            x = str(x)
            start = 0
            end = (len(x)-1)
            count = int((end+1)/2)
            for i in range(count):
                if(x[start] == x[end]):
                  start += 1
                  end -= 1 

                else:
                    return False

            return True        

        else:
            return False

""" my learning was 0 - 9 are palindrome numbers
i didnt consider this case 
i shoul start using slicing and you should know
str[::-1] means reverse the string
and many of leetcode cases can be solved using this particular slicing technique"""