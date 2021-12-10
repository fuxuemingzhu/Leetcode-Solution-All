# 【LeetCode】162. Find Peak Element 解题报告（Python）

标签（空格分隔）： LeetCode

---

题目地址：https://leetcode.com/problems/find-peak-element/description/

## 题目描述：

A peak element is an element that is greater than its neighbors.

Given an input array where num[i] ≠ num[i+1], find a peak element and return its index.

The array may contain multiple peaks, in that case return the index to any one of the peaks is fine.

You may imagine that num[-1] = num[n] = -∞.

For example, in array [1, 2, 3, 1], 3 is a peak element and your function should return the index number 2.

click to show spoilers.

Note:
Your solution should be in logarithmic complexity.

Credits:
Special thanks to @ts for adding this problem and creating all test cases.


    
## 题目大意

找到数组中的一个山峰节点位置，返回这个节点的位置。


## 解题方法

用两个mid，判断上坡还是下坡～二叉搜索，在这种题目中很常用～～

代码：

```python
class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left, right = 0, len(nums) - 1
        while left < right:
            mid1 = (left + right) / 2
            mid2 = mid1 + 1
            if nums[mid1] < nums[mid2]:
                left = mid2
            else:
                right = mid1
        return left
```

## 日期

2018 年 3 月 20 日 ————阳光明媚～


  [1]: http://blog.csdn.net/fuxuemingzhu/article/details/51291406