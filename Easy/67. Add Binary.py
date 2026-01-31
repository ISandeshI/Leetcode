# 67. Add Binary
# Easy
# Topics
# premium lock icon
# Companies
# Given two binary strings a and b, return their sum as a binary string.

 

# Example 1:

# Input: a = "11", b = "1"
# Output: "100"
# Example 2:

# Input: a = "1010", b = "1011"
# Output: "10101"
 

# Constraints:

# 1 <= a.length, b.length <= 104
# a and b consist only of '0' or '1' characters.
# Each string does not contain leading zeros except for the zero itself.


class Solution:
    def addBinary(self, a: str, b: str):
        maxLength = max(len(a), len(b))
        addition = ""
        carryBit = 0
        for i in range(maxLength):
            a_Current = len(a) - 1 - i
            b_Current = len(b) - 1 - i
            if a_Current < 0:
                a_Bit = 0
            else:
                a_Bit = int(a[a_Current:a_Current + 1])
            
            if b_Current < 0:
                b_Bit = 0
            else:
                b_Bit = int(b[b_Current:b_Current + 1])

            sumVal = a_Bit + b_Bit + carryBit
            carryBit = sumVal // 2
            totalVal = sumVal % 2

            addition += str(totalVal)

        if carryBit:
            addition += str(carryBit)

        return addition[::-1]
    

    """"
    Did not cheat and did not use built-in functions to convert to decimal and back.

    This solution run in 5ms runtime. There are better solutions:
    class Solution:
    def addBinary(self, a: str, b: str) -> str:
        i, j = len(a) - 1, len(b) - 1
        carry = 0
        result = []

        while i >= 0 or j >= 0 or carry:
            total = carry

            if i >= 0:
                total += int(a[i])
                i -= 1

            if j >= 0:
                total += int(b[j])
                j -= 1

            result.append(str(total % 2))
            carry = total // 2

        return "".join(reversed(result))


----------------------------------------------------------------

Following is the solution using built-in functions:
return bin(int(a, 2) + int(b, 2))[2:]

int(a, 2)
a is a binary string (e.g. "1010")

2 tells Python: “this number is in base-2”

int("1010", 2)  # → 10 (decimal)
int("1011", 2)  # → 11
So:

int(a, 2) + int(b, 2)
becomes:

10 + 11 = 21
🔹 Step 2: bin(...)
bin(21)
Converts an integer to binary string

BUT Python adds a prefix "0b" to indicate that it’s a binary number:
bin(21)  # → '0b10101'
To remove the "0b" prefix, we can slice the string starting from index 2:
bin(21)[2:]  # → '10101'

    
    """

