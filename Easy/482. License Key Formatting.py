# 482. License Key Formatting
# Easy
# Topics
# premium lock icon
# Companies
# You are given a license key represented as a string s that consists of only alphanumeric characters and dashes. The string is separated into n + 1 groups by n dashes. You are also given an integer k.

# We want to reformat the string s such that each group contains exactly k characters, except for the first group, which could be shorter than k but still must contain at least one character. Furthermore, there must be a dash inserted between two groups, and you should convert all lowercase letters to uppercase.

# Return the reformatted license key.

 

# Example 1:

# Input: s = "5F3Z-2e-9-w", k = 4
# Output: "5F3Z-2E9W"
# Explanation: The string s has been split into two parts, each part has 4 characters.
# Note that the two extra dashes are not needed and can be removed.
# Example 2:

# Input: s = "2-5g-3-J", k = 2
# Output: "2-5G-3J"
# Explanation: The string s has been split into three parts, each part has 2 characters except the first part as it could be shorter as mentioned above.
 

# Constraints:

# 1 <= s.length <= 105
# s consists of English letters, digits, and dashes '-'.
# 1 <= k <= 104

class Solution:
    def licenseKeyFormatting(self, s: str, k: int):
        s = s.upper()
        str2 = ""
        for i in s:
            if i != '-':
                str2 += i

        str2 = str2[::-1]
    
        ans = ""
        j = 0
        while j < len(str2):
            ans += str2[j:j + k]
            if j + k < len(str2):
                ans += '-'
            j += k

        return ans[::-1]
    
"""
This is over-engineered solution. it runs in 7ms.
I learned one thing, as we know strings are immutable so we can write:
str2 = str2[::-1]
in this line we are recreating str2

but we cannot write X
str2[::] = str2[::-1]
in this line we are assigning str2 some value, and str2 is immutable.


Following is a simple solution:
Main logic:
1. Remove dashes
2. Convert letters to uppercase
3. Group characters from the end in size k
4. First group may be shorter

class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        s = s.replace('-', '').upper()
        res = []

        while len(s) > k:
            res.append(s[-k:])
            s = s[:-k]

        if s:
            res.append(s)

        return '-'.join(reversed(res))


"""

 