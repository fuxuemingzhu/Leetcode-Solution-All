作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)

题目地址：https://leetcode.com/problems/number-of-islands/description/

## 题目描述

Given a 2d grid map of ``'1'``s (land) and ``'0'``s (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:

    Input:
    11110
    11010
    11000
    00000
    
    Output: 1

Example 2:

    Input:
    11000
    11000
    00100
    00011
    
    Output: 3

## 题目大意

有一片水域，四联通的算一个岛，求所有的岛的数目。

## 解题方法

### DFS

这个题在《挑战程序设计竞赛》书的前面就讲了，我觉得还是挺经典的题目。可以直接套模板解决。

做法是，我们对每个有`“1"`的位置进行 DFS，把和它四联通的位置全部变成`“0”`，这样就能把一个点推广到一个岛。

所以，我们总的进行了 DFS 的次数，就是总过有多少个岛的数目。

注意理解dfs函数的意义：已知当前是1，把它周围相邻的所有1全部转成0.

代码如下：

```python3
class Solution:
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        res = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == "1":
                    self.dfs(grid, r, c)
                    res += 1
        return res
        
    def dfs(self, grid, i, j):
        dirs = [[-1, 0], [0, 1], [0, -1], [1, 0]]
        grid[i][j] = "0"
        for dir in dirs:
            nr, nc = i + dir[0], j + dir[1]
            if nr >= 0 and nc >= 0 and nr < len(grid) and nc < len(grid[0]):
                if grid[nr][nc] == "1":
                    self.dfs(grid, nr, nc)
```

C++版本的代码如下：

```cpp
class Solution {
public:
    int numIslands(vector<vector<char>>& grid) {
        if (grid.empty() || grid[0].empty())
            return 0;
        const int M = grid.size();
        const int N = grid[0].size();
        int res = 0;
        for (int i = 0; i < M; ++i) {
            for (int j = 0; j < N; ++j) {
                if (grid[i][j] == '1') {
                    res ++;
                    dfs(grid, i, j);
                }
            }
        }
        return res;
    }
    void dfs(vector<vector<char>>& grid, int x, int y) {
        grid[x][y] = '0';
        const int M = grid.size();
        const int N = grid[0].size();
        for (auto& dir : dirs) {
            int nx = x + dir[0];
            int ny = y + dir[1];
            if (nx < 0 || nx >= M || ny < 0 || ny >= N || grid[nx][ny] == '0')
                continue;
            dfs(grid, nx, ny);
        }
    }
private:
    vector<vector<int>> dirs = {{0, 1}, {0, -1}, {-1, 0}, {1, 0}};
};
```

### BFS

这个题同样可以使用BFS解决。当遇到一个小岛的时候，做个BFS搜索，把它周围的小岛全部转成0即可。速度比DFS稍微慢了一点点。

Python 代码如下：

```python
class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid or not grid[0]: return 0
        M, N = len(grid), len(grid[0])
        que = collections.deque()
        res = 0
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for i in range(M):
            for j in range(N):
                if grid[i][j] == '1':
                    res += 1
                    grid[i][j] = '0'
                    que.append((i, j))
                    while que:
                        x, y = que.pop()
                        for d in directions:
                            nx, ny = x + d[0], y + d[1]
                            if 0 <= nx < M and 0 <= ny < N and grid[nx][ny] == '1':
                                grid[nx][ny] = '0'
                                que.append((nx, ny))
        return res
```

在写 BFS 的时候可以把代码包装成一个函数，需要注意的是，由于BFS会把周围的1全部改成0，所以在出队列的时候，做一个判断，如果当前围着孩子已经被改了，那么就不用下面的搜索了。

C++代码如下：

```cpp
class Solution {
public:
    int numIslands(vector<vector<char>>& grid) {
        if (grid.size() == 0 || grid[0].size() == 0) return 0;
        const int M = grid.size(), N = grid[0].size();
        int res = 0;
        for (int i = 0; i < M; ++i) {
            for (int j = 0; j < N; ++j) {
                if (grid[i][j] == '1') {
                    ++res;
                    bfs(grid, i, j);
                }
            }
        }
        return res;
    }
    // gird[x][y] = 1, delete it and its around.
    void bfs(vector<vector<char>>& grid, int x, int y) {
        const int M = grid.size(), N = grid[0].size();
        queue<pair<int, int>> q;
        q.push({x, y});
        while (!q.empty()) {
            auto head = q.front(); q.pop();
            int x = head.first;
            int y = head.second;
            if (grid[x][y] != '1') continue;
            grid[x][y] = '0';
            for (auto d : dirs) {
                int i = x + d.first;
                int j = y + d.second;
                if (i < 0 || i >= M || j < 0 || j >= N || grid[i][j] != '1') {
                    continue;
                }
                q.push({i, j});
            }
        }
    }
private:
    vector<pair<int, int>> dirs = {{1, 0}, {0, 1}, {-1, 0}, {0, -1}};
};
```

## 日期

2018 年 7 月 20 日 —— 北京的阴雨天，又闷又潮
2019 年 1 月 8 日 —— 别熬夜，我都开始有黑眼圈了。。
2020 年 4 月 20 日 —— 没想到我也会熬夜看剧
