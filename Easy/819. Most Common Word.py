# 819. Most Common Word
# Easy
# Topics
# premium lock icon
# Companies
# Given a string paragraph and a string array of the banned words banned, return the most frequent word that is not banned. It is guaranteed there is at least one word that is not banned, and that the answer is unique.

# The words in paragraph are case-insensitive and the answer should be returned in lowercase.

# Note that words can not contain punctuation symbols.

 

# Example 1:

# Input: paragraph = "Bob hit a ball, the hit BALL flew far after it was hit.", banned = ["hit"]
# Output: "ball"
# Explanation: 
# "hit" occurs 3 times, but it is a banned word.
# "ball" occurs twice (and no other word does), so it is the most frequent non-banned word in the paragraph. 
# Note that words in the paragraph are not case sensitive,
# that punctuation is ignored (even if adjacent to words, such as "ball,"), 
# and that "hit" isn't the answer even though it occurs more because it is banned.
# Example 2:

# Input: paragraph = "a.", banned = []
# Output: "a"
 

# Constraints:

# 1 <= paragraph.length <= 1000
# paragraph consists of English letters, space ' ', or one of the symbols: "!?',;.".
# 0 <= banned.length <= 100
# 1 <= banned[i].length <= 10
# banned[i] consists of only lowercase English letters.

import string
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        clean = "".join(" " if ch in string.punctuation else ch for ch in paragraph )
        list1 = clean.lower().split()

        counter = {}
        maxCount = 0
        ans = None

        for char in list1:
            if char not in banned:
                counter[char] = counter.get(char,0) + 1
                if counter[char] > maxCount:
                    ans = char
                    maxCount = counter[char]

        return ans
    

"""
Do not refer this answer it is running multiple operations to get the final answer for handling all the 
edge cases. it has runtime of 6ms beating only 10% + solutions.

sollowing is best:
from collections import defaultdict
import string

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        
        # Convert banned list to set (faster lookup)
        banned = set(banned)
        
        # Replace punctuation with space
        for ch in string.punctuation:
            paragraph = paragraph.replace(ch, " ")
        
        # Convert to lowercase and split into words
        words = paragraph.lower().split()
        
        # Count frequencies
        count = defaultdict(int)
        
        for word in words:
            if word not in banned:
                count[word] += 1
        
        # Return word with highest frequency
        return max(count, key=count.get)

this is most simple, but it's operations take time to have 3ms runtime beating only 63% + solutions.
------------------------------------------------------------------------------------

Following uses regular expression:

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        word_list = re.findall(r'\b\w+\b', paragraph.lower())
        hashmap = defaultdict(int)
        for each in word_list:
            if each not in banned:
                hashmap[each] = hashmap[each] + 1
        return max(hashmap, key=hashmap.get)

        
word_list = re.findall(r'\b\w+\b', paragraph.lower())
in this line we convert everything to lower case and r'\b\w+\b' this will make sure we pick chunks of 
all single or multilength words (number+alphabets combinations).
then store it in list : word_list

What does r'\b\w+\b' mean?
\b → word boundary
\w+ → one or more word characters (letters/numbers)
\b → word boundary

re.findall() It finds all matches of the pattern and returns them in a list.

"""