
作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)

题目地址：https://leetcode.com/problems/flood-fill/description/


## 题目描述

An image is represented by a 2-D array of integers, each integer representing the pixel value of the image (from 0 to 65535).

Given a coordinate ``(sr, sc)`` representing the starting pixel (row and column) of the flood fill, and a pixel value newColor, "flood fill" the image.

To perform a "flood fill", consider the starting pixel, plus any pixels connected 4-directionally to the starting pixel of the same color as the starting pixel, plus any pixels connected 4-directionally to those pixels (also with the same color as the starting pixel), and so on. Replace the color of all of the aforementioned pixels with the newColor.

At the end, return the modified image.

    Example 1:
    Input: 
    image = [[1,1,1],[1,1,0],[1,0,1]]
    sr = 1, sc = 1, newColor = 2
    Output: [[2,2,2],[2,2,0],[2,0,1]]

    Explanation: 
    From the center of the image (with position (sr, sc) = (1, 1)), all pixels connected 
    by a path of the same color as the starting pixel are colored with the new color.
    Note the bottom corner is not colored 2, because it is not 4-directionally connected to the starting pixel.

Note:

1. The length of image and image[0] will be in the range [1, 50].
1. The given starting pixel will satisfy 0 <= sr < image.length and 0 <= sc < 1. image[0].length.
1. The value of each color in image[i][j] and newColor will be an integer in [0, 65535].

## 题目大意

简而言之：对指定位置染色，染色后，再对与该染色点四个方向相邻的相同颜色的点进行染色，依次递归。

图像由二维整数数组表示，每个整数代表图像的像素值（从0到65535）。

给定表示填充的开始像素（行和列）的坐标（sr，sc）和像素值newColor，“填充”图像。

为了执行“填充填充”，考虑起始像素，加上与起始像素相同颜色的起始像素，以及与这些像素4方向连接的任何像素的4方向连接的任何像素（也与颜色相同起始像素）等等。用newColor替换上述所有像素的颜色。

最后，返回修改后的图像。

## 解题方法

### 方法一：DFS

经典的dfs方法，要保存一下指定位置的颜色再对该位置染色，并对其四个方向的相邻元素进行处理，如果颜色和以前的颜色相同即染色并递归调用。

```python
class Solution(object):
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        SR, SC = len(image), len(image[0])
        color = image[sr][sc]
        if color == newColor: return image
        def dfs(r, c):
            if image[r][c] == color:
                image[r][c] = newColor
                if r >= 1: dfs(r - 1, c)
                if r < SR - 1: dfs(r + 1, c)
                if c >= 1: dfs(r, c - 1)
                if c < SC - 1: dfs(r, c + 1)
        dfs(sr, sc)
        return image
```

### 方法二：BFS

使用BFS，需要注意的是如果起始位置的颜色等于新的颜色，那么直接返回掉，否则后面会死循环。

```python
class Solution:
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        que = collections.deque()
        que.append((sr, sc))
        start = image[sr][sc]
        if start == newColor: return image
        M, N = len(image), len(image[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        while que:
            pos = que.popleft()
            image[pos[0]][pos[1]] = newColor
            for d in directions:
                newx, newy = pos[0] + d[0], pos[1] + d[1]
                if 0 <= newx < M and 0 <= newy < N and image[newx][newy] == start:
                    que.append((newx, newy))
        return image
```

## 日期

2018 年 2 月 28 日 
2018 年 11 月 14 日 —— 很严重的雾霾
