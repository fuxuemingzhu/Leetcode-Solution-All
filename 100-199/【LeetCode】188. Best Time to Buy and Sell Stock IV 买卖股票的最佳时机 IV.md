
作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)


题目地址：https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/description/


## 题目描述

Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete at most ``k`` transactions.

Note:

You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).

Example 1:

    Input: [2,4,1], k = 2
    Output: 2
    Explanation: Buy on day 1 (price = 2) and sell on day 2 (price = 4), profit = 4-2 = 2.

Example 2:

    Input: [3,2,6,5,0,3], k = 2
    Output: 7
    Explanation: Buy on day 2 (price = 2) and sell on day 3 (price = 6), profit = 6-2 = 4.
                 Then buy on day 5 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.


## 题目大意

给出了一堆股票价格，最多做k次交易，求最大的收益。

## 解题方法

就是[123. Best Time to Buy and Sell Stock III][1]昨天的题，只是把交易2次改成了交易k次。这次题目有个坑，就是给了一个特别大的k，导致构建数组的时候，内存超了。在123题目里也说了，如果``k>=N``的时候相当于没有限制，题目退化成了不限次数的交易，所以我们直接求今天比昨天高的部分即可。当``k<N``的时候，我们仍然使用两个变量，全局的收益g和当前天卖出股票的收益l.

以下来自[Grandyang的博客][2]：

这里我们需要两个递推公式来分别更新两个变量local和global，参见网友Code Ganker的博客，我们其实可以求至少k次交易的最大利润。我们定义local[i][j]为在到达第i天时最多可进行j次交易并且最后一次交易在最后一天卖出的最大利润，此为局部最优。然后我们定义global[i][j]为在到达第i天时最多可进行j次交易的最大利润，此为全局最优。它们的递推式为：

local[i][j] = max(global[i - 1][j - 1] + max(diff, 0), local[i - 1][j] + diff)

global[i][j] = max(local[i][j], global[i - 1][j])，

其中局部最优值是比较前一天并少交易一次的全局最优加上大于0的差值，和前一天的局部最优加上差值后相比，两者之中取较大值，而全局最优比较局部最优和前一天的全局最优。

```python
class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        if k <= 0 or not prices: return 0
        N = len(prices)
        if k >= N:
            _sum = 0
            for i in xrange(1, N):
                if prices[i] > prices[i - 1]:
                    _sum += prices[i] - prices[i - 1]
            return _sum
        g = [0] * (k + 1)
        l = [0] * (k + 1)
        for i in xrange(N - 1):
            diff = prices[i + 1] - prices[i]
            for j in xrange(k, 0, -1):
                l[j] = max(g[j - 1] + max(diff, 0), l[j] + diff)
                g[j] = max(l[j], g[j])
        return g[-1]
```


## 日期

2018 年 12 月 1 日 —— 2018年余额不足了


  [1]: https://blog.csdn.net/fuxuemingzhu/article/details/84640318
  [2]: http://www.cnblogs.com/grandyang/p/4295761.html
