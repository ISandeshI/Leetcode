# 977. Squares of a Sorted Array
# Easy
# Topics
# premium lock icon
# Companies
# Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

 

# Example 1:

# Input: nums = [-4,-1,0,3,10]
# Output: [0,1,9,16,100]
# Explanation: After squaring, the array becomes [16,1,0,9,100].
# After sorting, it becomes [0,1,9,16,100].
# Example 2:

# Input: nums = [-7,-3,2,3,11]
# Output: [4,9,9,49,121]
 

# Constraints:

# 1 <= nums.length <= 104
# -104 <= nums[i] <= 104
# nums is sorted in non-decreasing order.
 

# Follow up: Squaring each element and sorting the new array is very trivial, could you find an O(n) solution using a different approach?

class Solution:
    def sortedSquares(self, nums: List[int]):
        negSquare = []
        posSquare = []
        finSquare = []
        for num in nums:
            if num < 0:
                negSquare.append(num*num)
            else:
                posSquare.append(num*num)

        if negSquare:
            j = len(negSquare) - 1
            i = 0
            
            while i < len(posSquare) and j >= 0:
                if posSquare[i] < negSquare[j]:
                    finSquare.append(posSquare[i])
                    i += 1
                else:
                    finSquare.append(negSquare[j])
                    j -= 1

            while i < len(posSquare):
                finSquare.append(posSquare[i])
                i += 1

            while j >= 0:
                finSquare.append(negSquare[j])
                j -= 1

            return finSquare

        return posSquare



"""
Welcome top idiots league.
It took me forever to solve this problem. Yet this has 11ms runtime.
And don't even think about the space complexity.
It is in the bottom because we have used three extra arrays.

We could have used two pointers approach to solve this problem in O(1) space complexity.
like: class Solution:
    def sortedSquares(self, nums: List[int]):
        n = len(nums)
        result = [0] * n

        left, right = 0, n - 1
        pos = n - 1

        while left <= right:
            if abs(nums[left]) > abs(nums[right]):
                result[pos] = nums[left] ** 2
                left += 1
            else:
                result[pos] = nums[right] ** 2
                right -= 1
            pos -= 1

        return result


Array is already sorted

Biggest values might be at the edges, left or right.
Largest square comes from:

either leftmost negative
or rightmost positive

So when we get biggest value we place it at the end of result array and move inward.



"""