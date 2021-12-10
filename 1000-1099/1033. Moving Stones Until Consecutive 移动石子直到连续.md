

作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)


题目地址：https://leetcode.com/problems/moving-stones-until-consecutive/

## 题目描述

Three stones are on a number line at positions `a`, `b`, and `c`.

Each turn, you pick up a stone at an endpoint (ie., either the lowest or highest position stone), and move it to an unoccupied position between those endpoints.  Formally, let's say the stones are currently at positions `x, y, z` with `x < y < z`.  You pick up the stone at either position x or position z, and move that stone to an integer position `k`, with `x < k < z` and `k != y`.

The game ends when you cannot make any more moves, ie. the stones are in consecutive positions.

When the game ends, what is the minimum and maximum number of moves that you could have made?  Return the answer as an length 2 array: `answer = [minimum_moves, maximum_moves]`

 

Example 1:

    Input: a = 1, b = 2, c = 5
    Output: [1,2]
    Explanation: Move the stone from 5 to 3, or move the stone from 5 to 4 to 3.

Example 2:

    Input: a = 4, b = 3, c = 2
    Output: [0,0]
    Explanation: We cannot make any moves.

Example 3:

    Input: a = 3, b = 5, c = 1
    Output: [1,2]
    Explanation: Move the stone from 1 to 4; or move the stone from 1 to 2 to 4.
     

Note:

1. `1 <= a <= 100`
1. `1 <= b <= 100`
1. `1 <= c <= 100`
1. `a != b, b != c, c != a`

## 题目大意

a,b,c表示三个位置，在三个位置上各有一个石头。现在要移动三个石头中的若干个，每次移动都必须选两端石头的里面的位置，最终使得它们三个放在连续的位置。问最少需要多少次移动，最多需要多少次移动。

## 解题方法

### 脑筋急转弯

这个题不是算法题，是个脑筋急转弯题。分情况讨论：

如果三个石头本来就连续，则不用移动。例：1，2，3

如果三个石头本来不连续，则：
**最少移动次数**：
    1. 有两个石头之间的距离小于等于2，则*最少*只需要一次移动。例：1，2，4，把4移动到3即可；或者例1，3，5，把5移到2即可。
    2. 所有石头之间的最小距离>2，则*最少*需要移动两个石头。例：1，4，7，需要把两个石头移动到另一个的旁边。
**最多移动次数**：
题目说了，只能像两端石头里面的那些位置上放，所以最多移动的次数就是本来两端石头中间包含的点（并且去掉中间的石头），策略是每次向内移动一步。例：1，3，5，在1和5中间之间共有2个可以放的点（分别为2，4），所以*最多*只能有max_ - min_ - 2次移动。

C++代码如下：

```cpp
class Solution {
public:
    vector<int> numMovesStones(int a, int b, int c) {
        int sum_ = a + b + c;
        int min_ = min(a, min(b, c));
        int max_ = max(a, max(b, c));
        int mid_ = sum_ - min_ - max_;
        
        if (max_ - min_ == 2)
            return {0, 0};
        
        int min_move = min(mid_ - min_, max_ - mid_) <= 2 ? 1 : 2;
        int max_move = max_ - min_ - 2;
        return {min_move, max_move};
    }
};
```

## 日期

2019 年 8 月 31 日 —— 赶在月底做个题
