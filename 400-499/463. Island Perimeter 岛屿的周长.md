作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)


题目地址：https://leetcode.com/problems/island-perimeter/description/


## 题目描述

You are given a map in form of a two-dimensional integer grid where 1 represents land and 0 represents water.

Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells).

The island doesn't have "lakes" (water inside that isn't connected to the water around the island). One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.

 

Example:

    Input:
    [[0,1,0,0],
     [1,1,1,0],
     [0,1,0,0],
     [1,1,0,0]]
    
    Output: 16
    
    Explanation: The perimeter is the 16 yellow stripes in the image below:

![此处输入图片的描述][1]


## 题目大意

给了一个二维数组表示的一张地图，如果某个位置是1，那么表示的是陆地，位置是0表示的是海洋。已知陆地连在一起的话会构成一个小岛，而且这个地图里面只有一个小岛。求小岛的周长。

## 解题方法

### 减去相交部分

直接求解好像很难，可以使用一个简单的方法：每个位置的周长是4，如果和另一个陆地相连，那么这两个陆地周长和减去2.所以整个小岛的周长是4×陆地数-2×相交数。

```python
class Solution:
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        M, N = len(grid), len(grid[0])
        counts = 0
        neighbors = 0
        for i in range(M):
            for j in range(N):
                if grid[i][j] == 1:
                    counts += 1
                    if i < M - 1:
                        if grid[i + 1][j] == 1:
                            neighbors += 1
                    if j < N - 1:
                        if grid[i][j + 1] == 1:
                            neighbors += 1
        return 4 * counts - 2 * neighbors

```


## 参考资料

https://leetcode.com/problems/island-perimeter/discuss/95001/clear-and-easy-java-solution

## 日期

2018 年 11 月 8 日 —— 项目进展缓慢


  [1]: https://assets.leetcode.com/uploads/2018/10/12/island.png
  [2]: https://charlesliuyx.github.io/2018/10/11/%E3%80%90%E7%9B%B4%E8%A7%82%E7%AE%97%E6%B3%95%E3%80%91Egg%20Puzzle%20%E9%B8%A1%E8%9B%8B%E9%9A%BE%E9%A2%98/
