
作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)


题目地址：https://leetcode.com/problems/delete-columns-to-make-sorted/description/


## 题目描述

We are given an array ``A`` of ``N`` lowercase letter strings, all of the same length.

Now, we may choose any set of deletion indices, and for each string, we delete all the characters in those indices.

For example, if we have a string ``"abcdef"`` and deletion indices ``{0, 2, 3}``, then the final string after deletion is "bef".

Suppose we chose a set of deletion indices D such that after deletions, each remaining column in A is in non-decreasing sorted order.

Formally, the ``c``-th column is ``[A[0][c], A[1][c], ..., A[A.length-1][c]]``

Return the minimum possible value of ``D.length``.

 

Example 1:

    Input: ["cba","daf","ghi"]
    Output: 1

Example 2:

    Input: ["a","b"]
    Output: 0

Example 3:

    Input: ["zyx","wvu","tsr"]
    Output: 3
 

Note:

1. ``1 <= A.length <= 100``
1. ``1 <= A[i].length <= 1000``

## 题目大意

有一个数组A，其中它的每个元素都是等长度的字符串。现在求最短的要删除的切片的长度，使得做完操作之后，数组中剩下的相同列是递增的。

## 解题方法

又是乍一看很难的题目，其实很简单的，直接暴力解决就好了。

主要是思路：如果一个列的元素已经是递增的，那么我们一定不能把这个列删除掉。如果删除掉某一列，那么其他的列将不受到任何影响。

所以，基于上面两个原则，我们可以直接对所有的列进行遍历，也就是说取得所有的列，然后判断这个列是不是递增的，如果不是递增的话，就删除掉。统计要删除掉多少个列即可。而判断某个列是不是递增的最简单方法就是排序之后，然后看是不是和之前的相等。

时间复杂度是O(N*(MlogM))，空间复杂度是O(M)。N是每个字符串长度，M是数组长度。还好给的区间很小，直接能过的。


```python
class Solution:
    def minDeletionSize(self, A):
        """
        :type A: List[str]
        :rtype: int
        """
        res = 0
        N = len(A[0])
        for i in range(N):
            col = [a[i] for a in A]
            if col != sorted(col):
                res += 1
        return res
```

## 日期

2018 年 11 月 18 日 —— 出去玩了一天，腿都要废了
