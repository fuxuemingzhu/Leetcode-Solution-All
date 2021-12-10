作者： 		负雪明烛 
id：				fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---

题目地址: https://leetcode.com/problems/burst-balloons/description/

## 题目描述：

Given ``n`` balloons, indexed from ``0`` to ``n-1``. Each balloon is painted with a number on it represented by array ``nums``. You are asked to burst all the balloons. If the you burst balloon ``i`` you will get ``nums[left] * nums[i] * nums[right]`` coins. Here ``left`` and ``right`` are adjacent indices of ``i``. After the burst, the ``left`` and ``right`` then becomes adjacent.

Find the maximum coins you can collect by bursting the balloons wisely.

Note:

- You may imagine nums[-1] = nums[n] = 1. They are not real therefore you can not burst them.
- 0 ≤ n ≤ 500, 0 ≤ nums[i] ≤ 100

Example:

    Input: [3,1,5,8]
    Output: 167 
    Explanation: nums = [3,1,5,8] --> [3,5,8] -->   [3,8]   -->  [8]  --> []
                 coins =  3*1*5      +  3*5*8    +  1*3*8      + 1*8*1   = 167


## 题目大意

打气球游戏，当我们打某个位置的气球的时候，能获得它左右两个气球上的分数和自身分数的乘积。问如何打气球能获得最多的分数？可以认为最左右两边隐含着分数为1不用打破的气球。

## 解题方法

这个是个DP的题目，当然也可以通过记忆化搜索的方式解决。

令dfs(i, j) 和 c[i][j]是在第[i, j]闭区间上打破气球能获得最大值。那么，在其中找到一个不打破的气球k，则可以得到以下关系：

    c[i][j] = max(c[i][j], self.dfs(nums, c, i, k - 1) + nums[i - 1] * nums[k] * nums[j + 1] + self.dfs(nums, c, k + 1, j))

含义是，我们找出在[i, k - 1]、[k + 1, j]闭区间打气球的分数最大值，然后会把第i - 1和第j + 1个气球保留下来，让这两个气球和第k个气球相乘，最后求三个加法。

模拟左右两边的气球的方法是直接添加上首尾各一个1，同时使用记忆化能加速不少，也为下一步的DP提供思路。

时间复杂度是O(N^2 * log(N))(不会算…)，空间复杂度是O(N)。

```python
class Solution(object):
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        nums.insert(0, 1)
        nums.append(1)
        c = [[0] * (n + 2) for _ in range(n + 2)]
        return self.dfs(nums, c, 1, n)
        
    def dfs(self, nums, c, i, j):
        if i > j: return 0
        if c[i][j] > 0: return c[i][j]
        if i == j: return nums[i - 1] * nums[i] * nums[i + 1]
        res = 0
        for k in range(i, j + 1):
            res = max(res, self.dfs(nums, c, i, k - 1) + nums[i - 1] * nums[k] * nums[j + 1] + self.dfs(nums, c, k + 1, j))
        c[i][j] = res
        return c[i][j]
```

第二种解法是使用DP。

DP一般都可以通过记忆化搜索来改出来，但是我不会。。很遗憾，参考了别人的代码，还是没搞懂。。

```python
class Solution(object):
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        nums.insert(0, 1)
        nums.append(1)
        dp = [[0] * (n + 2) for _ in range(n + 2)]
        for len_ in range(1, n + 1):
            for left in range(1, n - len_ + 2):
                right = left + len_ - 1
                for k in range(left, right + 1):
                    dp[left][right] = max(dp[left][right], dp[left][k - 1] + nums[left - 1] * nums[k] * nums[right + 1] + dp[k + 1][right])
        return dp[1][n]
```

参考资料：

http://www.cnblogs.com/grandyang/p/5006441.html
https://www.youtube.com/watch?v=z3hu2Be92UA

## 日期

2018 年 10 月 2 日 —— 小蓝单车莫名其妙收了我1块钱，明明每个月免费骑10次的啊！


  [1]: https://blog.csdn.net/fuxuemingzhu/article/details/82917037
