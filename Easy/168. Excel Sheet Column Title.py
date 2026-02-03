# 168. Excel Sheet Column Title
# Easy
# Topics
# premium lock icon
# Companies
# Given an integer columnNumber, return its corresponding column title as it appears in an Excel sheet.

# For example:

# A -> 1
# B -> 2
# C -> 3
# ...
# Z -> 26
# AA -> 27
# AB -> 28 
# ...
 

# Example 1:

# Input: columnNumber = 1
# Output: "A"
# Example 2:

# Input: columnNumber = 28
# Output: "AB"
# Example 3:

# Input: columnNumber = 701
# Output: "ZY"
 

# Constraints:

# 1 <= columnNumber <= 231 - 1

class Solution:
    def convertToTitle(self, columnNumber: int):
        map = {
            1:'A', 2:'B', 3:'C', 4:'D', 5:'E', 6:'F', 7:'G', 8:'H', 9:'I', 10:'J',
            11:'K', 12:'L', 13:'M', 14:'N', 15:'O', 16:'P', 17:'Q', 18:'R', 19:'S', 20:'T',
            21:'U', 22:'V', 23:'W', 24:'X', 25:'Y', 0:'Z'
        }

        str1 = ""

        while columnNumber > 0:
            reminder = columnNumber % 26
            columnNumber = (columnNumber - 1) // 26
            str1 += map[reminder]

        return str1[::-1]


"""
Above code runs in 0ms.

Following was my previous code:

        while columnNumber > 0:
            reminder = columnNumber % 26
            columnNumber = columnNumber // 26
            str1 += map[reminder]

it will generate extra character, consider 26%26 = 0 ( gives z) 26//26= 1
now 1%26 =1 (gives A)

so there is an extra A. Answer should have been Z only.

to mitigate this we have to reduce columnNumber by 1.
Basically excel indexing start from 1 to 26 so we are converting it into 0 - 25
by reducing columnNumber by 1.


we can also use following code :
26: 'Z' ....

        while columnNumber > 0:
            columnNumber -= 1              #critical fix
            remainder = columnNumber % 26
            result += mp[remainder + 1]
            columnNumber //= 26
-------------------------------------------------------------------------------

This is a standard problem called sliding window and search.
following is code with this:

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        seen = set()

        for i, num in enumerate(nums):
            if num in seen:
                return True

            seen.add(num)

            if len(seen) > k:
                seen.remove(nums[i - k])

        return False
"""