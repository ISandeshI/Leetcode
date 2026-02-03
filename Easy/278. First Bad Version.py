# 278. First Bad Version
# Easy
# Topics
# premium lock icon
# Companies
# You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails the quality check. Since each version is developed based on the previous version, all the versions after a bad version are also bad.

# Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad.

# You are given an API bool isBadVersion(version) which returns whether version is bad. Implement a function to find the first bad version. You should minimize the number of calls to the API.

 

# Example 1:

# Input: n = 5, bad = 4
# Output: 4
# Explanation:
# call isBadVersion(3) -> false
# call isBadVersion(5) -> true
# call isBadVersion(4) -> true
# Then 4 is the first bad version.
# Example 2:

# Input: n = 1, bad = 1
# Output: 1
 

# Constraints:

# 1 <= bad <= n <= 231 - 1



# -------------------------------------------------------------------


# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int):
        low, high = 1, n
        while low <= high:
            mid = (low + high) // 2
            if isBadVersion(mid):
                high = mid
            else:
                low = mid + 1

            if low == high == mid:
                return mid

"""
Looked simple BST problem but it has a twist, so it took me 1 hour to cross check on paper.
Because it has linear chek in ascending order. It is worst solution which takes 51ms runtime.
There are better solutions:
class Solution:
    def firstBadVersion(self, n: int) -> int:
        left, right = 1, n

        while left < right:
            mid = left + (right - left) // 2

            if isBadVersion(mid):
                right = mid      # first bad is at mid or before
            else:
                left = mid + 1   # first bad is after mid

        return left

After watching this, i thik i have overthought.
Check conditions here, low < right
no = sign
and high is staying at mid and only low is moving by one to mid.

We never skip a possible first bad version
Loop ends when left == right
That position must be the first bad version

Common Mistakes (avoid these):
❌ Using <= in loop
while left <= right:   # can cause infinite loop

❌ Returning mid

"""