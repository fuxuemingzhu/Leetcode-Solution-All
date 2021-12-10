作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)

[LeetCode]

题目地址：[https://leetcode.com/problems/house-robber/](https://leetcode.com/problems/house-robber/)

Total Accepted: 67398 Total Submissions: 196356 Difficulty: Easy


# 题目描述

You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security system connected and **it will automatically contact the police if two adjacent houses were broken into on the same night.**

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight **without alerting the police.**

Example 1:

	Input: [1,2,3,1]
	Output: 4
	Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
	             Total amount you can rob = 1 + 3 = 4.

Example 2:

	Input: [2,7,9,3,1]
	Output: 12
	Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
	             Total amount you can rob = 2 + 9 + 1 = 12.

# 题目大意

每个房间里有些价值的物品，不能偷连续的房间，那么求最多能偷多少物品？

# 解题方法

**动态规划**到底怎么想？其实可以先用 `递归+记忆化` 解决问题，然后再转化成动态规划。

首先说明的是 **递归+记忆化** 是**从顶向下**的一种解决方式：即我们要解决大问题，大问题拆解成小问题。
而 **动态规划** 是**从底向上**的一种解决方式：即我们先解决小问题，然后逐步推出大问题。

## 递归

假如`dfs(i)`表示从左到右的第 `i` 个位置能偷多少金额，是不是就是 `max(dfs(i - 1), dfs(i - 2) + nums[i])`。自顶向下的思路就是**递归**去求解 `dfs(i - 1)`, `dfs(i - 2)`。

所以我们有了最简单的一个**递归**代码：

```python
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        return self.dfs(nums, len(nums) - 1)
    
    # 在第 i 个房间之前（包括 i）能获取的最大收益
    def dfs(self, nums, i):
        if i == 0:
            return nums[0]
        if i == 1:
            return max(nums[0], nums[1])
        return max(self.dfs(nums, i - 1), self.dfs(nums, i - 2) + nums[i])
```

提交之后发现**超时**了。

## 递归 + 记忆化

为什么超时呢，是因为我们有重复计算：`dfs(2)` 需要求 `dfs(0)`、`dfs(1)`；而 `dfs(3)` 需要求 `dfs(2)`，然后再求一遍 `dfs(0)`、`dfs(1)`。

解决这个问题的方法是：记录一下已经求过的值，避免重复计算。

于是有了记忆化的方法，用`memo[i]`记录已经求过的`dfs(i)`，之后在搜索的时候，先找 `memo`中是否已经保存了这个数字，如果已经保存就不用再计算了。

于是有了以下的代码：

```python
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        self.memo = dict()
        return self.dfs(nums, len(nums) - 1)
    
    # 在第 i 个房间之前（包括 i）能获取的最大收益
    def dfs(self, nums, i):
        if i in self.memo:
            return self.memo[i]
        res = 0
        if i == 0:
            res = nums[0]
        elif i == 1:
            res = max(nums[0], nums[1])
        else:
            res = max(self.dfs(nums, i - 1), self.dfs(nums, i - 2) + nums[i])
        self.memo[i] = res
        return res
```

这份答案已经能通过了。

## 动态规划

上面分析了这么多，可以看出**递归**是先想获得 `i` 位置的结果 ，然后分解成求解 `i - 1` 位置的结果 和 `i - 2` 位置的结果。这就是`从顶向下`。

反过来我们也可以想到，如果先求 `i - 1` 位置的结果 和 `i - 2` 位置的结果，再求 `i` 位置的结果不是也行吗？对！这就是 **动态规划**，它的思想是`从底向上`。

首先定义状态： dp[i] 表示从左到右的第 `i` 个位置能偷多少金额。（和递归的定义是不是一样？）

然后明确状态转移方程：

	dp[0] = num[0] （当i=0时）
	dp[1] = max(num[0], num[1]) （当i=1时）
	dp[i] = max(num[i] + dp[i - 2], dp[i - 1]) （当 i !=0 and i != 1 时）


最后写代码：

```python
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        N = len(nums)
        dp = [0] * (N + 1)
        dp[1] = nums[0]
        for i in range(1, N):
            dp[i + 1] = max(dp[i], dp[i - 1] + nums[i])
        return dp[-1]
```

动态规划会比`递归 + 记忆化`的速度更快，主要是`递归 + 记忆化`需要开辟栈空间，而且还需要多一步是否在 `memo` 中存在的判断。


Java代码如下：

```java
public class Solution {
    public int rob(int[] nums) {
        if(nums.length==0) return 0;
        if(nums.length==1) return nums[0];
        int[] maxMoney=new int[nums.length];
        maxMoney[0]=nums[0];
        maxMoney[1]=Math.max(nums[0],nums[1]);
        for(int i=2; i<nums.length; i++){
            maxMoney[i]=Math.max(nums[i]+maxMoney[i-2], maxMoney[i-1]);
        }
        return maxMoney[nums.length-1];
    }
}
```
AC:0ms

## 优化动态规划空间

我们看到动态规划的解法中，`dp[i]` 只和 `dp[i - 1]` 和 `dp[ i - 2]` 有关，因此可以用变量优化使用空间：

Python代码如下：

```python
class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        prev, cur = 0, 0
        for value in nums:
            prev, cur = cur, max(prev + value, cur)
        return cur
```

## 日期

2016/5/1 21:44:42 
2018 年 9 月 9 日
2018 年 11 月 21 日 —— 又是一个美好的开始
2020 年 5 月 29 日 —— 答辩顺利
