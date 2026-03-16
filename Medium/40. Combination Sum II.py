# 40. Combination Sum II
# recursion included
# Medium
# Topics
# premium lock icon
# Companies
# Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.

# Each number in candidates may only be used once in the combination.

# Note: The solution set must not contain duplicate combinations.

 

# Example 1:

# Input: candidates = [10,1,2,7,6,1,5], target = 8
# Output: 
# [
# [1,1,6],
# [1,2,5],
# [1,7],
# [2,6]
# ]
# Example 2:

# Input: candidates = [2,5,2,1,2], target = 5
# Output: 
# [
# [1,2,2],
# [5]
# ]
 

# Constraints:

# 1 <= candidates.length <= 100
# 1 <= candidates[i] <= 50
# 1 <= target <= 30

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        candidates.sort()
        
        def recursion(currentIndex, currentArray, currentSum):
            if currentSum == target:
                ans.append(currentArray.copy())
                return
            
            if currentIndex == len(candidates) or currentSum > target:
                return
            
# As you can see we have two didfferent base cases. in both cases terminate further code and return
            
            for i in range(currentIndex, len(candidates)):
                if i > currentIndex and candidates[i] == candidates[i - 1]:
                    continue

                # if you starting a new loop then ok, otherwise you see previous integer is same then 
                # all the combinatios were calculated already in previous Loop, so skip it
                
                currentArray.append(candidates[i])
                recursion(i + 1, currentArray, currentSum + candidates[i])
                currentArray.pop()


        recursion(0, [], 0)
        return ans
    

"""
Runtime 19ms and beating only 54% + solutions and in memory beating 67% + solurions.


Again i made a lot of mistakes, i wrote initialy:

currentSum += candidates[i]
recursion(i + 1, currentArray, currentSum + candidates[i])

Here you modify the variable itself.
That modification remains for the next loop iteration. So, we get wrong answers.

Correct way:
recursion(i + 1, currentArray, currentSum + candidates[i])

Here:

currentSum + candidates[i]

is just a temporary expression.
It does not modify currentSum.


To make this work we will have to remove sum after recursion is done, so all original variable's come 
to same state.:

                currentArray.append(candidates[i])
                currentSum += candidates[i]
                recursion(i + 1, currentArray, currentSum)
                currentSum -= candidates[i]
                currentArray.pop()

-------------------------------------------------------------------------------

Also question asked not include duplicates combinations.
example:
[[1,2,5],[1,7],[1,6,1],[2,6],[2,1,5],[7,1]]
this was our answer
But
Expected output is:
[[1,1,6],[1,2,5],[1,7],[2,6]]

To resolve this issue, we have to sort the candidates first then if two consecutive integers are same then 
we have to skip the iteration. And thar's what we did.

Also i wrote:
                 if i > 0 and candidates[i] == candidates[i - 1]:
                    continue
                    
i thought let's skip all duplicate characters, but that's not the case. we can take duplicate characters 
just we are not allowed same combination.

example: [1,1,2] is valid even though there are two 1's
but [[1,1,2] , [1,2,1]] see both have same combination of individual integers.

solution:

if i > currentIndex and candidates[i] == candidates[i-1]
This skips duplicates only at the same recursion level.
"""