
作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)

题目地址：[https://leetcode.com/problems/toeplitz-matrix/description/][1]


## 题目描述

A matrix is Toeplitz if every diagonal from top-left to bottom-right has the same element.

Now given an M x N matrix, return True if and only if the matrix is Toeplitz.
 

Example 1:

	Input:
	matrix = [
	  [1,2,3,4],
	  [5,1,2,3],
	  [9,5,1,2]
	]
	Output: True
	Explanation:
	In the above grid, the diagonals are:
	"[9]", "[5, 5]", "[1, 1, 1]", "[2, 2, 2]", "[3, 3]", "[4]".
	In each diagonal all elements are the same, so the answer is True.

Example 2:

    Input: matrix = [[1,2],[2,2]]
    Output: False
    Explanation:
    The diagonal "[1, 2]" has different elements.

Note:

1. matrix will be a 2D array of integers.
1. matrix will have a number of rows and columns in range [1, 20].
1. matrix[i][j] will be integers in range [0, 99].

## 题目大意

如果一个矩阵中每条从左上到右下的线上的数值都相等，那么满足题目条件，否则不满足。求判断输入的每个矩阵是否满足。

## 解题方法

### 方法一：两两比较

这个题目如果按照题目意思解答，求出矩阵的所有对角线，情况很复杂。所以使用的是直接两两进行比较的方式。

判断每行元素的每个元素和其右下角的元素是否相等，如果不等就返回False；全部相等返回True.

```python
class Solution(object):
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        for row in xrange(len(matrix) - 1):
        	for col in xrange(len(matrix[0]) - 1):
        		if matrix[row][col] != matrix[row+1][col+1]:
        			return False
        return True
```

### 方法二：切片相等

只要观察到第二行的后面部分 和 第一行的前面部分相等即可。使用切片和一个for循环就能解决问题。

```python
class Solution(object):
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        return all(matrix[row+1][1:] == matrix[row][:-1] for row in range(len(matrix)-1))
```

### 方法三：判断每条对角线

二刷的时候没有想到更简单的方法，所以直接使用了题目说的，判断每条对角线的方式。把第一行和第一列作为起始，然后判断向右下的每条线上的元素是否和它相等。

```python
class Solution:
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        M, N = len(matrix), len(matrix[0])
        for row in range(M):
            first = matrix[row][0]
            j = 0
            for i in range(row, M):
                if 0 <= j < N:
                    if matrix[i][j] != first:
                        return False
                j += 1
        for col in range(N):
            first = matrix[0][col]
            i = 0
            for j in range(col, N):
                if 0 <= i < M:
                    if matrix[i][j] != first:
                        return False
                i += 1
        return True
```



## 日期

2018 年 1 月 22 日 
2018 年 11 月 8 日 —— 项目进展缓慢

  [1]: https://leetcode.com/problems/toeplitz-matrix/description/
