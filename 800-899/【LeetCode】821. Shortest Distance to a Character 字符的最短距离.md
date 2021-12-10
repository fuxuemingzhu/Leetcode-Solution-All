
作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)

题目地址：https://leetcode.com/problems/shortest-distance-to-a-character/description/

## 题目描述

Given a string S and a character C, return an array of integers representing the shortest distance from the character C in the string.

Example 1:

    Input: S = "loveleetcode", C = 'e'
    Output: [3, 2, 1, 0, 1, 0, 0, 1, 2, 2, 1, 0]
     

Note:

1. S string length is in [1, 10000].
1. C is a single character, and guaranteed to be in string S.
1. All letters in S and C are lowercase.


## 题目大意

给定字符串S和属于该字符串的一个字符C，要求出字符串中的每个字符到最近的C的距离。


## 解题方法

### 过两遍数组

这个解题方法，有点骚。属于两步走的方案：

第一步，先假设在很远的位置有个C字符，那么从左到右开始遍历，找出每个字符到其最近的左边的字符C的距离；
第二步，先假设在很远的位置有个C字符，那么从右到左开始遍历，找出每个字符到其最近的右边的字符C的距离，并和第一步求出的距离进行比较，找出最小值为结果；

两个技巧：

1. 设了一个比字符串长度更远的一个字符C，保证后面求最小值更新距离时一定会被更新。
2. 无论如何都用到了abs求绝对值，哪怕可能是不需要的，目的是不用费脑子思考谁大谁小了。


```python
class Solution:
    def shortestToChar(self, S, C):
        """
        :type S: str
        :type C: str
        :rtype: List[int]
        """
        _len = len(S)
        index = -1000000
        ans = [0] * _len
        for i, s in enumerate(S):
            if s == C:
                index = i
            ans[i] = abs(i - index)
        index = -100000
        for i in range(_len - 1, -1 , -1):
            if S[i] == C:
                index = i
            ans[i] = min(abs(i - index), ans[i])
        return ans
```

## 日期

2018 年 5 月 27 日 —— 周末的天气很好～
2018 年 11 月 6 日 —— 腰酸背痛要废了
