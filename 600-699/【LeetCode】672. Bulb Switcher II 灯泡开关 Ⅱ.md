
作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)

题目地址：https://leetcode.com/problems/bulb-switcher-ii/description/

## 题目描述

There is a room with n lights which are turned on initially and 4 buttons on the wall. After performing exactly m unknown operations towards buttons, you need to return how many different kinds of status of the n lights could be.

Suppose n lights are labeled as number [1, 2, 3 ..., n], function of these 4 buttons are given below:

1. Flip all the lights.
1. Flip lights with even numbers.
1. Flip lights with odd numbers.
1. Flip lights with (3k + 1) numbers, k = 0, 1, 2, ...

Example 1:

        Input: n = 1, m = 1.
        Output: 2
        Explanation: Status can be: [on], [off]
        
Example 2:

        Input: n = 2, m = 1.
        Output: 3
        Explanation: Status can be: [on, off], [off, on], [off, off]

Example 3:

        Input: n = 3, m = 1.
        Output: 4
        Explanation: Status can be: [off, on, off], [on, off, on], [off, off, off], [off, on, on].

Note: n and m both fit in range [0, 1000].

## 题目大意

有四种操作。分别对灯进行变换。。不是一个数学题，这个是脑筋急转弯。

## 解题方法

额，不会做。脑子不够用。。这个题被踩了这么多下，其实没有做的必要了。

可以看http://blog.csdn.net/huanghanqian/article/details/77857912

代码：

```python
class Solution:
    def flipLights(self, n, m):
        """
        :type n: int
        :type m: int
        :rtype: int
        """
        if m == 0:
            return 1
        if n >= 3:
            return 4 if m == 1 else 7 if m == 2 else 8
        if n == 2:
            return 3 if m == 1 else 4
        if n == 1:
            return 2
```

## 日期

2018 年 3 月 5 日 
