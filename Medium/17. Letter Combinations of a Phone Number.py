# 17. Letter Combinations of a Phone Number
# recursion included
# Medium
# Topics
# premium lock icon
# Companies
# Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

# A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.


 

# Example 1:

# Input: digits = "23"
# Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
# Example 2:

# Input: digits = "2"
# Output: ["a","b","c"]
 

# Constraints:

# 1 <= digits.length <= 4
# digits[i] is a digit in the range ['2', '9'].


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        map = {
            "2": "abc", "3":"def", "4": "ghi", "5": "jkl",
            "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"
        }
        
        ans = []

        def recursion(currentIndex, stringTillNow):
            if currentIndex == len(digits):
                ans.append(stringTillNow)
                return
            
            for char in map[digits[currentIndex]]:
                recursion(currentIndex + 1, stringTillNow + char)
            
        recursion(0, "")
        return ans
    
"""
Runtime 0ms, and in memory beatinf 71% + solutions.
Initialy i made mistake, i learned that in recursion we mostly use return statement in every condition.
But this was not true in this case.
i wrote at line 44:
            for char in map[digits[currentIndex]]:
                recursion(currentIndex + 1, stringTillNow + char)
                return


this causes one thing, our for loop never completed, after first iteration it ends due to return statement.
So, for input: digits = "23"

Output: 
["ad"]

whereas Expected result is:
["ad","ae","af","bd","be","bf","cd","ce","cf"]


"""