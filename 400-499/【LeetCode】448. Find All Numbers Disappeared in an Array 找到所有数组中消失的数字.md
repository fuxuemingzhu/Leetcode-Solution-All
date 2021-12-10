
作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)

[LeetCode]

题目地址：[https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/][1]

 - Total Accepted: 14302
 - Total Submissions: 24993
 - Difficulty: Easy

## 题目描述

Given an array of integers where ``1 ≤ a[i] ≤ n`` (n = size of array), some elements appear twice and others appear once.

Find all the elements of ``[1, n]`` inclusive that do not appear in this array.

Could you do it without extra space and in ``O(n) ``runtime? You may assume the returned list does not count as extra space.

Example:

	Input: [4,3,2,7,8,2,3,1]
	
	Output: [5,6]

## 题目大意

### 方法一：暴力求解

刚开始没想到很有效的方法，只能用暴力解决。但这个方法不符合题目没有额外空间的要求。


```python
class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        cList = list(range(1, len(nums) + 1))
    	returnList = []
    	for x in nums:
    		cList[x - 1] = 0
    	for x in cList:
    		if x != 0:
    			returnList.append(x)
    	return returnList
```

AC:359 ms

### 方法二：原地变负做标记

参考了别人的，我学会了一种方法：原地变负来标记。比如对于[4, 3, 2, 7, 8, 2, 3, 1]，把这些元素作为list的索引，指向的元素变换成负数，那么，没有变换成负数的位置就是没有人指向它，故这个位置对应的下标没有出现。

```python
class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        for i in range(len(nums)):
            index=abs(nums[i])-1
            nums[index]= - abs(nums[index])
    	return [i+1 for i in range(len(nums)) if nums[i] > 0]
```
AC:362 ms

这个速度仍然不理想。

### 方法三：使用set

已经告诉我们缺少了部分数字，那么我们可以先用set进行去重。然后再次遍历1~N各个数字，然后找出没有在set中出现的数字即可。

Python代码如下，打败96%.

```python
class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []
        numset = set(nums)
        N = len(nums)
        for num in range(1, N + 1):
            if num not in numset:
                res.append(num)
        return res
```

## 日期

2017 年 1 月 2 日 
2018 年 11 月 10 日 —— 这么快就到双十一了？？

  [1]: https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/
