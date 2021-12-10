
作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)

题目地址：https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/description/

## 题目描述

Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like (ie, buy one and sell one share of the stock multiple times) with the following restrictions:

- You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
- After you sell your stock, you cannot buy stock on next day. (ie, cooldown 1 day)

Example:

    Input: [1,2,3,0,2]
    Output: 3 
    Explanation: transactions = [buy, sell, cooldown, buy, sell]


## 题目大意

股票交易的原则是必须先买然后再卖，在买入之前必须至少休息一天。求最后能得到的最大收益。

## 解题方法

### 动态规划

感觉自己DP的能力还是太弱，越是这样越需要迎难而上。

这个题和[714. Best Time to Buy and Sell Stock with Transaction Fee][1]比较像。做题方法都是使用了两个数组：

1. cash 该天结束手里**没有**股票的情况下，已经获得的最大收益
1. hold 该天结束手里**有**股票的情况下，已经获得的最大收益

状态转移方程式这样的：

cash[i]代表的是手里没有股票的收益，这种可能性是今天卖了或者啥也没干。max(昨天手里有股票的收益+今天卖股票的收益，昨天手里没有股票的收益)， 即max(sell[i - 1], hold[i - 1] + prices[i])；
hold[i]代表的是手里有股票的收益，这种可能性是今天买了股票或者啥也没干，今天买股票必须昨天休息。所以为max(今天买股票是前天卖掉股票的收益-今天股票的价格，昨天手里有股票的收益）。即max(hold[i - 1], sell[i - 2] - prices[i])。

另外需要注意的是，题目说的是昨天卖了股票的话今天不能买，对于开始的第一天，不可能有卖股票的行为，所以需要做个判断。

该算法的时间复杂度是O(n)，空间复杂度是O(n)。

代码如下：

```python
class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices: return 0
        sell = [0] * len(prices)
        hold = [0] * len(prices)
        hold[0] = -prices[0]
        for i in range(1, len(prices)):
            sell[i] = max(sell[i - 1], hold[i - 1] + prices[i])
            hold[i] = max(hold[i - 1], (sell[i - 2] if i >= 2 else 0) - prices[i])
        return sell[-1]
```


如果使用O(1)的空间复杂度，那么就可以写成下面这样：

```python
class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices: return 0
        prev_sell = 0
        curr_sell = 0
        hold = -prices[0]
        for i in range(1, len(prices)):
            temp = curr_sell
            curr_sell = max(curr_sell, hold + prices[i])
            hold = max(hold, (prev_sell if i >= 2 else 0) - prices[i])
            prev_sell = temp
        return curr_sell
```

C++解法如下：

```cpp
class Solution {
public:
    int maxProfit(vector<int>& prices) {
        const int N = prices.size();
        if (N == 0) return 0;
        // cash[i] means the max profit if I dont have stock on day i
        vector<int> cash(N, 0);
        // stock[i] means the max profit if I have stock on day i
        vector<int> stock(N, 0);
        stock[0] = -prices[0];
        for (int i = 1; i < N; i++) {
            cash[i] = max(stock[i - 1] + prices[i], cash[i - 1]);
            stock[i] = max((i >= 2 ? cash[i - 2] : 0) - prices[i], stock[i - 1]);
        }
        return cash[N - 1];
    }
};
```


参考资料：

https://soulmachine.gitbooks.io/algorithm-essentials/java/dp/best-time-to-buy-and-sell-stock-with-cooldown.html

## 日期

2018 年 9 月 12 日 —— 做题还是要有耐心
2019 年 1 月 3 日 —— 2019年已经过去1%

  [1]: https://blog.csdn.net/fuxuemingzhu/article/details/79888528
