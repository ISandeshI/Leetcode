# 696. Count Binary Substrings
# Easy
# Topics
# premium lock icon
# Companies
# Hint
# Given a binary string s, return the number of non-empty substrings that have the same number of 0's and 1's, and all the 0's and all the 1's in these substrings are grouped consecutively.

# Substrings that occur multiple times are counted the number of times they occur.

 

# Example 1:

# Input: s = "00110011"
# Output: 6
# Explanation: There are 6 substrings that have equal number of consecutive 1's and 0's: "0011", "01", "1100", "10", "0011", and "01".
# Notice that some of these substrings repeat and are counted the number of times they occur.
# Also, "00110011" is not a valid substring because all the 0's (and 1's) are not grouped together.
# Example 2:

# Input: s = "10101"
# Output: 4
# Explanation: There are 4 substrings: "10", "01", "10", "01" that have equal number of consecutive 1's and 0's.
 

# Constraints:

# 1 <= s.length <= 105
# s[i] is either '0' or '1'.

class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        prev = 0
        curr = 1
        result = 0

        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                curr += 1
            else:
                result += min(prev, curr)
                prev = curr
                curr = 1 #do not forget to add this because i is already pointing to changed character

        result += min(prev, curr)
        #one more time last foundings has to add
        return result







"""
Above solution is AI generated, it runs in 59ms and beats 57% + solutions.
i am too dumb to understand this problem solution, there's a reason why it is in easy section.
someone saw a great combination. for consecutive chars, number of combinations with matching length 
is going to be min of two groups
ex. 11100
possible combinations are 1100,10
here count of 1s = 3, count of 0s = 2
so min is 2 and that is possible combinations.

for detailed explaination:
https://www.youtube.com/watch?v=9N2TwXfTYVY

My initial approach was different and it was right but flawed for larger inputs
Following was code with too much over-engineering and obviously it got TLE for large inputs:

class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        i = 0
        subStringCount = 0
        while i < len(s) - 1:
            sameCount = 1
            sameAsBegining = True
            alternateBit = 'x'
            for j in range(i + 1, len(s)):
                if s[i] == s[j] and sameAsBegining:
                    sameCount += 1
                    continue
                elif s[i] != s[j] and alternateBit == 'x':
                    sameAsBegining = False
                    alternateBit = s[j]
                    alternateCount = 1
                    if sameCount == alternateCount:
                        subStringCount += 1
                        break
                    continue

                if alternateBit == s[j]:
                    alternateCount += 1
                    if sameCount == alternateCount:
                        subStringCount += 1
                        break
                
                else:
                    break

            i += 1

        return subStringCount

"""