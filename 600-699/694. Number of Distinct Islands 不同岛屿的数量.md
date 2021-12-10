

- 作者：    负雪明烛
- id：      fuxuemingzhu
- 个人博客：[http://fuxuemingzhu.cn/](http://fuxuemingzhu.cn/)

---
@[TOC](目录)


题目地址：https://leetcode-cn.com/problems/number-of-distinct-islands/

## 题目描述

Given a non-empty 2D array grid of 0's and 1's, an island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

Count the number of distinct islands. An island is considered to be the same as another if and only if one island can be translated (and not rotated or reflected) to equal the other.

Example 1:

    11000
    11000
    00011
    00011
    Given the above grid map, return 1.

Example 2:

    11011
    10000
    00001
    11011
    Given the above grid map, return 3.

Notice that:
    
    11
    1

and

     1
    11

are considered different island shapes, because we do not consider reflection / rotation.

Note: The length of each dimension in the given grid does not exceed 50.


## 题目大意

找出形状不同的岛屿数目。

## 解题方法

### DFS

这个题如果是问岛屿的数量，那么可以直接使用单纯的DFS解决。但是难点在于考察`不同`的岛屿。

为了保存每个岛屿的形状，我们使用了vector<int> path，里面存放的是以进入dfs的坐标为起点，把四联通的每个1转化成相对坐标，并且hash运算，保存dfs的路径。只要dfs的查找方式是固定的，那么路径就是一样的，从而得到的小岛的形状也是固定的。

在dfs的搜索中，一边搜索一边把搜索过的位置全部至0，这是个小窍门，即设置已经走过的位置不可用，从而达到防止重复走的问题。

求相对形状：把每个岛的左上角当作是 (0, 0)，例如，如果一个岛是由 [(2, 3), (2, 4), (3, 4)] 构成，当固定左上角时，我们可以把这个形状看作是 [(0, 0), (0, 1), (1, 1)]。

C++中可以使用set对vector<int>去重，但是unordered_set是不可以的。


C++代码如下：

```cpp
class Solution {
public:
    int numDistinctIslands(vector<vector<int>>& grid) {
        if (!grid.size() || !grid[0].size()) return 0;
        M = grid.size();
        N = grid[0].size();
        set<vector<int>> s;
        for (int i = 0; i < M; ++i) {
            for (int j = 0; j < N; ++j) {
                if (grid[i][j] == 1) {
                    vector<int> path;
                    dfs(grid, path, i, j, i, j);
                    if (!path.empty()) {
                        s.insert(path);
                    }
                }
            }
        }
        return s.size();
    }
    void dfs(vector<vector<int>>& grid, vector<int>& path, int sr, int sc, int r, int c) {
        if (r < 0 || r >= M || c < 0 || c >= N || grid[r][c] == 0) return;
        path.push_back((r - sr) * N + c - sc);
        grid[r][c] = 0;
        dfs(grid, path, sr, sc, r - 1, c);
        dfs(grid, path, sr, sc, r + 1, c);
        dfs(grid, path, sr, sc, r, c - 1);
        dfs(grid, path, sr, sc, r, c + 1);
    }
private:
    int M = 0;
    int N = 0;
};
```

参考资料：https://leetcode-cn.com/problems/number-of-distinct-islands/solution/dfszhao-dao-yu-settong-ji-bu-tong-xing-zhuang-dao-/

## 日期

2019 年 9 月 21 日 —— 莫生气，我若气病谁如意


  [1]: https://assets.leetcode.com/uploads/2018/10/12/candy_crush_example_2.png
  [2]: https://blog.csdn.net/fuxuemingzhu/article/details/101068011
