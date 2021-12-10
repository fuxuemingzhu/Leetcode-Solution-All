作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)


题目地址：https://leetcode.com/problems/valid-mountain-array/description/


## 题目描述

Given an array ``A`` of integers, return ``true`` if and only if it is a valid mountain array.

Recall that A is a mountain array if and only if:

- ``A.length >= 3``
- There exists some ``i`` with ``0 < i < A.length - 1`` such that:
    - ``A[0] < A[1] < ... A[i-1] < A[i]``
    - ``A[i] > A[i+1] > ... > A[B.length - 1]``
 

Example 1:

    Input: [2,1]
    Output: false

Example 2:

    Input: [3,5,5]
    Output: false

Example 3:

    Input: [0,3,2,1]
    Output: true
 

Note:

1. ``0 <= A.length <= 10000``
1. ``0 <= A[i] <= 10000 ``


## 题目大意

判断一个数组是不是山形数组，山形数组最少有3个数字，中间有个最大的数字，往两边都是依次减小的。


## 解题方法

方法很直接，先判断是不是依次增加，然后再判断是不是依次减小，如果整个数组都是这样的就是山形数组了。

所以有两个while循环，一个是向后查找更大的数字，第二个是向后找最小的数字。在第一个while结束的时候，找到的元素的位置应该在数组中间，而第二个while结束之后，元素的位置应该在数组的结尾。

时间复杂度是O(N)，空间复杂度是O(1)。


```python
class Solution:
    def validMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        N = len(A)
        if N < 3:
            return False
        i = 0
        while i < N - 1:
            if A[i] < A[i + 1]:
                i += 1
            else:
                break
        if i == 0 or i == N - 1: return False
        while i < N - 1:
            if A[i] > A[i + 1]:
                i += 1
            else:
                break
        return i == N - 1
```

其实while的条件也可以使用判断语句，这样的话，我们就直接停止。

```python
class Solution(object):
    def validMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        print(A)
        N = len(A)
        if N < 3: return False
        i = 0
        while i < N - 1 and A[i + 1] > A[i]:
            i += 1
        if i == 0 or i == N - 1: return False
        while i < N - 1 and A[i] > A[i + 1]:
            i += 1
        return i == N - 1
```

## 日期

2018 年 11 月 18 日 —— 出去玩了一天，腿都要废了
2018 年 11 月 24 日 —— 周六快乐
