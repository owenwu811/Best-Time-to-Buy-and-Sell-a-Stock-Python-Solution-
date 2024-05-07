
#A transformation sequence from word beginWord to word endWord using a dictionary wordList is a sequence of words beginWord -> s1 -> s2 -> ... -> sk such that:

#Every adjacent pair of words differs by a single letter.
#Every si for 1 <= i <= k is in wordList. Note that beginWord does not need to be in wordList.
#sk == endWord
#Given two words, beginWord and endWord, and a dictionary wordList, return the number of words in the shortest transformation sequence from beginWord to endWord, or 0 if no such sequence exists.

 

#Example 1:

#Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
#Output: 5
#Explanation: One shortest transformation sequence is "hit" -> "hot" -> "dot" -> "dog" -> cog", which is 5 words long.



#python3 solution:

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList: return 0
        neighbor = defaultdict(list)
        wordList.append(beginWord)
        for word in wordList:
            for j in range(len(word)):
                pattern = word[:j] + "*" + word[j + 1:]
                neighbor[pattern].append(word)
        #run bfs 
        visited = set(beginWord)
        q = deque([beginWord])
        res = 1
        while q:
            for i in range(len(q)): #initially just beginWord
                cur = q.popleft()
                if cur == endWord:
                    return res
                for j in range(len(cur)):
                    pattern = cur[:j] + "*" + cur[j + 1:]
                    for n in neighbor[pattern]:
                        if n not in visited:
                            visited.add(n)
                            q.append(n)
            res += 1
        return 0


#practice again 5/6/24:

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList: return 0
        neighbor = defaultdict(list)
        wordList.append(beginWord) #we need to start the recursion with beginWord 
        for word in wordList:
            for j in range(len(word)): #j increases in next iteration
                pattern = word[:j] + "*" + word[j + 1:]
                neighbor[pattern].append(word)
        visited = set(beginWord) #the purpose of the set is to avoid redundant visits and to increase time complexity 
        q = deque([beginWord])
        res = 1
        while q:
            for i in range(len(q)):
                cur = q.popleft() #bfs = fifo
                if cur == endWord: 
                    return res
                for j in range(len(cur)):
                    pattern = cur[:j] + "*" + cur[j + 1:]
                    for n in neighbor[pattern]:
                        if n not in visited:
                            visited.add(n) 
                            q.append(n)
            res += 1
        return 0
