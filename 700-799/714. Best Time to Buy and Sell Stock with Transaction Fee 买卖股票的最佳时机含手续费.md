
作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)


题目地址：https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/description/

## 题目描述

Your are given an array of integers prices, for which the i-th element is the price of a given stock on day i; and a non-negative integer fee representing a transaction fee.

You may complete as many transactions as you like, but you need to pay the transaction fee for each transaction. You may not buy more than 1 share of a stock at a time (ie. you must sell the stock share before you buy again.)

Return the maximum profit you can make.

    Example 1:
    Input: prices = [1, 3, 2, 8, 4, 9], fee = 2
    Output: 8
    Explanation: The maximum profit can be achieved by:
    Buying at prices[0] = 1
    Selling at prices[3] = 8
    Buying at prices[4] = 4
    Selling at prices[5] = 9
    The total profit is ((8 - 1) - 2) + ((9 - 4) - 2) = 8.

Note:

- 0 < prices.length <= 50000.
- 0 < prices[i] < 50000.
- 0 <= fee < 50000.

## 题目大意

给出一系列的股票交易价格，每次股票交易会有交易fee，求买卖股票能获得的最大的收益。

## 解题方法

### 动态规划

可以使用dp的方法去做。该dp使用了两个数字，cash和hold。解释如下：

1. cash 该天结束手里**没有**股票的情况下，已经获得的最大收益
2. hold 该天结束手里**有**股票的情况下，已经获得的最大收益

所以转移状态分析如下：

cash 更新的策略是：既然今天结束之后手里没有股票，那么可能是今天没买（保持昨天的状态），也可能是今天把股票卖出了

hold 更新的策略是：今天今天结束之后手里有股票，那么可能是今天没卖（保持昨天的状态），也可能是今天买了股票


```python
class Solution:
    def maxProfit(self, prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        """
        cash = 0
        hold = -prices[0]
        for i in range(1, len(prices)):
            cash = max(cash, hold + prices[i] - fee)
            hold = max(hold, cash - prices[i])
        return cash
```

使用C++代码如下：

```cpp
class Solution {
public:
    int maxProfit(vector<int>& prices, int fee) {
        const int N = prices.size();
        vector<int> cash(N, 0);
        vector<int> hold(N, 0);
        cash[0] = 0;
        hold[0] = -prices[0];
        for (int i = 1; i < N; i ++) {
            cash[i] = max(cash[i - 1], prices[i] + hold[i - 1] - fee);
            hold[i] = max(hold[i - 1], cash[i - 1] - prices[i]);
        }
        return cash[N - 1];
    }
};
```

优化空间复杂度到O(1)的代码如下：

```cpp
class Solution {
public:
    int maxProfit(vector<int>& prices, int fee) {
        const int N = prices.size();
        // max profit if today don't have stock
        int cash = 0;
        // max profit if today have stock
        int hold = -prices[0];
        for (int i = 1; i < N; ++i) {
            cash = max(cash, prices[i] + hold - fee);
            hold = max(hold, cash - prices[i]);
        }
        return cash;
    }
};
```

## 日期

2018 年 4 月 10 日 —— 风很大，很舒服～～
2018 年 12 月 5 日 —— 周三啦！
2019 年 2 月 22 日 —— 这周结束了
