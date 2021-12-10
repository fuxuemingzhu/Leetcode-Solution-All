作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)


题目地址：https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/description/

## 题目描述

Given an array of integers ``nums`` sorted in ascending order, find the starting and ending position of a given ``target`` value.

Your algorithm's runtime complexity must be in the order of **O(log n)**.

If the target is not found in the array, return ``[-1, -1]``.

Example 1:

    Input: nums = [5,7,7,8,8,10], target = 8
    Output: [3,4]

Example 2:

    Input: nums = [5,7,7,8,8,10], target = 6
    Output: [-1,-1]


## 题目大意

在一个数组中，找出某个target值开始的最左边和最右边的索引，如果target不存在，那么就返回[-1, -1]。

## 解题方法

### 二分查找

本来见到这个题，第一感觉肯定就是二分查找左右区间，并且题目很明显的说了O(logn)的时间复杂度，那么明显就是要求使用二分。

题目要求找到开始的索引和结束索引，所以就是C++的lower_bound和upper_bound。代码我觉得应该是要背下来的，这两个函数只有一点不同，就是nums[mid]与target的判断，lower_bound倾向于找左边的元素，所以只有nums[mid] < target时才移动左指针；而upper_bound倾向于找右边的元素，所以当nums[mid] <= target就向右移动左指针了。

lower_bound返回的是开始的第一个满足条件的位置，而upper_bound返回的是第一个不满足条件的位置。所以，当两个相等的时候代表没有找到，如果找到了的话，需要返回的是[left, right - 1].

时间复杂度是O(logn)，空间复杂度是O(1).超过了100%的提交。

```python
class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        left = self.lowwer_bound(nums, target)
        right = self.higher_bound(nums, target)
        if left == right:
            return [-1, -1]
        return [left, right - 1]
    
    def lowwer_bound(self, nums, target):
        # find in range [left, right)
        left, right = 0, len(nums)
        while left < right:
            mid = left + (right - left) / 2
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid
        return left
    
    def higher_bound(self, nums, target):
        # find in range [left, right)
        left, right = 0, len(nums)
        while left < right:
            mid = left + (right - left) / 2
            if nums[mid] <= target:
                left = mid + 1
            else:
                right = mid
        return left
```

其实，在python中有封装好的二分查找模块，就是bisect模块。我第一个提交就是使用这个模块快速写出来提交的，如果是比赛的话尽量用别人封装好的。

时间复杂度是O(logn)，空间复杂度是O(1).超过了100%的提交。

```python
class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        left = bisect.bisect_left(nums, target)
        right = bisect.bisect_right(nums, target)
        if left == right:
            return [-1, -1]
        return [left, right - 1]
```

C++代码自己手写lower_bound和upper_bound函数如下：

```cpp
class Solution {
public:
    vector<int> searchRange(vector<int>& nums, int target) {
        int low = lower_bound(nums, target);
        int high = upper_bound(nums, target);
        if (low == high) 
            return {-1, -1};
        else
            return {low, high - 1};
    }
    int lower_bound(vector<int>& nums, int target) {
        const int N = nums.size();
        // [l, r)
        int l = 0, r = N;
        while (l < r) {
            int mid = l + (r - l) / 2;
            if (nums[mid] >= target) {
                r = mid;
            } else  {
                l = mid + 1;
            }
        }
        return l;
    }
    int upper_bound(vector<int>& nums, int target) {
        const int N = nums.size();
        // [l, r)
        int l = 0, r = N;
        while (l < r) {
            int mid = l + (r - l) / 2;
            if (nums[mid] <= target) {
                l = mid + 1;
            } else {
                r = mid;
            }
        }
        return l;
    }
};
```


C++代码使用lower_bound()和upper_bound()函数的代码如下：

```cpp
class Solution {
public:
    vector<int> searchRange(vector<int>& nums, int target) {
        auto low = lower_bound(nums.begin(), nums.end(), target);
        auto high = upper_bound(nums.begin(), nums.end(), target);
        if (low == high) return {-1, -1};
        return {low - nums.begin(), high - nums.begin() - 1};
    }
};
```

## 日期

2018 年 10 月 21 日 —— 新的一周又开始了
2019 年 1 月 11 日 —— 小光棍节？
