
作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)

题目地址：https://leetcode.com/problems/transpose-matrix/description/

## 题目描述

Given a matrix A, return the transpose of A.

The transpose of a matrix is the matrix flipped over it's main diagonal, switching the row and column indices of the matrix.

 

Example 1:

    Input: [[1,2,3],[4,5,6],[7,8,9]]
    Output: [[1,4,7],[2,5,8],[3,6,9]]

Example 2:

    Input: [[1,2,3],[4,5,6]]
    Output: [[1,4],[2,5],[3,6]]
 

Note:

1. 1 <= A.length <= 1000
1. 1 <= A[0].length <= 1000

## 题目大意

把矩阵进行转置。

## 解题方法

### 先构建数组再遍历实现翻转

第一遍看这个题的时候，感觉挺难的。今天再次看的时候，突然想明白，所谓转置，就是把一个矩阵的行和列进行互换。因此这个题其实就是考察了，把一个原始矩阵通过行列元素互换得到新的矩阵。

那么只要我们新建一个行数等于原始列数，列数等于原始行数的矩阵，再对原始矩阵进行遍历即可。

时间复杂度是O(MN)，空间复杂度是O(1).

代码如下：

```python
class Solution:
    def transpose(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        rows, cols = len(A), len(A[0])
        res = [[0] * rows for _ in range(cols)]
        for row in range(rows):
            for col in range(cols):
                res[col][row] = A[row][col]
        return res
```

## 日期

2018 年 7 月 12 日 —— 天阴阴地潮潮，已经连着两天这样了
2018 年 11 月 5 日 —— 打了羽毛球，有点累
