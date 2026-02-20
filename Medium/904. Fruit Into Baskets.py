# 904. Fruit Into Baskets
# Medium
# Topics
# premium lock icon
# Companies
# You are visiting a farm that has a single row of fruit trees arranged from left to right. The trees are represented by an integer array fruits where fruits[i] is the type of fruit the ith tree produces.

# You want to collect as much fruit as possible. However, the owner has some strict rules that you must follow:

# You only have two baskets, and each basket can only hold a single type of fruit. There is no limit on the amount of fruit each basket can hold.
# Starting from any tree of your choice, you must pick exactly one fruit from every tree (including the start tree) while moving to the right. The picked fruits must fit in one of your baskets.
# Once you reach a tree with fruit that cannot fit in your baskets, you must stop.
# Given the integer array fruits, return the maximum number of fruits you can pick.

 

# Example 1:

# Input: fruits = [1,2,1]
# Output: 3
# Explanation: We can pick from all 3 trees.
# Example 2:

# Input: fruits = [0,1,2,2]
# Output: 3
# Explanation: We can pick from trees [1,2,2].
# If we had started at the first tree, we would only pick from trees [0,1].
# Example 3:

# Input: fruits = [1,2,3,2,2]
# Output: 4
# Explanation: We can pick from trees [2,3,2,2].
# If we had started at the first tree, we would only pick from trees [1,2].
 

# Constraints:

# 1 <= fruits.length <= 105
# 0 <= fruits[i] < fruits.length

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        left = 0
        basket = {}
        
        for right in range(len(fruits)):
            basket[fruits[right]] = basket.get(fruits[right], 0) + 1
            
            if len(basket) > 2:
                basket[fruits[left]] -= 1
                if basket[fruits[left]] == 0:
                    del basket[fruits[left]]
                left += 1
                
        return right - left + 1


"""
how above code works if we do not recording maxlength at any point?
until lenght of counter reaches 2, only right is moving forward and left stays same.
if length of counter is more than 2, then we increased left only once and so does right.
so even if in any case counter length is more than 2, still distance between left and right is max of what 
we found till. Just incase if we find bigger distance with counter length is 2, then left again stays 
same and only right moves forward.
so key answer is right is always moving but left is moving strategicaly.

This is AI generated response and much better in complexity. 
i did not understood this question. In this question we have to find logest subarray 
with two distinct integers and return length of this array.
Runtime of 127ms and beats 92% + solutions.

Following is an alternate version which take extra variable to note down max length till the end.
here inside we used while loop for checking sliding window condition. this is most common pattern.
Both are correct and following is more simple to impliment.

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        left = 0
        freq = {}
        max_fruits = 0
        
        for right in range(len(fruits)):
            freq[fruits[right]] = freq.get(fruits[right], 0) + 1
            
            while len(freq) > 2:
                freq[fruits[left]] -= 1
                if freq[fruits[left]] == 0:
                    del freq[fruits[left]]
                left += 1
            
            max_fruits = max(max_fruits, right - left + 1)
            
        return max_fruits

"""