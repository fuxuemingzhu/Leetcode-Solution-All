
作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)

题目地址：https://leetcode.com/problems/subarray-sum-equals-k/description/

## 题目描述

Given an array of integers and an integer k, you need to find the total number of continuous subarrays whose sum equals to k.

Example 1:

    Input:nums = [1,1,1], k = 2
    Output: 2

Note:

1. The length of the array is in range [1, 20,000].
1. The range of numbers in the array is [-1000, 1000] and the range of the integer k is [-1e7, 1e7].



## 题目大意

求数组中有多少个连续子数组的和正好等于k。

## 解题方法

看了数组的长度，明显O(n^2)的时间复杂度会超时。这个时间复杂度一般只能用O(N)的解法了。

使用一个字典保存数组某个位置之前的数组和，然后遍历数组求和，这样当我们求到一个位置的和的时候，向前找sum-k是否在数组中，如果在的话，更新结果为之前的结果+(sum-k出现的次数)。同时，当前这个sum出现的次数就多了一次。

这个字典的意义是什么呢？其意义就是我们在到达i位置的时候，``前i项的和``出现的次数的统计。我们想找的是在i位置向前的连续区间中，有多少个位置的和是k。有了这个统计，我们就不用向前一一遍历找sum - k在哪些位置出现了，而是直接得出了前面有多少个区间。所以，在每个位置我们都得到了``以这个位置为结尾的并且和等于k的区间``的个数，所以总和就是结果。

这个题的解法不难想出来，因为如果要降低时间复杂度，应该能想到增加空间复杂度，那么要么使用数组，要么就是用字典之类的，保留之前的结果。

时间复杂度是O(N)，空间复杂度是O(N).

代码如下：

```python
class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)
        d = collections.defaultdict(int)
        d[0] = 1
        sum = 0
        res = 0
        for i in range(n):
            sum += nums[i]
            if sum - k in d:
                res += d[sum - k]
            d[sum] += 1
        return res
```

参考资料：

https://www.youtube.com/watch?v=mKXIH9GnhgU

## 日期

2018 年 9 月 19 日 —— 梦见李彦宏和我聊微信，他感谢我给一个短视频App做了分享功能……
2019 年 1 月 4 日 —— 这周就过去了
