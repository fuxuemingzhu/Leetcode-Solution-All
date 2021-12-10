- 作者：    负雪明烛
- id：      fuxuemingzhu
- 个人博客：[http://fuxuemingzhu.cn/](http://fuxuemingzhu.cn/)

---
@[TOC](目录)

题目地址：https://leetcode-cn.com/problems/search-in-a-sorted-array-of-unknown-size/

## 题目描述

Given an integer array sorted in ascending order, write a function to search target in nums.  If target exists, then return its index, otherwise return -1. However, the array size is unknown to you. You may only access the array using an ArrayReader interface, where ArrayReader.get(k) returns the element of the array at index k (0-indexed).

You may assume all integers in the array are less than 10000, and if you access the array out of bounds, ArrayReader.get will return 2147483647.

Example 1:

    Input: array = [-1,0,3,5,9,12], target = 9
    Output: 4
    Explanation: 9 exists in nums and its index is 4

Example 2:

    Input: array = [-1,0,3,5,9,12], target = 2
    Output: -1
    Explanation: 2 does not exist in nums so return -1

Note:

1. You may assume that all elements in the array are unique.
1. The value of each element in the array will be in the range [-9999, 9999].

## 题目大意

给定一个升序整数数组，写一个函数搜索 nums 中数字 target。如果 target 存在，返回它的下标，否则返回 -1。注意，这个数组的大小是未知的。你只可以通过 ArrayReader 接口访问这个数组，ArrayReader.get(k) 返回数组中第 k 个元素（下标从 0 开始）。

你可以认为数组中所有的整数都小于 10000。如果你访问数组越界，ArrayReader.get 会返回 2147483647。

## 解题方法

### 遍历

直接可以线性遍历，如果ArrayReader不结束，那么一直向后查找，忽略掉题目给出的数组是有序的特征。

这样时间复杂度是O(N)，事实证明题目给出的ArrayReader长度不长，下面的做法超过了96%的提交。

C++代码如下：

```cpp
// Forward declaration of ArrayReader class.
class ArrayReader;

class Solution {
public:
    int search(const ArrayReader& reader, int target) {
        int index = 0;
        while (reader.get(index) != 2147483647) {
            if (reader.get(index) == target)
                return index;
            index ++;
        }
        return -1;
    }
};
```

### 二分查找

既然题目说了数组是有序的，就是提示我们用二分查找。因为数组是递增且不同的，所以总的元素个数应该小于20000.

然后使用标准的二分模板写一遍就好了，注意这个区间是左开右闭。

这个时间复杂度是O(log(N))，但是提交后发现运行时间反而变慢，超过了39%的用户。

C++代码如下：

```cpp
// Forward declaration of ArrayReader class.
class ArrayReader;

class Solution {
public:
    int search(const ArrayReader& reader, int target) {
        int left = 0;
        int right = 20010;
        // [left, right)
        while (left < right) {
            int mid = left + (right - left) / 2;
            int val = reader.get(mid);
            if (val == target) {
                return mid;
            } else if (val < target) {
                left = mid + 1;
            } else {
                right = mid;
            }
        }
        return -1;
    }
};
```

## 日期

2019 年 9 月 24 日 —— 梦见回到了小学，小学已经芳草萋萋破败不堪


  [1]: https://ss0.bdstatic.com/70cFvHSh_Q1YnxGkpoWK1HF6hhy/it/u=3958884440,3883801982&fm=26&gp=0.jpg
