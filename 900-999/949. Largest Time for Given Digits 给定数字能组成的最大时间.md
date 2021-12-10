
作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)


题目地址：https://leetcode.com/problems/largest-time-for-given-digits/description/


## 题目描述

Given an array of 4 digits, return the largest 24 hour time that can be made.

The smallest 24 hour time is 00:00, and the largest is 23:59.  Starting from 00:00, a time is larger if more time has elapsed since midnight.

Return the answer as a string of length 5.  If no valid time can be made, return an empty string.

Example 1:

    Input: [1,2,3,4]
    Output: "23:41"

Example 2:

    Input: [5,5,5,5]
    Output: ""
 

Note:

1. A.length == 4
1. 0 <= A[i] <= 9

## 题目大意

给了4个数字，找出能做到的排列出的24小时制时间最大值。

## 解题方法

这个题有人使用的是Permutation的方法，需要把每个permutation做出来，然后进行判断。当然了，只有4个数字，不会超时。

我的做法是从23:59向00:00遍历24小时制的每一个分钟，这样的话，我们看这个时间能不能由题目给的4个数字表示出来。如果可以的话立即终止即可。总共24*60个分钟，中间进行判断的方式是排序，整体的时间复杂度很小的。所以也能通过。

```python
class Solution(object):
    def largestTimeFromDigits(self, A):
        """
        :type A: List[int]
        :rtype: str
        """
        A.sort()
        for h in range(23, -1, -1):
            for m in range(59, -1, -1):
                t = [h / 10, h % 10, m / 10, m % 10]
                ts = sorted(t)
                if ts == A:
                    return str(t[0]) + str(t[1]) + ":" + str(t[2]) + str(t[3])
        return ""
```


## 日期

2018 年 12 月 2 日 —— 又到了周日


  [1]: https://blog.csdn.net/fuxuemingzhu/article/details/84640318
  [2]: http://www.cnblogs.com/grandyang/p/4295761.html
