# 1550. Three Consecutive Odds
# Easy
# Topics
# premium lock icon
# Companies
# Hint
# Given an integer array arr, return true if there are three consecutive odd numbers in the array. Otherwise, return false.
 

# Example 1:

# Input: arr = [2,6,4,1]
# Output: false
# Explanation: There are no three consecutive odds.
# Example 2:

# Input: arr = [1,2,34,3,4,5,7,23,12]
# Output: true
# Explanation: [5,7,23] are three consecutive odds.
 

# Constraints:

# 1 <= arr.length <= 1000
# 1 <= arr[i] <= 1000

class Solution:
    def threeConsecutiveOdds(self, arr: List[int]):
        i = 0
        while i < len(arr) - 2:
            if arr[i] % 2 == 0:
                i += 1

            else:
                if arr[i+1] % 2 == 0:
                    i += 2
                else:
                    if arr[i+2] % 2 == 0:
                        i += 3
                    else:
                        return True
                    
        return False


"""
This is among top solutions with 0ms runtime.
I was still thinking about how to optimize the code using less conditions.
May be using recursion or a different approach.

Following is good approach, Although it will check same if statemtents multiple times.
It is still clean and easy to understand

class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        count = 0

        for num in arr:
            if num % 2:
                count += 1
                if count == 3:
                    return True
            else:
                count = 0

        return False

"""
