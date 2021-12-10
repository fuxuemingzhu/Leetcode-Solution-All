
作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)

题目地址：https://leetcode.com/problems/find-all-duplicates-in-an-array/description/

## 题目描述

Given an array of integers, 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

Find all the elements that appear twice in this array.

Could you do it without extra space and in O(n) runtime?

    Example:
    Input:
    [4,3,2,7,8,2,3,1]
    
    Output:
    [2,3]

## 题目大意

在一个数组中，有些数字出现了两次，有些数字出现一次。找出出现两次的所有数字。

## 解题方法

### 字典

使用字典统计出现次数。

```cpp
class Solution {
public:
    vector<int> findDuplicates(vector<int>& nums) {
        map<int, int> count;
        for (int num : nums) {
            count[num] ++;
        }
        vector<int> res;
        for (auto c : count) {
            if (c.second == 2)
                res.push_back(c.first);
        }
        return res;
    }
};
```

### 原地变负

这个题的难点在于O(n)的时间复杂度和不用额外空间。下面的做法我是按照Discuss做的，使用了题目给的一个trick,``1 ≤ a[i] ≤ n``，这样使用a[i]-1把数组中该位置的元素求反，当再次遇到该位置时能够通过这个位置是负数来确定出现了两次。因为可能会对还没有扫描到的位置进行求反，所以当扫描到该位置的时候应该进行求绝对值操作。


```python
class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = []
        for num in nums:
            if nums[abs(num) - 1] < 0:
                ans.append(abs(num))
            nums[abs(num) - 1] *= - 1
        return ans
```

C++代码如下：

```cpp
class Solution {
public:
    vector<int> findDuplicates(vector<int>& nums) {
        const int N = nums.size();
        vector<int> res;
        for (int i = 0; i < N; i++) {
            if (nums[abs(nums[i]) - 1] < 0)
                res.push_back(abs(nums[i]));
            nums[abs(nums[i]) - 1] *= -1;
        }
        return res;
    }
};
```


## 日期

2018 年 2 月 6 日 
2018 年 12 月 5 日 —— 周三啦！
