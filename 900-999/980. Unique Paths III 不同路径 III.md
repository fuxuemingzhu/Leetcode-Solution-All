作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)


题目地址：https://leetcode.com/problems/unique-paths-iii/


## 题目描述

On a 2-dimensional ``grid``, there are 4 types of squares:

- 1 represents the starting square.  There is exactly one starting square.
- 2 represents the ending square.  There is exactly one ending square.
- 0 represents empty squares we can walk over.
- -1 represents obstacles that we cannot walk over.
Return the number of 4-directional walks from the starting square to the ending square, that **walk over every non-obstacle square exactly once*.

 

Example 1:

    Input: [[1,0,0,0],[0,0,0,0],[0,0,2,-1]]
    Output: 2
    Explanation: We have the following two paths: 
    1. (0,0),(0,1),(0,2),(0,3),(1,3),(1,2),(1,1),(1,0),(2,0),(2,1),(2,2)
    2. (0,0),(1,0),(2,0),(2,1),(1,1),(0,1),(0,2),(0,3),(1,3),(1,2),(2,2)

Example 2:

    Input: [[1,0,0,0],[0,0,0,0],[0,0,0,2]]
    Output: 4
    Explanation: We have the following four paths: 
    1. (0,0),(0,1),(0,2),(0,3),(1,3),(1,2),(1,1),(1,0),(2,0),(2,1),(2,2),(2,3)
    2. (0,0),(0,1),(1,1),(1,0),(2,0),(2,1),(2,2),(1,2),(0,2),(0,3),(1,3),(2,3)
    3. (0,0),(1,0),(2,0),(2,1),(2,2),(1,2),(1,1),(0,1),(0,2),(0,3),(1,3),(2,3)
    4. (0,0),(1,0),(2,0),(2,1),(1,1),(0,1),(0,2),(0,3),(1,3),(1,2),(2,2),(2,3)

Example 3:

    Input: [[0,1],[2,0]]
    Output: 0
    Explanation: 
    There is no path that walks over every empty square exactly once.
    Note that the starting and ending square can be anywhere in the grid.
     

Note:

1. 1 <= grid.length * grid[0].length <= 20

## 题目大意

给了一个二维矩阵，1代表起点，2代表终点，0代表可以走的格子，-1代表障碍物。求从起点到终点，把所有的可以走的格子都遍历一遍，所有可能的不同路径数。

## 解题方法

### 回溯法

周赛最后一题却是一个很简单的题目，因为题目给定了格子的大小总共才20个！也就是说可以使用O(2^N)的解法来做，即可以使用回溯法暴力求解所有可能路径，然后判断每个路径是否符合要求。（注：2的20次方 = 1048576.）

本身很简单哈，题目其实只有两个限制：第一，所有空白格子必须走一遍；第二，不能走障碍物上。

因此，我先统计了一下总的有多少个空白格子，然后每次经过一个空白格子都累加一下，如果遍历到终点并且走过的空白格子数等于grid中初始的zerocount，那么说明走过了所有空白格子，符合要求。

至于不能走障碍物，直接判断一下就好了，这个没啥说的。总之题目很简单，暴力求解不用怕。

下面做一下回溯法的思考：

第一，我在第一遍的时候保存了经历的路径，然后使用set去重，我以为只有这样才能保证结果里面不会出现重复的路径，但事实上是不需要的。回溯法不出现重复的路径，因为我们向后退了一步之后，下一轮的时候不会再沿着刚才已经尝试过的方向走了，这也就是对方向进行遍历的意义所在。只要回到上一步的位置，然后沿着另外一个方向继续寻找，那么找到的新的路径一定是不一样的。这也是回溯法的时间复杂度是O(2^N)的原因：找到了所有可能的路径，而这些路径是不会重复的。

第二，在dfs的时候，如果当前位置是0的话，我就对找到的0的个数pathcount+1，而之后是没有pathcount-1操作的。为什么？其实可以看出这个变量是统计在已经路过的路径上1的个数，而不同的路径的1的个数一定是不一样的，所以dfs()函数定义的时候对该变量做的是传值而不是传引用。所以，该变量在完成新的路径上0的个数统计之后已经没有意义了，不同的路径是不能共享该变量的，所以不用再对这个变量进行回溯操作。他会在完成自己的历史使命之后，在该dfs()函数结束的时候，退出历史舞台。

c++代码如下：

```cpp
class Solution {
public:
    int uniquePathsIII(vector<vector<int>>& grid) {
        const int M = grid.size();
        const int N = grid[0].size();
        int zerocount = 0;
        int res = 0;
        for (int i = 0; i < M; ++i) {
            for (int j = 0; j < N; ++j) {
                if (grid[i][j] == 0) {
                    ++zerocount;
                }
            }
        }
        for (int i = 0; i < M; ++i) {
            for (int j = 0; j < N; ++j) {
                if (grid[i][j] == 1) {
                    dfs(grid, i, j, 0, zerocount, res);
                }
            }
        }
        return res;
    }
    
    void dfs(vector<vector<int>>& grid, int x, int y, int pathcount, int zerocount, int& res) {
        if (grid[x][y] == 2 && pathcount == zerocount) 
            ++res;
        const int M = grid.size();
        const int N = grid[0].size();
        int pre = grid[x][y];
        if (pre == 0)
            ++pathcount;
        grid[x][y] = -1;
        for (auto d : dirs) {
            int nx = x + d.first;
            int ny = y + d.second;
            if (nx < 0 || nx >= M || ny < 0 || ny >= N || grid[nx][ny] == -1)
                continue;
            dfs(grid, nx, ny, pathcount, zerocount, res);
        }
        grid[x][y] = pre;
    }
private:
    vector<pair<int, int>> dirs = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};
};
```


## 日期

2019 年 1 月 20 日 —— 这次周赛有点简单
