

作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)

题目地址：[https://leetcode.com/problems/degree-of-an-array/description/][1]


## 题目描述

Given a non-empty array of non-negative integers nums, the degree of this array is defined as the maximum frequency of any one of its elements.

Your task is to find the smallest possible length of a (contiguous) subarray of nums, that has the same degree as nums.

Example 1:

    Input: [1, 2, 2, 3, 1]
    Output: 2
    
    Explanation: 
    The input array has a degree of 2 because both elements 1 and 2 appear twice.
    Of the subarrays that have the same degree:
    [1, 2, 2, 3, 1], [1, 2, 2, 3], [2, 2, 3, 1], [1, 2, 2], [2, 2, 3], [2, 2]
    The shortest length is 2. So return 2.

Example 2:

    Input: [1,2,2,3,1,4,2]
    Output: 6

Note:

1. nums.length will be between 1 and 50,000.
1. nums[i] will be an integer between 0 and 49,999.

## 题目大意

数组的度是出现次数最多的数字的出现次数。求一个最短子数组的长度，其度等于数组的度。

## 解题方法

### 求出最短相同子数组度的长度

题目大意：

给定非空非负整数数组，数组的度是指元素的最大出现次数。

寻找最大连续区间，使得区间的度与原数组的度相同。

想法很粗暴，直接求出整个数组的degree，然后找出所有的度等于该degree的数，找出最小度的数。

```python
import collections
class Solution(object):
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == len(set(nums)):
            return 1
        counter = collections.Counter(nums)
        degree_num = counter.most_common(1)[0]
        most_numbers = [num for num in counter if counter[num] == degree_num[1]]
        scale = 100000000
        for most_number in most_numbers:
            appear = [i for i,num in enumerate(nums) if num == most_number]
            appear_scale = max(appear) - min(appear) + 1
            if appear_scale < scale:
                scale = appear_scale
        return scale
```

上面使用了Counter，下面的直接数，速度有一点提高。

```python
import collections
class Solution(object):
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums_set = set(nums)
        if len(nums) == len(nums_set):
            return 1
        degree = max([nums.count(num) for num in nums_set])
        most_numbers = [num for num in nums_set if nums.count(num) == degree]
        scale = 100000000
        for most_number in most_numbers:
            appear = [i for i,num in enumerate(nums) if num == most_number]
            appear_scale = max(appear) - min(appear) + 1
            if appear_scale < scale:
                scale = appear_scale
        return scale
```

上面的不够快是因为重复计算了多次的nums.count(num)，避免重复计算可以使用字典进行保存。这个方法超出了96.7%的提交。

```python
import collections
class Solution(object):
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums_set = set(nums)
        if len(nums) == len(nums_set):
            return 1
        num_dict = {num:nums.count(num) for num in nums_set}
        degree = max(num_dict.values())
        most_numbers = [num for num in nums_set if num_dict[num] == degree]
        scale = 100000000
        for most_number in most_numbers:
            appear = [i for i,num in enumerate(nums) if num == most_number]
            appear_scale = max(appear) - min(appear) + 1
            if appear_scale < scale:
                scale = appear_scale
        return scale
```

还能更快吗？可以。把能压缩的列表表达式拆开，这样迭代一次就可以了。最后用了个提前终止，如果``scale==degree``说明这段子列表里没有其他元素了，一定是最短的。

这个方法超过了99.91%的提交。

```python
import collections
class Solution(object):
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums_set = set(nums)
        if len(nums) == len(nums_set):
            return 1
        num_dict = {}
        degree = -1
        for num in nums_set:
            _count = nums.count(num)
            num_dict[num] = _count
            if _count > degree:
                degree = _count
        most_numbers = [num for num in nums_set if num_dict[num] == degree]
        scale = 100000000
        for most_number in most_numbers:
            _min = nums.index(most_number)
            for i in xrange(len(nums)-1, -1, -1):
                if nums[i] == most_number:
                    _max = i
                    break
            appear_scale = _max - _min + 1
            if appear_scale < scale:
                scale = appear_scale
            if scale == degree:
                break
        return scale
```

### 使用堆求最大次数和最小长度

二刷的时候，想到其实同时优化两个指标：最大次数和最小长度。所以，直接遍历所有的数字，同时统计它的次数，起始位置和结束位置，然后用一个堆，进行最大次数和最小长度的选择，对应的长度就是最小长度。

```python
class Solution:
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = collections.defaultdict(tuple)
        for i, num in enumerate(nums):
            if num not in count:
                count[num] = (1, i, i)
            else:
                count[num] = (count[num][0] + 1, count[num][1], i)
        heap = [(-times, end - start + 1) for times, start, end in count.values()]
        heapq.heapify(heap)
        return heapq.heappop(heap)[1]
```

### 保存最左边出现位置和最右边出现位置

使用两个字典，保存每个数字出现的最左边和最右边位置，这样的话，我们找到了出现次数等于数组的度的数字，然后看它的长度是不是最小的即可。

```python
class Solution:
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left, right = dict(), dict()
        count = collections.defaultdict(int)
        for i, num in enumerate(nums):
            if num not in left:
                left[num] = i
            right[num] = i
            count[num] += 1
        degree = max(count.values())
        res = float("inf")
        for num, c in count.items():
            if c == degree:
                res = min(res, right[num] - left[num] + 1)
        return res
```

## 日期

2018 年 1 月 23 日 
2018 年 11 月 16 日 —— 又到周五了！

  [1]: https://leetcode.com/problems/degree-of-an-array/description/
