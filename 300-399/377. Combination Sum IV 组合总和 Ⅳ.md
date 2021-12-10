
作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)

题目地址：https://leetcode.com/problems/combination-sum-iv/description/


## 题目描述

Given an integer array with all positive numbers and no duplicates, find the number of possible combinations that add up to a positive integer target.

Example:

	nums = [1, 2, 3]
	target = 4
	
	The possible combination ways are:
	(1, 1, 1, 1)
	(1, 1, 2)
	(1, 2, 1)
	(1, 3)
	(2, 1, 1)
	(2, 2)
	(3, 1)

	Note that different sequences are counted as different combinations.
	
	Therefore the output is 7.

Follow up:

- What if negative numbers are allowed in the given array?
- How does it change the problem?
- What limitation we need to add to the question to allow negative numbers?

## 题目大意

给了一个只包含正整数且不重复的数组，有多少种和为target的方案。

## 解题方法

这个题用回溯法竟然超时了！怪不得需要返回个数而不是所有的答案。

我们需要一个一维数组dp，其中dp[i]表示目标数为i的解的个数，然后我们从1遍历到target，对于每一个数i，遍历nums数组，如果i>=x, dp[i] += dp[i - x]。这个也很好理解，比如说对于[1,2,3] 4，这个例子，当我们在计算dp[3]的时候，3可以拆分为1+x，而x即为dp[2]，3也可以拆分为2+x，此时x为dp[1]，3同样可以拆为3+x，此时x为dp[0]，我们把所有的情况加起来就是组成3的所有情况了。


算dp[n]的时候遍历num[1] to num[n] index = i

如果i < dp[n] 那么dp[n] = dp[n] + dp[n-i]

从逻辑上来考虑比较复杂，比如4=0+4 1+3 2+2 3+1 4+0

0+4 1 （1+1+1+1）
1+3 1的组合3的组合
2+2 2的组合2的组合
3+1 3的组合*1的组合
4+0 1 （4）

1+4+4+4+1 然后除以2 因为重复了一遍
但是结果似乎不对

看答案 算法是

dp[n] = dp[n] + dp[n-i]
比如4
从1遍历到4
1<4
dp[4] = dp[4] + dp[4-1]

Python解法如下：

```python
class Solution(object):
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        dp = [0] * (target + 1)
        dp[0] = 1
        for i in xrange(1, target + 1):
            for num in nums:
                if i >= num:
                    dp[i] += dp[i - num]
        return dp.pop()
```

C++代码如下：

```cpp
class Solution {
public:
    int combinationSum4(vector<int>& nums, int target) {
        vector<int> dp(target + 1, 0);
        dp[0] = 1;
        for (int i = 1; i <= target; i++) {
            for (auto a : nums) {
                if (i >= a) {
                    dp[i] += dp[i - a];
                } 
            }
        }
        return dp.back();
    }
};
```


## 日期

2018 年 2 月 21 日 
2018 年 12 月 20 日 —— 感冒害的我睡不着
