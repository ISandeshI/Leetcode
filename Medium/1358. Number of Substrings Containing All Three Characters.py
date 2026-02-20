# 1358. Number of Substrings Containing All Three Characters
# Medium
# Topics
# premium lock icon
# Companies
# Hint
# Given a string s consisting only of characters a, b and c.

# Return the number of substrings containing at least one occurrence of all these characters a, b and c.

 

# Example 1:

# Input: s = "abcabc"
# Output: 10
# Explanation: The substrings containing at least one occurrence of the characters a, b and c are "abc", "abca", "abcab", "abcabc", "bca", "bcab", "bcabc", "cab", "cabc" and "abc" (again). 
# Example 2:

# Input: s = "aaacb"
# Output: 3
# Explanation: The substrings containing at least one occurrence of the characters a, b and c are "aaacb", "aacb" and "acb". 
# Example 3:

# Input: s = "abc"
# Output: 1
 

# Constraints:

# 3 <= s.length <= 5 x 10^4
# s only consists of a, b or c characters.


class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        left = 0
        count = 0
        length = len(s)
        counter = {}
        
        for right in range(length):
            counter[s[right]] = counter.get(s[right], 0) + 1
            
            while len(counter) == 3:
                count += (length - right)
                
                counter[s[left]] -= 1
                if counter[s[left]] == 0:
                    del counter[s[left]]
                left += 1
                
        return count


"""
runtime is 97ms and beats only 69% + solurions.
Initialy i used if on line 45 and it didn't calculate correct value. Then i started playing with 
combinations of edge cases and adding smaller codes for them.
Never do such thing at best there is an exceptional case just once.
if your code is getting increased for each exception then it means your core logic is wrong.
"""