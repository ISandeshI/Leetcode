# 39. Combination Sum
# recursion included
# Medium
# Topics
# premium lock icon
# Companies
# Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.

# The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the frequency of at least one of the chosen numbers is different.

# The test cases are generated such that the number of unique combinations that sum up to target is less than 150 combinations for the given input.

 

# Example 1:

# Input: candidates = [2,3,6,7], target = 7
# Output: [[2,2,3],[7]]
# Explanation:
# 2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
# 7 is a candidate, and 7 = 7.
# These are the only two combinations.
# Example 2:

# Input: candidates = [2,3,5], target = 8
# Output: [[2,2,2,2],[2,3,3],[3,5]]
# Example 3:

# Input: candidates = [2], target = 1
# Output: []
 

# Constraints:

# 1 <= candidates.length <= 30
# 2 <= candidates[i] <= 40
# All elements of candidates are distinct.
# 1 <= target <= 40

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []

        def recursion(currentIndex, currentArray, currentSum):
            if currentSum == target:
                ans.append(list(currentArray))
                return
            
            if currentSum > target:
                return
            
# As you can see we have two didfferent base cases. in both cases terminate further code and return
            
            for i in range(currentIndex, len(candidates)):
                currentArray.append(candidates[i])
                recursion(i, currentArray, currentSum + candidates[i])
                currentArray.pop()


        recursion(0, [], 0)
        return ans
    

"""
Runtime 9ms beating 30% + solutions and in memory beating only 33% + solutions.
I made a lot of mistakes and learned a lot.

for line 46 i wrote: ans.append(currentArray)
this gave wrong copy of currentArray.
why?
basicaly array is memory space, we are just modifying it, so all answers would point 
to the same list object, which keeps changing.
like: [[2,2,3], [2,2,3], [2,2,3]] this would be our final answer.

Now we have two solutions:
1. ans.append(list(currentArray))
we converted current array into separate list and appended it into ans.
2. ans.append(currentArray.copy())
.copy() stores a snapshot of the current combination, it is more faster so next time use it.

-----------------------------------------------------------------------------------------------

for line 52 - 55 i wrote:
for i in range(currentIndex, len(candidates)): 
    recursion(i, currentArray.append(candidates[i]), currentSum + candidates[i]) 
    currentArray.pop()

this gave error, because you cannot change array in place of assignments or arguments of function call.
why?
list.append() does not return the list.
It modifies the list in place and returns None.

Example:
a = [1,2]
b = a.append(3)

print(a)  # [1,2,3]
print(b)  # None

So your call becomes:
recursion(i, None, currentSum + candidates[i])

Then later Python tries:
currentArray.append(...)
but currentArray is now None → error.

so solution is:
Modify the list before recursion, then undo it after recursion.

that's why we wrote:
append first
then recursion call
then pop from list again to explore other sum combinations.

"""