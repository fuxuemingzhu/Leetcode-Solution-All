
- 作者：    负雪明烛
- id：      fuxuemingzhu
- 个人博客：[http://fuxuemingzhu.cn/](http://fuxuemingzhu.cn/)

---
@[TOC](目录)


题目地址：https://leetcode-cn.com/problems/two-sum-less-than-k/

## 题目描述

Given an array `A` of integers and integer `K`, return the maximum `S` such that there exists `i < j` with `A[i] + A[j] = S` and `S < K`. If no `i, j` exist satisfying this equation, return -1.


Example 1:

    Input: A = [34,23,1,24,75,33,54,8], K = 60
    Output: 58
    Explanation: 
    We can use 34 and 24 to sum 58 which is less than 60.

Example 2:

    Input: A = [10,20,30], K = 15
    Output: -1
    Explanation: 
    In this case it's not possible to get a pair sum less that 15.

Note:

1. `1 <= A.length <= 100`
1. `1 <= A[i] <= 1000`
1. `1 <= K <= 2000`

## 题目大意

给你一个整数数组 A 和一个整数 K，请在该数组中找出两个元素，使它们的和小于 K 但尽可能地接近 K，返回这两个元素的和。

如不存在这样的两个元素，请返回 -1。

## 解题方法

### 暴力求解

本来觉得这个题好难，但是看了数组的范围才有100个元素，果断暴力求解即可。

C++代码如下：

```cpp
class Solution {
public:
    int twoSumLessThanK(vector<int>& A, int K) {
        const int N = A.size();
        int res = -1;
        int minDist = INT_MAX;
        for (int i = 0; i < N; i ++) {
            for (int j = i + 1; j < N; j ++) {
                int sum = A[i] + A[j];
                if (sum < K && K - sum < minDist) {
                    minDist = K - sum;
                    res = sum;
                }
            }
        }
        return res;
    }
};
```

## 日期

2019 年 9 月 18 日 —— 今日又是九一八


  [1]: https://blog.csdn.net/fuxuemingzhu/article/details/100977773
