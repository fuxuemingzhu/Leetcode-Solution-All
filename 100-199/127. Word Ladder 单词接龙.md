
作者： 		负雪明烛 
id：				fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---

题目地址: https://leetcode.com/problems/word-ladder/description/

## 题目描述：

Given two words (beginWord and endWord), and a dictionary's word list, find the length of shortest transformation sequence from beginWord to endWord, such that:

1. Only one letter can be changed at a time.
1. Each transformed word must exist in the word list. Note that beginWord is not a transformed word.

Note:

- Return 0 if there is no such transformation sequence.
- All words have the same length.
- All words contain only lowercase alphabetic characters.
- You may assume no duplicates in the word list.
- You may assume beginWord and endWord are non-empty and are not the same.

Example 1:

    Input:
    beginWord = "hit",
    endWord = "cog",
    wordList = ["hot","dot","dog","lot","log","cog"]
    
    Output: 5
    
    Explanation: As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
    return its length 5.

Example 2:

    Input:
    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot","dot","dog","lot","log"]
    
    Output: 0

Explanation: The endWord "cog" is not in wordList, therefore no possible transformation.

## 题目大意

这个题名字是词语梯子，简单理解就是从begin开始，每次只能替换已经转化了的单词的其中一个字符，看最终能不能得到end。有个要求就是，每次变化不是任意的，是必须变成wordList中的其中一个才行。

## 解题方法

拿到这个题没有什么思路，看了别人解答之后，才猛然发现这个题是走迷宫问题的变形！也就是说，我们每次变化有26个方向，如果变化之后的位置在wordList中，我们认为这个走法是合规的，最后问能不能走到endWord？

很显然这个问题是BFS的问题，只是把走迷宫问题的4个方向转变成了26个方向，直接BFS会超时，所以我使用了个visited来保存已经遍历了的字符串，代表已经走过了的位置。代码总体思路很简单，就是利用队列保存每个遍历的有效的字符串，然后对队列中的每个字符串再次遍历，保存每次遍历的长度即可。

时间复杂度是O(NL)，空间复杂度是O(N).其中N是wordList中的单词个数，L是其实字符串的长度。

```python
class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        wordset = set(wordList)
        if endWord not in wordset:
            return 0
        visited = set([beginWord])
        chrs = [chr(ord('a') + i) for i in range(26)]
        bfs = collections.deque([beginWord])
        res = 1
        while bfs:
            len_bfs = len(bfs)
            for _ in range(len_bfs):
                origin = bfs.popleft()
                for i in range(len(origin)):
                    originlist = list(origin)
                    for c in chrs:
                        originlist[i] = c
                        transword = "".join(originlist)
                        if transword not in visited:
                            if transword == endWord:
                                return res + 1
                            elif transword in wordset:
                                bfs.append(transword)
                                visited.add(transword)
            res += 1
        return 0
```

显然上面的这个做法还是可以变短一点的，想起之前的二叉树的BFS的时候，会在每个节点入队列的时候同时保存了这个节点的深度，这样就少了一层对bfs当前长度的循环，可以使得代码变短。同时，学会了一个技巧，直接把已经遍历过的位置从wordList中删除，这样就相当于我上面的那个visited数组。下面这个代码很经典了，可以记住。

```python
class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        wordset = set(wordList)
        bfs = collections.deque()
        bfs.append((beginWord, 1))
        while bfs:
            word, length = bfs.popleft()
            if word == endWord:
                return length
            for i in range(len(word)):
                for c in "abcdefghijklmnopqrstuvwxyz":
                    newWord = word[:i] + c + word[i + 1:]
                    if newWord in wordset and newWord != word:
                        wordset.remove(newWord)
                        bfs.append((newWord, length + 1))
        return 0
```

参考资料：

http://www.cnblogs.com/grandyang/p/4539768.html

## 日期

2018 年 9 月 29 日 —— 国庆9天长假第一天！
