# 451. Sort Characters By Frequency
# Medium
# Topics
# premium lock icon
# Companies
# Given a string s, sort it in decreasing order based on the frequency of the characters. The frequency of a character is the number of times it appears in the string.

# Return the sorted string. If there are multiple answers, return any of them.

 

# Example 1:

# Input: s = "tree"
# Output: "eert"
# Explanation: 'e' appears twice while 'r' and 't' both appear once.
# So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.
# Example 2:

# Input: s = "cccaaa"
# Output: "aaaccc"
# Explanation: Both 'c' and 'a' appear three times, so both "cccaaa" and "aaaccc" are valid answers.
# Note that "cacaca" is incorrect, as the same characters must be together.
# Example 3:

# Input: s = "Aabb"
# Output: "bbAa"
# Explanation: "bbaA" is also a valid answer, but "Aabb" is incorrect.
# Note that 'A' and 'a' are treated as two different characters.
 

# Constraints:

# 1 <= s.length <= 5 * 105
# s consists of uppercase and lowercase English letters and digits.

from collections import Counter
import heapq
class Solution:
    def frequencySort(self, s: str) -> str:
        hashMap = Counter(s)
        heap1 = []

        for key, freq in hashMap.items():
            heapq.heappush(heap1, (freq, key))

        ans = ""
        for i in range(len(heap1)):
            tup = heapq.heappop(heap1)
            str1 = tup[0] * tup[1]
            ans += str1

        return ans[::-1]
    
"""
Runtime is 5ms beating 85% + Solutions and in memory beating 73% + solutions
I used heapq on purpose just for practise. could have solved in another ways too.
"""