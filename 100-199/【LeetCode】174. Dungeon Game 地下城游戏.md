
作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)


题目地址：https://leetcode.com/problems/dungeon-game/


## 题目描述

The demons had captured the princess (P) and imprisoned her in the bottom-right corner of a dungeon. The dungeon consists of M x N rooms laid out in a 2D grid. Our valiant knight (K) was initially positioned in the top-left room and must fight his way through the dungeon to rescue the princess.

The knight has an initial health point represented by a positive integer. If at any point his health point drops to 0 or below, he dies immediately.

Some of the rooms are guarded by demons, so the knight loses health (negative integers) upon entering these rooms; other rooms are either empty (0's) or contain magic orbs that increase the knight's health (positive integers).

In order to reach the princess as quickly as possible, the knight decides to move only rightward or downward in each step.


``Write a function to determine the knight's minimum initial health so that he is able to rescue the princess.``

For example, given the dungeon below, the initial health of the knight must be at least ``7`` if he follows the optimal path ``RIGHT-> RIGHT -> DOWN -> DOWN``.

. | . | . 
--- | --- | --- 
-2 (K) |	-3 |	3
-5	| -10	| 1
10 | 	30  |	-5 ( P )

Note:

1. The knight's health has no upper bound.
1. Any room can contain threats or power-ups, even the first room the knight enters and the bottom-right room where the princess is imprisoned.


## 题目大意

骑士救公主，骑士在左上角，公主在右下角，每个房间都会有个血量变化，如果血量<=0，立马死去。问骑士出发的时候带了多少血，才能成功就到公主。每个移动只能向右或者向下。

## 解题方法

### 动态规划

如果做了[64. Minimum Path Sum][1]，发现还有点类似，不过64题是只有正数，而这个题里面有正负数。

我们同样的想到了动态规划，但是一般的题目里面都是告诉了初始状态，但是这个题目要求初始状态，所以难度加大了。其实换一个思维，要求初始状态血量最小值，就是要到达右下角之后血量为1，即我们知道了结束状态是1。那么，我们需要换一个思路，就是从右下角出发到达左上角，需要的最少血量。

我们定义动态规划二维数组dp[i][j]表示，从右下角移动到i,j位置，需要的最少血量。那么，我们在最右边和最下边在来一层无穷大，表示到达这些位置是不可能的，但是，我们需要在公主的右边和下边的格子里血量初始化为1，即我们移动到这两个位置需要最少血量是1.

. | . | . |.
--- | --- | --- |---
-2 (K) |	-3 |	3 | INT_MAX
-5	| -10	| 1 | INT_MAX
10 | 	30  |	-5 ( P ) | 1
INT_MAX | INT_MAX | 1 | INT_MAX

有个简单的状态转移能看出来：``dp[i][j] = min(dp[i + 1][j], dp[i][j + 1]) - dungeon[i][j]``，即每个位置需要的最少血量是左边和下边的需要的最少血量 - 当前的房间的扣血量。这里需要解释一下为什么是减号：骑士到达这个屋子如果能活下去，那么需要的血量是多少呢？必须减掉扣血量才是当前需要的血量啊！

另外我们注意到，上面的dp[i][j]有可能是0或者负数，这种情况下骑士是没法存活的，骑士的最小血量要求是1，所以有最终的状态转移版本：

``dp[i][j] = max(1, min(dp[i + 1][j], dp[i][j + 1]) - dungeon[i][j]);``



C++代码如下：

```cpp
class Solution {
public:
    int calculateMinimumHP(vector<vector<int>>& dungeon) {
        const int M = dungeon.size(), N = dungeon[0].size();
        vector<vector<int>> dp(M + 1, vector<int>(N + 1, INT_MAX));
        dp[M][N - 1] = dp[M - 1][N] = 1;
        for (int i = M - 1; i >= 0; i--) {
            for (int j = N - 1; j >= 0; j--) {
                dp[i][j] = max(1, min(dp[i + 1][j], dp[i][j + 1]) - dungeon[i][j]);
            }
        }
        return dp[0][0];
    }
};
```



## 日期

2018 年 12 月 29 日 —— 2018年剩余电量不足1%


  [1]: https://blog.csdn.net/fuxuemingzhu/article/details/82620422
