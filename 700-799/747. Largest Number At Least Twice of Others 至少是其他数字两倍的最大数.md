
作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)

题目地址：[https://leetcode.com/problems/largest-number-at-least-twice-of-others/description/][1]


## 题目描述

In a given integer array ``nums``, there is always exactly one largest element.

Find whether the largest element in the array is at least twice as much as every other number in the array.

If it is, return the index of the largest element, otherwise return -1.

Example 1:

    Input: nums = [3, 6, 1, 0]
    Output: 1
    Explanation: 6 is the largest integer, and for every other number in the array x,
    6 is more than twice as big as x.  The index of value 6 is 1, so we return 1.

Example 2:

    Input: nums = [1, 2, 3, 4]
    Output: -1
    Explanation: 4 isn't at least as big as twice the value of 3, so we return -1.

Note:

1. nums will have a length in the range [1, 50].
1. Every nums[i] will be an integer in the range [0, 99].

## 题目大意

判断一个数组中的最大数字是不是其他数字的至少2倍。如果是的话返回最大数字的索引，否则返回-1.

## 解题方法

### 寻找两次最大值

最大值是其他值的二倍，也就是说最大值是次大值的二倍即可。

题目已经说了，最大值只存在一个。所以找到最大值，然后找到其索引，弹出该值之后再求最大值。

```python
class Solution(object):
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return 0
        largest = max(nums)
        ind = nums.index(largest)
        nums.pop(ind)
        if largest >= 2 * max(nums):
            return ind
        else:
            return -1
```

### 排序

先排序，然后看最大是不是次大的二倍，这样也可以。不过排序会改变位置，所以先保存最大数字的位置。

```python
class Solution(object):
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return 0
        largest = max(nums)
        ind = nums.index(largest)
        nums.sort()
        if largest >= 2 * nums[-2]:
            return ind
        else:
            return -1
```

### 大顶堆

使用大顶堆保存了数字和索引的映射，这样弹出来两个位置，便是最大和次大，在判断即可。

```python
class Solution(object):
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return 0
        heap = [(-num, i) for i, num in enumerate(nums)]
        heapq.heapify(heap)
        largest, ind = heapq.heappop(heap)
        if largest <= 2 * heapq.heappop(heap)[0]:
            return ind
        return -1
```

## 日期

2018 年 1 月 28 日 
2018 年 11 月 21 日 —— 又是一个美好的开始

  [1]: https://leetcode.com/problems/largest-number-at-least-twice-of-others/description/
