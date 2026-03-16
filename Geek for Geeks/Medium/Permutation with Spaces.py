# Permutation with Spaces
# recursion included
# Difficulty: MediumAccuracy: 57.68%Submissions: 35K+Points: 4
# Given a string s, you need to print all possible strings that can be made by placing spaces (zero or one) in between them. The output should be printed in sorted increasing order of strings.

# Example 1:

# Input:
# s = "ABC"
# Output: (A B C)(A BC)(AB C)(ABC)
# Explanation:
# ABC
# AB C
# A BC
# A B C
# These are the possible combination of "ABC".
# Example 2:

# Input:
# s = "BBR"
# Output: (B B R)(B BR)(BB R)(BBR)

# Your Task:  
# You don't need to read input or print anything. Your task is to complete the function permutation() which takes the string s as input parameters and returns the sorted array of the string denoting the different permutations (DON'T ADD '(' and ')' it will be handled by the driver code only).

# Expected Time Complexity: O(2s)
# Expected Auxiliary Space: O(1)

 

# CONSTRAINTS:
# 1 <= |s| < 10
# s only contains lowercase and Uppercase English letters.


#User function Template for python3


class Solution:

    def permutation(self, s):
        ans = []

        def recursion(currentIndex, stringTillNow):
            if currentIndex == len(s):
                ans.append(stringTillNow)
                return
            
            if currentIndex < len(s) - 1:
                recursion(currentIndex + 1, stringTillNow + s[currentIndex] + " ")
            recursion(currentIndex + 1, stringTillNow + s[currentIndex])            

        recursion(0, "")
        return ans
    

"""
Initialy i did not included if statement, so it was creating extra outputs.
whenever a string is completed then also it generates extra space.
ex. (ABC) != (ABC )
without if statement we get such extra inputs.
But problem statement says you have to treat these two instances as one.
So we have to include only first type which is without trailing space.
So only add (ABC) in the final answer.

To abide this condition we check if currentIndex is last index of "s".
if yes then do not go for adding space ahead of it.
"""
