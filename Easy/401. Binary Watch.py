# 401. Binary Watch
# Easy
# Topics
# premium lock icon
# Companies
# Hint
# A binary watch has 4 LEDs on the top to represent the hours (0-11), and 6 LEDs on the bottom to represent the minutes (0-59). Each LED represents a zero or one, with the least significant bit on the right.

# For example, the below binary watch reads "4:51".


# Given an integer turnedOn which represents the number of LEDs that are currently on (ignoring the PM), return all possible times the watch could represent. You may return the answer in any order.

# The hour must not contain a leading zero.

# For example, "01:00" is not valid. It should be "1:00".
# The minute must consist of two digits and may contain a leading zero.

# For example, "10:2" is not valid. It should be "10:02".
 

# Example 1:

# Input: turnedOn = 1
# Output: ["0:01","0:02","0:04","0:08","0:16","0:32","1:00","2:00","4:00","8:00"]
# Example 2:

# Input: turnedOn = 9
# Output: []
 

# Constraints:

# 0 <= turnedOn <= 10

class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        res = []
        for h in range(12):        # hours: 0–11
            for m in range(60):    # minutes: 0–59
                if bin(h).count('1') + bin(m).count('1') == turnedOn:
                    str1 = str(h) + ":" + str(100 + m)[1:]
                    res.append(str1)
        return res



"""
I believe this question should have been in hard difficulty.
I just stole whole code from chatgpt and obviously it runs in 0ms.
Although line 42-43 has following alternate:
res.append(f"{h}:{m:02d}")

Try every valid hour (0-11) and minute (0-59).
Convert them to binary.
Count how many LEDs are ON.
If the total equals turnedOn, keep that time.
Apparantly no number can have another combination of integers. Infact coincidently number of 1s in binary
at max shows integer representation on clock in same value.
So binary conversion directly works here.
----------------------------------------------------------------------------------------------

Following is alternate backtracking method that any talented programer should have figured out.
I am dumb and still didn't fully understand it yet:

from typing import List

class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        res = []
        
        leds = [1, 2, 4, 8, 1, 2, 4, 8, 16, 32]

        def backtrack(index, count, hour, minute):
            # Too many LEDs ON
            if hour > 11 or minute > 59:
                return
            
            # Required LEDs ON
            if count == turnedOn:
                res.append(f"{hour}:{minute:02d}")
                return
            
            # No LEDs left
            if index == 10:
                return
            
            # 🔹 Option 1: turn ON this LED
            if index < 4:
                backtrack(index + 1, count + 1, hour + leds[index], minute)
            else:
                backtrack(index + 1, count + 1, hour, minute + leds[index])
            
            # 🔹 Option 2: keep this LED OFF
            backtrack(index + 1, count, hour, minute)

        backtrack(0, 0, 0, 0)
        return res


"""

