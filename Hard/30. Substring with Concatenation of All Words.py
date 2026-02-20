# 30. Substring with Concatenation of All Words
# Hard
# Topics
# premium lock icon
# Companies
# You are given a string s and an array of strings words. All the strings of words are of the same length.

# A concatenated string is a string that exactly contains all the strings of any permutation of words concatenated.

# For example, if words = ["ab","cd","ef"], then "abcdef", "abefcd", "cdabef", "cdefab", "efabcd", and "efcdab" are all concatenated strings. "acdbef" is not a concatenated string because it is not the concatenation of any permutation of words.
# Return an array of the starting indices of all the concatenated substrings in s. You can return the answer in any order.

 

# Example 1:

# Input: s = "barfoothefoobarman", words = ["foo","bar"]

# Output: [0,9]

# Explanation:

# The substring starting at 0 is "barfoo". It is the concatenation of ["bar","foo"] which is a permutation of words.
# The substring starting at 9 is "foobar". It is the concatenation of ["foo","bar"] which is a permutation of words.

# Example 2:

# Input: s = "wordgoodgoodgoodbestword", words = ["word","good","best","word"]

# Output: []

# Explanation:

# There is no concatenated substring.

# Example 3:

# Input: s = "barfoofoobarthefoobarman", words = ["bar","foo","the"]

# Output: [6,9,12]

# Explanation:

# The substring starting at 6 is "foobarthe". It is the concatenation of ["foo","bar","the"].
# The substring starting at 9 is "barthefoo". It is the concatenation of ["bar","the","foo"].
# The substring starting at 12 is "thefoobar". It is the concatenation of ["the","foo","bar"].

 

# Constraints:

# 1 <= s.length <= 104
# 1 <= words.length <= 5000
# 1 <= words[i].length <= 30
# s and words[i] consist of lowercase English letters.

from collections import Counter
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:

        if not s or not words:
            return []

        word_len = len(words[0])
        word_count = len(words)
        total_len = word_len * word_count

        word_freq = Counter(words)
        result = []

        for offset in range(word_len):

            left = offset
            count = 0
            window = {}

            for right in range(offset, len(s) - word_len + 1, word_len):

                word = s[right:right + word_len]

                if word in word_freq:

                    window[word] = window.get(word, 0) + 1
                    count += 1

                    while window[word] > word_freq[word]:
                        left_word = s[left:left + word_len]
                        window[left_word] -= 1
                        left += word_len
                        count -= 1

                    if count == word_count:
                        result.append(left)

                else:
                    window.clear()
                    count = 0
                    left = right + word_len

        return result


"""
Above code is AI generated and runs in 24ms and beats 66% + solutions. More important thing is 
it has time complexity of O(n), that is impressive
how this problem solution works:
1. create offset. if word's length is 3, then offset is 3, all further combinations are from 0,1 and 2
check from these indexes in our widow slide because widow will slide with 3 distance each time.
2.counter of words can be created using collections because it is one time thing, but counter for current 
window of 's', which is going to be length of 'words'. create this using left and right pointer.
each time move your right by word's length and manualy add it to counter dictionary of 's'.
check for that word if it is exceeding count compared with word's counter, if yes then move left to right 
by word's length and also decrease counter of that word from left.
3. meanwhile maintain variable count, each time new woed is added increase it, and if deleted then decrease it.
at any iteration of right if this count matches with length of word's. then it is a match of all 
permutation of words. and note down result in an array.
4. in the begining if right do not match with anyone from words, then we have to clear counter that we 
created manualy for 's', and reset the count to zero. Also ther's no point in keeping track of left, now whole 
window is ruined, so move left to nextcoming space of right.

this is clever approach of creating counter of window manualy each time using sliding and adjusting counter 
in specific window, also not to check condition of two counters matching or not each time, because this would cost 
us in runtime. both counters could be big data set, so we create variable 'count' and check if it is matching 
with word's length or not. And we are making sure count will match only if both counters are same.


-------------------------------------------------------------------------------
following solution runs without TLE, but it has worst performance till now.
5650ms of runtime and beats only 21% + solutions. here i created counter for 'words', and each time for
fix length i create counter for 's', check if both matches or not

from collections import Counter
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        result = []
        lengthOfS = len(s)
        str1 = ''.join(words)
        lengthOfWords = len(str1)
        lengthOfSubString = len(words[0])
        words2 = Counter(words)

        for i in range(lengthOfS - lengthOfWords + 1):
            
            counter = Counter(s[k:k+lengthOfSubString] for k in range(i, i + lengthOfWords, lengthOfSubString))
            if counter == words2:
                result.append(i)

        return result
--------------------------------------------------------------------------------
Following solution was using brute force and obviously got TLE 181/182:
from collections import Counter
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        result = []
        lengthOfS = len(s)
        str1 = ''.join(words)
        lengthOfWords = len(str1)
        lengthOfSubString = len(words[0])

        for i in range(lengthOfS - lengthOfWords + 1):
            words2 = Counter(words)
            j = i
            while j <= i + lengthOfWords - lengthOfSubString:
                if s[j:j + lengthOfSubString] in words2 and words2[s[j:j + lengthOfSubString]] > 0:
                    words2[s[j:j + lengthOfSubString]] -= 1
                    if words2[s[j:j + lengthOfSubString]] == 0:
                        del words2[s[j:j + lengthOfSubString]]
                    j += lengthOfSubString
                    if not words2:
                        result.append(i)
                        break
                else:
                    break

        return result
--------------------------------------------------------------------------------
Following solution was using brute force and obviously got TLE 179/182.
Still i got some learnings.:

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        result = []
        lengthOfS = len(s)
        str1 = ''.join(words)
        lengthOfWords = len(str1)
        lengthOfSubString = len(words[0])

        for i in range(lengthOfS - lengthOfWords + 1):
            words2[:] = words[:]
            j = i
            while j <= i + lengthOfWords - lengthOfSubString:
                if s[j:j + lengthOfSubString] in words2:
                    words2.remove(s[j:j + lengthOfSubString])
                    j += lengthOfSubString
                    if not words2:
                        result.append(i)
                        break
                else:
                    break

        return result

       
words2[:] = words[:] this is wrong because you have to initialise words2 first
words2 = words this is wrong because it copy by reference so changes made to words2 reflects in words also

correct way is, because both are different copies.:
words2 = words[:]
words2 = words.copy()

"""