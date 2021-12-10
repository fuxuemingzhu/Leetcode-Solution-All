
作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)

题目地址：[https://leetcode.com/problems/merge-sorted-array/description/][1]


## 题目描述


Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

Note:

1. The number of elements initialized in nums1 and nums2 are m and n respectively.
1. You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional elements from nums2.

Example:

	Input:
	nums1 = [1,2,3,0,0,0], m = 3
	nums2 = [2,5,6],       n = 3
	
	Output: [1,2,2,3,5,6]

## 题目大意

把两个有序的数组合并，把结果放到nums1中去。

## 解题方法

这个题的核心是注意到两个数组是已经有序的！这样就可以很简单的解决。

方法是在每个数组的最后一个指定位置判断大小，根据判定的大小放到nums1的最后位置里，然后移动指针，继续判断，直到一个数组先遍历结束。

注意，如果nums1已经遍历结束了，就要把nums2剩下的元素放到nums1的前面。最后可以确保有序。

另外，我以后可能就使用python刷题了，虽然语言大同小异，最主要的还是锻炼自己的语言基础。这个题中函数不用返回。

```python
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        while m > 0 and n > 0:
            if nums1[m - 1] > nums2[n -1]:
                nums1[m + n - 1] = nums1[m - 1]
                m -= 1
            else:
                nums1[m + n - 1] = nums2[n - 1]
                n -= 1
        nums1[:n] = nums2[:n]
```

二刷的版本：

```python
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        i, j = m - 1, n - 1
        k = m + n - 1
        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1
        while j >= 0:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1
```


### 新建数组

新建一个数组，保存结果，然后把排序了的结果放入到nums1中就好了。

```python
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        nums = [n1 for i, n1 in enumerate(nums1) if i < m] + [n2 for i, n2 in enumerate(nums2) if i < n]
        nums.sort()
        for i, num in enumerate(nums):
            nums1[i] = num
```



## 日期

2017 年 8 月 21 日 
2018 年 11 月 24 日 —— 周六快乐

  [1]: https://leetcode.com/problems/merge-sorted-array/description/
