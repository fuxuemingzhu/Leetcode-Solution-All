- 作者：    负雪明烛
- id：      fuxuemingzhu
- 个人博客：[http://fuxuemingzhu.cn/](http://fuxuemingzhu.cn/)

---
@[TOC](目录)


题目地址：https://leetcode-cn.com/problems/maximum-distance-in-arrays/

## 题目描述

Given m arrays, and each array is sorted in ascending order. Now you can pick up two integers from two different arrays (each array picks one) and calculate the distance. We define the distance between two integers `a` and `b` to be their absolute difference `|a-b|`. Your task is to find the maximum distance.

Example 1:

    Input: 
    [[1,2,3],
     [4,5],
     [1,2,3]]
    Output: 4
    Explanation: 
    One way to reach the maximum distance 4 is to pick 1 in the first or third array and pick 5 in the second array.

Note:

1. Each given array will have at least 1 number. There will be at least two non-empty arrays.
1. The total number of the integers in all the m arrays will be in the range of [2, 10000].
1. The integers in the m arrays will be in the range of [-10000, 10000].


## 题目大意

给定 m 个数组，每个数组都已经按照升序排好序了。现在你需要从两个不同的数组中选择两个整数（每个数组选一个）并且计算它们的距离。两个整数 a 和 b 之间的距离定义为它们差的绝对值 |a-b| 。你的任务就是去找到最大距离

## 解题方法

### 大根堆+小根堆

由于数组都是已经排好序的，因此要想使绝对值差最大，只能是所有数组中的最大的最后一个数字的和所有数组中最小的第一个数字之差。要注意题目要求，当两者属于同一个数组时，需要使用次大值和次小值。

找出最大最小、次大次小的方法可以使用堆，具体而言是用大根堆小根堆分别保存最大终点和最小起点，每个堆同时保存值和数组编号。先判断最大最小是否是同一数组，如果不是同一数组，那么直接返回；如果是同一数组，那么从堆中找出次大和次小，此时的绝对值差会是`max(最大-次小，次大-最小)`。

C++代码如下：

```cpp
class Solution {
public:
    int maxDistance(vector<vector<int>>& arrays) {
        priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> mins;
        priority_queue<pair<int, int>> maxs;
        for (int i = 0; i < arrays.size(); ++i) {
            auto arr = arrays[i];
            mins.push({arr[0], i});
            maxs.push({arr[arr.size() - 1], i});
        }
        int res = INT_MIN;
        auto min_first = mins.top(); mins.pop();
        auto max_first = maxs.top(); maxs.pop();
        if (min_first.second != max_first.second) {
            return max_first.first - min_first.first;
        } 
        auto min_second = mins.top();
        auto max_second = maxs.top();
        return max(max_second.first - min_first.first, max_first.first - min_second.first);
    }
};
```

### 保存已有的最大最小

一种更简单的方法是，使用两个变量分别保存已经见到的最大curMax/最小curMin，对每个数组遍历的过程中，全局最大绝对值之差等于`max(当前数组的最大值-curMin, curMax-当前数组的最小值`。

C++代码如下：

```cpp
class Solution {
public:
    int maxDistance(vector<vector<int>>& arrays) {
        const int N = arrays.size();
        int curMin =  10010;
        int curMax = -10010;
        int res = 0;
        for (auto& arr : arrays) {
            res = max(res, (arr[arr.size() - 1] - curMin));
            res = max(res, (curMax - arr[0]));
            curMin = min(curMin, arr[0]);
            curMax = max(curMax, arr[arr.size() - 1]);
        }
        return res;
    }
};
```

## 日期

2019 年 9 月 19 日 —— 举杯邀明月，对影成三人


  [1]: https://blog.csdn.net/fuxuemingzhu/article/details/100977773
