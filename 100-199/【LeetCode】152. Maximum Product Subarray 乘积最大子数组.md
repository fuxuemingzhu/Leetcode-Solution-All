
作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)

题目地址：https://leetcode.com/problems/maximum-product-subarray/description/


## 题目描述

Given an integer array ``nums``, find the contiguous subarray within an array (containing at least one number) which has the largest product.

Example 1:

    Input: [2,3,-2,4]
    Output: 6
    Explanation: [2,3] has the largest product 6.

Example 2:

    Input: [-2,0,-1]
    Output: 0
    Explanation: The result cannot be 2, because [-2,-1] is not a subarray.


## 题目大意

求连续子数组最大乘积。

## 解题方法

### 双重循环

这个题最简单粗暴的方法当然是两重循环啦！遍历每个区间的开始和结束位置，然后求这个区间的积，然后保留最大的积即可。没想到C++直接提交竟然给通过了！说明这个O(N^2)的时间复杂度还是能够接受的。

```cpp
class Solution {
public:
    int maxProduct(vector<int>& nums) {
        const int N = nums.size();
        int res = INT_MIN;
        for (int i = 0; i < N; ++i) {
            int cur = 1;
            for (int j = i; j < N; ++j) {
                if (j == i)
                    cur = nums[i];
                else 
                    cur = cur * nums[j];
                res = max(res, cur);
            }
        }
        return res;
    }
};
```

### 动态规划

如果是连续子数组的和的问题我们肯定能想到虫取法之类的，但是求积就比较麻烦了，因为某个位置可能出现了0或者负数。。当遇到0的时候，整个乘积会变成0；当遇到负数的时候，当前的最大乘积会变成最小乘积，最小乘积会变成最大乘积。

有上面的分析可以看出，必须使用两个数组分别记录以某个位置i结尾的时候的最大乘积和最小乘积了。令最大乘积为f，最小乘积为g。那么有：

- 当前的最大值等于已知的最大值、最小值和当前值的乘积，当前值，这三个数的最大值。
- 当前的最小值等于已知的最大值、最小值和当前值的乘积，当前值，这三个数的最小值。
- 结果是最大值数组中的最大值。

时间复杂度是O(N)，空间复杂度是O(N). N是数组大小。超过了87%的提交。

题外话：是不是和股票交易问题很像？

```python
class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return 0
        N = len(nums)
        f = [0] * N
        g = [0] * N
        f[0] = g[0] = res = nums[0]
        for i in range(1, N):
            f[i] = max(f[i - 1] * nums[i], nums[i], g[i - 1] * nums[i])
            g[i] = min(f[i - 1] * nums[i], nums[i], g[i - 1] * nums[i])
            res = max(res, f[i])
        return res
```

这个版本的C++代码如下：

```cpp
class Solution {
public:
    int maxProduct(vector<int>& nums) {
        const int N = nums.size();
        vector<int> mx(N);
        vector<int> mn(N);
        int res = mx[0] = mn[0] = nums[0];
        for (int i = 1; i < N; ++i) {
            mx[i] = max(nums[i], max(mx[i - 1] * nums[i], mn[i - 1] * nums[i]));
            mn[i] = min(nums[i], min(mx[i - 1] * nums[i], mn[i - 1] * nums[i]));
            res = max(mx[i], res);
        }
        return res;
    }
};
```

上面的方法使用了数组实现，我们注意到，每次更新只用到了前面的一个值，所以可以使用变量优化空间复杂度。

```python
class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return 0
        N = len(nums)
        f = g = res = nums[0]
        for i in range(1, N):
            pre_f, pre_g = f, g
            f = max(pre_f * nums[i], nums[i], pre_g * nums[i])
            g = min(pre_f * nums[i], nums[i], pre_g * nums[i])
            res = max(res, f)
        return res
```

时间复杂度是O(N)，空间复杂度是O(1).N是数组大小。超过了99.9%的提交。

在上面两个做法中，使用求三个数最大、最小的方式来更新状态，确实很暴力。事实上可以使用判断，直接知道怎么优化。当nums[i]为正的时候，那么正常更新。如果nums[i]<=0的时候，需要反向更新。

```python
class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return 0
        N = len(nums)
        f = g = res = nums[0]
        for i in range(1, N):
            if nums[i] > 0:
                f, g = max(f * nums[i], nums[i]), min(g * nums[i], nums[i])
            else:
                f, g = max(g * nums[i], nums[i]), min(f * nums[i], nums[i])
            res = max(res, f)
        return res
```

时间复杂度是O(N)，空间复杂度是O(1).N是数组大小。超过了47%的提交。

在上面的做法中可以看出来，两个更新公式里面f和g的位置是互换的，所以可以提前判断nums[i]的正负进行提前的互换。

```python
class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return 0
        N = len(nums)
        f = g = res = nums[0]
        for i in range(1, N):
            if nums[i] < 0:
                f, g = g, f
            f, g = max(f * nums[i], nums[i]), min(g * nums[i], nums[i])
            res = max(res, f)
        return res
```

时间复杂度是O(N)，空间复杂度是O(1).N是数组大小。超过了47%的提交。

## 参考资料

http://www.cnblogs.com/grandyang/p/4028713.html


## 日期

2018 年 10 月 20 日 —— 10月剩余的时间又不多了


  [1]: https://www.youtube.com/watch?v=tLxBwSL3lPQ
