# 350. Intersection of Two Arrays II
# Easy
# Topics
# premium lock icon
# Companies
# Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.

 

# Example 1:

# Input: nums1 = [1,2,2,1], nums2 = [2,2]
# Output: [2,2]
# Example 2:

# Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
# Output: [4,9]
# Explanation: [9,4] is also accepted.
 

# Constraints:

# 1 <= nums1.length, nums2.length <= 1000
# 0 <= nums1[i], nums2[i] <= 1000
 

# Follow up:

# What if the given array is already sorted? How would you optimize your algorithm?
# What if nums1's size is small compared to nums2's size? Which algorithm is better?
# What if elements of nums2 are stored on disk, and the memory is limited such that you cannot load all elements into the memory at once?

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]):
        list1 = list(set(nums1).intersection(set(nums2)))
        list2 = []
        for i in list1:
            minCount = min(nums1.count(i), nums2.count(i))
            while minCount > 1:
                list2.append(i)
                minCount -= 1

        list1.extend(list2)
        return list1
    

"""
Above code is worse, it runs in 19ms. 90%+ of solutions have 0ms.
Initialy code output was null because:

return list1.extend(list2)
This line is wrong. extend function returns None
extend() modifies the list in-place and returns None. So i had two following choices:
1. extend first, then return list1
2. OR create a new list and return it

------------------------------------------------------------------------
This is smallest answer. Explaination:

return list((Counter(nums1) & Counter(nums2)).elements())

What does "&" do for Counters?
It keeps only common keys and takes the minimum count.

.elements() converts the Counter back into a sequence:
example: Counter({2: 2, 1: 3}).elements()
-> 2, 2, 1, 1, 1
So, 
Counter(nums1) & Counter(nums2) keeps only common elements and assigns each the 
minimum frequency from both arrays.

.elements() expands this Counter into individual values repeated by their counts, 
and list() converts it to the final intersection list with duplicates.

"""