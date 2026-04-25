# 355. Design Twitter
# Medium
# Topics
# premium lock icon
# Companies
# Design a simplified version of Twitter where users can post tweets, follow/unfollow another user, and is able to see the 10 most recent tweets in the user's news feed.

# Implement the Twitter class:

# Twitter() Initializes your twitter object.
# void postTweet(int userId, int tweetId) Composes a new tweet with ID tweetId by the user userId. Each call to this function will be made with a unique tweetId.
# List<Integer> getNewsFeed(int userId) Retrieves the 10 most recent tweet IDs in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user themself. Tweets must be ordered from most recent to least recent.
# void follow(int followerId, int followeeId) The user with ID followerId started following the user with ID followeeId.
# void unfollow(int followerId, int followeeId) The user with ID followerId started unfollowing the user with ID followeeId.
 

# Example 1:

# Input
# ["Twitter", "postTweet", "getNewsFeed", "follow", "postTweet", "getNewsFeed", "unfollow", "getNewsFeed"]
# [[], [1, 5], [1], [1, 2], [2, 6], [1], [1, 2], [1]]
# Output
# [null, null, [5], null, null, [6, 5], null, [5]]

# Explanation
# Twitter twitter = new Twitter();
# twitter.postTweet(1, 5); // User 1 posts a new tweet (id = 5).
# twitter.getNewsFeed(1);  // User 1's news feed should return a list with 1 tweet id -> [5]. return [5]
# twitter.follow(1, 2);    // User 1 follows user 2.
# twitter.postTweet(2, 6); // User 2 posts a new tweet (id = 6).
# twitter.getNewsFeed(1);  // User 1's news feed should return a list with 2 tweet ids -> [6, 5]. Tweet id 6 should precede tweet id 5 because it is posted after tweet id 5.
# twitter.unfollow(1, 2);  // User 1 unfollows user 2.
# twitter.getNewsFeed(1);  // User 1's news feed should return a list with 1 tweet id -> [5], since user 1 is no longer following user 2.
 

# Constraints:

# 1 <= userId, followerId, followeeId <= 500
# 0 <= tweetId <= 104
# All the tweets have unique IDs.
# At most 3 * 104 calls will be made to postTweet, getNewsFeed, follow, and unfollow.
# A user cannot follow himself.


from collections import defaultdict
import heapq
class Twitter:

    def __init__(self):
        self.timeCount = 0
        self.tweetMap = defaultdict(list) #this will store own tweets
        self.followeeMap = defaultdict(set) #this will store to whom you follow

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append([self.timeCount, tweetId])
        self.timeCount -= 1
        # heapq don't have max heap method. so we give negative value to our max element, 
        # in this case this is latest tweet so we gave it less number which is higher negative number

    def getNewsFeed(self, userId: int) -> List[int]:
        result = [] #10 tweets will be added here
        minHeap = [] #top 10 will be chosen from all stored in here

        self.followeeMap[userId].add(userId)
        # user will also see his own tweets if he's in top 10, so he is added in his own followee list

        for followeeId in self.followeeMap[userId]:
            if followeeId in self.tweetMap: #there's a chance this user never tweeted, so use of retrieving his tweets
                index = len(self.tweetMap[followeeId]) - 1
                count, tweetId = self.tweetMap[followeeId][index]
                heapq.heappush(minHeap, (count, tweetId, followeeId, index - 1))
                # we did index - 1 here for future reference, just in case if next tweet is on highest priority

        while minHeap and len(result) < 10:
            count, tweetId, followeeId, index = heapq.heappop(minHeap)
            result.append(tweetId)

            if index >= 0:
                count, tweetId = self.tweetMap[followeeId][index]
                heapq.heappush(minHeap, (count, tweetId, followeeId, index - 1))

        return result


    def follow(self, followerId: int, followeeId: int) -> None:
        self.followeeMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followeeMap[followerId]:
            self.followeeMap[followerId].remove(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)

"""
Runtime 12ms beating 67% + solutions and in memory beating only 5% + solutions.
I could not have solved this ever. This is total logic of Neetcode. For more explaination watch:
https://www.youtube.com/watch?v=pNichitDD2E
"""