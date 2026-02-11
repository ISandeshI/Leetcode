# 415. Add Strings
# Easy
# Topics
# premium lock icon
# Companies
# Given two non-negative integers, num1 and num2 represented as string, return the sum of num1 and num2 as a string.

# You must solve the problem without using any built-in library for handling large integers (such as BigInteger). You must also not convert the inputs to integers directly.

 

# Example 1:

# Input: num1 = "11", num2 = "123"
# Output: "134"
# Example 2:

# Input: num1 = "456", num2 = "77"
# Output: "533"
# Example 3:

# Input: num1 = "0", num2 = "0"
# Output: "0"
 

# Constraints:

# 1 <= num1.length, num2.length <= 104
# num1 and num2 consist of only digits.
# num1 and num2 don't have any leading zeros except for the zero itself.

class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        maxLength = max(len(num1), len(num2))
        map1 = { '1': 1, '2': 2, '3': 3, '4': 4, '5': 5,
                '6': 6, '7': 7, '8': 8, '9': 9, '0': 0
                }
        
        map2 = { 1: '1', 2: '2', 3:'3', 4: '4', 5: '5',
                6: '6', 7: '7', 8: '8', 9: '9', 0: '0'
                }
        
        i, j = 1, 1
        ans = ""
        carry = 0
        while maxLength > 0:
            A, B = 0, 0
            if i < len(num1) + 1:
                A = map1[num1[i * -1]]
            if j < len(num2) + 1:
                B = map1[num2[j * -1]]

            result = A + B + carry
            carry = result // 10
            result = result % 10

            ans += map2[result]

            maxLength -= 1
            i += 1
            j += 1

        if carry:
            ans += map2[carry]

        return ans[::-1]
    

"""
This runs in 3ms and beats only 87% solutions and in memory it is beating 58% solutions.
Problem specificaly told not to use any inbuilt function so this solution doesn't make anyse.
Because i converted single string to digit or each character of string to digit; it is same overall.

there is a different solution which makes this task very easy. Converting given string character to ASCII
and finding difference with character '0' ASCII, it will give same ineteger value.
then do the sum, and convert back ASCII to integer:

class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        i = len(num1) - 1
        j = len(num2) - 1
        carry = 0
        result = []

        while i >= 0 or j >= 0 or carry:
            d1 = ord(num1[i]) - ord('0') if i >= 0 else 0
            d2 = ord(num2[j]) - ord('0') if j >= 0 else 0

            total = d1 + d2 + carry
            carry = total // 10
            result.append(chr(total % 10 + ord('0')))

            i -= 1
            j -= 1

        return "".join(result[::-1])

"""