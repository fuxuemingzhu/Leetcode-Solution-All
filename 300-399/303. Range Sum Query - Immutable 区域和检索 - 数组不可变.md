
作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)

题目地址：[https://leetcode.com/problems/range-sum-query-immutable/description/][1]


## 题目描述

Given an integer array nums, find the sum of the elements between indices i and j (i ≤ j), inclusive.

    Example:
    Given nums = [-2, 0, 3, -5, 2, -1]
    
    sumRange(0, 2) -> 1
    sumRange(2, 5) -> -1
    sumRange(0, 5) -> -3

Note:

- You may assume that the array does not change.
- There are many calls to sumRange function.

## 解题方法

### 保存累积和

可以直接用切片求和的方法做，也能A，但是效率太慢。

下面这个方式可以先把sums求出来，然后再调用的时候直接右边的sums-左边的sums即可得到结果。

```python
class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.sums = [0] * len(nums)
        total = 0
        for i, num in enumerate(nums):
            total += num
            self.sums[i] = total
        

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        if i == 0:
            return self.sums[j]
        else:
            return self.sums[j] - self.sums[i - 1]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)
```

如果多用一个元素放在开头，那么上面的这个代码可以简化。

```python
class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        N = len(nums)
        self.sums = [0] * (N + 1)
        for i in range(1, N + 1):
            self.sums[i] = self.sums[i - 1] + nums[i - 1]

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.sums[j + 1] - self.sums[i]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)
```

## 日期

2018 年 2 月 4 日 
2018 年 11 月 24 日 —— 周六快乐

  [1]: https://leetcode.com/problems/range-sum-query-immutable/description/
