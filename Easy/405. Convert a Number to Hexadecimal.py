# 405. Convert a Number to Hexadecimal
# Easy
# Topics
# premium lock icon
# Companies
# Given a 32-bit integer num, return a string representing its hexadecimal representation. For negative integers, two’s complement method is used.

# All the letters in the answer string should be lowercase characters, and there should not be any leading zeros in the answer except for the zero itself.

# Note: You are not allowed to use any built-in library method to directly solve this problem.

 

# Example 1:

# Input: num = 26
# Output: "1a"
# Example 2:

# Input: num = -1
# Output: "ffffffff"
 

# Constraints:

# -231 <= num <= 231 - 1

class Solution:
    def toHex(self, num: int):

        map1 = {0 :'0', 1:'1', 2:'2', 3:'3', 4:'4',
               5:'5', 6:'6', 7:'7', 8:'8',
                9:'9', 10:'a', 11:'b', 12:'c', 13:'d', 14:'e', 15:'f'}

        num &= 0xFFFFFFFF

        # if num < 0:
        #   num += 2**32 this is also alternate version for above line

        if num == 0:
            return '0'
        
        else:
            string = ""
            while num > 0:
                string += map1[num % 16]
                num //= 16
                
            return string[::-1]





"""
This runs in 0ms. obviously because AI helped.
Following was my code where everything is done manually. This code is not correct at all conditions.
This was rejected by leetcode. This gave Memory limit exceed (MLE) error.
core idea about two's complement taking a lot to proceed. eventualy you have to know the tricks about 
bit manipulations. I used chatgpt to know shortest way to get this two's complement for converting negative
integers.


class Solution:
    def toHex(self, num: int):
        def convertToBinary(number):
                string = ""
                while number > 0:
                    i = number % 2
                    number //= 2
                    string += str(i)
                return string[::-1].zfill(32)
        
        def convertToHex(number):
            string = ""
            while number > 0:
                i = number % 16
                number //= 16
                string += map1[i]
            return string[::-1]


        map1 = {0 :'0', 1:'1', 2:'2', 3:'3', 4:'4',
               5:'5', 6:'6', 7:'7', 8:'8',
                9:'9', 10:'a', 11:'b', 12:'c', 13:'d', 14:'e', 15:'f'}
        
        ansString = ""
        if num < 0:
            oneBitString = '1' * 32
            num = abs(num)
            ansString = convertToBinary(num)

            xorNumber = int(oneBitString, base= 2) ^ int(ansString, base= 2)
            ansString = convertToBinary(xorNumber)
            
            for i in range(31, 0, -1):
                if ansString[i] == '1':
                    ansString = ansString[:i] + '0' + ansString[i+1:]
                else:
                    ansString = ansString[:i] + '1' + ansString[i+1:]
                    break

            j = 31
            sum = 0
            for k in range(32):
                sum += int(ansString[k]) * (2 ** j)
                j -= 1

            ansString = convertToHex(sum)

            return ansString
        
        elif num == 0:
            return '0'
        
        else:
            ansString = convertToHex(num)
            return ansString

"""