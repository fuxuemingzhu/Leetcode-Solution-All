

- 作者：    负雪明烛
- id：      fuxuemingzhu
- 个人博客：[http://fuxuemingzhu.cn/](http://fuxuemingzhu.cn/)

---
@[TOC](目录)


题目地址：https://leetcode-cn.com/problems/check-if-a-number-is-majority-element-in-a-sorted-array/

## 题目描述

Given an array nums sorted in non-decreasing order, and a number target, return True if and only if target is a majority element.

A majority element is an element that appears more than `N/2` times in an array of length `N`.


Example 1:

    Input: nums = [2,4,5,5,5,5,5,6,6], target = 5
    Output: true
    Explanation: 
    The value 5 appears 5 times and the length of the array is 9.
    Thus, 5 is a majority element because 5 > 9/2 is true.

Example 2:

    Input: nums = [10,100,101,101], target = 101
    Output: false
    Explanation: 
    The value 101 appears 2 times and the length of the array is 4.
    Thus, 101 is not a majority element because 2 > 4/2 is false.

Note:

1. `1 <= nums.length <= 1000`
1. `1 <= nums[i] <= 10^9`
1. `1 <= target <= 10^9`


## 题目大意

给出一个按 非递减 顺序排列的数组 nums，和一个目标数值 target。假如数组 nums 中绝大多数元素的数值都等于 target，则返回 True，否则请返回 False。

所谓占绝大多数，是指在长度为 N 的数组中出现必须 超过 N/2 次。


## 解题方法

### 字典

字典统计出每个数字出现的次数，然后看target的次数是否出现超过了N/2次。

C++代码如下：

```cpp
class Solution {
public:
    bool isMajorityElement(vector<int>& nums, int target) {
        unordered_map<int, int> count;
        for (int num : nums) {
            count[num]++;
        }
        return count[target] > nums.size() / 2;
    }
};
```

### 二分查找

题目告诉了数组是单调非减的，所以使用二分查找，分别找到target在数组中的起始位置和结束位置，找出两者的差就是target出现的次数。

1. lower_bound(val):返回容器中第一个值【大于或等于】val的元素的iterator位置。
1. upper_bound(val): 返回容器中第一个值【大于】

一要注意两个函数返回的是迭代器，二要注意target可能不存在。

C++代码如下：

```cpp
class Solution {
public:
    bool isMajorityElement(vector<int>& nums, int target) {
        int left = lower_bound(nums.begin(), nums.end(), target) - nums.begin();
        int right = upper_bound(nums.begin(), nums.end(), target) - nums.begin();
        if (left >= nums.size() || nums[left] != target) return false;
        return right - left > nums.size() / 2;
    }
};
```

## 日期

2019 年 9 月 18 日 —— 今日又是九一八
