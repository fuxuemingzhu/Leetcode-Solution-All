
- 作者：    负雪明烛
- id：      fuxuemingzhu
- 个人博客：[http://fuxuemingzhu.cn/](http://fuxuemingzhu.cn/)

---
@[TOC](目录)


题目地址：https://leetcode-cn.com/problems/fixed-point/

## 题目描述

Given an array A of distinct integers sorted in ascending order, return the smallest index i that satisfies `A[i] == i`.  Return -1 if no such i exists.

 

Example 1:

    Input: [-10,-5,0,3,7]
    Output: 3
    Explanation: 
    For the given array, A[0] = -10, A[1] = -5, A[2] = 0, A[3] = 3, thus the output is 3.

Example 2:

    Input: [0,2,5,8,17]
    Output: 0
    Explanation: 
    A[0] = 0, thus the output is 0.

Example 3:

    Input: [-10,-5,3,4,7,9]
    Output: -1
    Explanation: 
    There is no such i that A[i] = i, thus the output is -1.
     

Note:

1. `1 <= A.length < 10^4`
1. `-10^9 <= A[i] <= 10^9`


## 题目大意

给定已经按升序排列、由不同整数组成的数组 A，返回满足 A[i] == i 的最小索引 i。如果不存在这样的 i，返回 -1。

## 解题方法

### 暴力求解

从头遍历一遍即可。

C++代码如下：

```cpp
class Solution {
public:
    int fixedPoint(vector<int>& A) {
        const int N = A.size();
        for (int i = 0; i < N; ++i) {
            if (A[i] == i)
                return i;
        }
        return -1;
    }
};
```

## 日期

2019 年 9 月 18 日 —— 今日又是九一八


  [1]: https://blog.csdn.net/fuxuemingzhu/article/details/100977773
