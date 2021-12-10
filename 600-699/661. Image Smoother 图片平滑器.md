
作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)

题目地址：[https://leetcode.com/problems/image-smoother/description/][1]


## 题目描述

Given a 2D integer matrix M representing the gray scale of an image, you need to design a smoother to make the gray scale of each cell becomes the average gray scale (rounding down) of all the 8 surrounding cells and itself. If a cell has less than 8 surrounding cells, then use as many as you can.

Example 1:

    Input:
    [[1,1,1],
     [1,0,1],
     [1,1,1]]
    Output:
    [[0, 0, 0],
     [0, 0, 0],
     [0, 0, 0]]

    Explanation:
    For the point (0,0), (0,2), (2,0), (2,2): floor(3/4) = floor(0.75) = 0
    For the point (0,1), (1,0), (1,2), (2,1): floor(5/6) = floor(0.83333333) = 0
    For the point (1,1): floor(8/9) = floor(0.88888889) = 0

Note:
1. The value in the given matrix is in the range of [0, 255].
1. The length and width of the given matrix are in the range of [1, 150].

## 题目大意

对一张图片取模糊，每个位置的数值等于9联通区域内的所有数字的平均值取整。

## 解题方法

### 方法一：暴力解决

非常粗暴的解法。判断数组中每个元素的周边的所有元素的和，并记录元素的个数。用判断边界的方式，防止过界。

```python
from copy import deepcopy as copy
class Solution(object):
    def imageSmoother(self, M):
        """
        :type M: List[List[int]]
        :rtype: List[List[int]]
        """
        if not M or not M[0]:
            return M
        rows = len(M)
        cols = len(M[0])
        isValid = lambda i,j: i >=0 and i < rows and j >= 0 and j < cols
        row, col = 0, 0
        answer = copy(M)
        for row in xrange(rows):
            for col in xrange(cols):
                _sum, count = 0, 0
                for i in xrange(-1, 2):
                    for j in xrange(-1, 2):
                        if isValid(row + i, col + j):
                            _sum += M[row + i][col + j]
                            count += 1
                answer[row][col] = _sum / count
        return answer
        
```


## 日期

2018 年 1 月 24 日 
2018 年 11 月 16 日 —— 又到周五了！

  [1]: https://leetcode.com/problems/image-smoother/description/
