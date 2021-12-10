
作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)

题目地址：https://leetcode.com/problems/camelcase-matching/

## 题目描述

A query word matches a given ``pattern`` if we can insert lowercase letters to the ``pattern`` word so that it equals the ``query``. (We may insert each character at any position, and may insert 0 characters.)

Given a list of ``queries``, and a ``pattern``, return an answer list of booleans, where ``answer[i]`` is true if and only if ``queries[i]`` matches the pattern.


Example 1:

    Input: queries = ["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"], pattern = "FB"
    Output: [true,false,true,true,false]
    Explanation: 
    "FooBar" can be generated like this "F" + "oo" + "B" + "ar".
    "FootBall" can be generated like this "F" + "oot" + "B" + "all".
    "FrameBuffer" can be generated like this "F" + "rame" + "B" + "uffer".

Example 2:

    Input: queries = ["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"], pattern = "FoBa"
    Output: [true,false,true,false,false]
    Explanation: 
    "FooBar" can be generated like this "Fo" + "o" + "Ba" + "r".
    "FootBall" can be generated like this "Fo" + "ot" + "Ba" + "ll".

Example 3:

    Input: queries = ["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"], pattern = "FoBaT"
    Output: [false,true,false,false,false]
    Explanation: 
    "FooBarTest" can be generated like this "Fo" + "o" + "Ba" + "r" + "T" + "est".
 

Note:

1. ``1 <= queries.length <= 100``
1. ``1 <= queries[i].length <= 100``
1. ``1 <= pattern.length <= 100``
1. All strings consists only of lower and upper case English letters.

## 题目大意

判断每个query是不是能通过Pattern的大写字母中插入若干个（可以为0）个小写字母实现。

## 解题方法

### 正则+字典

这题的含义其实就是pattern按照大写字母分开，query也按大写字母分开，分开时要保证大写字母是每一段的第一个字符。然后要求pattern中的每一段都是query中每一段的subsequence。

把一个字符串分成一个大写+n个小写的子字符串的方式可以使用正则，表达式是"[A-Z][a-z]*".

判断subsequence需要使用遍历的方式求解，这里学习了lee215的一个写法,iter(qu)这样即可保证顺序查找、找到停止，然后等待下一次查找开始。

Python代码如下：

```python
class Solution(object):
    def camelMatch(self, queries, pattern):
        """
        :type queries: List[str]
        :type pattern: str
        :rtype: List[bool]
        """
        import re
        ps = re.findall("[A-Z][a-z]*", pattern)
        N = len(queries)
        res = []
        for q in queries:
            qs = re.findall("[A-Z][a-z]*", q)
            hasFind = False
            if len(ps) == len(qs):
                if all(self.isSubSeq(q, p) for (q, p) in zip(qs, ps)):
                    hasFind = True
            res.append(hasFind)
        return res
    
    def isSubSeq(self, qu, pa):
        qu = iter(qu)
        return all(p in qu for p in pa)
```

## 日期

2019 年 4 月 7 日 —— 周赛bug了3次。。


  [1]: https://assets.leetcode.com/uploads/2019/04/04/sum-of-root-to-leaf-binary-numbers.png
