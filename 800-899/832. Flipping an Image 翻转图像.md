
作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)


题目地址：https://leetcode.com/problems/flipping-an-image/description/

## 题目描述

Given a binary matrix A, we want to flip the image horizontally, then invert it, and return the resulting image.

To flip an image horizontally means that each row of the image is reversed.  For example, flipping [1, 1, 0] horizontally results in [0, 1, 1].

To invert an image means that each 0 is replaced by 1, and each 1 is replaced by 0. For example, inverting [0, 1, 1] results in [1, 0, 0].

Example 1:

    Input: [[1,1,0],[1,0,1],[0,0,0]]
    Output: [[1,0,0],[0,1,0],[1,1,1]]
    Explanation: First reverse each row: [[0,1,1],[1,0,1],[0,0,0]].
    Then, invert the image: [[1,0,0],[0,1,0],[1,1,1]]

Example 2:

    Input: [[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]
    Output: [[1,1,0,0],[0,1,1,0],[0,0,0,1],[1,0,1,0]]
    Explanation: First reverse each row: [[0,0,1,1],[1,0,0,1],[1,1,1,0],[0,1,0,1]].
    Then invert the image: [[1,1,0,0],[0,1,1,0],[0,0,0,1],[1,0,1,0]]


Notes:

1. 1 <= A.length = A[0].length <= 20
1. 0 <= A[i][j] <= 1   


## 题目大意

把一个数组分两步处理：第一步，左右翻转；第二步，把每个位置的0或者1变成1或者0.

## 解题方法

### 翻转 + 异或

就是按照两步操作就好了。这个题非常简单。先逆序，然后用异或操作，就能实现了。

时间复杂度O(N)，空间复杂度O(1).超过98%.

```python
class Solution:
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        rows = len(A)
        cols = len(A[0])
        for row in range(rows):
            A[row] = A[row][::-1]
            for col in range(cols):
                A[row][col] ^= 1
        return A
```

### 直接计算

直接计算的方式看起来更美观一些。先构造一个和A一样大小的结果数组，然后第i行第j列的结果等于1-A[N - 1 - j].

时间复杂度O(N)，空间复杂度O(1).超过98%.

```python
class Solution:
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        M, N = len(A), len(A[0])
        res = [[0] * N for _ in range(M)]
        for i in range(M):
            for j in range(N):
                res[i][j] = 1 - A[i][N - 1 - j]
        return res
```

## 日期

2018 年 5 月 27 日 —— 很久没刷题了，这个是恢复的第一个题目。
2018 年 11 月 3 日 —— 雾霾的周六
