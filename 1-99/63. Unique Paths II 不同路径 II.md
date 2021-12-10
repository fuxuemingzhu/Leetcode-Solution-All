作者： 		负雪明烛 
id：				fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---

题目地址：https://leetcode.com/problems/unique-paths-ii/description/


## 题目描述：

A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

Now consider if some obstacles are added to the grids. How many unique paths would there be?

![此处输入图片的描述][1]

An obstacle and empty space is marked as ``1`` and ``0`` respectively in the grid.

Note: m and n will be at most 100.

Example 1:

    Input:
    [
      [0,0,0],
      [0,1,0],
      [0,0,0]
    ]
    Output: 2
    
    Explanation:
    There is one obstacle in the middle of the 3x3 grid above.
    There are two ways to reach the bottom-right corner:
    1. Right -> Right -> Down -> Down
    2. Down -> Down -> Right -> Right


## 题目大意

给出了一个m * n的地图，上面有个机器人位于左上角，现在他想到达右下角。但是这个地图某些位置可能有障碍物。它每次只能向右边或者下边走一步，问能到达右下角的方式有多少种。

## 解题方法

### 方法一：记忆化搜索

这个题是[62. Unique Paths][2]的翻版，加上了障碍物一项。同样的分析：

到达某个位置的次数怎么计算？可以想到是到达这个位置上面的位置的次数+到达坐标的次数。

注意了，有障碍物！其实有障碍物的话可以直接返回这个点的可能次数是0.为什么？因为每个点能从左或者上边过来，如果某个方向是障碍物的话，那么从障碍物过来的可能性是0.

如果递归到边界以外的话，可能性也是0，这样给第一行或者第一列提供了终止条件。如果是左上角开始的位置，那么方式只有1种，代表了起始条件。

另外使用了记忆化数组保存已经走过位置的次数，可以加快运算。

时间复杂度是O(m * n)，空间复杂度是O(m * n)。这个方法AC了，但是竟然没进排名。。

```python
class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        memo = [[0] * n for _ in range(m)]
        return self.dfs(m - 1, n - 1, obstacleGrid, memo)
    
    def dfs(self, m, n, obstacleGrid, memo): # methods of postion m, n
        if obstacleGrid[m][n] == 1:
            return 0
        if m < 0 or n < 0:
            return 0
        if m == n == 0:
            return 1
        if memo[m][n]:
            return memo[m][n]
        up = self.dfs(m - 1, n, obstacleGrid, memo)
        left = self.dfs(m, n - 1, obstacleGrid, memo)
        memo[m][n] = up + left
        return memo[m][n]
```

### 方法二：动态规划

看到上面记忆化搜索的方法就知道这个题同样可以使用动态规划解决。第一行第一列的所有方式只有1种，到达其他位置的方式是这个位置上面 + 这个位置左边用DP的话，注意需要判断某个位置是不是有障碍物，如果有障碍物，那么到达这个地方的方法是0。总体思路和上面记忆化搜索差不多。

时间复杂度是O(m * n)，空间复杂度是O(m * n)。

动态规划写了三种方法，不停地优化，最后打败了100%的提交。

第一种，就是对上面的记忆化搜索的修改，给整个数组最上面和最左边加了一层边界，其含义是到达这个位置的方法是0，然后这么做的目的是防止下标越界。

这个做法超过了69%的提交。

```python
class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if obstacleGrid[i - 1][j - 1] == 1:
                    dp[i][j] = 0
                else:
                    if i == j == 1:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[m][n]
```

上面的方法不好，因为修改了边界之后和原始的地图对应关系被打乱了，很容易出错。所以有了第二个版本，不要添加边界，直接判断是不是到达了最上面一行或者最左边一行，如果不是第一行那么加上上面行的数值，如果不是第一列那么加上第一列的数值。

这个做法打败了100%的提交。

```python
class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0] * n for _ in range(m)]
        if obstacleGrid[0][0] == 0:
            dp[0][0] = 1
        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                else:
                    if i != 0:
                        dp[i][j] += dp[i - 1][j]
                    if j != 0:
                        dp[i][j] += dp[i][j - 1]
        return dp[m - 1][n - 1]
```

第三个版本，利用Python语言特性来减少判断次数。我们遍历的方向是第一行从左到右，然后再第二行从左到右的方式进行的，这样如果把dp全部初始化成了0，那么当计算第一行的时候dp[-1][j]实际上就是最后一行的dp，也就是0.同样的，dp[i][-1]实际上是最后一列的dp，但是还没遍历到过，所以也是0.总之，虽然dp数组在计算第一行和第一列的时候用到了最后一行最后一列的dp数据，但是由于还没有遍历到，那么dp数组实际上是0，所以完全可以省去判断。这种方式对于C++和Java不能进行负数索引的不能用。

这个做法打败了100%的提交。


```python
class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0] * n for _ in range(m)]
        if obstacleGrid[0][0] == 0:
            dp[0][0] = 1
        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] == 0:
                    if i == j == 0:
                        continue
                    else:
                        dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[m - 1][n - 1]
```

上面两个做法可以看出，这个题的规模确实很小，总运行时间只有20ms，就能打败100%。哪怕少了一个判断，就能超出一部分提交。

二刷的时候，使用动态规划，C++代码如下：

```cpp
class Solution {
public:
    int uniquePathsWithObstacles(vector<vector<int>>& obstacleGrid)  {
        const int M = obstacleGrid.size(), N = obstacleGrid[0].size();
        vector<vector<int>> dp(M + 1, vector<int>(N + 1, 0));
        if (obstacleGrid[0][0] != 1) 
            dp[1][1] = 1;
        for (int i = 1; i < M + 1; ++i) {
            for (int j = 1; j < N + 1; ++j) {
                if (i == 1 && j == 1) continue;
                if (obstacleGrid[i - 1][j - 1] != 1) 
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1];
            } 
        }
        return dp[M][N];
    }
};
```


## 日期

2018 年 10 月 18 日 —— 做梦都在科研
2018 年 12 月 29 日 —— 2018年剩余电量不足1%

  [1]: https://leetcode.com/static/images/problemset/robot_maze.png
  [2]: https://blog.csdn.net/fuxuemingzhu/article/details/79337352
  [3]: https://gss3.bdstatic.com/-Po3dSag_xI4khGkpoWK1HF6hhy/baike/s=162/sign=f68c65f4b5b7d0a27fc9009bf9ee760d/5d6034a85edf8db190ab75220e23dd54574e74ea.jpg
