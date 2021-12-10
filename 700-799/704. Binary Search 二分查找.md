
作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)

题目地址：https://leetcode.com/problems/binary-search/description/

## 题目描述

Given a sorted (in ascending order) integer array nums of n elements and a target value, write a function to search target in nums. If target exists, then return its index, otherwise return -1.


Example 1:

    Input: nums = [-1,0,3,5,9,12], target = 9
    Output: 4
    Explanation: 9 exists in nums and its index is 4

Example 2:

    Input: nums = [-1,0,3,5,9,12], target = 2
    Output: -1
    Explanation: 2 does not exist in nums so return -1
 
Note:

1. You may assume that all elements in ``nums`` are unique.
1. n will be in the range ``[1, 10000]``.
1. The value of each element in ``nums`` will be in the range ``[-9999, 9999]``.


## 题目大意

二分查找某个元素出现的位置。

## 解题方法

### 线性查找

这个题目名字叫做二分查找，但是给的测试用例使用10000个，那么完全可以线性查找，代码如下。

```python
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        try:
            return nums.index(target)
        except:
            return -1
```

### 二分查找

不懂为啥这么简单的题，没人做？

二分查找真是最基本的题目了吧，应该保证一遍就过的。就不多说了。

下面的做法是查找[left, right]闭区间。代码如下：

```python
class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1
```

如果是查找[left, right)左闭右开区间的话，代码如下：

```python
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        N = len(nums)
        left, right = 0, N
        # [0, N)
        while left < right:
            mid = left + (right - left) / 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid
            else:
                left = mid + 1
        return -1
```

## 日期

2018 年 7 月 12 日 —— 天阴阴地潮潮，已经连着两天这样了
2018 年 11 月 21 日 —— 又是一个美好的开始

  [1]: https://blog.csdn.net/fuxuemingzhu/article/details/81016992
