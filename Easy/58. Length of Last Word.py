# 58. Length of Last Word
# Given a string s consisting of words and spaces, return the length of the last word in the string.

# A word is a maximal substring consisting of non-space characters only.

 

# Example 1:

# Input: s = "Hello World"
# Output: 5
# Explanation: The last word is "World" with length 5.
# Example 2:

# Input: s = "   fly me   to   the moon  "
# Output: 4
# Explanation: The last word is "moon" with length 4.
# Example 3:

# Input: s = "luffy is still joyboy"
# Output: 6
# Explanation: The last word is "joyboy" with length 6.
 

# Constraints:

# 1 <= s.length <= 104
# s consists of only English letters and spaces ' '.
# There will be at least one word in s.


class Solution:
    def lengthOfLastWord(self, s: str):
        last = len(s) - 1
        
        while last >= 0 and s[last].isalpha() == False:
            last -= 1

        count = 0
        while last >= 0 and s[last].isalpha() == True:
            count += 1
            last -= 1

        return count

    

    """
    i made mistake at 36 and 40, i did not check for last >= 0 condition
    which would have caused index out of range error 
    consider last starts decreasing from 0 to minus values.
    which is invalid index for string s. so i have to check for last >= 0
    this code is still not perfect as its taking 3ms,

    there is best solution using split function also which solves in 0ms

    class Solution:
    def lengthOfLastWord(self, s: str):
        s = s.strip()
        return len(s.split()[-1])

    """
      