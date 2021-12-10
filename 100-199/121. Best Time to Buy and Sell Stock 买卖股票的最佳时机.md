作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)

[LeetCode]

题目地址：[https://leetcode.com/problems/best-time-to-buy-and-sell-stock/](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/)

Total Accepted: 98941 Total Submissions: 274449 Difficulty: Easy

## 题目描述



Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.

Note that you cannot sell a stock before you buy one.

Example 1:

	Input: [7,1,5,3,6,4]
	Output: 5
	Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
	             Not 7-1 = 6, as selling price needs to be larger than buying price.

Example 2:

	Input: [7,6,4,3,1]
	Output: 0
	Explanation: In this case, no transaction is done, i.e. max profit = 0.

## 题目大意

可以在某一天买股票，在之后卖股票，求最大收益。


## 解题方法

### Java解法

动态规划求解。

因为买股票再卖掉是要求有先后顺序的。肯定是找到当前项的值与之前最小值的差值的最大值。

动态规划问题，可以用数组去写。我偷看别人的，没用数组。

1.保存在见到这个数值时，之前的所有值的最小值。
2.记录当前值与这个最小值的差。
3.找到在所有里边差值的最大值。

不得不说下面这个方法还是很巧的。因为没有笨的像我一样在每个值时都去遍历查找之前所有值的最小值。而是采用保存下来的方法。

```java
public class Solution {
    public int maxProfit(int[] prices) {
        if(prices.length<2) return 0;
        int maxProfit=0;
        int min=prices[0];
        int cur=0;
        for(int i=1;i<prices.length;i++){
            cur=prices[i];
            min=Math.min(min,cur);
            maxProfit=Math.max(maxProfit,cur-min);
        }
        return maxProfit;
    }
}
```
AC:3ms

### Python解法

四刷，使用数组分别保存每个数字左边和右边的最小值与最大值，然后我们找到每个位置它右边的最大值-左边的最小值即可。

```python
class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices: return 0
        N = len(prices)
        mins = [0] * N
        maxs = [0] * N
        mins[0] = prices[0]
        for i in range(1, N):
            mins[i] = min(mins[i - 1], prices[i])
        maxs[N - 1] = prices[N - 1]
        for j in range(N - 2, -1, -1):
            maxs[j] = max(maxs[j + 1], prices[j])
        return max(maxs[i] - mins[i] for i in range(N))
```

二刷，python。只使用了两个变量，保存目前的最小值和当前最大的收益。

```python
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices: return 0
        minPrice = float('inf')
        profit = 0
        for price in prices:
            minPrice = min(minPrice, price)
            profit = max(profit, price - minPrice)
        return profit
```

三刷，保存最新的最小值和最大值。这样只用遍历一次，如果遇到更小的值，那么把最小值和最大值同时更新；如果遇到更大的值，那么只更新最大值；最后的结果是最大值和最小值的差。

```python
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        N = len(prices)
        res = 0
        minP, maxP = float("inf"), 0
        for i in range(N):
            if minP > prices[i]:
                minP = prices[i]
                maxP = 0
            if maxP < prices[i]:
                maxP = prices[i]
            res = max(res, maxP - minP)
        return res
```

### C++ 解法

五刷，我们在遍历的过程中，始终保持目前最好的收益，那么遍历到最后的结果就是我们要求的。这个思路，在很多题目里面都有运用。

这个题而言，使用变量minP保存当前遇到了的最小值，那么，我们遇到每一个值的时候，都减去当前的最小值就是收益，所有收益最大值就是最大收益。

```cpp
class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int minP = INT_MAX;
        int res = 0;
        for (int p : prices) {
            if (p < minP) 
                minP = p;
            res = max(res, p - minP);
        }
        return res;
    }
};
```


## 日期


2016/5/1 17:59:24 
2018 年 4 月 10 号
2018 年 11 月 11 日 —— 剁手节快乐
2018 年 11 月 17 日 —— 美妙的周末，美丽的天气
2018 年 11 月 24 日 —— 周日开始！一周就过去了～
2019 年 1 月 3 日 —— 2019年已经过去1%
