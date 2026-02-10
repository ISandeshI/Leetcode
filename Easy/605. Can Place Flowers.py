# 605. Can Place Flowers
# Easy
# Topics
# premium lock icon
# Companies
# You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.

# Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, return true if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule and false otherwise.

 

# Example 1:

# Input: flowerbed = [1,0,0,0,1], n = 1
# Output: true
# Example 2:

# Input: flowerbed = [1,0,0,0,1], n = 2
# Output: false
 

# Constraints:

# 1 <= flowerbed.length <= 2 * 104
# flowerbed[i] is 0 or 1.
# There are no two adjacent flowers in flowerbed.
# 0 <= n <= flowerbed.length

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        i = 0
        while i < len(flowerbed):
            mid = flowerbed[i]
            if i == 0:
                left = 0
            else:
                left = flowerbed[i - 1]

            if i == len(flowerbed) - 1:
                right = 0
            else:
                right = flowerbed[i + 1]

            if (left + mid + right) == 0:
                n -= 1
                i +=2
            else:
                i += 1

        return False if n > 0 else True
    
"""
This ran in 11ms. very low
Following is one of the simple solutions:
Here you will see a case where we have to think for indexes which are out of bound of given array.


def canPlaceFlowers(flowerbed, n):
    for i in range(len(flowerbed)):
        if flowerbed[i] == 0:
            left = (i == 0 or flowerbed[i - 1] == 0)
            right = (i == len(flowerbed) - 1 or flowerbed[i + 1] == 0)

            if left and right:
                flowerbed[i] = 1
                n -= 1
                if n <= 0:
                    return True

    return n == 0


"""