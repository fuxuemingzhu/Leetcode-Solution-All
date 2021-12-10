
作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)

题目地址：[https://leetcode.com/problems/min-cost-climbing-stairs/description/][1]


## 题目描述

On a staircase, the i-th step has some non-negative cost cost[i] assigned (0 indexed).

Once you pay the cost, you can either climb one or two steps. You need to find minimum cost to reach the top of the floor, and you can either start from the step with index 0, or the step with index 1.

    Example 1:
    Input: cost = [10, 15, 20]
    Output: 15
    Explanation: Cheapest is start on cost[1], pay that cost and go to the top.
    Example 2:
    Input: cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
    Output: 6
    Explanation: Cheapest is start on cost[0], and only step on 1s, skipping cost[3].

Note:

1. cost will have a length in the range [2, 1000].
1. Every cost[i] will be an integer in the range [0, 999].

## 题目大意

爬楼梯，每次可以走1步或者2步，求走到顶的最小花费。其中，开始的位置可以是第一个位置或者第二个位置。

## 解题方法

### 动态规划

非常初级的动态规划的问题。需要做的是另外找一个列表保存节点的路径的代价，某个节点的路径的代价等于前两个节点的路径的代价和前两个节点对应的代价之和。最后返回的结果是倒数两个节点的代价和节点值之和的最小值。

```python
class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        costed = [0, 0]
        for i in xrange(2, len(cost)):
            costed.append(min(costed[i - 1] + cost[i - 1], costed[i - 2] + cost[i - 2]))
        return min(costed[-1] + cost[-1], costed[-2] + cost[-2])
```

二刷，同样的动态规划，提前把所有的dp状态声明出来，然后每一步的转移等于前两步的最小值+当前的值。因为需要上到最上面的楼梯，所以假设增加一个花费是0的楼梯。


```python
class Solution:
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        N = len(cost)
        cost.append(0)
        dp = [0] * (N + 1)
        dp[0] = cost[0]
        dp[1] = cost[1]
        for i in range(2, N + 1):
            dp[i] = min(dp[i - 1], dp[i - 2]) + cost[i]
        return dp[-1]
```

## 日期

2018 年 1 月 28 日 
2018 年 11 月 17 日 —— 美妙的周末，美丽的天气

  [1]: https://leetcode.com/problems/min-cost-climbing-stairs/description/
