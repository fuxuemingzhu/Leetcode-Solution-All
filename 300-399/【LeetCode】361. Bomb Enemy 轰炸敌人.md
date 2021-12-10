

- 作者：    负雪明烛
- id：      fuxuemingzhu
- 个人博客：[http://fuxuemingzhu.cn/](http://fuxuemingzhu.cn/)

---
@[TOC](目录)


题目地址：https://leetcode-cn.com/problems/bomb-enemy/

## 题目描述

Given a 2D grid, each cell is either a wall 'W', an enemy 'E' or empty '0' (the number zero), return the maximum enemies you can kill using one bomb.
The bomb kills all the enemies in the same row and column from the planted point until it hits the wall since the wall is too strong to be destroyed.
Note: You can only put the bomb at an empty cell.

![此处输入图片的描述][1]

Example:

    Input: [["0","E","0","0"],["E","0","W","E"],["0","E","0","0"]]
    Output: 3 
    Explanation: For the given grid,
    
    0 E 0 0 
    E 0 W E 
    0 E 0 0
    
    Placing a bomb at (1,1) kills 3 enemies.
    

## 题目大意

请你计算一个炸弹最多能炸多少敌人。
由于炸弹的威力不足以穿透墙体，炸弹只能炸到同一行和同一列没被墙体挡住的敌人。

## 解题方法

### 暴力搜索

这是在微软面试遇到的真题，做法其实很直接，就是暴力计算放置在每个空位置上能炸死的一行一列的所有敌人就行了。需要注意的是需要从放炸弹的位置向四个方向进行搜索，并且超出边界或者遇到墙壁就停止。

C++代码如下：

```cpp
class Solution {
public:
    int maxKilledEnemies(vector<vector<char>>& grid) {
        if (grid.empty() || grid[0].empty()) return 0;
        int res = 0;
        for (int i = 0; i < grid.size(); ++i) {
            for (int j = 0; j < grid[0].size(); ++j) {
                if (grid[i][j] == '0') {
                    res = max(res, killEnemies(grid, i, j));
                }
            }
        }
        return res;
    }
    int killEnemies(vector<vector<char>>& grid, int x, int y) {
        int count = 0;
        for (vector<int>& curd : dirs) {
            int newx = x;
            int newy = y;
            while (newx >= 0 && newx < grid.size() && newy >= 0 && newy < grid[0].size() 
                   && grid[newx][newy] != 'W') {
                if (grid[newx][newy] == 'E')
                    count ++;
                newx += curd[0];
                newy += curd[1];
            }
        }
        return count;
    }
private:
    vector<vector<int>> dirs = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};
};
```

## 日期

2019 年 9 月 20 日 —— 是选择中国互联网式加班？还是外企式养生？


  [1]: https://assets.leetcode-cn.com/aliyun-lc-upload/images/361_Bomb_Enemy.gif
