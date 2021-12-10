
作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)

题目地址：[https://leetcode.com/problems/longest-word-in-dictionary/description/][1]


## 题目描述

Given a list of strings words representing an English Dictionary, find the longest word in words that can be built one character at a time by other words in words. If there is more than one possible answer, return the longest word with the smallest lexicographical order.

If there is no answer, return the empty string.

    Example 1:
    Input: 
    words = ["w","wo","wor","worl", "world"]
    Output: "world"
    Explanation: 
    The word "world" can be built one character at a time by "w", "wo", "wor", and "worl".

Example 2:

    Input: 
    words = ["a", "banana", "app", "appl", "ap", "apply", "apple"]
    Output: "apple"
    Explanation: 
    Both "apply" and "apple" can be built from other words in the dictionary. However, "apple" is lexicographically smaller than "apply".

Note:

1. All the strings in the input will only contain lowercase letters.
1. The length of words will be in the range [1, 1000].
1. The length of words[i] will be in the range [1, 30].

## 题目大意

找出字符串数组中最长的一个字符串，这个字符串的所有前缀都能在这个数组中找到。如果存在多个长度相等的满足要求的字符串，返回字母序最小的那个。

## 解题方法

### 暴力查找

对于每个字符串都去查找它的所有前缀是不是都在数组中，如果是的话，然后比较是不是最长的、如果同样长度的话是不是字母序更小。

```python
class Solution(object):
    def longestWord(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        wset = set(words)
        res = ""
        for w in words:
            isIn = True
            for i in range(1, len(w)):
                if w[:i] not in wset:
                    isIn = False
                    break
            if isIn:
                if not res or len(w) > len(res):
                    res = w
                elif len(w) == len(res) and res > w:
                    res = w
        return res
```

### 排序

巧妙用了set（）,判断每个单词的除去倒数第一个字母是否在set里，用一个变量保存最长的单词。

用判断新单词是否比最长单词更长的方式完成两个需求：1.找出最长；2.同样最长的情况下，保留字母序最小的。这样做的前提是先对words进行排序。

```python
class Solution(object):
    def longestWord(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        words.sort()
        res = set([''])
        longestWord = ''
        for word in words:
            if word[:-1] in res:
                res.add(word)
                if len(word) > len(longestWord):
                    longestWord = word
        return longestWord
```

## 日期

2018 年 1 月 21 日 
2018 年 11 月 19 日 —— 周一又开始了

  [1]: https://leetcode.com/problems/longest-word-in-dictionary/description/
