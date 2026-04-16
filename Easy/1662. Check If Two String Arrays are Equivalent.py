# 1662. Check If Two String Arrays are Equivalent
# Easy
# Topics
# premium lock icon
# Companies
# Hint
# Given two string arrays word1 and word2, return true if the two arrays represent the same string, and false otherwise.

# A string is represented by an array if the array elements concatenated in order forms the string.

 

# Example 1:

# Input: word1 = ["ab", "c"], word2 = ["a", "bc"]
# Output: true
# Explanation:
# word1 represents string "ab" + "c" -> "abc"
# word2 represents string "a" + "bc" -> "abc"
# The strings are the same, so return true.
# Example 2:

# Input: word1 = ["a", "cb"], word2 = ["ab", "c"]
# Output: false
# Example 3:

# Input: word1  = ["abc", "d", "defg"], word2 = ["abcddefg"]
# Output: true
 

# Constraints:

# 1 <= word1.length, word2.length <= 103
# 1 <= word1[i].length, word2[i].length <= 103
# 1 <= sum(word1[i].length), sum(word2[i].length) <= 103
# word1[i] and word2[i] consist of lowercase letters.

class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        return "".join(word1) == "".join(word2)
    

"""
Runtime 0ms and in memory beating 99% + solutions.
That's it.

Following is best manual way to solve this:

class Solution:
    def arrayStringsAreEqual(self, word1, word2):
        i = j = 0   # index for word1 and word2 lists
        p = q = 0   # index inside each string

        while i < len(word1) and j < len(word2):
            if word1[i][p] != word2[j][q]:
                return False
            
            p += 1
            q += 1

            # move to next string in word1
            if p == len(word1[i]):
                i += 1
                p = 0

            # move to next string in word2
            if q == len(word2[j]):
                j += 1
                q = 0

        # both should finish at same time
        return i == len(word1) and j == len(word2)

"""