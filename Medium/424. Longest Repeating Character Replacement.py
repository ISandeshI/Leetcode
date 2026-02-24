# 424. Longest Repeating Character Replacement
# Medium
# Topics
# premium lock icon
# Companies
# You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.

# Return the length of the longest substring containing the same letter you can get after performing the above operations.

 

# Example 1:

# Input: s = "ABAB", k = 2
# Output: 4
# Explanation: Replace the two 'A's with two 'B's or vice versa.
# Example 2:

# Input: s = "AABABBA", k = 1
# Output: 4
# Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
# The substring "BBBB" has the longest repeating letters, which is 4.
# There may exists other ways to achieve this answer too.
 

# Constraints:

# 1 <= s.length <= 105
# s consists of only uppercase English letters.
# 0 <= k <= s.length

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = 0
        left = 0
        hashMap = {}
        
        for right in range(len(s)):
            hashMap[s[right]] = hashMap.get(s[right], 0) + 1
            higestKey = max(hashMap, key = hashMap.get)
            higestKeyValue = hashMap[higestKey]
        
            if (right - left + 1) - higestKeyValue > k:
                hashMap[s[left]] -= 1
                if hashMap[s[left]] == 0:
                    del hashMap[s[left]]

                left += 1

            count = max(count, (right - left + 1))

        return count


"""
This runs but has 162ms of runtime and beats only 41% + solutions in memory.
Many of them have 63ms runtime. This is because we are using max() for finding highest of hasmap's key.
This iterate over all hashmap and check which one is highest in value.
Following is better solution where we keep one variable to check whichever character till the time has 
highest frequency, and check with current one and update accordingly.
code:

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        count = 0
        maxFreq = 0
        hashMap = {}
        
        for right in range(len(s)):
            hashMap[s[right]] = hashMap.get(s[right], 0) + 1
            
            # Update max frequency
            maxFreq = max(maxFreq, hashMap[s[right]])
            
            # If window invalid, shrink
            if (right - left + 1) - maxFreq > k:
                hashMap[s[left]] -= 1
                left += 1
            
            count = max(count, right - left + 1)
        
        return count


"""