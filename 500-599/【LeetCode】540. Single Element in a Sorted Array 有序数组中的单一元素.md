
作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)

题目地址：https://leetcode.com/problems/single-element-in-a-sorted-array/description/

## 题目描述

Given a sorted array consisting of only integers where every element appears twice except for one element which appears once. Find this single element that appears only once.

Example 1:

    Input: [1,1,2,3,3,4,4,8,8]
    Output: 2

Example 2:

    Input: [3,3,7,7,10,11,11]
    Output: 10

## 解题方法

### 方法一：异或

一个数组中，每个数字都出现了两次，只有一个数字出现了一次，求出现一次的数字。这样的题目使用异或操作遍历一遍即可。原理是：

1. 相同元素的异或操作是0;
2. 0与任何元素的异或操作结果是该数字；
3. 异或操作具有交换律和结合律。

```python
class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return reduce(lambda x, y: x^y, nums)
```

C++代码如下：

```cpp
class Solution {
public:
    int singleNonDuplicate(vector<int>& nums) {
        int res = 0;
        for (int a : nums) res ^= a;
        return res;
    }
};
```

### 方法二：判断相邻元素是否相等

这个方法应该比上面的方法好想一点。题目中已经说了是有序的数组，那么相等的元素必相邻，找到第一个和后面元素不等的数字即为所求。为了防止数组越界，只遍历到len(nums)-1处，如果遍历结束没有找到，则为最后一个元素。

```python
class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in range(0, len(nums) - 1, 2):
            if nums[i] != nums[i + 1]:
                return nums[i]
        return nums[-1]
```

C++代码如下：

```cpp
class Solution {
public:
    int singleNonDuplicate(vector<int>& nums) {
        int pos = 0;
        const int N = nums.size();
        while (pos < N) {
            if (nums[pos] != nums[pos + 1])
                return nums[pos];
            pos += 2;
        }
        return nums[N - 1];
    }
};
```

### 方法三：二分查找

这个二分查找的思路很奇特。如果i是个偶数，如果``nums[i] == nums[i + 1]``，那么，说明那个单独出现的元素在i的右边；如果``nums[i] != nums[i + 1]``，那么说明单独出现的元素在i的左边。所以这个题其实考的lower_bound的写法。

Python的写法如下：

```python
class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        N = len(nums)
        left, right = 0, N - 1 #[left, right]
        while (left < right):
            mid = left + (right - left) / 2
            if mid % 2 == 1: mid -= 1
            if nums[mid] != nums[mid + 1]:
                right = mid
            else:
                left = mid + 2
        return nums[left]
```

C++代码如下：

```cpp
class Solution {
public:
    int singleNonDuplicate(vector<int>& nums) {
        const int N = nums.size();
        int left = 0, right = N - 1;
        while (left < right) {
            int mid = (right - left) / 2 + left;
            if (mid % 2 == 1) mid--;
            if (nums[mid] != nums[mid + 1])
                right = mid;
            else
                left = mid + 2;
        }
        return nums[left];
    }
};
```

## 日期

2018 年 2 月 6 日 
2018 年 12 月 7 日 —— 恩，12月又过去一周了
