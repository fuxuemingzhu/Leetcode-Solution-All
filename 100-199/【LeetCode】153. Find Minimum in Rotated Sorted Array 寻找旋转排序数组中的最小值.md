# 【LeetCode】153. Find Minimum in Rotated Sorted Array 解题报告（Python）

标签： LeetCode

---

题目地址：https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/

## 题目描述：

Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

Find the minimum element.

You may assume no duplicate exists in the array.


## 题目大意

找出旋转有序数组中的最小值。

## 解题方法

这个题是剑指offer上的原题，这里在复习一下。看到有序的数组就想到二分查找。这个是变种而已。

注意边界和循环条件。

![这里写图片描述](http://img.blog.csdn.net/20180312214100966?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvZnV4dWVtaW5nemh1/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)

```python
class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1: return nums[0]
        left, right = 0, len(nums) - 1
        mid = left
        while nums[left] >= nums[right]:
            if left + 1 == right:
                mid = right
                break
            mid = (left + right) / 2
            if nums[mid] >= nums[left]:
                left = mid
            elif nums[mid] <= nums[right]:
                right = mid
        return nums[mid]
```

## 日期

2018 年 3 月 12 日 