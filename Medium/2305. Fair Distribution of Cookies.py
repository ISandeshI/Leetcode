# 2305. Fair Distribution of Cookies
# recursion included
# Medium
# Topics
# premium lock icon
# Companies
# Hint
# You are given an integer array cookies, where cookies[i] denotes the number of cookies in the ith bag. You are also given an integer k that denotes the number of children to distribute all the bags of cookies to. All the cookies in the same bag must go to the same child and cannot be split up.

# The unfairness of a distribution is defined as the maximum total cookies obtained by a single child in the distribution.

# Return the minimum unfairness of all distributions.

 

# Example 1:

# Input: cookies = [8,15,10,20,8], k = 2
# Output: 31
# Explanation: One optimal distribution is [8,15,8] and [10,20]
# - The 1st child receives [8,15,8] which has a total of 8 + 15 + 8 = 31 cookies.
# - The 2nd child receives [10,20] which has a total of 10 + 20 = 30 cookies.
# The unfairness of the distribution is max(31,30) = 31.
# It can be shown that there is no distribution with an unfairness less than 31.
# Example 2:

# Input: cookies = [6,1,3,2,2,4,1,2], k = 3
# Output: 7
# Explanation: One optimal distribution is [6,1], [3,2,2], and [4,1,2]
# - The 1st child receives [6,1] which has a total of 6 + 1 = 7 cookies.
# - The 2nd child receives [3,2,2] which has a total of 3 + 2 + 2 = 7 cookies.
# - The 3rd child receives [4,1,2] which has a total of 4 + 1 + 2 = 7 cookies.
# The unfairness of the distribution is max(7,7,7) = 7.
# It can be shown that there is no distribution with an unfairness less than 7.
 

# Constraints:

# 2 <= cookies.length <= 8
# 1 <= cookies[i] <= 105
# 2 <= k <= cookies.length

class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        distribution = [0] * k
        ans = float('inf')
        n = len(cookies)

        def backtrack(currentIndex, distArray):
            nonlocal ans
            if currentIndex == n:
                ans = min(ans, max(distArray))
                return
            
            for i in range(k):
                if max(distArray) >= ans:
                    continue
                distArray[i] += cookies[currentIndex]
                backtrack(currentIndex + 1, distArray)
                distArray[i] -= cookies[currentIndex]
                # if distArray[i] == 0:
                #     break


        backtrack(0, distribution)
        return ans

"""
Worst solution ever, Runtime 9710ms Beating 5.16% + solutions only.
Now check line on 61-62, If you add this then we suddenly get runtime 5ms among 58% + solutions.
why?
if distArray[i] == 0:
    break
    
what does this do?
If multiple children currently have 0 cookies, they are indistinguishable.
Example

Initial state:

distribution = [0, 0, 0]
cookies = [8, 5, 3]


At index 0 (cookie = 8):

Without this condition:

You try:

[8, 0, 0]
[0, 8, 0]
[0, 0, 8]


All 3 are identical states (just permuted)

→ Wastes 3X work.

With this condition

After trying:

distribution[0] += 8   → [8, 0, 0]


When backtracking:

distribution[0] = 0


Now:

if distribution[i] == 0:
    break


→ Stops loop immediately
→ Skips trying:

[0, 8, 0]
[0, 0, 8]
"""