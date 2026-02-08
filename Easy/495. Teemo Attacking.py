# 495. Teemo Attacking
# Easy
# Topics
# premium lock icon
# Companies
# Our hero Teemo is attacking an enemy Ashe with poison attacks! When Teemo attacks Ashe, Ashe gets poisoned for a exactly duration seconds. More formally, an attack at second t will mean Ashe is poisoned during the inclusive time interval [t, t + duration - 1]. If Teemo attacks again before the poison effect ends, the timer for it is reset, and the poison effect will end duration seconds after the new attack.

# You are given a non-decreasing integer array timeSeries, where timeSeries[i] denotes that Teemo attacks Ashe at second timeSeries[i], and an integer duration.

# Return the total number of seconds that Ashe is poisoned.

 

# Example 1:

# Input: timeSeries = [1,4], duration = 2
# Output: 4
# Explanation: Teemo's attacks on Ashe go as follows:
# - At second 1, Teemo attacks, and Ashe is poisoned for seconds 1 and 2.
# - At second 4, Teemo attacks, and Ashe is poisoned for seconds 4 and 5.
# Ashe is poisoned for seconds 1, 2, 4, and 5, which is 4 seconds in total.
# Example 2:

# Input: timeSeries = [1,2], duration = 2
# Output: 3
# Explanation: Teemo's attacks on Ashe go as follows:
# - At second 1, Teemo attacks, and Ashe is poisoned for seconds 1 and 2.
# - At second 2 however, Teemo attacks again and resets the poison timer. Ashe is poisoned for seconds 2 and 3.
# Ashe is poisoned for seconds 1, 2, and 3, which is 3 seconds in total.
 

# Constraints:

# 1 <= timeSeries.length <= 104
# 0 <= timeSeries[i], duration <= 107
# timeSeries is sorted in non-decreasing order.

class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        totalTime = 0
        for i in range(len(timeSeries) - 1):
            if timeSeries[i + 1] - timeSeries[i] >= duration:
                totalTime += duration
            else:
                totalTime += timeSeries[i + 1] - timeSeries[i]
        totalTime += duration

        return totalTime




"""
Above solution has 19ms of runtime and beats only 39% + solutions.
line 42-45 can be summarize in following single line:

totalTime += min(duration, timeSeries[i + 1] - timeSeries[i])

This make solution smaller and runs in 10ms.

Following solution has 0ms runtime. it checks how long previous poison attack lasts and later
it just add extra time poison is active. This way do not have to calculate last poison attack for extra
last time.

        curr = 0
        res = 0
        for t in timeSeries:
            if t>curr:
                res+=duration
            else:
                res += t+duration-curr
            curr = t+duration
        return res

----------------------------------------------------------------------------
Following approch failed completely with TLE.
Set operation takes a lot of time for durations more than 1000 seconds.
Aproach should be greedy that just calculates times and add it and if time overlaps then add the gaps.

        set1 = set()
        for i in timeSeries:
            for j in range(duration):
                set1.add(i + j)

        return len(set1)

"""