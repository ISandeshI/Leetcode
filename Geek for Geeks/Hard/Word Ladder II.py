# Word Ladder II
# Graph Included
# Difficulty: HardAccuracy: 50.0%Submissions: 43K+Points: 8Average Time: 60m
# Given two distinct words startWord and targetWord, and a list denoting wordList of unique words of equal lengths. Find all shortest transformation sequence(s) from startWord to targetWord. You can return them in any order possible.
# Keep the following conditions in mind:

# A word can only consist of lowercase characters.
# Only one letter can be changed in each transformation.
# Each transformed word must exist in the wordList including the targetWord.
# startWord may or may not be part of the wordList.
# Return an empty list if there is no such transformation sequence.
# The first part of this problem can be found here.


# Example 1:

# Input:
# startWord = "der", targetWord = "dfs",
# wordList = {"des","der","dfr","dgt","dfs"}
# Output:
# der dfr dfs
# der des dfs
# Explanation:
# The length of the smallest transformation is 3.
# And the following are the only two ways to get
# to targetWord:-
# "der" -> "des" -> "dfs".
# "der" -> "dfr" -> "dfs".
# Example 2:

# Input:
# startWord = "gedk", targetWord = "geek", 
# wordList = {"geek", "gefk"}
# Output:
# "gedk" -> "geek"

# Your Task:
# You don't need to read or print anything, Your task is to complete the function findSequences() which takes startWord, targetWord and wordList as input parameter and returns a list of list of strings of the shortest transformation sequence from startWord to targetWord.
# Note: You don't have to return -1 in case of no possible sequence. Just return the Empty List.


# Expected Time Compelxity: O(N*(logN * M * 26))
# Expected Auxiliary Space: O(N * M) where N = length of wordList and M = |wordListi|


# Constraints:
# 1 ≤ N ≤ 100
# 1 ≤ M ≤ 10

#User function Template for python3

from collections import defaultdict, deque
class Solution:
    def findSequences(self, startWord, targetWord, wordList):
        wordSet = set(wordList)
        if targetWord not in wordSet:
            return []

        # Step 1: BFS to build parent graph
        parents = defaultdict(list)
        level = {startWord}
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

                            if new_word == targetWord:
                                found = True
            
            level = next_level

        # Step 2: Backtrack to build paths
        res = []

        def backtrack(word, path):
            if word == startWord:
                res.append(path[::-1])
                return
            
            for parent in parents[word]:
                backtrack(parent, path + [parent])

        if found:
            backtrack(targetWord, [targetWord])

        return res
    
"""
Same question in Leetcode 126, I couldn't solved this so used AI. And just copied same answer here with 
variable name changes as per current requirement.
"""