
作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)

题目地址：https://leetcode.com/problems/online-stock-span/description/

## 题目描述

Write a class StockSpanner which collects daily price quotes for some stock, and returns the span of that stock's price for the current day.

The span of the stock's price today is defined as the maximum number of consecutive days (starting from today and going backwards) for which the price of the stock was less than or equal to today's price.

For example, if the price of a stock over the next 7 days were [100, 80, 60, 70, 60, 75, 85], then the stock spans would be [1, 1, 1, 2, 1, 4, 6].

 

Example 1:

    Input: ["StockSpanner","next","next","next","next","next","next","next"], [[],[100],[80],[60],[70],[60],[75],[85]]
    Output: [null,1,1,1,2,1,4,6]
    Explanation: 
    First, S = StockSpanner() is initialized.  Then:
    S.next(100) is called and returns 1,
    S.next(80) is called and returns 1,
    S.next(60) is called and returns 1,
    S.next(70) is called and returns 2,
    S.next(60) is called and returns 1,
    S.next(75) is called and returns 4,
    S.next(85) is called and returns 6.
    
    Note that (for example) S.next(75) returned 4, because the last 4 prices
    (including today's price of 75) were less than or equal to today's price.
     

Note:

1. Calls to StockSpanner.next(int price) will have 1 <= price <= 10^5.
1. There will be at most 10000 calls to StockSpanner.next per test case.
1. There will be at most 150000 calls to StockSpanner.next across all test cases.
1. The total time limit for this problem has been reduced by 75% for C++, and 50% for all other languages.

## 题目大意

这个题要我们求，当一个新的股票价格来到的时候，在这个天数过去的多少天内，股票的价格是小于等于今天的。注意的是，从今天向前面数已经经过的天数，今天也包括在内。

## 解题方法
### 单调递减栈

看了数值的范围，可以肯定这个题的时间复杂度必须在O(n)以内，也就是说平均每次next()方法调用的时候，必须在将近O(1)的时间内找到前面多少天的价格是小于等于今天的。

这个题的重点在于``连续``二字上，我们只需要向前找到第一个比当前数字大的位置就停止。那么我们只需要找到数字A其前面有多少个连续的并且比它小的数字个数a即可，这样，当我们后面出现一个数字B，当B>=A时，在B前面小于等于B的连续数字共有a + 1个；当B < A时，在B前面小于等于B的连续数字只有1个，那就是B自己。

思路是使用一个单调递减栈，这个栈里保存的是当前的价格向前可以找连续的多少天。注意这个栈里存放的内容是严格单调递减的，如果新来的数值大于了栈顶元素，那么就要把栈顶的元素给弹出去，直到当前元素小于栈顶才行。

这样做的好处就是，我们没必要保留较小的元素，只需要知道每个元素前面有几个比它小的数字就行了。因为我们在遍历的过程中，是在找比当前元素小的元素个数，栈顶保留的只有较大的元素和它前面出现的次数，那么就知道了前面比它小的元素个数。

如果按照题目的示例，每次next()函数调用之后，栈中的内容如下：

	[(100, 1)]
	[(100, 1), (80, 1)]
	[(100, 1), (80, 1), (60, 1)]
	[(100, 1), (80, 1), (70, 2)]
	[(100, 1), (80, 1), (70, 2), (60, 1)]
	[(100, 1), (80, 1), (75, 4)]
	[(100, 1), (85, 6)]

每步操作的平均时间复杂度是O(1)，最坏的时间复杂度是O(n)，空间复杂度是O(1).

代码如下：

```python
class StockSpanner(object):

    def __init__(self):
        self.a = []

    def next(self, price):
        """
        :type price: int
        :rtype: int
        """
        res = 1
        while self.a and self.a[-1][0] <= price:
            res += self.a.pop()[1]
        self.a.append((price, res))
        return res
        
# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
```

参考资料：

https://leetcode.com/problems/online-stock-span/discuss/168311/C++JavaPython-O(1)

## 日期

2018 年 9 月 20 日 —— 趁年轻多读书
2019 年 3 月 24 日 —— 再做一遍还是不会
