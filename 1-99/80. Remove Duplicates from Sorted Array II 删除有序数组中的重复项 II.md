
作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)

题目地址：https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/description/

## 题目描述

Given a sorted array nums, remove the duplicates in-place such that duplicates appeared at most twice and return the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

Example 1:

    Given nums = [1,1,1,2,2,3],
    
    Your function should return length = 5, with the first five elements of nums being 1, 1, 2, 2 and 3 respectively.
    
    It doesn't matter what you leave beyond the returned length.

Example 2:

    Given nums = [0,0,1,1,1,1,2,3,3],
    
    Your function should return length = 7, with the first seven elements of nums being modified to 0, 0, 1, 1, 2, 3 and 3 respectively.
    
    It doesn't matter what values are set beyond the returned length.

Clarification:

Confused why the returned value is an integer but your answer is an array?

Note that the input array is passed in by reference, which means modification to the input array will be known to the caller as well.

Internally you can think of this:

    // nums is passed in by reference. (i.e., without making a copy)
    int len = removeDuplicates(nums);
    
    // any modification to nums in your function would be known by the caller.
    // using the length returned by your function, it prints the first len elements.
    for (int i = 0; i < len; i++) {
        print(nums[i]);
    }


## 题目大意

把有序数组中出现次数超过2的给过滤掉，原地操作。

## 解题方法

看到原地操作一般会想到指针，这个题目需要双指针。

刚开始想的双指针的操作方式是从两头向中间遍历，这样一想，发现后面的数字会被交换到前面去，这样就没法判断后面的数字出现的次数了。

注意到题目是有序的，这个题正确的做法是从前面开始，一个快指针对所有的数字进行遍历，另外一个慢指针指向了不满足题目要求的第一个位置。这样当遍历到一个新的数字而且这个新的数字和慢指针指向的前两个数字相同时，把它交换到这个不满足的位置，然后两个指针同时右移即可。

时间复杂度是O(N)，空间复杂度是O(1).

代码如下：

```python
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        for n in nums:
            if i < 2 or n != nums[i - 2]:
                nums[i] = n
                i += 1
        return i
```

----

二刷，使用了更明显的双指针，left指针指向第一个要判断的位置，right指针指向后面的位置。判断right和left是否相等，直到right和left不等的时候，把后面的这个数字移到前面来即可。

```python
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        N = len(nums)
        if N <= 1: return N
        left, right = 0, 1
        while right < N:
            while right < N and nums[right] == nums[left]:
                right += 1
            left += 1
            if right < N:
                nums[left] = nums[right]
        return left
```

参考资料：

https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/discuss/27976/3-6-easy-lines-C++-Java-Python-Ruby

## 日期

2018 年 9 月 24 日 —— 祝大家中秋节快乐
2018 年 11 月 23 日 —— 这就星期五了？？
