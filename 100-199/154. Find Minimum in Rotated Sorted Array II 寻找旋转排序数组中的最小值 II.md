# 【LeetCode】154. Find Minimum in Rotated Sorted Array II 解题报告（Python）

标签： LeetCode

---

题目地址：https://leetcode.com/problems/find-minimum-in-rotated-sorted-array-ii/description/

## 题目描述：

    Follow up for "Find Minimum in Rotated Sorted Array":
    What if duplicates are allowed?
    
    Would this affect the run-time complexity? How and why?

Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

Find the minimum element.

The array may contain duplicates.


## 题目大意

找出可能含有重复数字的旋转有序数组中的最小值。

## 解题方法

这个题就是剑指offer中的原题。可以看我之前的博客http://blog.csdn.net/fuxuemingzhu/article/details/79501202。

思想就是如果出现了重复数字，那么二分查找就没有作用了，必须使用顺序查找了。

```python
class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        p1, p2 = 0, len(nums) - 1
        mid = p1
        while nums[p1] >= nums[p2]:
            if p2 - p1 == 1:
                mid = p2
                break
            mid = (p1 + p2) / 2
            if nums[mid] == nums[p1] and nums[mid] == nums[p2]:
                return self.minInOrder(nums, p1, p2)
            if nums[mid] >= nums[p1]:
                p1 = mid
            elif nums[mid] <= nums[p2]:
                p2 = mid
        return nums[mid]
    
    def minInOrder(self, nums, index1, index2):
        n1 = nums[index1]
        for i in range(index1 + 1, index2):
            if n1 > nums[i]:
                return nums[i]
        return n1
```

## 日期

2018 年 3 月 13 日 