
作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)

题目地址：https://leetcode.com/problems/range-addition-ii/description/


## 题目描述

Given an ``m * n`` matrix M initialized with all 0's and several update operations.

Operations are represented by a 2D array, and each operation is represented by an array with two positive integers a and b, which means ``M[i][j]`` should be added by one for all ``0 <= i < a`` and ``0 <= j < b``.

You need to count and return the number of maximum integers in the matrix after performing all the operations.

    Example 1:
    Input: 
    m = 3, n = 3
    operations = [[2,2],[3,3]]
    Output: 4
    Explanation: 
    Initially, M = 
    [[0, 0, 0],
     [0, 0, 0],
     [0, 0, 0]]
    
    After performing [2,2], M = 
    [[1, 1, 0],
     [1, 1, 0],
     [0, 0, 0]]
    
    After performing [3,3], M = 
    [[2, 2, 1],
     [2, 2, 1],
     [1, 1, 1]]

    So the maximum integer in M is 2, and there are four of it in M. So return 4.

Note:

1. The range of m and n is [1,40000].
1. The range of a is [1,m], and the range of b is [1,n].
1. The range of operations size won't exceed 10,000.


## 题目大意

对于一个初始全部为零的二维数组，经过一串操作后，找出数组中最大的数字出现的``次数``。操作是指，把二维数组中小于(m,n)左上角的元素都 + 1.

## 解题方法

首先要明白，要求的结果是最终二维数组中最大值出现的``次数``。那么，被重复加的最多的数组元素一定最大，其出现次数就是答案。

每次操作都是对左上角部分区域进行操作的，并且，a,b的范围都是大于1的，即每次都会有元素改变。那么，最终二维数组中最大值出现的次数一定是操作中最小范围中的那批元素构成的矩形区域面积。

如果没有进行操作，那么，返回的应该是全部0的个数。

```python
class Solution(object):
    def maxCount(self, m, n, ops):
        """
        :type m: int
        :type n: int
        :type ops: List[List[int]]
        :rtype: int
        """
        if not ops:
            return m * n
        return min([op[0] for op in ops]) * min([op[1] for op in ops])
```

## 日期

2018 年 2 月 28 日 
2018 年 11 月 15 日 —— 时间太快，不忍直视
