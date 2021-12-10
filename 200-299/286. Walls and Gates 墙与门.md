

- 作者：    负雪明烛
- id：      fuxuemingzhu
- 个人博客：[http://fuxuemingzhu.cn/](http://fuxuemingzhu.cn/)

---
@[TOC](目录)

题目地址：https://leetcode-cn.com/problems/walls-and-gates/

## 题目描述

You are given a m x n 2D grid initialized with these three possible values.

- `-1` - A wall or an obstacle.
- `0` - A gate.
- `INF` - Infinity means an empty room. We use the value 231 - 1 = 2147483647 to represent INF as you may assume that the distance to a gate is less than 2147483647.

Fill each empty room with the distance to its nearest gate. If it is impossible to reach a gate, it should be filled with INF.

Example: 

    Given the 2D grid:
    
    INF  -1  0  INF
    INF INF INF  -1
    INF  -1 INF  -1
      0  -1 INF INF
    After running your function, the 2D grid should be:
    
      3  -1   0   1
      2   2   1  -1
      1  -1   2  -1
      0  -1   3   4

## 题目大意

你被给定一个 m × n 的二维网格，网格中有以下三种可能的初始化值：

1. -1 表示墙或是障碍物
1. 0 表示一扇门
1. INF 无限表示一个空的房间。然后，我们用 231 - 1 = 2147483647 代表 INF。你可以认为通往门的距离总是小于 2147483647 的。

你要给每个空房间位上填上该房间到 最近 门的距离，如果无法到达门，则填 INF 即可。

## 解题方法

### BFS

这个题可以使用BFS和DFS去解决，我选用的BFS。

1. 找出所有为0的位置，放入队列中
2. 从为0的位置开始向四个方向遍历，直接修改迷宫的可以走的位置的数字是距离门最近的距离
3. 把新的可以走的位置放入队列中，继续搜索

C++代码如下：

```cpp
class Solution {
public:
    void wallsAndGates(vector<vector<int>>& rooms) {
        if (rooms.empty() || rooms[0].empty()) return;
        M = rooms.size();
        N = rooms[0].size();
        for (int i = 0; i < M; ++i) {
            for (int j = 0; j < N; ++j) {
                if (rooms[i][j] == 0) {
                    bfs(rooms, i, j);
                }
            }
        }
    }
    void bfs(vector<vector<int>>& rooms, int x, int y) {
        if (rooms[x][y] != 0) return;
        queue<vector<int>> que;
        que.push({x, y});
        while (!que.empty()) {
            vector<int> cur = que.front(); que.pop();
            for (auto& dir : dirs) {
                int newx = cur[0] + dir[0];
                int newy = cur[1] + dir[1];
                if (newx < 0 || newx >= M || newy < 0 || newy >= N 
                    || rooms[newx][newy] <= rooms[cur[0]][cur[1]])
                    continue;
                rooms[newx][newy] = rooms[cur[0]][cur[1]] + 1;
                que.push({newx, newy});
            }
        }
    }
private:
    int M, N;
    vector<vector<int>> dirs = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};
};
```

## 日期

2019 年 9 月 23 日 —— 昨夜睡的早，错过了北京的烟火
