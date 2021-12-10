

- 作者：    负雪明烛
- id：      fuxuemingzhu
- 个人博客：[http://fuxuemingzhu.cn/](http://fuxuemingzhu.cn/)

---
@[TOC](目录)

题目地址：https://leetcode-cn.com/problems/number-of-corner-rectangles/

## 题目描述

Given a grid where each entry is only 0 or 1, find the number of corner rectangles.

A corner rectangle is 4 distinct 1s on the grid that form an axis-aligned rectangle. Note that only the corners need to have the value 1. Also, all four 1s used must be distinct.

Example 1:

    Input: grid = 
    [[1, 0, 0, 1, 0],
     [0, 0, 1, 0, 1],
     [0, 0, 0, 1, 0],
     [1, 0, 1, 0, 1]]
    Output: 1
    Explanation: There is only one corner rectangle, with corners grid[1][2], grid[1][4], grid[3][2], grid[3][4].

Example 2:

    Input: grid = 
    [[1, 1, 1],
     [1, 1, 1],
     [1, 1, 1]]
    Output: 9
    Explanation: There are four 2x2 rectangles, four 2x3 and 3x2 rectangles, and one 3x3 rectangle.

Example 3:

    Input: grid = 
    [[1, 1, 1, 1]]
    Output: 0
    Explanation: Rectangles must have four distinct corners.

Note:

1. The number of rows and columns of grid will each be in the range `[1, 200]`.
1. Each `grid[i][j]` will be either 0 or 1.
1. The number of 1s in the grid will be at most 6000.

## 题目大意

给定一个只包含 0 和 1 的网格，找出其中角矩形的数量。

一个 角矩形 是由四个不同的在网格上的 1 形成的轴对称的矩形。注意只有角的位置才需要为 1。并且，4 个 1 需要是不同的。

## 解题方法

### 遍历

一定需要四重循环分别维护矩形的上下左右四条边吗？答案是否定的。

可以固定矩形的上下两条边界，然后遍历其中的每一列，统计这两行一列的交点是否都为1，所有都为1的列累计得到count。那么在固定此上下两条边界的情况下，能组成的所有角都为1的矩形是从count条边中选择两条不同的，答案是`count * (count - 1) / 2`.

总共是三重循环，时间复杂度是O(M^2*N).

C++代码如下：

```cpp
class Solution {
public:
    int countCornerRectangles(vector<vector<int>>& grid) {
        if (!grid.size() || !grid[0].size()) return 0;
        const int M = grid.size();
        const int N = grid[0].size();
        int res = 0;
        for (int row1 = 0; row1 < M; ++row1) {
            for (int row2 = row1 + 1; row2 < M; ++row2) {
                int count = 0;
                for (int col = 0; col < N; ++col) {
                    if (grid[row1][col] == 1 && grid[row2][col] == 1) {
                        count ++;
                    }
                }
                res += count * (count - 1) / 2;
            }
        }
        return res;
    }
};
```

参考资料：https://leetcode-cn.com/problems/number-of-corner-rectangles/solution/java-by-zxy0917-16/

## 日期

2019 年 9 月 24 日 —— 梦见回到了小学，小学已经芳草萋萋破败不堪


  [1]: https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1569299800527&di=0791f14b34f5db98eb9acb10fbb908b1&imgtype=0&src=http://gss0.baidu.com/94o3dSag_xI4khGko9WTAnF6hhy/zhidao/pic/item/1ad5ad6eddc451da41652b3bb0fd5266d116324a.jpg
