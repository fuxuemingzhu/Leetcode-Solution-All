
- 作者：    负雪明烛
- id：      fuxuemingzhu
- 个人博客：[http://fuxuemingzhu.cn/](http://fuxuemingzhu.cn/)

---
@[TOC](目录)

题目地址：https://leetcode.com/problems/minimum-cost-for-tickets/

## 题目描述

In a country popular for train travel, you have planned some train travelling one year in advance.  The days of the year that you will travel is given as an array days.  Each day is an integer from 1 to 365.

Train tickets are sold in 3 different ways:

- a 1-day pass is sold for costs[0] dollars;
- a 7-day pass is sold for costs[1] dollars;
- a 30-day pass is sold for costs[2] dollars.

The passes allow that many days of consecutive travel.  For example, if we get a 7-day pass on day 2, then we can travel for 7 days: day 2, 3, 4, 5, 6, 7, and 8.

Return the minimum number of dollars you need to travel every day in the given list of days.


Example 1:
    
    Input: days = [1,4,6,7,8,20], costs = [2,7,15]
    Output: 11
    Explanation: 
    For example, here is one way to buy passes that lets you travel your travel plan:
    On day 1, you bought a 1-day pass for costs[0] = $2, which covered day 1.
    On day 3, you bought a 7-day pass for costs[1] = $7, which covered days 3, 4, ..., 9.
    On day 20, you bought a 1-day pass for costs[0] = $2, which covered day 20.
    In total you spent $11 and covered all the days of your travel.

Example 2:

    Input: days = [1,2,3,4,5,6,7,8,9,10,30,31], costs = [2,7,15]
    Output: 17
    Explanation: 
    For example, here is one way to buy passes that lets you travel your travel plan:
    On day 1, you bought a 30-day pass for costs[2] = $15 which covered days 1, 2, ..., 30.
    On day 31, you bought a 1-day pass for costs[0] = $2 which covered day 31.
    In total you spent $17 and covered all the days of your travel.
     

Note:

1. ``1 <= days.length <= 365``
1. ``1 <= days[i] <= 365``
1. days is in strictly increasing order.
1. ``costs.length == 3``
1. ``1 <= costs[i] <= 1000``


## 题目大意

在一年内的某些天会有若干天进行旅行，火车票卖票有三种方式：1天票、7天票、30天票，这几种票的价格分别是costs的三个元素。现在要在这些天内进行旅行，问覆盖这些天最少需要多少钱。

## 解题方法

### 动态规划

我竟然没有看出这个题是几个动态规划的题目。

这个题目比较长，但是理解起来还是比较简单的：有三种方式进行选择，要在三种方式里面选择一种，问最少的价格。听起来可以使用搜索的方式进行，应该也是可以的。但是更好的方式就是动态规划。

使用一个 dp 数组，其中 dp[i] 代表着我们旅行到 i 天为止需要的最少旅行价格。那么，如果当前天不需要旅行（不在days中），当然这一天就不用额外买票，所以需要花费的价格等于昨天的价格；如果当前天需要旅行的话，那么需要求三种买票方式的最小价格：昨天的最少价格+一天的票 costs[0]，7天前的最少价格+7天的票钱 costs[1] ，30天前的最少价格+30天的票钱 costs[2]。

总之，递推公式是：

1. dp[i] = dp[i - 1]  当第i天不用旅行
1. dp[i] = min(dp[i - 1] + costs[0], dp[i - 7] + costs[1], dp[i - 30] + costs[2]) 当第i天需要旅行

实际操作时需要注意向前查找的时候是否越界的问题。


下面的代码里或许不能理解的是为什么把要旅行的天 dp[day] 初始化成0。其实这里真不用考虑太多，这个值只是做了一个标记，代表这天的状态不是INT_MAX，我们在下面计算状态转移的时候会根据这天是不是INT_MAX进行状态转移，等于INT_MAX的代表这天不用旅行，不等INT_MAX的时候代表着需要旅行。所以把days都初始化成一个非INT_MAX的数字即可，我们求需要状态转移的dp[i]，需要并且只需要计算三种买票状态的最小值。

C++代码如下：

```cpp
class Solution {
public:
    int mincostTickets(vector<int>& days, vector<int>& costs) {
        // dp[i] means min cost for day i
        vector<int> dp(366, INT_MAX);
        for (int day : days)
            dp[day] = 0;
        dp[0] = 0;
        for (int i = 1; i < 366; ++i) {
            if (dp[i] == INT_MAX)
                dp[i] = dp[i - 1];
            else {
                int cur = dp[i - 1] + costs[0];
                cur = min(cur, costs[1] + dp[max(0, i - 7)]);
                cur = min(cur, costs[2] + dp[max(0, i - 30)]);
                dp[i] = cur;
            }
        }
        return dp[days[days.size() - 1]];
     }
};
```

Python代码如下：

```python
class Solution(object):
    def mincostTickets(self, days, costs):
        """
        :type days: List[int]
        :type costs: List[int]
        :rtype: int
        """
        dp = [float("inf")] * 366
        for day in days:
            dp[day] = 0
        dp[0] = 0
        for i in range(1, 366):
            if dp[i] == float("inf"):
                dp[i] = dp[i - 1]
            else:
                cur = dp[i - 1] + costs[0]
                cur = min(dp[max(0, i - 7)] + costs[1], cur)
                cur = min(dp[max(0, i - 30)] + costs[2], cur)
                dp[i] = cur
        return dp[days[-1]]
```

## 日期

2019 年 1 月 29 日 —— 小年好
2020 年 5 月 6 日 —— 今天的每日一题
