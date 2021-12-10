
作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)

题目地址：https://leetcode.com/problems/rotate-string/description/

## 题目描述

We are given two strings, A and B.

A shift on A consists of taking string A and moving the leftmost character to the rightmost position. For example, if A = 'abcde', then it will be 'bcdea' after one shift on A. Return True if and only if A can become B after some number of shifts on A.

    Example 1:
    Input: A = 'abcde', B = 'cdeab'
    Output: true
    
    Example 2:
    Input: A = 'abcde', B = 'abced'
    Output: false
    
Note:
    
    A and B will have length at most 100.

## 题目大意

判断字符串A执行一定次数的循环移位操作之后能不能变成B.

## 解题方法

在python中很容易使用切片操作达到循环移位的做法。只需要循环A长度次，看看每个结果即是所有的可能的移位结果。

```python
class Solution(object):
    def rotateString(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        if A == B == "":
            return True
        for i in range(len(A)):
            if A[i:] + A[:i] == B:
                return True
        return False
```

## 日期

2018 年 3 月 11 日 
2018 年 11 月 14 日 —— 很严重的雾霾

  [1]: https://leetcode.com/static/images/problemset/8-queens.png
