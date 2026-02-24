# 771. Jewels and Stones
# Easy
# Topics
# premium lock icon
# Companies
# Hint
# You're given strings jewels representing the types of stones that are jewels, and stones representing the stones you have. Each character in stones is a type of stone you have. You want to know how many of the stones you have are also jewels.

# Letters are case sensitive, so "a" is considered a different type of stone from "A".

 

# Example 1:

# Input: jewels = "aA", stones = "aAAbbbb"
# Output: 3
# Example 2:

# Input: jewels = "z", stones = "ZZ"
# Output: 0
 

# Constraints:

# 1 <= jewels.length, stones.length <= 50
# jewels and stones consist of only English letters.
# All the characters of jewels are unique.

from collections import Counter
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        map1 = Counter(stones)
        set1 = set (jewels)
        count = 0

        for element in set1:
            count += map1[element]

        return count


"""
I thought this would go like pro but it has runtime of 4ms beating only 2% + solutions because others 
have runtime of 0ms and it beats 72% + solutions in memory.
Well creatring hashmap and set is taking bit of time.
Following is clever solution with 0ms:

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        count = 0
        for stone in stones:
            if stone in jewels:
                count += 1
        
        return count
"""