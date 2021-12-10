
- 作者：    负雪明烛
- id：      fuxuemingzhu
- 个人博客：[http://fuxuemingzhu.cn/](http://fuxuemingzhu.cn/)

---
@[TOC](目录)


题目地址：https://leetcode-cn.com/problems/paint-house/

## 题目描述

There are a row of n houses, each house can be painted with one of the three colors: `red, blue or green`. The cost of painting each house with a certain color is different. You have to paint all the houses such that no two adjacent houses have the same color.

The cost of painting each house with a certain color is represented by a `n x 3` cost matrix. For example, `costs[0][0]` is the cost of painting house 0 with color `red`; `costs[1][2]` is the cost of painting house 1 with color `green`, and so on... Find the minimum cost to paint all houses.

Note:
All costs are positive integers.

Example:

    Input: [[17,2,17],[16,16,5],[14,3,19]]
    Output: 10
    Explanation: Paint house 0 into blue, paint house 1 into green, paint house 2 into blue. 
                 Minimum cost: 2 + 5 + 3 = 10.

## 题目大意

假如有一排房子，共 n 个，每个房子可以被粉刷成红色、蓝色或者绿色这三种颜色中的一种，你需要粉刷所有的房子并且使其相邻的两个房子颜色不能相同。

当然，因为市场上不同颜色油漆的价格不同，所以房子粉刷成不同颜色的花费成本也是不同的。每个房子粉刷成不同颜色的花费是以一个n x 3的矩阵来表示的。

例如，costs[0][0] 表示第 0 号房子粉刷成红色的成本花费；costs[1][2]表示第 1 号房子粉刷成绿色的花费，以此类推。请你计算出粉刷完所有房子最少的花费成本。

## 解题方法

### 动态规划

计算**刷完**第n房子为止，三种颜色分别累计需要的最少花费dp[n][0], dp[n][1], d[n][2]。那么递推公式是：

    dp[n][0] = min(dp[n - 1][1], dp[n - 1][2]) + costs[n - 1][0];
    dp[n][1] = min(dp[n - 1][0], dp[n - 1][2]) + costs[n - 1][1];
    dp[n][2] = min(dp[n - 1][0], dp[n - 1][1]) + costs[n - 1][2];

意义是不能和前面的房子刷相同的颜色，那么就使用前面房子另外两种颜色的累计最小花费，加上刷当前的颜色的花费。最后去最小即可。

C++代码如下：

```cpp
class Solution {
public:
    int minCost(vector<vector<int>>& costs) {
        const int N = costs.size();
        vector<vector<int>> dp(N + 1, vector<int>(3, 0));
        int res = 0;
        for (int n = 1; n <= N; ++n) {
            dp[n][0] = min(dp[n - 1][1], dp[n - 1][2]) + costs[n - 1][0];
            dp[n][1] = min(dp[n - 1][0], dp[n - 1][2]) + costs[n - 1][1];
            dp[n][2] = min(dp[n - 1][0], dp[n - 1][1]) + costs[n - 1][2];
        }
        return min(dp[N][0], min(dp[N][1], dp[N][2]));
    }
};
```

## 日期

2019 年 9 月 18 日 —— 今日又是九一八
