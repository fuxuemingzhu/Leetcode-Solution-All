
作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)

[LeetCode]

题目地址：[https://leetcode.com/problems/contains-duplicate/](https://leetcode.com/problems/contains-duplicate/)

Total Accepted: 86528 Total Submissions: 209877 Difficulty: Easy

## 题目描述

Given an array of integers, find if the array contains any duplicates.

Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.

Example 1:

	Input: [1,2,3,1]
	Output: true

Example 2:

	Input: [1,2,3,4]
	Output: false

Example 3:

	Input: [1,1,1,3,3,4,3,2,4,2]
	Output: true

## 题目大意

判断是否有重复元素.

## 解题方法

这个题想到了五种解法。

方法一，两个for循环排序，肯定效率低。

方法二，用ArrayList，判断在已经添加的元素中是否要插入的这个元素。事实证明这个方法超时。

方法三，用HashMap，统计词频最高的是不是1。

方法四，用HashSet判断set之后长度是否变短。

方法五，排序，看排序之后相邻的元素是不是有相等。

### 字典统计词频

使用HashMap：

```java
public class Solution {
    public boolean containsDuplicate(int[] nums) {
        HashMap map = new HashMap();
        for (int i = 0; i < nums.length; i++) {
            if (map.containsKey(nums[i])) {
                return true;
            } else {
                map.put(nums[i], nums[i]);
            }
        }
        return false;
    }
}
```
AC:17ms

python版本：

```python
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if not nums: return False
        count = collections.Counter(nums)
        return count.most_common(1)[0][1] > 1
```

### 使用set

使用HashSet:

```java
public class Solution {
    public boolean containsDuplicate(int[] nums) {
        Set<Integer> set=new HashSet();
        for (int i = 0; i < nums.length; i++) {
            if (set.contains(nums[i])) {
                return true;
            } else {
                set.add(nums[i]);
            }
        }
        return false;
    }
}
```
AC:16ms

查阅资料，此处应该使用HashSet，因为HashMap存储时是对键值对进行存储，如果用一个无穷，不重复的数组进行判断，复杂度与时间消耗是很多的。
而HashSet的好处在于：HashSet实现了Set接口，它不允许集合中有重复的值，在进行存储时，先进行判断，使用contain方法即可，复杂度与时间消耗就随之降下来了。

python版本：

```python
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        return len(nums) != len(set(nums))
```

### 排序

排序判断相邻的元素是否相等，即可知道是否有重复了。

```python
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if not nums: return False
        nums.sort()
        return any(nums[x] - nums[x + 1] == 0 for x in xrange(len(nums) - 1))
```

## 日期

2016/5/1 10:55:17 
2018 年 11 月 13 日 —— 时间有点快
