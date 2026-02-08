# 492. Construct the Rectangle
# Easy
# Topics
# premium lock icon
# Companies
# Hint
# A web developer needs to know how to design a web page's size. So, given a specific rectangular web page’s area, your job by now is to design a rectangular web page, whose length L and width W satisfy the following requirements:

# The area of the rectangular web page you designed must equal to the given target area.
# The width W should not be larger than the length L, which means L >= W.
# The difference between length L and width W should be as small as possible.
# Return an array [L, W] where L and W are the length and width of the web page you designed in sequence.

 

# Example 1:

# Input: area = 4
# Output: [2,2]
# Explanation: The target area is 4, and all the possible ways to construct it are [1,4], [2,2], [4,1]. 
# But according to requirement 2, [1,4] is illegal; according to requirement 3,  [4,1] is not optimal compared to [2,2]. So the length L is 2, and the width W is 2.
# Example 2:

# Input: area = 37
# Output: [37,1]
# Example 3:

# Input: area = 122122
# Output: [427,286]
 

# Constraints:

# 1 <= area <= 107

class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        maxWidth = int(area ** 0.5)

        while area % maxWidth != 0:
            maxWidth -= 1

        length = area // maxWidth

        return [length, maxWidth]





"""
I am uselees and felt like donkey. Such a simple problem and yet i managed to make it over compllicated.
Above solution runs in 3ms and 80% + solutions have same runtime.
It is not mine completely stole from AI.

Basic logic:
1. At max width is closest to √area
2. Move downward
3. First divisor you find → optimal width
4. That is what we were doing trying to find max width. If not found then eventualy width will be 1 and
length will be equal to area.

Following code was my first approach based on checking for prime number. this algo was taken from chatgpt.
since the begining i had intuition it is not going to work and that happened.

class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        length = area
        width = 1
        prevArea = area
        while length > width:
            if area % 2 == 0:
                area //= 2
                length //= 2
                width *= 2
            
            elif area % 3 == 0:
                area //= 3
                length //= 3
                width *= 3

            else:
                i = 5
                while i * i <= area:
                    if area % i == 0:
                        area //= i
                        length //= i
                        width *= i
                        break
                        
                    else:
                        if area % (i + 2) == 0:
                            area //= i + 2
                            length //= i + 2
                            width *= i + 2
                            break

                    i += 6

            if prevArea == area:
                break
            else:
                prevArea = area

        return [length, width]

"""