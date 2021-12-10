
作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)

题目地址：[https://leetcode.com/problems/contains-duplicate-ii/description/][1]


## 题目描述

Given an array of integers and an integer k, find out whether there are two distinct indices ``i`` and ``j`` in the array such that ``nums[i] = nums[j]`` and the absolute difference between ``i`` and ``j`` is at most ``k``.

Example 1:

	Input: nums = [1,2,3,1], k = 3
	Output: true

Example 2:

	Input: nums = [1,0,1,1], k = 1
	Output: true

Example 3:

	Input: nums = [1,2,3,1,2,3], k = 2
	Output: false

## 题目大意

在一个数组中是否存在两个数字相等，并且他们的间距最多为k.

## 解题方法

### 使用set

想法是用一个set来保存已经出现过的数据，然后只用遍历一次数组，把每个数放到set里，因为步长最多是k，所以，如果i超过k就删除最早放到set里的元素。set添加元素的时候，如果已经包含了该元素，那么add方法会返回false.

```java
class Solution {
    public boolean containsNearbyDuplicate(int[] nums, int k) {
        Set<Integer> set = new HashSet<Integer>();
        for(int i = 0; i < nums.length; i++){
            if(i > k) set.remove(nums[i - k - 1]);
            if(!set.add(nums[i])) return true;
        }
        return false;
    }
}
```

### 使用字典

更通用的方法是使用一个字典，保存每个数字出现的位置，如果在K以内，说明满足要求的，否则就更新这个位置。

```python
class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        d = dict()
        for i, num in enumerate(nums):
            if num in d:
                if i - d[num] <= k:
                    return True
            d[num] = i
        return False
```


## 日期

2017 年 8 月 18 日 
2018 年 11 月 24 日 —— 周六快乐

  [1]: https://leetcode.com/problems/contains-duplicate-ii/description/
