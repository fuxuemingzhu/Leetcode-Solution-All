
作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)


题目地址：https://leetcode.com/problems/palindrome-pairs/description/


## 题目描述

Given a list of **unique** words, find all pairs of **distinct** indices ``(i, j)`` in the given list, so that the concatenation of the two words, i.e. ``words[i] + words[j]`` is a palindrome.

Example 1:

    Input: ["abcd","dcba","lls","s","sssll"]
    Output: [[0,1],[1,0],[3,2],[2,4]] 
    Explanation: The palindromes are ["dcbaabcd","abcddcba","slls","llssssll"]

Example 2:

    Input: ["bat","tab","cat"]
    Output: [[0,1],[1,0]] 
    Explanation: The palindromes are ["battab","tabbat"]

## 题目大意

如果从input进来的字符串中选取两个拼接在一起能构成回文字符串，那么就把这两个的索引加入到结果中。返回所有的索引列表。

## 解题方法

### HashTable

这个题暴力求解会超时，优秀的解法还真不是容易想出来。不愧是Hard题啊，这个也是我做的第600个题。我就照搬大神的解法了[\[LeetCode\]Palindrome Pairs][1] 。

O(k * n ^2)解法 其中k为单词个数，n为单词的长度：

    利用字典wmap保存单词 -> 下标的键值对
    
    遍历单词列表words，记当前单词为word，下标为idx：
    
    1). 若当前单词word本身为回文，且words中存在空串，则将空串下标bidx与idx加入答案
    
    2). 若当前单词的逆序串在words中，则将逆序串下标ridx与idx加入答案
    
    3). 将当前单词word拆分为左右两半left，right。
    
         3.1) 若left为回文，并且right的逆序串在words中，则将right的逆序串下标rridx与idx加入答案
         
         3.2) 若right为回文，并且left的逆序串在words中，则将left的逆序串下标idx与rlidx加入答案


时间复杂度是O(k * n ^2)，空间复杂度是O(kN).

```python
class Solution(object):
    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        wmap = {w : i for i, w in enumerate(words)}
        
        def isPalindrome(word):
            _len = len(word)
            for x in range(_len / 2):
                if word[x] != word[_len - x - 1]:
                    return False
            return True
        
        res = set()
        for idx, word in enumerate(words):
            if word and isPalindrome(word) and "" in wmap:
                nidx = wmap[""]
                res.add((idx, nidx))
                res.add((nidx, idx))
            
            rword = word[::-1]
            if word and rword in wmap:
                nidx = wmap[rword]
                if idx != nidx:
                    res.add((idx, nidx))
                    res.add((nidx, idx))
            
            for x in range(1, len(word)):
                left, right = word[:x], word[x:]
                rleft, rright = left[::-1], right[::-1]
                if isPalindrome(left) and rright in wmap:
                    res.add((wmap[rright], idx))
                if isPalindrome(right) and rleft in wmap:
                    res.add((idx, wmap[rleft]))
        return list(res)
```


## 相似题目


## 参考资料

http://bookshadow.com/weblog/2016/03/10/leetcode-palindrome-pairs/

## 日期

2018 年 11 月 1 日 —— 小光棍节


  [1]: http://bookshadow.com/weblog/2016/03/10/leetcode-palindrome-pairs/
