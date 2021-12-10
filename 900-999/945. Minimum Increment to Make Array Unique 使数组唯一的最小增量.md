
作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)


题目地址：https://leetcode.com/problems/minimum-increment-to-make-array-unique/description/


## 题目描述

Given an array of integers A, a move consists of choosing any ``A[i]``, and incrementing it by ``1``.

Return the least number of moves to make every value in ``A`` unique.


Example 1:

    Input: [1,2,2]
    Output: 1
    Explanation:  After 1 move, the array could be [1, 2, 3].

Example 2:

    Input: [3,2,1,2,1,7]
    Output: 6
    Explanation:  After 6 moves, the array could be [3, 4, 1, 2, 5, 7].
    It can be shown with 5 or less moves that it is impossible for the array to have all unique values.
 

Note:

1. 0 <= A.length <= 40000
1. 0 <= A[i] < 40000
 

## 题目大意

每次移动可以把一个数字增加1，现在要把数组变成没有重复数字的数组，问需要的最少移动是多少。

## 解题方法

### 暴力求解，TLE

看到这个题有点慌，觉得需要找规律，然后我发现如果这个数字是重复数字，那么需要把它一直不停+1，直到和它不等的数字为止，这个做法非常类似与Hash的一种向后寻找的做法，时间复杂度是O(N^2)，果然超时了。

```python
class Solution(object):
    def minIncrementForUnique(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        N = len(A)
        seats = [0] * 80010
        res = 0
        for a in A:
            if not seats[a]:
                seats[a] = 1
            else:
                pos = a
                while pos < 80010 and seats[pos] == 1:
                    pos += 1
                seats[pos] = 1
                res += pos - a
        return res
```


### 一次遍历

这个思想我觉得还是非常巧妙的，首先先做一个排序。排序之后，使用一个变量保存当前不重复的数字已经增加到哪里了，所以，当下一个数字到来的时候，它应该增加到这个数字的位置，可以直接求出它需要扩大的步数。

```python
class Solution(object):
    def minIncrementForUnique(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        N = len(A)
        if N == 0: return 0
        A.sort()
        res = 0
        prev = A[0]
        for i in range(1, N):
            if A[i] <= prev:
                prev += 1
                res += prev - A[i]
            else:
                prev = A[i]
        return res
```

## 日期

2018 年 11 月 24 日 —— 周日开始！一周就过去了～


  [1]: http://zxi.mytechroad.com/blog/dynamic-programming/leetcode-730-count-different-palindromic-subsequences/
