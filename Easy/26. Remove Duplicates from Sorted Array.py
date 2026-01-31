# 26. Remove Duplicates from Sorted Array
# Easy
# Topics
# premium lock icon
# Companies
# Hint
# Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same.

# Consider the number of unique elements in nums to be k​​​​​​​​​​​​​​. After removing duplicates, return the number of unique elements k.

# The first k elements of nums should contain the unique numbers in sorted order. The remaining elements beyond index k - 1 can be ignored.

# Custom Judge:

# The judge will test your solution with the following code:

# int[] nums = [...]; // Input array
# int[] expectedNums = [...]; // The expected answer with correct length

# int k = removeDuplicates(nums); // Calls your implementation

# assert k == expectedNums.length;
# for (int i = 0; i < k; i++) {
#     assert nums[i] == expectedNums[i];
# }
# If all assertions pass, then your solution will be accepted.

 

# Example 1:

# Input: nums = [1,1,2]
# Output: 2, nums = [1,2,_]
# Explanation: Your function should return k = 2, with the first two elements of nums being 1 and 2 respectively.
# It does not matter what you leave beyond the returned k (hence they are underscores).
# Example 2:

# Input: nums = [0,0,1,1,1,2,2,3,3,4]
# Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
# Explanation: Your function should return k = 5, with the first five elements of nums being 0, 1, 2, 3, and 4 respectively.
# It does not matter what you leave beyond the returned k (hence they are underscores).
 

# Constraints:

# 1 <= nums.length <= 3 * 104
# -100 <= nums[i] <= 100
# nums is sorted in non-decreasing order.

class Solution:
    def removeDuplicates(self, nums: List[int]):
        i = 0
        for j in range(len(nums)- 1):
            if nums[i] != nums[i+1]:
                i += 1

            else:
                nums.pop(i+1)

        return i + 1


"""
This is the worst solution possible because popping from a list is O(n) operation.
It has 55ms runtime on Leetcode which is not good for such an easy problem.

Following is a best solution:
        k = 1  # index for next unique element

        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[k] = nums[i]
                k += 1

        return k


I knew this pattern but i was not able to address basic issues.
We know that popping take more time so we should avoid it.
In the begining i thought how to avoid first index swap becauase it is unnecessary.

Above solution shows perfectly start from index 1 and compare with previous index.
As usual one pointer moves consistently by 1 and other pointer moves only when unique element is found.

This is a reminder about how to use same pattern based on given constraints.
If we have used it from 0 index then we have to handle first index swap which is unnecessary just in case 
same element is at starting indexes.

So always think about constraints and how to use them to optimize your solution.

"""