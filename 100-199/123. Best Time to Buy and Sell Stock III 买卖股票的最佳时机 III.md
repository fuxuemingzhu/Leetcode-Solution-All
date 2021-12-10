
作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)


题目地址：https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/description/


## 题目描述

Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete at most two transactions.

Note: You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).

Example 1:

    Input: [3,3,5,0,0,3,1,4]
    Output: 6
    Explanation: Buy on day 4 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.
                 Then buy on day 7 (price = 1) and sell on day 8 (price = 4), profit = 4-1 = 3.

Example 2:

    Input: [1,2,3,4,5]
    Output: 4
    Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
                 Note that you cannot buy on day 1, buy on day 2 and sell them later, as you are
                 engaging multiple transactions at the same time. You must sell before buying again.

Example 3:

    Input: [7,6,4,3,1]
    Output: 0
    Explanation: In this case, no transaction is done, i.e. max profit = 0.


## 题目大意

给出了一堆股票价格，最多做两次交易，求最大的收益。

## 解题方法

这个题太难了，看了一个多小时没看懂。直接抄的Gradyang的做法，罪过罪过。

地址：http://www.cnblogs.com/grandyang/p/4281975.html

```python
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices: return 0
        N = len(prices)
        g = [[0] * 3 for _ in range(N)]
        l = [[0] * 3 for _ in range(N)]
        for i in range(1, N):
            diff = prices[i] - prices[i - 1]
            for j in range(1, 3):
                l[i][j] = max(g[i - 1][j - 1] + max(diff, 0), l[i - 1][j] + diff)
                g[i][j] = max(l[i][j], g[i - 1][j])
        return g[-1][-1]
```


## 日期

2018 年 11 月 29 日 —— 时不我待


  [1]: https://blog.csdn.net/fuxuemingzhu/article/details/83504437
