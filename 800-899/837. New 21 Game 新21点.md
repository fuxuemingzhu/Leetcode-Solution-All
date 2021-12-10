作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)


题目地址：https://leetcode.com/problems/new-21-game/description/


## 题目描述

Alice plays the following game, loosely based on the card game "21".

Alice starts with ``0`` points, and draws numbers while she has less than ``K`` points.  During each draw, she gains an integer number of points randomly from the range ``[1, W]``, where ``W`` is an integer.  Each draw is independent and the outcomes have equal probabilities.

Alice stops drawing numbers when she gets ``K`` or more points.  What is the probability that she has ``N`` or less points?

Example 1:

    Input: N = 10, K = 1, W = 10
    Output: 1.00000
    Explanation:  Alice gets a single card, then stops.

Example 2:

    Input: N = 6, K = 1, W = 10
    Output: 0.60000
    Explanation:  Alice gets a single card, then stops.
    In 6 out of W = 10 possibilities, she is at or below N = 6 points.

Example 3:

    Input: N = 21, K = 17, W = 10
    Output: 0.73278

Note:

1. 0 <= K <= N <= 10000
1. 1 <= W <= 10000
1. Answers will be accepted as correct if they are within 10^-5 of the correct answer.
The judging time limit has been reduced for this question.


## 题目大意

刚开始的时候，有0分，她会已知在[1,W]中随机选数字，直到有K分或者K分以上停止。问她能够正好得到N分或者更少分的概率。


## 解题方法

### 动态规划

类似**爬楼梯**的问题，每次可以跨[1,W]个楼梯，当一共爬了K个和以上的台阶时停止，问这个时候总台阶数<=N的概率。

使用动态规划，dp[i]表示得到点数i的概率，只有当现在的总点数少于K的时候，才会继续取数。那么状态转移方程可以写成：

1. 当``i <= K``时，``dp[i] = （前W个dp的和）/ W``；(爬楼梯得到总楼梯数为i的概率）
2. 当``K < i < K + W``时，那么在这次的前一次的点数范围是``[i - W, K - 1]``。我们的dp数组表示的是得到点i的概率，所以``dp[i]=(dp[K-1]+dp[K-2]+…+dp[i-W])/W``.（可以从前一次的基础的上选[1,W]个数字中的一个）
3. 当i>=K+W时，这种情况下无论如何不都应该存在的，所以dp[i]=0.

时间复杂度是O(N)，空间复杂度是O(N).

```python
class Solution(object):
    def new21Game(self, N, K, W):
        """
        :type N: int
        :type K: int
        :type W: int
        :rtype: float
        """
        if K == 0: return 1
        dp = [1.0] + [0] * N
        tSum = 1.0
        for i in range(1, N + 1):
            dp[i] = tSum / W
            if i < K:
                tSum += dp[i]
            if 0 <= i - W < K:
                tSum -= dp[i - W]
        return sum(dp[K:])
```


## 相似题目


## 参考资料

https://blog.csdn.net/qq_20141867/article/details/81261711

## 日期

2018 年 11 月 1 日 —— 小光棍节
