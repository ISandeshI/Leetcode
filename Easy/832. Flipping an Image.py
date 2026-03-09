# 832. Flipping an Image
# Easy
# Topics
# premium lock icon
# Companies
# Given an n x n binary matrix image, flip the image horizontally, then invert it, and return the resulting image.

# To flip an image horizontally means that each row of the image is reversed.

# For example, flipping [1,1,0] horizontally results in [0,1,1].
# To invert an image means that each 0 is replaced by 1, and each 1 is replaced by 0.

# For example, inverting [0,1,1] results in [1,0,0].
 

# Example 1:

# Input: image = [[1,1,0],[1,0,1],[0,0,0]]
# Output: [[1,0,0],[0,1,0],[1,1,1]]
# Explanation: First reverse each row: [[0,1,1],[1,0,1],[0,0,0]].
# Then, invert the image: [[1,0,0],[0,1,0],[1,1,1]]
# Example 2:

# Input: image = [[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]
# Output: [[1,1,0,0],[0,1,1,0],[0,0,0,1],[1,0,1,0]]
# Explanation: First reverse each row: [[0,0,1,1],[1,0,0,1],[1,1,1,0],[0,1,0,1]].
# Then invert the image: [[1,1,0,0],[0,1,1,0],[0,0,0,1],[1,0,1,0]]
 

# Constraints:

# n == image.length
# n == image[i].length
# 1 <= n <= 20
# images[i][j] is either 0 or 1.


class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        rowLength = len(image)
        xorLength = "1" * rowLength
        xorSecondInteger = int(xorLength, base= 2)

        for i in range(rowLength):
            image[i] = image[i][::-1]
            for j in range(rowLength):
                if image[i][j] == 1:
                    image[i][j] = 0
                else:
                    image[i][j] = 1

        return image
    

"""
Don't refer this it has 3ms runtime beating only 11% + solutions, many have 0ms runtime. 
In memory it is beating 96% + solutions.
use of XOR was in my strategy first. But couldn't think about actual implementation.
following is one of simplest solution:

class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        res=[]
        for i in image:
            i.reverse()
            res.append([x^1 for x in i])
        return res
"""