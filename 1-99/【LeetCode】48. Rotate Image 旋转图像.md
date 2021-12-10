
作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)

题目地址：https://leetcode.com/problems/rotate-image/description/

## 题目描述

You are given an n x n 2D matrix representing an image.

Rotate the image by 90 degrees (clockwise).

Note:
You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

Example 1:
    
    Given input matrix = 
    [
      [1,2,3],
      [4,5,6],
      [7,8,9]
    ],
    
    rotate the input matrix in-place such that it becomes:
    [
      [7,4,1],
      [8,5,2],
      [9,6,3]
    ]

Example 2:
    
    Given input matrix =
    [
      [ 5, 1, 9,11],
      [ 2, 4, 8,10],
      [13, 3, 6, 7],
      [15,14,12,16]
    ], 
    
    rotate the input matrix in-place such that it becomes:
    [
      [15,13, 2, 5],
      [14, 3, 4, 1],
      [12, 6, 8, 9],
      [16, 7,10,11]
    ]

## 题目大意

把矩阵原地顺时针旋转90度。

## 解题方法

做法挺简单，先上下翻转，再延左上到右下的对角线进行翻转(镜像操作)。

需要注意的是上下翻转的时候是rows-i-1，而不是rows-i。

代码：

```python
class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        if matrix:
            rows = len(matrix)
            cols = len(matrix[0])
            for i in xrange(rows / 2):
                for j in xrange(cols):
                    matrix[i][j], matrix[rows - i - 1][j] = matrix[rows - i - 1][j], matrix[i][j]
            for i in xrange(rows):
                for j in xrange(i):
                    matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
```

二刷的时候使用的另外一种旋转的方法：先左右镜像翻转，然后再沿着副对角线（从右上到左下的对角线↙）进行翻转。比上面的麻烦一点。

使用的C++代码如下：

```cpp
class Solution {
public:
    void rotate(vector<vector<int>>& matrix) {
        if (!matrix.size()) return;
        const int N = matrix.size();
        for (int i = 0; i < N; i ++) {
            for (int j = 0; j < N / 2; j ++) {
                int tmp = matrix[i][j];
                matrix[i][j] = matrix[i][N - j - 1];
                matrix[i][N - j - 1] = tmp;
            }
        }
        for (int i = 0; i < N; i ++) {
            for (int j = 0; j < N - i; j ++) {
                int tmp = matrix[i][j];
                matrix[i][j] = matrix[N - j - 1][N - i - 1];
                matrix[N - j - 1][N - i - 1] = tmp;
            }
        }
    }
};
```

## 日期

2018 年 3 月 5 日 
2018 年 12 月 30 日 —— 周赛差强人意
