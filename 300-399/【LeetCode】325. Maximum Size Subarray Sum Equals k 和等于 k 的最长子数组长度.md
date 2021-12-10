- 作者：    负雪明烛
- id：      fuxuemingzhu
- 个人博客：[http://fuxuemingzhu.cn/](http://fuxuemingzhu.cn/)

---
@[TOC](目录)

题目地址：https://leetcode-cn.com/problems/maximum-size-subarray-sum-equals-k/

## 题目描述

Given an array `nums` and a target value `k`, find the maximum length of a subarray that sums to `k`. If there isn't one, return 0 instead.

Note:
The sum of the entire nums array is guaranteed to fit within the 32-bit signed integer range.

Example 1:

    Input: nums = [1, -1, 5, -2, 3], k = 3
    Output: 4 
    Explanation: The subarray [1, -1, 5, -2] sums to 3 and is the longest.

Example 2:

    Input: nums = [-2, -1, 2, 1], k = 1
    Output: 2 
    Explanation: The subarray [-1, 2] sums to 1 and is the longest.

Follow Up:
- Can you do it in O(n) time?


## 题目大意

给定一个长度为 n 的整数数组和一个目标值 target，寻找能够使条件 `nums[i] + nums[j] + nums[k] < target` 成立的三元组  `i, j, k` 个数`（0 <= i < j < k < n）`。

## 解题方法

### prefix Sum

很常见的做法，求数组每个位置的prefix sum（前缀和），并把该sum和其对应的位置i放到字典里保存，由于我们需要找到最长的，因此如果有重复的prefix sum不可以覆盖之前的值。

知道了目标的target是k，每个位置的prefix sum，我们想得到`prefix[i] - prefix[j] = k`，所以在i位置我们可以向前寻找到`prefix[j] = prefix[i] - k`，这个值可以从字典中直接读取出来。这个就是以i为结尾的最长区间。

我下面的做法为了方便，preSum在最起始位置增加了一个0，其索引位置是-1。

另外这个题中，需要注意的是区间的长度是不是要+1的问题，答案是不用+1，因为知道的`prefix[j]`是区间起始位置的前一个位置，即真正的和是k的区间是`[j + 1, i]`双闭区间，其区间长度是`i - j`。

C++代码如下：

```cpp
class Solution {
public:
    int maxSubArrayLen(vector<int>& nums, int k) {
        const int N = nums.size();
        vector<int> preSum(N + 1, 0);
        unordered_map<int, int> m;
        m[0] = -1;
        int res = 0;
        for (int i = 0; i < N; ++i) {
            preSum[i + 1] += preSum[i] + nums[i];
            if (!m.count(preSum[i + 1])) {
                m[preSum[i + 1]] = i;
            }
            int cur = preSum[i + 1] - k;
            if (m.count(cur)) {
                res = max(res, i - m[cur]);
            }
        }
        return res;
    }
};
```

## 日期

2019 年 9 月 22 日 —— 熬夜废掉半条命


  [1]: https://assets.leetcode.com/uploads/2018/10/12/maze_1_example_1.png
  [2]: https://assets.leetcode.com/uploads/2018/10/13/maze_1_example_2.png
  [3]: https://blog.csdn.net/fuxuemingzhu/article/details/101056461
