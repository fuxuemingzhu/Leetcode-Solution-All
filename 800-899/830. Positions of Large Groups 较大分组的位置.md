
作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)

题目地址：https://leetcode.com/problems/positions-of-large-groups/description/

## 题目描述

In a string ``S`` of lowercase letters, these letters form consecutive groups of the same character.

For example, a string like ``S = "abbxxxxzyy"`` has the groups ``"a"``, ``"bb"``, ``"xxxx"``, ``"z"`` and ``"yy"``.

Call a group large if it has 3 or more characters.  We would like the starting and ending positions of every large group.

The final answer should be in lexicographic order.

 

    Example 1:
    
    Input: "abbxxxxzzy"
    Output: [[3,6]]
    Explanation: "xxxx" is the single large group with starting  3 and ending positions 6.
    
    Example 2:
    
    Input: "abc"
    Output: []
    Explanation: We have "a","b" and "c" but no large group.
    
    Example 3:
    
    Input: "abcdddeeeeaabbbcd"
    Output: [[3,5],[6,9],[12,14]]
 

Note:  ``1 <= S.length <= 1000``

## 题目大意

一个长字符串可以按照字符的连续出现，分组。每个组内都是一段连续的，字符相同的子字符串。

要求，长度不小于3的所有组的字符串起始和结束位置。

## 解题方法

直接暴力求解即可！从左到右遍历字符串，只要后面的字符和该组起始的字符相同，那么就是属于同一个组；否则，开辟一个新组，并且判断之前的这个组长度是否>=3，是的话进行保存。

第一遍提交没通过的原因是忘了判断，当字符串结束的时候也是一个组终止的标志。比如字符串``"aaa"``。

```python
class Solution:
    def largeGroupPositions(self, S):
        """
        :type S: str
        :rtype: List[List[int]]
        """
        groups = []
        before_index, before_char = 0, S[0]
        for i, s in enumerate(S):
            if s != before_char:
                if i - before_index >= 3:
                    groups.append([before_index, i - 1])
                before_index = i
                before_char = s
        if i - before_index >= 2:
            groups.append([before_index, i])
        return groups
```

二刷的时候，对结尾的判断是添加了一个大写字符，这样的话在不打扰之前小写字符串的基础上，增加了结束符号。

```python
class Solution:
    def largeGroupPositions(self, S):
        """
        :type S: str
        :rtype: List[List[int]]
        """
        S = S + "A"
        groups = []
        previndex, prevc = 0, ""
        for i, c in enumerate(S):
            if not prevc:
                prevc = c
                previndex = i
            elif prevc != c:
                if i - previndex >= 3:
                    groups.append([previndex, i - 1])
                previndex = i
                prevc = c
        return groups
```

## 日期

2018 年 5 月 27 日 ———— 周末的天气很好～
2018 年 11 月 16 日 —— 又到周五了！
