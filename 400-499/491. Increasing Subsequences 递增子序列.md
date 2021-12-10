
作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)

题目地址：https://leetcode.com/problems/increasing-subsequences/description/

## 题目描述

Given an integer array, your task is to find all the different possible increasing subsequences of the given array, and the length of an increasing subsequence should be at least 2 .

    Example:
    Input: [4, 6, 7, 7]
    Output: [[4, 6], [4, 7], [4, 6, 7], [4, 6, 7, 7], [6, 7], [6, 7, 7], [7,7], [4,7,7]]

Note:

1. The length of the given array will not exceed 15.
1. The range of integer in the given array is [-100,100].
1. The given array may contain duplicates, and two equal integers should also be considered as a special case of increasing sequence.


## 题目大意

找出一个数组中所有的递增的序列。

## 解题方法

我先写了dfs的做法，数组规模不超过15，那么O(N!)的时间复杂度能接受的。

dfs做法：

```python
class Solution(object):
    def findSubsequences(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = set()
        self.dfs(nums, 0, res, [])
        return map(list, res)
    
    def dfs(self, nums, index, res, path):
        if len(path) >= 2:
            res.add(tuple(path))
        for i in range(index, len(nums)):
            if not path or nums[i] >= path[-1]:
                self.dfs(nums, i + 1, res, path + [nums[i]])
```

下面是动态规划的代码，使用了一个set来保证不会有重复，然后由于set之中只能放不可变的对象，所以放进去的是元组对象。当我们遍历到nums的每个数字的时候，对set中的所有的元素进行遍历，看每个tuple元素的最后一个数字是否是小于等于当前的num的，如果是的话就把当前的元素添加到原来的tuple的后面。这样的循环虽说稍显复杂，但是竟然也能通过了。。

代码：

```python
class Solution(object):
    def findSubsequences(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        dp = set()
        for n in nums:
            for y in list(dp):
                if n >= y[-1]:
                    dp.add(y + (n,))
            dp.add((n,))
        return list(e for e in dp if len(e) > 1)
```

## 日期

2018 年 4 月 5 日 —— 清明节假期开始，小长假真好～～


  [1]: https://blog.csdn.net/fuxuemingzhu/article/details/79821305
