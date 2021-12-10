
作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)
题目地址：[https://leetcode.com/problems/maximum-subarray/#/description][1]


## 题目描述


Given an integer array nums, find the contiguous ``subarray`` (containing at least one number) which has the largest sum and return its sum.

Example:

	Input: [-2,1,-3,4,-1,2,1,-5,4],
	Output: 6
	Explanation: [4,-1,2,1] has the largest sum = 6.

Follow up:

If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.

## 题目大意

找出子数组的最大和。

## 解题方法

### 暴力解法
所谓暴力解法，就是找出所有子数组的最大的和。

为了快速求子数组的和，我们有个常用的技巧，就是用个 `preSum[i]` 数组表示在 `i` 位置之前的数组的和。即 `preSum[i] = sum(num[0]...nums[i])`。

然后使用两重循环，遍历所有的子数组，子数组和可以用 `preSum[j] - preSum[i]` 直接求出。

总的时间复杂度是 `O(N ^ 2)`，可以通过。

C++代码如下：

```cpp
class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        const int N = nums.size();
        vector<int> preSum(N + 1, 0);
        for (int i = 0; i < N; ++i) {
            preSum[i + 1] = preSum[i] + nums[i];
        }
        int res = INT_MIN;
        for (int i = 0; i < N + 1; ++i) {
            for (int j = i + 1; j < N + 1; ++j) {
                res = max(res, preSum[j] - preSum[i]);
            }
        }
        return res;
    }
};
```

### 动态规划

明显的DP方法去解决。

通过构建一个和原长一样长的数组， dp 数组的含义是以 `dp[i]` 为结尾的最大子数组的和。

状态转移公式：
1.  `dp[i] = dp[i - 1] + nums[i]` 当 nums[i] >= 0 。
2.   `dp[i] = nums[i]` 当 nums[i] < 0 。

题目求的最大子数组的和，就是 dp 数组的最大值。

Java 代码如下：

```java
public class Solution {
    public int maxSubArray(int[] nums) {
        int len = nums.length;
        int[] dp = new int[len];
        dp[0] = nums[0];
        int max = dp[0];
        for(int i = 1; i < len; i++){
            dp[i] = nums[i] + (dp[i -1] > 0 ? dp[i -1] : 0);
            max = Math.max(max, dp[i]);
        }
        return max;
    }
}
```

二刷，Python解法如下：

```python
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return 0
        N = len(nums)
        cur, prev = 0, 0
        res = float("-inf")
        for i in range(N):
            cur = nums[i] + (prev if prev > 0 else 0)
            prev = cur
            res = max(res, cur)
        return res
```

三刷，C++解法如下：

```cpp
class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        const int N = nums.size();
        int res = nums[0];
        vector<int> dp(N, 0); // 以i为结尾的最大子数组的max subarray.
        dp[0] = nums[0];
        for (int i = 1; i < N; ++i) {
            dp[i] = nums[i] + (dp[i - 1] > 0 ? dp[i - 1] : 0);
            res = max(res, dp[i]);
        }
        return res;
    }
};
```

## 日期

2017 年 5 月 2 日 
2018 年 11 月 19 日 —— 周一又开始了
2020 年 4 月 3 日 —— 这个题是英文版leetcode的每日一题

  [1]: https://leetcode.com/problems/maximum-subarray/#/description
