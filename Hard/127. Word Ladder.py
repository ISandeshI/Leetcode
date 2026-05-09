# 127. Word Ladder
# Graph Included
# Hard
# Topics
# premium lock icon
# Companies
# A transformation sequence from word beginWord to word endWord using a dictionary wordList is a sequence of words beginWord -> s1 -> s2 -> ... -> sk such that:

# Every adjacent pair of words differs by a single letter.
# Every si for 1 <= i <= k is in wordList. Note that beginWord does not need to be in wordList.
# sk == endWord
# Given two words, beginWord and endWord, and a dictionary wordList, return the number of words in the shortest transformation sequence from beginWord to endWord, or 0 if no such sequence exists.

 

# Example 1:

# Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
# Output: 5
# Explanation: One shortest transformation sequence is "hit" -> "hot" -> "dot" -> "dog" -> cog", which is 5 words long.
# Example 2:

# Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]
# Output: 0
# Explanation: The endWord "cog" is not in wordList, therefore there is no valid transformation sequence.
 

# Constraints:

# 1 <= beginWord.length <= 10
# endWord.length == beginWord.length
# 1 <= wordList.length <= 5000
# wordList[i].length == beginWord.length
# beginWord, endWord, and wordList[i] consist of lowercase English letters.
# beginWord != endWord
# All the words in wordList are unique.

from collections import deque, defaultdict
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        
        wordList.append(beginWord)
        n = len(beginWord)
        patternHashMap = defaultdict(list)
        visited = set()
        queue = deque()
        
        # let's create adj list of words reaching other words just by changing onw character

        for word in wordList:
            for i in range(n):
                pattern = word[:i] + "*" + word[i + 1:]
                patternHashMap[pattern].append(word)

        queue.append(beginWord)
        visited.add(beginWord)
        transitionCount = 1

        while queue:
            m = len(queue)
            for j in range(m):
                currWord = queue.popleft()
                if currWord == endWord:
                    return transitionCount
                
                for i in range(n):
                    pattern = currWord[:i] + "*" + currWord[i + 1:]
                    for word1 in patternHashMap[pattern]:
                        if word1 not in visited:
                            queue.append(word1)
                            visited.add(word1)

            transitionCount += 1

        return 0
        # in case when we could transition to some place but not to ending word

"""
Runtime is 51ms beating 88% + solution and in memory beating only 38% + solutions.
No matter what i did, just couldn't solve this problem. So refer the logic of neetcode guy.
If you want, you can just checkout the explaination:
https://www.youtube.com/watch?v=h9iTnkgv05E
"""