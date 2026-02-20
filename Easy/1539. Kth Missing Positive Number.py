# 1539. Kth Missing Positive Number
# Easy
# Topics
# premium lock icon
# Companies
# Hint
# Given an array arr of positive integers sorted in a strictly increasing order, and an integer k.

# Return the kth positive integer that is missing from this array.

 

# Example 1:

# Input: arr = [2,3,4,7,11], k = 5
# Output: 9
# Explanation: The missing positive integers are [1,5,6,8,9,10,12,13,...]. The 5th missing positive integer is 9.
# Example 2:

# Input: arr = [1,2,3,4], k = 2
# Output: 6
# Explanation: The missing positive integers are [5,6,7,...]. The 2nd missing positive integer is 6.
 

# Constraints:

# 1 <= arr.length <= 1000
# 1 <= arr[i] <= 1000
# 1 <= k <= 1000
# arr[i] < arr[j] for 1 <= i < j <= arr.length

class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
                
        low, high = 0, len(arr) - 1

        while low <= high:
            mid = (low + high) // 2
            missingCount = arr[mid] - (mid + 1)

            if missingCount < k:
                low = mid + 1

            else:
                high = mid - 1

        return low + k


"""
I am dumb. I could not even solve such simple question. Used AI it has runtime of 0ms.

there is another version where we count k from high side. It doesn't matter at last you get your answer 
from low side or high side.:

class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
                
        low, high = 0, len(arr) - 1

        while low <= high:
            mid = (low + high) // 2
            missingCount = arr[mid] - (mid + 1)

            if missingCount < k:
                low = mid + 1

            else:
                high = mid - 1

        missingAtHigh = arr[high] - (high + 1) #this ine becomes useless after following
        return high + k + 1

# arr[high] + (k - missingCount) this we want to return but after solving equation we get that it 
#is similar to high + K + 1
#if you notice now low = high + 1 (in last phase of BS)
#that's the reason in original solution we returned low + k

"""