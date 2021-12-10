# 【LeetCode】673. Number of Longest Increasing Subsequence 解题报告（Python）

标签（空格分隔）： LeetCode

---

题目地址：https://leetcode.com/problems/number-of-longest-increasing-subsequence/description/

## 题目描述：

Given an unsorted array of integers, find the number of longest increasing subsequence.

    Example 1:
    Input: [1,3,5,4,7]
    Output: 2
    Explanation: The two longest increasing subsequence are [1, 3, 4, 7] and [1, 3, 5, 7].
    
    Example 2:
    Input: [2,2,2,2,2]
    Output: 5
    Explanation: The length of longest continuous increasing subsequence is 1, and there are 5 subsequences' length is 1, so output 5.

Note: Length of the given array will be not exceed 2000 and the answer is guaranteed to be fit in 32-bit signed int.

    
## 题目大意

这个题是最长递增子序列的变种。求最长的子序列有多少个。

## 解题方法

首先肯定还是使用dp去求。不过，我们得对dp的数组进行改进，我们在每个位置记录当前的LIS和能得到该LIS长度的子序列数目。在对每个位置进行计算的时候，我们都要找到该位置的LIS长度，并对能得到该长度的子序列的个数进行求和。

最后，我们需要对所有位置等于LIS长度的进行统计。

代码：

```python
class Solution(object):
    def findNumberOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp, longest = [[1, 1] for _ in range(len(nums))], 1
        for i in range(1, len(nums)):
            curr_longest, count = 1, 0
            for j in range(i):
                if nums[j] < nums[i]:
                    curr_longest = max(curr_longest, dp[j][0] + 1)
            for j in range(i):
                if dp[j][0] == curr_longest - 1 and nums[j] < nums[i]:
                    count += dp[j][1]
            dp[i] = [curr_longest, max(count, dp[i][1])]
            longest = max(longest, curr_longest)
        return sum([item[1] for item in dp if item[0] == longest])
```

## 日期

2018 年 4 月 4 日 ———— 清明时节雪纷纷～～下雪了，惊不惊喜，意不意外？


  [1]: https://leetcode.com/articles/delete-operation-for-two-strings/