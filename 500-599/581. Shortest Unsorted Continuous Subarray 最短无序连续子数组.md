
作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)

题目地址：https://leetcode.com/problems/shortest-unsorted-continuous-subarray/description/


## 题目描述

Given an integer array, you need to find one continuous subarray that if you only sort this subarray in ascending order, then the whole array will be sorted in ascending order, too.

You need to find the shortest such subarray and output its length.

Example 1:

    Input: [2, 6, 4, 8, 10, 9, 15]
    Output: 5
    Explanation: You need to sort [6, 4, 8, 10, 9] in ascending order to make the whole array sorted in ascending order.

Note:

1. Then length of the input array is in range [1, 10,000].
1. The input array may contain duplicates, so ascending order here means <=.

## 解题方法

### 方法一：排序比较

这个题竟然真的是排序之后，然后和原来的数组进行比较得到的。

因为题目中的数组的长度最大只有1000，所以排序的时间不算很高。排序后的数组和之前的数组进行比较，找出最小的不相等的数字位置和最大不相等的数字的位置，两者的差相减+1即为所求。

```python
class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        _len, _nums = len(nums), sorted(nums)
        if nums == _nums:
            return 0
        l = min([i for i in range(_len) if nums[i] != _nums[i]])
        r = max([i for i in range(_len) if nums[i] != _nums[i]])
        return r - l + 1
```

二刷用到C++，代码如下：

```cpp
class Solution {
public:
    int findUnsortedSubarray(vector<int>& nums) {
        const int N = nums.size();
        auto t = nums;
        sort(t.begin(), t.end());
        int l = N, r = 0;
        for (int i = 0; i < N; ++i) {
            if (t[i] != nums[i]) {
                l = min(l, i);
                r = max(r, i);
            }
        }
        return r >= l ? r - l + 1 : 0;
    }
};
```

## 日期

2018 年 2 月 4 日 
2018 年 11 月 27 日 —— 最近的雾霾太可怕
