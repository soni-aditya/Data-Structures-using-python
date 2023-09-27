'''
A transformational sequence from word beginWord to word endWord using a dictionary wordList is a sequence of 
words beginWord -> s1 -> s2....-> sn such that:
1. Every adjacent pair of words differ by a single letter
2. Every si for 1<=i<=n is in wordList (note that beginWord doesn't need to be in wordList)
3. sn == endWord

Given two words, beginWord and endWord and a wordList, return the number of words in the shortest transformational sequence, or 0 if no such sequence exists

input: beginWord="hit", endWord="cog", wordList = ["hot","dot","dog","log","cog"]
output: 5
'''
from collections import List,defaultdict,deque

class Solution:
    def ladder_length(self,beginWord: str, endWord: str, wordList: List[str])-> int:
        if endWord in wordList:
            return 0

        nei = defaultdict(list)
        wordList.append(beginWord)

        for word in wordList:
            for j in range(len(word)):
                pattern = word[:j]+"*"+word[j+1:]
                nei[pattern].append(word)
        visit = set([beginWord])
        q = deque([beginWord])
        while q:
            res+= 1
        return 0






