# 【LeetCode】375. Guess Number Higher or Lower II 解题报告（Python）

作者： 		负雪明烛 
id：				fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---

题目地址: https://leetcode.com/problems/guess-number-higher-or-lower-ii/description/

## 题目描述：

We are playing the Guess Game. The game is as follows:

I pick a number from ``1`` to ``n``. You have to guess which number I picked.

Every time you guess wrong, I'll tell you whether the number I picked is higher or lower.

However, when you guess a particular number x, and you guess wrong, you pay ``$x``. You win the game when you guess the number I picked.

Example:

    n = 10, I pick 8.
    
    First round:  You guess 5, I tell you that it's higher. You pay $5.
    Second round: You guess 7, I tell you that it's higher. You pay $7.
    Third round:  You guess 9, I tell you that it's lower. You pay $9.
    
    Game over. 8 is the number I picked.
    
    You end up paying $5 + $7 + $9 = $21.

Given a particular n ≥ 1, find out how much money you need to have to guarantee a win.

## 题目大意

这个题应该理解为玩家是个绝对聪明的个体，他每一步都能使用最优的策略去查找要求的这个数字。那么，问找出1～n这里面的某个数字最少需要的花费。


## 解题方法

这个题说实话，我还真是不会，以下是[细语呢喃][1]的讲解，非常详细。建议大家看原博。

> 这题要求我们在猜测数字y未知的情况下（1~n任意一个数），要我们在最坏情况下我们支付最少的钱。也就是说要考虑所有y的情况。
> 
> 我们假定选择了一个错误的数x，（1<=x<=n && x!=y ）那么就知道接下来应该从[1,x-1 ] 或者[x+1,n]中进行查找。
> 假如我们已经解决了[1,x-1] 和 [x+1,n]计算问题，我们将其表示为solve(L,x-1)
> 和solve(x+1,n)，那么我们应该选择max(solve(L,x-1),solve(x+1,n))
> 这样就是求最坏情况下的损失。总的损失就是 f(x) = x + max(solve(L,x-1),solve(x+1,n))
> 
> 那么将x从1~n进行遍历，取使得 f(x) 达到最小，来确定最坏情况下最小的损失，也就是我们初始应该选择哪个数。
> 
> 上面的说法其实是一个自顶向下的过程（Top-down），可以用递归来解决。很容易得到如下的代码（这里用了记忆化搜索）：

```python
class Solution(object):
    def getMoneyAmount(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [[0] * (n + 1) for _ in range(n + 1)]
        return self.solve(dp, 1, n)

    def solve(self, dp, L, R):
        if L >= R: return 0
        if dp[L][R]: return dp[L][R]
        dp[L][R] = min(i + max(self.solve(dp, L, i - 1), self.solve(dp, i + 1, R)) for i in range(L, R + 1))
        return dp[L][R]
```

把递归改为迭代，方法如下：

```python
class Solution(object):
    def getMoneyAmount(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [[0] * (n + 1) for _ in range(n + 1)]
        for l in range(n - 1, 0, -1):
            for r in range(l + 1, n + 1):
                dp[l][r] = min(i + max(dp[l][i - 1], dp[i + 1][r]) for i in range(l, r))
        return dp[1][n]
```

参考资料：

https://www.hrwhisper.me/leetcode-guess-number-higher-lower-ii/

## 日期

2018 年 9 月 29 日 —— 国庆9天长假第一天！


  [1]: https://www.hrwhisper.me/leetcode-guess-number-higher-lower-ii/
