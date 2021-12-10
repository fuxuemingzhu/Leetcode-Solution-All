
作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)

题目地址：https://leetcode.com/problems/longest-increasing-subsequence/description/

## 题目描述

Given an unsorted array of integers, find the length of longest increasing subsequence.

Example:

	Input: [10,9,2,5,3,7,101,18]
	Output: 4 
	Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4. 

Note:

1. There may be more than one LIS combination, it is only necessary for you to return the length.
1. Your algorithm should run in O(n2) complexity.

Follow up: Could you improve it to O(n log n) time complexity?
    
## 题目大意

求数组的最长递增子序列。即LIS.

## 解题方法

这个题是动态规划的经典题目，其实没有那么难，只要明白其中的道理即可。在《计算机考研机试指南》P160中有详细的解答。

核心思想是使用一个数组dp来保存，dp[i]的意义是到该位置为止的最长递增子序列。

最后求所有位置的``最大值``，而不是dp的最后元素。

![这里写图片描述](https://img-blog.csdn.net/20180404182025966?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2Z1eHVlbWluZ3podQ==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)

Python代码：

```python
class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return 0
        dp = [0] * len(nums)
        dp[0] = 1
        for i in range(1, len(nums)):
            tmax = 1
            for j in range(0, i):
                if nums[i] > nums[j]:
                    tmax = max(tmax, dp[j] + 1)
            dp[i] = tmax
        return max(dp)
```

C++代码如下：

```cpp
class Solution {
public:
    int lengthOfLIS(vector<int>& nums) {
        const int N = nums.size();
        if (N == 0) return 0;
        // dp[i] means the LIS when the subsequence ends with nums[i]
        vector<int> dp(N, 1);
        for (int i = 1; i < N; ++i) {
            for (int j = i - 1; j >= 0; --j) {
                if (nums[j] < nums[i]) {
                    dp[i] = max(dp[i], dp[j] + 1);
                }
            }
        }
        return *max_element(dp.begin(), dp.end());
    }
};
```

## 日期

2018 年 4 月 4 日 —— 清明时节雪纷纷～～下雪了，惊不惊喜，意不意外？
2019 年 1 月 7 日 —— 新的一周开始啦啦啊
