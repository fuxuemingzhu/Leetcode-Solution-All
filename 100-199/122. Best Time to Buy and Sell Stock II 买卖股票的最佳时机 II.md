
作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)

题目地址：[https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/#/description][1]


## 题目描述


Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times).

Note: You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).

Example 1:

	Input: [7,1,5,3,6,4]
	Output: 7
	Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
	             Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.

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

可以多次进行买卖操作，但是每天只能要么买要么卖，求最大收益。

## 解题方法


这个题不是说可以任意的挑选，而是要按照每天的顺序挑选。这样就很简单了，只要后面的一天比这天的价格高就买入卖出就可。

Java解法如下：

```java
public class Solution {
    public int maxProfit(int[] prices) {
        int len = prices.length;
        int ans = 0;
        for(int i = 0; i < len - 1; i++){
            if(prices[i + 1] > prices[i]){
                ans += prices[i + 1] - prices[i];
            }
        }
        return ans;
    }
}
```

----

二刷， python

二刷的时候对这个题有更深的看法了，这个题一定是要有序的输入，我们在某个位置不能同时买卖，但是可以看做先全卖掉再全买下，那么就相当于没有买卖。比如一个区间划分成了两部分，区间的总长度=两个子区间的长度和。

```python
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices: return 0
        ans = 0
        for i in range(len(prices) - 1):
            if prices[i + 1] > prices[i]:
                ans += prices[i + 1] - prices[i]
        return ans
```

三刷，C++。和上面的代码思路完全一致。

```cpp
class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int N = prices.size();
        int res = 0;
        for (int i = 1; i < N; i ++) {
            if (prices[i] > prices[i - 1]) {
                res += prices[i] - prices[i - 1];
            }
        }
        return res;
    }
};
```

## 日期

2017 年 4 月 20 日 
2018 年 4 月 10 日 
2018 年 11 月 26 日 —— 11月最后一周！


  [1]: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/#/description
