
作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)

题目地址：[https://leetcode.com/problems/find-pivot-index/description/][1]


## 题目描述

Given an array of integers nums, write a method that returns the "pivot" index of this array.

We define the pivot index as the index where the sum of the numbers to the left of the index is equal to the sum of the numbers to the right of the index.

If no such index exists, we should return -1. If there are multiple pivot indexes, you should return the left-most pivot index.

Example 1:

    Input: 
    nums = [1, 7, 3, 6, 5, 6]
    Output: 3
    Explanation: 
    The sum of the numbers to the left of index 3 (nums[3] = 6) is equal to the sum of numbers to the right of index 3.
    Also, 3 is the first index where this occurs.

Example 2:

    Input: 
    nums = [1, 2, 3]
    Output: -1
    Explanation: 
    There is no index that satisfies the conditions in the problem statement.

Note:

1. The length of nums will be in the range [0, 10000].
1. Each element nums[i] will be an integer in the range [-1000, 1000].

## 题目大意

找出数组中的某个位置使得这个位置的左边元素的和等于右边元素的和。

## 解题方法

### 先求和，再遍历

题面比较简单，找出列表的一个分割点，使该分割点左右的所有元素的和相等。

如果是不停的求sum()的方法，一定会超时的，所以比较机智的方式是先求出sum，然后通过指针的移动来求左右的和的变化。

需要注意的一点就是，求和是不包括当前的节点的，因此，当i==0的时候，不应把left加上，而且左边的求和只能求到i-1。

```python
class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return -1
        left = 0
        right = sum(nums)
        for i in range(len(nums)):
            if i != 0:
                left += nums[i - 1]
            right -= nums[i]
            if left == right:
                return i
        return -1
```

事实上，右边的和也可以使用整体的和减去左边和+现在的位置的数字来得到。代码如下：

```python
class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return -1
        N = len(nums)
        sums = [0] * (N + 1)
        for i in range(N):
            sums[i + 1] = sums[i] + nums[i]
        for i in range(N):
            if sums[i] == sums[-1] - sums[i + 1]:
                return i
        return -1
```

## 日期

2018 年 2 月 3 日 
2018 年 11 月 22 日 —— 感恩节快乐~

  [1]: https://leetcode.com/problems/find-pivot-index/description/
