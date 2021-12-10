
作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)

题目地址：https://leetcode.com/problems/minimum-path-sum/description/

## 题目描述

Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

Example:

    Input:
    [
      [1,3,1],
      [1,5,1],
      [4,2,1]
    ]
    Output: 7
    Explanation: Because the path 1→3→1→1→1 minimizes the sum.


## 题目大意

求一个矩阵从左上角到右下角的最短路径和。

## 解题方法

第一感觉是dfs，但是题目没有说范围，估计会超时。然后就想到了DP。

使用DP创建了一个path数组，和grid数组是一样的。path代表了从左上角开始到某个点的最短路径。那么很容易知道，新的一个点的最短路径一定等于其上方、左方最短路径+当前的值。因此写成双重循环即可。因为要用到上方、左方的值，数组第一行和第一列会超出边框，其实只需要把这个方向设为前面的那个路径值即可。

这个算法的时间啊复杂度是O(m * n)，空间复杂度是O(m * n)。

代码如下：

```python
class Solution:
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid or not grid[0]: return 0
        m, n = len(grid), len(grid[0])
        path = copy.deepcopy(grid)
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    before = 0
                elif i == 0:
                    before = path[i][j-1]
                elif j == 0:
                    before = path[i-1][j]
                else:
                    before = min(path[i-1][j], path[i][j-1])
                path[i][j] = before + grid[i][j]
        return path[m-1][n-1]
```

发现path数组没有必要重新复制出来，可以直接使用grid代表了。这样实际上就对grid进行了一个覆盖：遍历过的地方代表path，还没遍历到的地方代表grid。

这个算法的时间复杂度是O(m * n)，空间复杂度是O(1)。由于少了复制数组的一步，事实上真的变快了。

```python
class Solution:
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid or not grid[0]: return 0
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    before = 0
                elif i == 0:
                    before = grid[i][j-1]
                elif j == 0:
                    before = grid[i-1][j]
                else:
                    before = min(grid[i-1][j], grid[i][j-1])
                grid[i][j] = before + grid[i][j]
        return grid[m-1][n-1]
```

二刷的时候使用的C++，方法仍然是动态规划，第一行的每个状态等于左边状态+当前位置，和第一列的每个状态等于上边状态+当前位置。其余位置等于上边和左边的状态最小值加上当前位置。

C++代码如下：

```cpp
class Solution {
public:
    int minPathSum(vector<vector<int>>& grid) {
        const int M = grid.size(), N = grid[0].size();
        vector<vector<int>> dp(M, vector<int>(N, 0));
        dp[0][0] = grid[0][0];
        for (int i = 1; i < M; ++i)
            dp[i][0] = dp[i - 1][0] + grid[i][0];
        for (int j = 0; j < N; ++j)
            dp[0][j] = dp[0][j - 1] + grid[0][j];
        for (int i = 1; i < M; ++i) {
            for (int j = 1; j < N; ++j) {
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j];
            }
        }
        return dp[M - 1][N - 1];
    }
};
```


参考资料：


## 日期

2018 年 9 月 11 日 —— 天好阴啊
2018 年 12 月 29 日 —— 2018年剩余电量不足1%
