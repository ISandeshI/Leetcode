# Allocate Minimum Pages
# Difficulty: MediumAccuracy: 35.51%Submissions: 371K+Points: 4Average Time: 35m
# Given an array arr[] of integers, where each element arr[i] represents the number of pages in the i-th book. You also have an integer k representing the number of students. The task is to allocate books to each student such that:

# Each student receives atleast one book.
# Each student is assigned a contiguous sequence of books.
# No book is assigned to more than one student.
# The objective is to minimize the maximum number of pages assigned to any student. In other words, out of all possible allocations, find the arrangement where the student who receives the most pages still has the smallest possible maximum.

# Note: If it is not possible to allocate books to all students, return -1.

# Examples:

# Input: arr[] = [12, 34, 67, 90], k = 2
# Output: 113
# Explanation: Allocation can be done in following ways:
# => [12] and [34, 67, 90] Maximum Pages = 191
# => [12, 34] and [67, 90] Maximum Pages = 157
# => [12, 34, 67] and [90] Maximum Pages = 113.
# The third combination has the minimum pages assigned to a student which is 113.
# Input: arr[] = [15, 17, 20], k = 5
# Output: -1
# Explanation: Since there are more students than total books, it's impossible to allocate a book to each student.
# Constraints:
# 1 ≤ arr.size() ≤ 106
# 1 ≤ arr[i], k ≤ 103

class Solution:
    def findPages(self, arr, k):
        if k > len(arr):
            return -1
        
        low, high = max(arr), sum(arr)
        ans = low

        while low <= high:
            mid =(low + high) // 2

            count = 1
            sum1 = 0
            for i in range(len(arr)):
                if sum1 + arr[i] > mid:
                    count += 1
                    sum1 = arr[i]
                    
                else:
                    sum1 += arr[i]

            if count <= k:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1

        return ans
    

"""
Couldn't understand at all so used chatgpt.
For future reference if asked ever minimize the maximum
means in a a case if answer is found, store it in ans, and we still trying to lower it
so do high = mid - 1. Just for checking, if not either way we already store previos best in ans.

"""