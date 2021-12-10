
作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)
题目地址：[https://leetcode.com/problems/set-mismatch/description/][1]


## 题目描述

The set ``S`` originally contains numbers from ``1 to n``. But unfortunately, due to the data error, one of the numbers in the set got duplicated to another number in the set, which results in repetition of one number and loss of another number.

Given an array ``nums`` representing the data status of this set after the error. Your task is to firstly find the number occurs twice and then find the number that is missing. Return them in the form of an array.

Example 1:

    Input: nums = [1,2,2,4]
    Output: [2,3]

Note:

- The given array size will in the range [2, 10000].
- The given array's numbers won't have any order.

## 题目大意

数组正常的状态是1~N，但是有个数字重复出现了，导致覆盖了另外一个数字，现在要求重复出现的数字，和缺失的数字。

## 解题方法

### Hash方法

这个题明显使用hash的思想。把每个位置出现的次数统计一下，找出出现了2次和0次的数字的位置即可。

```python
class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        hashs = [0] * len(nums)
        missing = -1
        for i in range(len(nums)):
            hashs[nums[i] - 1] += 1
        return [hashs.index(2) + 1, hashs.index(0) + 1]
```

### 直接计算

和[268. Missing Number](https://blog.csdn.net/fuxuemingzhu/article/details/70332471)很像，直接计算出来也可以，速度稍快点。

```python
class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        N = len(nums)
        nset = set(nums)
        missing = N * (N + 1) / 2 - sum(nset)
        duplicated = sum(nums) - sum(nset)
        return [duplicated, missing]
```

## 日期

2018 年 2 月 3 日 
2018 年 11 月 21 日 —— 又是一个美好的开始

  [1]: https://leetcode.com/problems/set-mismatch/description/
