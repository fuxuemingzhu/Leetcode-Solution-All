
作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)


题目地址：https://leetcode.com/problems/divisor-game/

## 题目描述

Alice and Bob take turns playing a game, with Alice starting first.

Initially, there is a number `N` on the chalkboard.  On each player's turn, that player makes a move consisting of:

1. Choosing any `x` with `0 < x < N` and `N % x == 0`.
2. Replacing the number N on the chalkboard with `N - x`.

Also, if a player cannot make a move, they lose the game.

Return True if and only if Alice wins the game, assuming both players play optimally.

 

Example 1:

    Input: 2
    Output: true
    Explanation: Alice chooses 1, and Bob has no more moves.

Example 2:

    Input: 3
    Output: false
    Explanation: Alice chooses 1, Bob chooses 1, and Alice has no more moves.
 

Note:

- 1 <= N <= 1000


## 题目大意

对于数字N，做两个操作：1. 找出一个因数x，2. 把N换成N - x。两个人轮流做这个操作，问第一个人是否能赢。

## 解题方法

### 找规律

首先说结论：当N是偶数时第一个人一定赢，当N是奇数时第一个一定输。

1. 奇数的因子只有奇数，偶数的因子至少一个偶数2
2. 奇数 - 奇数 = 偶数
3. 当Alice的值是N时必输，则当Alice的值是N+1时必赢(拿1即可)

那么，当N为下列数字时，先发的状态如下。
当N=1，输；
当N=2，赢（性质3）；
当N=3，输（性质1和2，对方一定是偶数，上面的偶数情况都赢）；
当N=4，赢（性质3）；
当N=5，输（性质1和2，对方一定是偶数，上面的偶数情况都赢）；
...
所以，N为偶数都赢，N为奇数都输。

C++代码如下：

```cpp
class Solution {
public:
    bool divisorGame(int N) {
        return N % 2 == 0;
    }
};
```

### 动态规划

动态规划就是很朴素的做法了，对每个位置i，遍历其因数x，判断N-x的状态，当N-x为输的时候自己赢。

C++代码如下：

```cpp
class Solution {
public:
    bool divisorGame(int N) {
        if (N == 1) return false;
        if (N == 2) return true;
        vector<bool> dp(N, false);
        dp[1] = true;
        for (int i = 3; i <= N; ++i) {
            for (int j = 1; j < i; ++j) {
                if (i % j == 0 && !dp[i - j - 1]) {
                    dp[i - 1] = true;
                    break;
                }
            }
        }
        return dp[N - 1];
    }
};
```

参考资料：https://leetcode.com/problems/divisor-game/discuss/368269/C%2B%2B-100-and-96-and

## 日期

2019 年 8 月 30 日 —— 赶在月底做个题
