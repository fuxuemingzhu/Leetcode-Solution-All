

作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)


题目地址：https://leetcode.com/problems/rotate-array/description/


## 题目描述

Rotate an array of n elements to the right by k steps.

    For example, with n = 7 and k = 3, the array [1,2,3,4,5,6,7] is rotated to [5,6,7,1,2,3,4].

Note:

- Try to come up as many solutions as you can, there are at least 3 different ways to solve this problem.
- Could you do it in-place with O(1) extra space?

## 题目大意

把一个数组向右移动k步，原地操作。

## 解题方法

### 切片

题目要求旋转，而且是从右边数k个值放到前面去进行旋转。需要注意的两点：

1. k可能很大，也就是会旋转多次
2. 原地翻转

下面的做法是先去除了多次旋转的情况，然后通过遍历在原地翻转

```python
class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        while k > len(nums):
            k -= len(nums)
        changed = nums[-k:] + nums[:-k]
        for i in range(len(changed)):
            nums[i] = changed[i]
```

更优雅的方法，使用k对len进行求余，另外使用``nums[:]``即可原地翻转。


```python
class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        k %= len(nums)
        nums[:] = nums[-k:] + nums[:-k]
```

### 递归

先把整个的翻转，再把前k个翻转，再把后面的翻转。

```python
class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        N = len(nums)
        k %= N
        self.reverse(nums, 0, N - 1);
        self.reverse(nums, 0, k - 1);
        self.reverse(nums, k, N - 1);

    def reverse(self, nums, start, end):
        while start <= end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1
```

## 日期

2018 年 2 月 5 日 
2018 年 11 月 29 日 —— 时不我待
