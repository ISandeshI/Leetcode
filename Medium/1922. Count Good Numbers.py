# 1922. Count Good Numbers
# recursion included
# Medium
# Topics
# premium lock icon
# Companies
# Hint
# A digit string is good if the digits (0-indexed) at even indices are even and the digits at odd indices are prime (2, 3, 5, or 7).

# For example, "2582" is good because the digits (2 and 8) at even positions are even and the digits (5 and 2) at odd positions are prime. However, "3245" is not good because 3 is at an even index but is not even.
# Given an integer n, return the total number of good digit strings of length n. Since the answer may be large, return it modulo 109 + 7.

# A digit string is a string consisting of digits 0 through 9 that may contain leading zeros.

 

# Example 1:

# Input: n = 1
# Output: 5
# Explanation: The good numbers of length 1 are "0", "2", "4", "6", "8".
# Example 2:

# Input: n = 4
# Output: 400
# Example 3:

# Input: n = 50
# Output: 564908303
 

# Constraints:

# 1 <= n <= 1015


class Solution:
    def countGoodNumbers(self, n: int) -> int:
        if n % 2 == 1:
            y = (n // 2) + 1
            x= y - 1
        else:
            y = n // 2
            x = y

        foursPower = x
        fivesPower = y
        MOD = 10**9 + 7
        
        return (pow(5, y, MOD) * pow(4, x, MOD)) % MOD


"""
Runtime 0ms and in memory beating 97% + solutions
This was easy for me because i already know mathematical formula to get answer. Problem was answer is so big
that we get TLE. To remove TLE i used AI for calculating power of 5 and 4 and at the same time if integer 
range is exceeded then we have to modulo it by our given MOD. so range of integer is intact.
Initialy i wrote following line although i knew calculating 5's and 4's power will give an error.:
return ((5**y) * (4**x)) % MOD

Logic of this query:

at even index we have 5 options: 0,2,4,6,8
at odd index we have 4 options: 2,3,5,7

so using permutation, we will get for length 3: 5*4*5
for lenght 4: 5*4*5*4

and so on....

using this pattern we adjusted our algorithm and solved this problem


------------------------------------------------------------------------------

we created our own power function using recursion:

class Solution:

    def power(self, a, b, MOD):
        if b == 0:
            return 1
        
        half = self.power(a, b // 2, MOD)

        # we are asking to return answer of half size of power
        # ex. if power was 4, then give me first answer when power was 2 and so on....
        
        if b % 2 == 0:
            return (half * half) % MOD

            # if power integer was even means we have to take half twice 
        else:
            return (a * half * half) % MOD
            
            # if power integer was odd means we have to take half twice and base numer one more time.


    def countGoodNumbers(self, n: int) -> int:
        MOD = 10**9 + 7
        
        even_positions = (n + 1) // 2
        odd_positions = n // 2
        
        part1 = self.power(5, even_positions, MOD)
        part2 = self.power(4, odd_positions, MOD)
        
        return (part1 * part2) % MOD


"""
