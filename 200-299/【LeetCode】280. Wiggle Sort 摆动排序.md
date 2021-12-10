

- 作者：    负雪明烛
- id：      fuxuemingzhu
- 个人博客：[http://fuxuemingzhu.cn/](http://fuxuemingzhu.cn/)

---
@[TOC](目录)

题目地址：https://leetcode-cn.com/problems/wiggle-sort/

## 题目描述

Given an unsorted array nums, reorder it in-place such that `nums[0] <= nums[1] >= nums[2] <= nums[3]....`

Example:

    Input: nums = [3,5,2,1,6,4]
    Output: One possible answer is [3,5,1,6,2,4]


## 题目大意

给你一个无序的数组 nums, 将该数字 原地 重排后使得 `nums[0] <= nums[1] >= nums[2] <= nums[3]...`。

## 解题方法

### 排序后交换相邻元素

只要给出一种符合要求的结果即可，因此我们可以找出一种最简单易实现的方案就行。

先把所有的数字排序，然后交换相邻的元素就可以实现这种波浪形的数组。举例如下：

    输入：[3,5,2,1,6,4]
    排序：[1,2,3,4,5,6]
    交换：[1,3,2,5,4,6]

C++代码如下：

```cpp
class Solution {
public:
    void wiggleSort(vector<int>& nums) {
        const int N = nums.size();
        sort(nums.begin(), nums.end());
        for (int i = 1; i < N - 1; i += 2) {
            swap(nums[i], nums[i + 1]);
        }
    }
};
```

## 日期

2019 年 9 月 22 日 —— 熬夜废掉半条命


  [1]: https://assets.leetcode.com/uploads/2018/10/12/candy_crush_example_2.png
  [2]: https://blog.csdn.net/fuxuemingzhu/article/details/101068011
