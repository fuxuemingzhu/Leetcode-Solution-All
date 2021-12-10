# 【LeetCode】518. Coin Change 2 解题报告（Python）

作者： 		负雪明烛 
id：				fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---

题目地址：https://leetcode.com/problems/coin-change-2/description/

## 题目描述：

You are given coins of different denominations and a total amount of money. Write a function to compute the number of combinations that make up that amount. You may assume that you have infinite number of each kind of coin.

Note: You can assume that

1. 0 <= amount <= 5000
1. 1 <= coin <= 5000
1. the number of coins is less than 500
1. the answer is guaranteed to fit into signed 32-bit integer
 

Example 1:

    Input: amount = 5, coins = [1, 2, 5]
    Output: 4
    Explanation: there are four ways to make up the amount:
    5=5
    5=2+2+1
    5=2+1+1+1
    5=1+1+1+1+1
 

Example 2:

    Input: amount = 3, coins = [2]
    Output: 0
    Explanation: the amount of 3 cannot be made up just with coins of 2.
 

Example 3:

    Input: amount = 10, coins = [10] 
    Output: 1

## 题目大意

有一堆一定面额的硬币，问有多少种可以组成amount的方案。假定硬币的数量是不限量的。

## 解题方法

DP。第一感觉是完全背包问题，但其实由于没有重量和价值的对应关系，所以不一样。

生成了一个一维数组dp，dp[i]代表了生成总价值为i有多少方案。

对已有的所有面值的硬币进行遍历，其实思路很简单：dp[i] += dp[i - coin]，价值为i的解决方案应该加上价值为i - coin的解决方案。

时间复杂度是O(L * A)，空间复杂度是O(A); A = amount.

代码如下：

```python
class Solution(object):
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        dp = [0] * (amount + 1)
        dp[0] = 1
        for coin in coins:
            for i in range(1, amount + 1):
                if coin <= i:
                    dp[i] += dp[i - coin]
        return dp[amount]
```

参考资料：

https://www.youtube.com/watch?v=jaNZ83Q3QGc

## 日期

2018 年 9 月 25 日 —— 美好的一周又开始了，划重点，今天是周二
