# Merge Sort
# recursion included
# Difficulty: MediumAccuracy: 54.1%Submissions: 281K+Points: 4Average Time: 15m
# Given an array arr[], its starting position l and its ending position r. Sort the array using the merge sort algorithm.

# Examples:

# Input: arr[] = [4, 1, 3, 9, 7]
# Output: [1, 3, 4, 7, 9]
# Explanation: We get the sorted array after using merge sort
# Input: arr[] = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
# Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Explanation: We get the sorted array after using merge sort 
# Constraints:
# 1 ≤ arr.size() ≤ 105
# 1 ≤ arr[i] ≤ 105

class Solution:

    def merge(self, leftArray, rightArray):
        n = len(leftArray)
        m = len(rightArray)
        i, j = 0, 0
        result = []

        while i < n and j < m:
            if leftArray[i] <= rightArray[j]:
                result.append(leftArray[i])
                i += 1

            else:
                result.append(rightArray[j])
                j += 1

        while i < n:
            result.append(leftArray[i])
            i += 1

        while j < m:
            result.append(rightArray[j])
            j += 1

        return result


    def mergeSort(self, arr, l, r):
        def recursion(array):
            if len(array) == 1:
                return array
            
            mid = len(array) // 2
            left = recursion(array[:mid])
            right = recursion(array[mid:])

            sortedArray = self.merge(left, right)
            return sortedArray

        arr[:] = recursion(arr)


"""
On the last line i wrote:
arr = recursion(arr)

Creates a new list object
arr now points to a different list
Original list (used by caller) remains unchanged
That's why we got wrong answer.

But:

arr[:] = recursion(arr)

Here, 
arr[:] refers to the entire list slice (same object in memory)
You are replacing contents, not the reference

"""