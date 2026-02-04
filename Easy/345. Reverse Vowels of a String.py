# 345. Reverse Vowels of a String
# Easy
# Topics
# premium lock icon
# Companies
# Given a string s, reverse only all the vowels in the string and return it.

# The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

 

# Example 1:

# Input: s = "IceCreAm"

# Output: "AceCreIm"

# Explanation:

# The vowels in s are ['I', 'e', 'e', 'A']. On reversing the vowels, s becomes "AceCreIm".

# Example 2:

# Input: s = "leetcode"

# Output: "leotcede"

 

# Constraints:

# 1 <= s.length <= 3 * 105
# s consist of printable ASCII characters.

class Solution:
    def reverseVowels(self, s: str):
        vowels = "AEIOUaeiou"
        list1 = [] #storing vowels here in series
        list2 = [] #storing those vowels position

        for i, char in enumerate(s):
            if char in vowels:
                list1.append(char)
                list2.append(i)

        list1 = list1[::-1]
        for j in range(len(list2)):
            s = s[:list2[j]] + list1[j] + s[list2[j] + 1:]

        return s
    

"""
This is one of the worst solution out there. 242ms of runtime.
I know two pointers strategy could have been very simplest yet i choose different approach.
Following is solution:
class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels=set("aeiouAEIOU")
        s=list(s)
        left,right=0,len(s)-1
        while left<right:
            if s[left] not in vowels:
                left+=1
            elif s[right] not in vowels:
                right-=1
            else:
                s[left],s[right]=s[right],s[left]
                left+=1
                right-=1
        return "".join(s)
"""