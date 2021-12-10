
作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)

题目地址：[https://leetcode.com/problems/maximum-product-of-three-numbers/description/][1]


## 题目描述

Given an integer array, find three numbers whose product is maximum and output the maximum product.

Example 1:

    Input: [1,2,3]
    Output: 6

Example 2:

    Input: [1,2,3,4]
    Output: 24

Note:

1. The length of the given array will be in range [3,104] and all elements are in the range [-1000, 1000].
1. Multiplication of any three numbers in the input won't exceed the range of 32-bit signed integer.

## 题目大意

从一个数组中找出三个数字，求这三个数字的乘积是最大的值。


## 解题方法

### 方法一：排序

这个题要求数组中三个数乘积最大的值。我觉得可以从为什么问3个数字而不是其他数字去考虑。

输入有可能存在负值，所以3个数字的乘积时会考虑到负负得正的情况。只有三个数都是正数或者有只有两个负数时得到的结果是正的。这样，首先通过排序，得到最右边三个数的乘积，和最小的两个负数（如果存在负数）和最大数字的乘积，比较两个乘积的大小就行了。

如果排序后取到的三个数存在奇数个负数也没关系，我们取最大值的时候会保证取到最大的。

```python
class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        right = nums[-3] * nums[-2] * nums[-1]
        left = nums[0] * nums[1] * nums[-1]
        return max(left, right)
```

## 日期

2018 年 1 月 26 日 
2018 年 11 月 17 日 —— 美妙的周末，美丽的天气

  [1]: https://leetcode.com/problems/minimum-index-sum-of-two-lists/description/
