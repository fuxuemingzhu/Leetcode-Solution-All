作者： 		负雪明烛 
id：				fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---

题目地址: https://leetcode.com/problems/subarray-product-less-than-k/description/

## 题目描述：

Your are given an array of positive integers ``nums``.

Count and print the number of (contiguous) subarrays where the product of all the elements in the subarray is less than ``k``.

Example 1:

    Input: nums = [10, 5, 2, 6], k = 100
    Output: 8
    Explanation: The 8 subarrays that have product less than 100 are: [10], [5], [2], [6], [10, 5], [5, 2], [2, 6], [5, 2, 6].
    Note that [10, 5, 2] is not included as the product of 100 is not strictly less than k.

Note:

- 0 < nums.length <= 50000.
- 0 < nums[i] < 1000.
- 0 <= k < 10^6.

## 题目大意

找出一个数组中连续子数组的乘积有多少个小于k的。

## 解题方法

因为只要求个数，不要求列出来，那么可以想到双指针。

这个题的做法还是很简单的，使用两个指针确定子数组的边界，然后求子数组的乘积，如果乘积大于等于k了，需要移动左指针。每次移动有指针之后，符合题目要求的结果增加的是以右指针为边界的子数组数量，也就是r - l + 1。

注意移动左指针的时候，不能超过右指针。

时间复杂度是O(N)，空间复杂度是O(1)。

```python
class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        N = len(nums)
        prod = 1
        l, r = 0, 0
        res = 0
        while r < N:
            prod *= nums[r]
            while l <= r and prod >= k:
                prod /= nums[l]
                l += 1
            res += r - l + 1
            r += 1
        return res
```


参考资料：


## 日期

2018 年 10 月 14 日 —— 周赛做出来3个题，开心
