
作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)

题目地址：https://leetcode.com/problems/target-sum/description/

## 题目描述

You are given a list of non-negative integers, a1, a2, ..., an, and a target, S. Now you have 2 symbols + and -. For each integer, you should choose one from + and - as its new symbol.

Find out how many ways to assign symbols to make sum of integers equal to target S.

    Example 1:
    
    Input: nums is [1, 1, 1, 1, 1], S is 3. 
    Output: 5
    Explanation: 
    
    -1+1+1+1+1 = 3
    +1-1+1+1+1 = 3
    +1+1-1+1+1 = 3
    +1+1+1-1+1 = 3
    +1+1+1+1-1 = 3

There are 5 ways to assign symbols to make the sum of nums be target 3.

Note:

1. The length of the given array is positive and will not exceed 20.
1. The sum of elements in the given array will not exceed 1000.
1. Your output answer is guaranteed to be fitted in a 32-bit integer.

## 题目大意

给了一个数组和一个target number，现在要给这个数组的每个数添加上+或-， 使得求和的结果是target number。求满足条件的组合个数。

## 解题方法

### 动态规划

这个题让我扔了三个月，今天又看了两个小时，动态规划不很懂就是这个后果！

刚开始用的dfs做的，遍历所有的结果，统计满足结果的个数就可以了。没错，超时了。超时的代码如下：

```python
class Solution(object):
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        def helper(index, acc):
            if index == len(nums):
                if acc == S:
                    return 1
                else:
                    return 0
            return helper(index + 1, acc + nums[index]) + helper(index + 1, acc - nums[index])
        return helper(0, 0)
```

其实一般能用dfs解决的题目，如果题目只要求满足条件的数字而不是所有的结果，那么dfs会超时。解决方法其实基本只有一条路：动态规划。

我们定义了一个二维数组，这个二维数组dp[i][j]的意义是我们从最开始的位置到第i个位置上能够成和为j的组合有多少种，因为求和之后数的范围不确定，所以数组中保存的是字典，字典保存的是到i位置能求得的和为某个数的个数。

所以从左到右进行遍历，在每个位置都把前一个位置的字典拿出来，看前一个位置的所有能求得的和。和当前的数值分别进行加减操作，就能得出新一个位置能求得的和了。

状态转移方程是：

```
dp[0][0] = 1;
dp[i + 1][x + nums[i]] += dp[i][x];
dp[i + 1][x - nums[i]] += dp[i][x];
注意：其中x是在前一个位置能够成的和。
```

要注意一点是，dp初始不能采用下面方式：

```python
dp = [collections.defaultdict(int)] * (_len + 1) 
```
这种初始化方式会使每个位置的元素其实是同一个字典。

代码如下：

```python
class Solution:
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        _len = len(nums)
        dp = [collections.defaultdict(int) for _ in range(_len + 1)] 
        dp[0][0] = 1
        for i, num in enumerate(nums):
            for sum, cnt in dp[i].items():
                dp[i + 1][sum + num] += cnt
                dp[i + 1][sum - num] += cnt
        return dp[_len][S]
```

这个题的C++代码如下，这里的代码说明了对于unordered_map，在C++里面调用一个不存在的key的时候，会使用默认初始化的版本，类似于Python的collections.defaultdict()。比如这里调用的+=符号，在左侧不存在的时候，会初始化0。

```cpp
class Solution {
public:
    int findTargetSumWays(vector<int>& nums, int S) {
        const int N = nums.size();
        vector<unordered_map<int, int>> dp(N + 1);
        dp[0][0] = 1;
        for (int i = 0; i < N; i ++) {
            for (auto m : dp[i]) {
                dp[i + 1][m.first + nums[i]] += m.second;
                dp[i + 1][m.first - nums[i]] += m.second;
            }
        }
        return dp[N][S];
    }
};
```

## 日期

2018 年 5 月 28 日 —— 太阳真的像日光灯～
2018 年 12 月 31 日 —— 2018年最后一天！
