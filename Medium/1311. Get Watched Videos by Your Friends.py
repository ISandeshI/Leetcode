# 1311. Get Watched Videos by Your Friends
# Graph Included
# Medium
# Topics
# premium lock icon
# Companies
# Hint
# There are n people, each person has a unique id between 0 and n-1. Given the arrays watchedVideos and friends, where watchedVideos[i] and friends[i] contain the list of watched videos and the list of friends respectively for the person with id = i.

# Level 1 of videos are all watched videos by your friends, level 2 of videos are all watched videos by the friends of your friends and so on. In general, the level k of videos are all watched videos by people with the shortest path exactly equal to k with you. Given your id and the level of videos, return the list of videos ordered by their frequencies (increasing). For videos with the same frequency order them alphabetically from least to greatest. 

 

# Example 1:



# Input: watchedVideos = [["A","B"],["C"],["B","C"],["D"]], friends = [[1,2],[0,3],[0,3],[1,2]], id = 0, level = 1
# Output: ["B","C"] 
# Explanation: 
# You have id = 0 (green color in the figure) and your friends are (yellow color in the figure):
# Person with id = 1 -> watchedVideos = ["C"] 
# Person with id = 2 -> watchedVideos = ["B","C"] 
# The frequencies of watchedVideos by your friends are: 
# B -> 1 
# C -> 2
# Example 2:



# Input: watchedVideos = [["A","B"],["C"],["B","C"],["D"]], friends = [[1,2],[0,3],[0,3],[1,2]], id = 0, level = 2
# Output: ["D"]
# Explanation: 
# You have id = 0 (green color in the figure) and the only friend of your friends is the person with id = 3 (yellow color in the figure).
 

# Constraints:

# n == watchedVideos.length == friends.length
# 2 <= n <= 100
# 1 <= watchedVideos[i].length <= 100
# 1 <= watchedVideos[i][j].length <= 8
# 0 <= friends[i].length < n
# 0 <= friends[i][j] < n
# 0 <= id < n
# 1 <= level < n
# if friends[i] contains j, then friends[j] contains i

from collections import deque, Counter
class Solution:
    def watchedVideosByFriends(self, watchedVideos: List[List[str]], friends: List[List[int]], id: int, level: int) -> List[str]:
        currLevel = 0
        queue = deque()
        set1 = set()
        set1.add(id)
        queue.append(id)

        while queue and currLevel < level:
            for i in range(len(queue)):
                person = queue.popleft()
                for friendOf in friends[person]:
                    if friendOf not in set1:
                        queue.append(friendOf)
                        set1.add(friendOf)

            currLevel += 1

        videos = []
        for i in range(len(queue)):
            for currVideo in watchedVideos[queue[i]]:
                videos.append(currVideo)

        hashMap = Counter(videos)

        result = sorted(hashMap.keys(), key = lambda x: (hashMap[x], x))
        return result
    

"""
Runtime is 20ms beating only 47% + solutions and in memory beating only 37% + solutions.
Hardly able to solve any problems, i have to take help of AI after half of the code.
I am useless.
I should learn how to sort any hashmap with various combinations.
there are keys and values
You have sort in ascending or descending for each of it so total combination is 4.
"""