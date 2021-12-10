

作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)


题目地址：https://leetcode.com/problems/available-captures-for-rook/


## 题目描述

On a ``N x N`` grid of cells, each cell ``(x, y)`` with ``0 <= x < N`` and ``0 <= y < N`` has a lamp.

Initially, some number of lamps are on.  ``lamps[i]`` tells us the location of the i-th lamp that is on.  Each lamp that is on illuminates every square on its x-axis, y-axis, and both diagonals (similar to a Queen in chess).

For the i-th query queries[i] = (x, y), the answer to the query is 1 if the cell (x, y) is illuminated, else 0.

After each query ``(x, y)`` [in the order given by ``queries``], we turn off any lamps that are at cell ``(x, y)`` or are adjacent 8-directionally (ie., share a corner or edge with cell ``(x, y)``.)

Return an array of answers.  Each value ``answer[i]`` should be equal to the answer of the ``i``-th query ``queries[i]``.
 

Example 1:

    Input: N = 5, lamps = [[0,0],[4,4]], queries = [[1,1],[1,0]]
    Output: [1,0]
    Explanation: 
    Before performing the first query we have both lamps [0,0] and [4,4] on.
    The grid representing which cells are lit looks like this, where [0,0] is the top left corner, and [4,4] is the bottom right corner:
    1 1 1 1 1
    1 1 0 0 1
    1 0 1 0 1
    1 0 0 1 1
    1 1 1 1 1
    Then the query at [1, 1] returns 1 because the cell is lit.  After this query, the lamp at [0, 0] turns off, and the grid now looks like this:
    1 0 0 0 1
    0 1 0 0 1
    0 0 1 0 1
    0 0 0 1 1
    1 1 1 1 1
    Before performing the second query we have only the lamp [4,4] on.  Now the query at [1,0] returns 0, because the cell is no longer lit.
 

Note:

1. 1 <= N <= 10^9
1. 0 <= lamps.length <= 20000
1. 0 <= queries.length <= 20000
1. lamps[i].length == queries[i].length == 2

## 题目大意

给出了一个N*N的格子空间，在lams[i]位置上有灯，每个灯会照亮相同x方向、相同y方向、和两条对角线方向共四个方向。我们给出了一系列的queries，这个queries[i]代表查询该位置是否有亮光，同时每次查询的话会把该位置和该位置的8联通方向的亮灯全部关掉。如果queries[i]有光亮的话，那么返回1，否则返回0，问最后的查询结果是多少。

## 解题方法

### 哈希

这个题目其实已经告诉我们，类似于象棋的皇后问题。那么就联想起前面做过的[51. N-Queens][1]问题，在N皇后问题中，判断两个点是否相同的x和y坐标当然容易，判断两点是否在对角线上怎么做呢？

在同一条左斜线上的点，方程式都形如x+y = c，也就是他们的坐标之和相等
在同一条右斜线上的点，方程式都刑辱y = x+c，也就是他们的坐标之差相等

所以，如果知道了这个结论，我们只需要四个字典，分别保存每个点的横坐标、纵坐标、x + y、x - y，然后如果有两个点的满足其中任何一个相等就说明两者共线。

代码还是很简单的，只是别手误就行。

C++代码如下：

```cpp
class Solution {
public:
    vector<int> gridIllumination(int N, vector<vector<int>>& lamps, vector<vector<int>>& queries) {
        unordered_map<int, int> xcount;
        unordered_map<int, int> ycount;
        unordered_map<int, int> l_diagcount;
        unordered_map<int, int> r_diagcount;
        set<pair<int, int>> lset;
        for (auto l : lamps) {
            ++xcount[l[0]];
            ++ycount[l[1]];
            ++l_diagcount[l[0] + l[1]];
            ++r_diagcount[l[0] - l[1]];
            lset.insert({l[0], l[1]});
        }
        vector<int> res;
        for (auto q : queries) {
            if (xcount[q[0]] || ycount[q[1]] || l_diagcount[q[0] + q[1]] || r_diagcount[q[0] - q[1]]) {
                res.push_back(1);
            } else {
                res.push_back(0);
            }
            for (int i = -1; i <= 1; ++i) {
                for (int j = -1; j <= 1; ++j) {
                    pair<int, int> xy = {q[0] + i, q[1] + j};
                    if (lset.count(xy)) {
                        --xcount[xy.first];
                        --ycount[xy.second];
                        --l_diagcount[xy.first + xy.second];
                        --r_diagcount[xy.first - xy.second];
                        lset.erase(xy);
                    }
                }
            }
        }
        return res;
    }
};
```

## 日期

2019 年 2 月 24 日 —— 周末又结束了


  [1]: https://blog.csdn.net/fuxuemingzhu/article/details/85227593
