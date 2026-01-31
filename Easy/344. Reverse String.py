#  344. Reverse String
# Solved
# Easy
# Topics
# premium lock icon
# Companies
# Hint
# Write a function that reverses a string. The input string is given as an array of characters s.

# You must do this by modifying the input array in-place with O(1) extra memory.

 

# Example 1:

# Input: s = ["h","e","l","l","o"]
# Output: ["o","l","l","e","h"]
# Example 2:

# Input: s = ["H","a","n","n","a","h"]
# Output: ["h","a","n","n","a","H"]
 

# Constraints:

# 1 <= s.length <= 105
# s[i] is a printable ascii character.


class Solution:
    def reverseString(self, s):
        new = []
        x = len(s)
        for i in range(x):
            new.append(s[x-1])
            x -=1

        s[:] = new

""" my new learnigs are:
i tried new[i] = s[x-1] but it gave me index error 
because new is empty initially so we cant assign value to any index
 so if there is list which is empty then we cannot assign value to 
 any index directly we have to use append method to add values to it.

in the end i just wrote s = new but it didnt worked because
s is a reference to the original list
 so if we just assign s to new then it will point to new list only
 and original list will remain unchanged
 so to change the original list we have to use s[:] = new
 which will change the contents of original list to new list contents


"""

        """
        Do not return anything, modify s in-place instead.
        """
        