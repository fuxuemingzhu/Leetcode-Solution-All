
作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)

题目地址：[https://leetcode.com/problems/max-area-of-island/description/][1]


## 题目描述

Given a non-empty 2D array grid of 0's and 1's, an island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

Find the maximum area of an island in the given 2D array. (If there is no island, the maximum area is 0.)

Example 1:

    [[0,0,1,0,0,0,0,1,0,0,0,0,0],
     [0,0,0,0,0,0,0,1,1,1,0,0,0],
     [0,1,1,0,1,0,0,0,0,0,0,0,0],
     [0,1,0,0,1,1,0,0,1,0,1,0,0],
     [0,1,0,0,1,1,0,0,1,1,1,0,0],
     [0,0,0,0,0,0,0,0,0,0,1,0,0],
     [0,0,0,0,0,0,0,1,1,1,0,0,0],
     [0,0,0,0,0,0,0,1,1,0,0,0,0]]
    Given the above grid, return 6. Note the answer is not 11, because the island must be connected 4-directionally.

Example 2:

    [[0,0,0,0,0,0,0,0]]
    Given the above grid, return 0.

Note: The length of each dimension in the given grid does not exceed 50.

## 题目大意

４－联通的一个区域是一个岛，现在要统计面积最大的岛的面积。

## 解题方法

### 方法一：DFS

DFS是深度优先遍历，在不能再走的时候，要回撤再搜索。这里可能就会出现一个问题，回撤之后再搜索的时候怎么能判定哪些位置已经搜索过了，避免重复搜索问题呢？一般有两个方法：(1)使用一个visited数组保存已经走过的位置；(2)把已经走过的位置设置为不可走的状态。

下面的方法使用**把已经走过的路给设成０，即不能再走**。对原始的地图中所有的点都遍历一遍，找出每个点所从属的小岛的最大面积。再用一个全局的变量，记录所有小岛的最大面积。

为了便于理解，我举个例子，如果有下面的地图：

	1,1
	1,1

使用DFS的遍历位置的路径是这样的（蓝色），每次把遍历到的位置设置为0，下次就不会继续搜索这个已经搜索过位置（黄色）了：
![在这里插入图片描述](https://img-blog.csdnimg.cn/20200315200756145.jpg?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2Z1eHVlbWluZ3podQ==,size_16,color_FFFFFF,t_70)

python代码如下：

```python
class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        row, col = len(grid), len(grid[0])
        answer = 0
        def dfs(i, j):
            if 0 <= i <= row - 1 and 0 <= j <= col - 1 and grid[i][j]:
                grid[i][j] = 0 # 重要，防止再次搜索
                return  1 + dfs(i - 1, j) + dfs(i + 1, j) + dfs(i, j - 1) + dfs(i, j + 1)
            return 0
        return max(dfs(i, j) for i in xrange(row) for j in xrange(col))
```

二刷，直接按照模板来写的。

```python
class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        self.res = 0
        self.island = 0
        M, N = len(grid), len(grid[0])
        for i in range(M):
            for j in range(N):
                if grid[i][j]:
                    self.dfs(grid, i, j)
                    self.res = max(self.res, self.island)
                    self.island = 0
        return self.res
    
    def dfs(self, grid, i, j): # ensure grid[i][j] == 1
        M, N = len(grid), len(grid[0])
        grid[i][j] = 0
        self.island += 1
        dirs = [(0, 1), (0, -1), (-1, 0), (1, 0)]
        for d in dirs:
            x, y = i + d[0], j + d[1]
            if 0 <= x < M and 0 <= y < N and grid[x][y]:
                self.dfs(grid, x, y)
```

C++代码如下：

```cpp
class Solution {
public:
    vector<vector<int>> dirs{{1, 0}, {-1, 0}, {0, -1}, {0, 1}};
    int maxAreaOfIsland(vector<vector<int>>& grid) {
        const int M = grid.size(), N = grid[0].size();
        int res = 0, island = 0;
        for (int i = 0; i < M; i++) {
            for (int j = 0; j < N; j++) {
                if (grid[i][j]) {
                    dfs(grid, i, j, island);
                    res = max(res, island);
                    island = 0;
                }
            }
        }
        return res;
    }
    void dfs(vector<vector<int>>& grid, int i, int j, int& island) {
        const int M = grid.size(), N = grid[0].size();
        grid[i][j] = 0; // 重要
        island ++;
        for (auto d : dirs) {
            int x = i + d[0], y = j + d[1];
            if (x >= 0 && x < M && y >= 0 && y < N && grid[x][y])
                dfs(grid, x, y, island);
        }
    }
};
```

### 方法二：BFS

BFS方法也是显而易见的，只要找出一个1的节点之后，然后把所有的4联通全部都进入队列，然后搜索就好了。

这个方法需要注意的是，把一个位置放入队列的同时，应该理解把该位置置0，否则有可能被重复的放入队列。

继续举上面的个例子，如果有下面的地图：

	1,1
	1,1

BFS中放入队列中的顺序是这样的（蓝色），每次把遍历到的位置设置为0，下次就不会继续搜索这个已经搜索过位置（黄色）了：：
![在这里插入图片描述](https://img-blog.csdnimg.cn/20200315200053331.jpg?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2Z1eHVlbWluZ3podQ==,size_16,color_FFFFFF,t_70)
因此，把每个位置放入队列之后，立马把这个位置设置为0，就可以防止下次被别的节点放进队列中了。


C++代码如下：

```cpp
class Solution {
public:
    vector<vector<int>> ds{{1, 0}, {-1, 0}, {0, -1}, {0, 1}};
    int maxAreaOfIsland(vector<vector<int>>& grid) {
        const int M = grid.size(), N = grid[0].size();
        queue<pair<int, int>> q;
        int res = 0;
        for (int i = 0; i < M; i++) {
            for (int j = 0; j < N; j++) {
                if (grid[i][j]) {
                    int island = 0;
                    q.push({i, j});
                    while (!q.empty()) {
                        auto p = q.front(); q.pop();
                        grid[p.first][p.second] = 0;
                        island ++;
                        for (auto d : ds) {
                            int x = p.first + d[0];
                            int y = p.second + d[1];
                            if (x >= 0 && x < M && y >= 0 && y < N && grid[x][y]) {
                                grid[x][y] = 0;
                                q.push({x, y});
                            }
                        }
                    }
                    res = max(res, island);
                }
            }
        }
        return res;
    }
};
```

## 日期

2018 年 1 月 27 日 
2018 年 12 月 10 日 —— 又是周一！
2020 年 3 月 15 日 —— 今天给这个博客新加了两个图便于理解

  [1]: https://leetcode.com/problems/max-area-of-island/description/
