# 126. Word Ladder II
# Graph Included
# Hard
# Topics
# premium lock icon
# Companies
# A transformation sequence from word beginWord to word endWord using a dictionary wordList is a sequence of words beginWord -> s1 -> s2 -> ... -> sk such that:

# Every adjacent pair of words differs by a single letter.
# Every si for 1 <= i <= k is in wordList. Note that beginWord does not need to be in wordList.
# sk == endWord
# Given two words, beginWord and endWord, and a dictionary wordList, return all the shortest transformation sequences from beginWord to endWord, or an empty list if no such sequence exists. Each sequence should be returned as a list of the words [beginWord, s1, s2, ..., sk].

 

# Example 1:

# Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
# Output: [["hit","hot","dot","dog","cog"],["hit","hot","lot","log","cog"]]
# Explanation: There are 2 shortest transformation sequences:
# "hit" -> "hot" -> "dot" -> "dog" -> "cog"
# "hit" -> "hot" -> "lot" -> "log" -> "cog"
# Example 2:

# Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]
# Output: []
# Explanation: The endWord "cog" is not in wordList, therefore there is no valid transformation sequence.
 

# Constraints:

# 1 <= beginWord.length <= 5
# endWord.length == beginWord.length
# 1 <= wordList.length <= 500
# wordList[i].length == beginWord.length
# beginWord, endWord, and wordList[i] consist of lowercase English letters.
# beginWord != endWord
# All the words in wordList are unique.
# The sum of all shortest transformation sequences does not exceed 105.

from collections import defaultdict, deque
class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        wordSet = set(wordList)
        # Fast lookup → O(1)
        # We will check thousands of words during BFS

        if endWord not in wordSet:
            return []

        # Step 1: BFS to build parent graph
        parents = defaultdict(list)
        level = {beginWord}
        # starting from the current BFS layer
        
        found = False

        while level and not found:
            next_level = set()
            for word in level:
                wordSet.discard(word)

            for word in level:
                for i in range(len(word)):
                    for c in 'abcdefghijklmnopqrstuvwxyz':
                        new_word = word[:i] + c + word[i+1:]
                        
                        if new_word in wordSet:
                            next_level.add(new_word)
                            parents[new_word].append(word)

                            if new_word == endWord:
                                found = True
            
            level = next_level

        # Step 2: Backtrack to build paths
        res = []

        def backtrack(word, path):
            if word == beginWord:
                res.append(path[::-1])
                return
            
            for parent in parents[word]:
                backtrack(parent, path + [parent])

        if found:
            backtrack(endWord, [endWord])

        return res
    

"""
Runtime is 27ms beating only 65% + solutions and in memory beating 88% + solutions.
This is complete AI generated answer, I just couldn't solve this, saw countless videos but it is no help.
same problem on GFG.
"""