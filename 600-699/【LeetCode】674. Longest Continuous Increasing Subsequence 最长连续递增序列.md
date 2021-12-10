
作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)

题目地址：[https://leetcode.com/problems/longest-continuous-increasing-subsequence/description/][1]


## 题目描述

Given an unsorted array of integers, find the length of longest continuous increasing subsequence (subarray).

Example 1:

	Input: [1,3,5,4,7]
	Output: 3
	Explanation: The longest continuous increasing subsequence is [1,3,5], its length is 3. 
	Even though [1,3,5,7] is also an increasing subsequence, it's not a continuous one where 5 and 7 are separated by 4. 

Example 2:

	Input: [2,2,2,2,2]
	Output: 1
	Explanation: The longest continuous increasing subsequence is [2], its length is 1. 
	Note: Length of the array will not exceed 10,000.

## 题目大意

找出数组中最长连续递增子序列（子数组）

## 解题方法

### 动态规划

直接使用dp作为到某个位置的最长连续子序列。所以，如果当前的值比前一个值大，那么dp应该是前面的一个位置的数值+1，否则当前的值应该是1。另外需要注意的是当输入是空的时候，应该返回0.

```python
class Solution(object):
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return 0
        N = len(nums)
        dp = [1] * N
        for i in range(1, N):
            if nums[i] > nums[i - 1]:
                dp[i] = dp[i - 1] + 1
        return max(dp)
```

### 空间压缩DP

在上面的做法中看出，每步的结果之和上面一步有关，所以可以优化空间复杂度。


```python
class Solution(object):
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        longest = 0
        cur = 0
        for i in range(len(nums)):
            if i == 0 or nums[i] > nums[i - 1]:
                cur += 1
                longest = max(longest, cur)
            else:
                cur = 1
        return longest
```

---
二刷的时候版本。

```python
class Solution(object):
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return 0
        N = len(nums)
        dp = 1
        res = 1
        for i in range(1, N):
            if nums[i] > nums[i - 1]:
                dp += 1
                res = max(res, dp)
            else:
                dp = 1
        return res
```

## 日期

2018 年 1 月 29 日 
2018 年 11 月 19 日 —— 周一又开始了

  [1]: https://leetcode.com/problems/longest-continuous-increasing-subsequence/description/
