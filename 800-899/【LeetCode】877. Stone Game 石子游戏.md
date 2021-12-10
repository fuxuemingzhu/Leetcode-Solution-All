
作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)

题目地址：https://leetcode.com/problems/stone-game/description/

## 题目描述

Alex and Lee play a game with piles of stones.  There are an even number of piles arranged in a row, and each pile has a positive integer number of stones piles[i].

The objective of the game is to end with the most stones.  The total number of stones is odd, so there are no ties.

Alex and Lee take turns, with Alex starting first.  Each turn, a player takes the entire pile of stones from either the beginning or the end of the row.  This continues until there are no more piles left, at which point the person with the most stones wins.

Assuming Alex and Lee play optimally, return True if and only if Alex wins the game.

 

Example 1:

    Input: [5,3,4,5]
    Output: true
    Explanation: 
    Alex starts first, and can only take the first 5 or the last 5.
    Say he takes the first 5, so that the row becomes [3, 4, 5].
    If Lee takes 3, then the board is [4, 5], and Alex takes 5 to win with 10 points.
    If Lee takes the last 5, then the board is [3, 4], and Alex takes 4 to win with 9 points.
    This demonstrated that taking the first 5 was a winning move for Alex, so we return true.
 

Note:

1. 2 <= piles.length <= 500
1. piles.length is even.
1. 1 <= piles[i] <= 500
1. sum(piles) is odd.


## 题目大意

有一个数组，两人玩游戏，可以从这个数组的开头或者结尾选择一个数字拿走，拿走以后，另一个人可以继续拿。问，先拿的那个人是否会赢。

## 解题方法

### 数学

直接return True就行。因为题目给了限定条件，总和是奇数，数字的个数是偶数。这样也就是简化成了问第一个人拿到的数字总和能否超过sum/2.

所以，第一个人直接选择偶数位置或者奇数位置的数字可以。

比如Alex选择偶数，piles[0], piles[2], ....., piles[n-2]，
他选择了piles[0]，这个时候Lee可以选择piles[1] 或 piles[n - 1].
之后Alex可以继续选择偶数的位置。所以Lee就被迫选择了所有奇数的位置。

反之，如果Alex从倒数第一个开始选，那么他能选到所有的奇数位置，Lee被迫选偶数位置。

故，Alex只要选出奇数、偶数位置中求和之后最大的就行，一定会赢。

```python
class Solution:
    def stoneGame(self, piles):
        return True
```

### 双函数

使用递归求解。这个解法是左程云的算法讲解。

思路就是，作为先选的人，要选择从前面选和从后面选两种方案中的最大值。
作为后选的人，要选择前面选和从后面选两种方案中的最小值。

alex是先选的，所以调用f函数判断他能否赢。

直接递归超时，所以我是用了记忆化搜索减少了时间，就能通过了。

代码如下：

```python
class Solution(object):
    
    def stoneGame(self, piles):
        """
        :type piles: List[int]
        :rtype: bool
        """
        if not piles:
            return False
        self.F = [[0 for i in range(len(piles))] for j in range(len(piles))]
        self.S = [[0 for i in range(len(piles))] for j in range(len(piles))]
        _sum = sum(piles)
        alex = self.f(piles, 0, len(piles) - 1)
        return alex > _sum / 2
        
    def f(self, piles, i, j):
        """
        先选
        """
        if i == j:
            return piles[i]
        if self.F[i][j] != 0:
            return self.F[i][j]
        curr = max(piles[i] + self.s(piles, i + 1, j), piles[j] + self.s(piles, i, j - 1))
        self.F[i][j] = curr
        return curr
        
    def s(self, piles, i, j):
        """
        后选
        """
        if i == j:
            return 0
        if self.S[i][j] != 0:
            return self.S[i][j]
        curr = min(self.f(piles, i + 1, j), self.f(piles, i, j - 1))
        self.S[i][j] = curr
        return curr
```

使用map来完成记忆化搜索，也能通过：

```python
class Solution(object):
    
    def stoneGame(self, piles):
        """
        :type piles: List[int]
        :rtype: bool
        """
        self.f_map, self.s_map = dict(), dict()
        _sum = sum(piles)
        alex = self.f(piles, 0, len(piles)-1)
        print(alex, _sum)
        return alex > _sum / 2.0
        
    def f(self, piles, start, end):
        if start == end:
            return piles[start]
        if (start, end) not in self.f_map:
            f_val = max(piles[start] + self.s(piles, start+1, end), piles[end] + self.s(piles, start, end-1))
            self.f_map[(start, end)] = f_val
        return self.f_map[(start, end)]
    
    def s(self, piles, start, end):
        if start == end:
            return 0
        if (start, end) not in self.s_map:
            s_val = min(self.f(piles, start+1, end), self.f(piles, start, end-1))
            self.s_map[(start, end)] = s_val
        return self.s_map[(start, end)]
```

### 单函数 + 记忆化递归

使用score函数表示Alex能比Lee多选的分数。可能比双函数更简洁易懂了。

记忆化递归的缺点：１．有可能爆栈；２．无法降维，而DP是可以降维的。


我写的是cpp代码：

```cpp
class Solution {
public:
    bool stoneGame(vector<int>& piles) {
        const int N = piles.size();
        m_ = vector<vector<int>>(N, vector<int>(N, INT_MIN));
        return score(piles, 0, N - 1) > 0;
    }
private:
    vector<vector<int>> m_;
    //Alex比Lee多的分数
    int score(vector<int>& piles, int l, int r) {
        if (l == r) return piles[l];
        if (m_[l][r] == INT_MIN) {
            m_[l][r] = max(piles[l] - score(piles, l + 1, r),
                          piles[r] - score(piles, l, r - 1));
        }
        return m_[l][r];
    }
};
```

### 动态规划

动态规划解法比较难想，dp数组的第i个位置表示的是从第i个石头到第i+l-1个石头之间最大的比对手得分。

使用的是一个长度变量和起始索引，计算每个位置开始的长度1～N长度的区间的dp状态。

```cpp
class Solution {
public:
    bool stoneGame(vector<int>& piles) {
        const int N = piles.size();
        // dp[i] := max(your_stones - op_stones) for piles[i] to piles[i + l - 1]
        vector<vector<int>> dp(N, vector<int>(N, INT_MIN));
        for (int i = 0; i < N; i++)
            dp[i][i] = piles[i];
        for (int l = 2; l <= N; l++) {
            for (int i = 0; i < N - l + 1; i++) {
                int j = i + l - 1;
                dp[i][j] = max(piles[i] - dp[i + 1][j], piles[j] - dp[i][j - 1]);
            }
        }
        return dp[0][N - 1] > 0;
    }
};
```

参考资料：

https://leetcode.com/problems/stone-game/discuss/154610/C++JavaPython-DP-or-Just-return-true

## 日期

2018 年 9 月 4 日 —— 迎接明媚的阳光！
2018 年 12 月 4 日 —— 周二啦！
