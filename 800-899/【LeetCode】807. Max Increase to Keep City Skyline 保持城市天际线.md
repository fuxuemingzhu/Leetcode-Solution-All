
作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)

题目地址：https://leetcode.com/problems/max-increase-to-keep-city-skyline/description/

## 题目描述

In a 2 dimensional array grid, each value grid[i][j] represents the height of a building located there. We are allowed to increase the height of any number of buildings, by any amount (the amounts can be different for different buildings). Height 0 is considered to be a building as well. 

At the end, the "skyline" when viewed from all four directions of the grid, i.e. top, bottom, left, and right, must be the same as the skyline of the original grid. A city's skyline is the outer contour of the rectangles formed by all the buildings when viewed from a distance. See the following example.

What is the maximum total sum that the height of the buildings can be increased?

Example:
    
    Input: grid = [[3,0,8,4],[2,4,5,7],[9,2,6,3],[0,3,1,0]]
    Output: 35
    Explanation: 
    The grid is:
    [ [3, 0, 8, 4], 
      [2, 4, 5, 7],
      [9, 2, 6, 3],
      [0, 3, 1, 0] ]
    
    The skyline viewed from top or bottom is: [9, 4, 8, 7]
    The skyline viewed from left or right is: [8, 7, 9, 3]
    
    The grid after increasing the height of buildings without affecting skylines is:
    
    gridNew = [ [8, 4, 8, 7],
                [7, 4, 7, 7],
                [9, 4, 8, 7],
                [3, 3, 3, 3] ]

Notes:

1. 1 < grid.length = grid[0].length <= 50.
1. All heights grid[i][j] are in the range [0, 100].
1. All buildings in grid[i][j] occupy the entire grid cell: that is, they are a 1 x 1 x grid[i][j] rectangular prism.

    
## 题目大意

这个题很符合年前北京的漏出天际线的活动啊～这个题意思是，有一个矩阵代表了现在所有房子的高度，我们想提高每个房子的高度，同时保证其在前后左右四个方向观察到的天际线的高度是不变的。问我们增加多少楼层高度的和。

## 解题方法

题目已经给了我们比较清楚的测试用例，通过测试用例中给的思想也能看出来，我们完全可以构造一个新的矩阵，代表着能增加高度之后的各个楼层的高度。下面讨论增加楼层高度的方式。既然我们要求每个楼层观察到的各个方向的天际线的高度是不变的，那么我们让其增加到其所在行的最高天际线和其所在列的最高天际线的最小值。比如，

题目中我们可以得出每行的天际线的高度是[8, 7, 9, 3]，每列的天际线的高度是[9, 4, 8, 7]。那么，gridNew =

    __|_9__4__8__7__
    8 | 8, 4, 8, 7
    7 | 7, 4, 7, 7
    9 | 9, 4, 8, 7
    3 | 3, 3, 3, 3

代码：

```python
class Solution(object):
    def maxIncreaseKeepingSkyline(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        gridNew = [[0] * len(grid[0]) for _ in range(len(grid))] 
        top = [max(grid[rows][cols] for rows in range(len(grid))) for cols in range(len(grid[0]))]
        left = [max(grid[rows][cols] for cols in range(len(grid[0]))) for rows in range(len(grid))]
        for row, row_max in enumerate(left):
            for col, col_max in enumerate(top):
                gridNew[row][col] = min(row_max, col_max)
        return sum(gridNew[row][col] - grid[row][col] for row in range(len(left)) for col in range(len(top)))
```

二刷，没有创建新的数组，直接在原地进行判断。

```python
class Solution(object):
    def maxIncreaseKeepingSkyline(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid or not grid[0]: return 0
        M, N = len(grid), len(grid[0])
        rows, cols = [0] * M, [0] * N
        for i in range(M):
            rows[i] = max(grid[i][j] for j in range(N))
        for j in range(N):
            cols[j] = max(grid[i][j] for i in range(M))
        res = 0
        for i in range(M):
            for j in range(N):
                res += min(rows[i], cols[j]) - grid[i][j]
        return res
```

C++版本的代码如下：

```cpp
class Solution {
public:
    int maxIncreaseKeepingSkyline(vector<vector<int>>& grid) {
        int M = grid.size(), N = grid.size();
        vector<int> rows(M), cols(N);
        for (int i = 0; i < M; i++) {
            for (int j = 0; j < N; j++) {
                rows[i] = max(rows[i], grid[i][j]);
                cols[j] = max(cols[j], grid[i][j]);
            }
        }
        int res = 0;
        for (int i = 0; i < M; i++) {
            for (int j = 0; j < N; j++) {
                res += min(rows[i], cols[j]) - grid[i][j];
            }
        }
        return res;
    }
};
```

## 日期

2018 年 4 月 4 日 —— 清明时节雪纷纷～～下雪了，惊不惊喜，意不意外？
2018 年 12 月 2 日 —— 又到了周日
