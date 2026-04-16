# 1239. Maximum Length of a Concatenated String with Unique Characters
# Medium
# Topics
# premium lock icon
# Companies
# Hint
# You are given an array of strings arr. A string s is formed by the concatenation of a subsequence of arr that has unique characters.

# Return the maximum possible length of s.

# A subsequence is an array that can be derived from another array by deleting some or no elements without changing the order of the remaining elements.

 

# Example 1:

# Input: arr = ["un","iq","ue"]
# Output: 4
# Explanation: All the valid concatenations are:
# - ""
# - "un"
# - "iq"
# - "ue"
# - "uniq" ("un" + "iq")
# - "ique" ("iq" + "ue")
# Maximum length is 4.
# Example 2:

# Input: arr = ["cha","r","act","ers"]
# Output: 6
# Explanation: Possible longest valid concatenations are "chaers" ("cha" + "ers") and "acters" ("act" + "ers").
# Example 3:

# Input: arr = ["abcdefghijklmnopqrstuvwxyz"]
# Output: 26
# Explanation: The only string in arr has all 26 characters.
 

# Constraints:

# 1 <= arr.length <= 16
# 1 <= arr[i].length <= 26
# arr[i] contains only lowercase English letters.

class Solution:
    def maxLength(self, arr: List[str]) -> int:
        n = len(arr)
        self.maxCount = 0

        def backtracking(currIndex, currString):
            self.maxCount = max(self.maxCount, len(currString))
            if currIndex == n:
                return

            for i in range(currIndex, n):
                str1 = currString + arr[i]
                if len(str1) == len(set(str1)):
                    backtracking(i + 1, str1)
                else:
                    m = len(arr[i])
                    str1 = str1 [:(-1) * m]
                            
        backtracking(0, "")
        return self.maxCount
    
"""
Runtime is 32ms beating 69% + solutions and in memory beating 94% + solutions.
initialy i used len(counter(str1)) on line 58, that make code much slower.
this is still useless code, there is no need to keep changing str1.
Following is optimized code:

class Solution:
    def maxLength(self, arr: List[str]) -> int:
        n = len(arr)
        self.maxCount = 0

        def backtracking(currIndex, currString):
            self.maxCount = max(self.maxCount, len(currString))

            for i in range(currIndex, n):
                str1 = currString + arr[i]

                # check unique characters
                if len(str1) == len(set(str1)):
                    backtracking(i + 1, str1)

        backtracking(0, "")
        return self.maxCount


"""