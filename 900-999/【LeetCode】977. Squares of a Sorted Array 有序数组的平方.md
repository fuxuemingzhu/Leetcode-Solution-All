
作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)

题目地址：https://leetcode.com/problems/squares-of-a-sorted-array/


## 题目描述

Given an array of integers ``A`` sorted in non-decreasing order, return an array of the squares of each number, also in sorted non-decreasing order.


Example 1:

    Input: [-4,-1,0,3,10]
    Output: [0,1,9,16,100]

Example 2:
    
    Input: [-7,-3,2,3,11]
    Output: [4,9,9,49,121]

Note:

1. 1 <= A.length <= 10000
1. -10000 <= A[i] <= 10000
1. A is sorted in non-decreasing order.

## 题目大意

给了一个单调不减的数组，返回排序了的每个元素求平方的结果。

## 解题方法

### 排序

没错这个是Easy题目，不用想太多，直接对每个元素进行求平方并排序即可。

需要注意的是，求平方之后是否会超出int的最大值呢？还好题目给了A[i]的范围只有10000，那么平方是1个亿，不会超过int最大。所以是安全的。

数组总长度是10000，所以O(NlongN)的时间复杂度是完全OK的。

c++代码如下：

```cpp
class Solution {
public:
    vector<int> sortedSquares(vector<int>& A) {
        vector<int> res;
        for (int a : A) {
            res.push_back(a * a);
        }
        sort(res.begin(), res.end());
        return res;
    }
};
```

## 日期

2019 年 1 月 20 日 —— 这次周赛有点简单


  [1]: https://assets.leetcode.com/uploads/2018/12/29/bst_cameras_01.png
  [2]: https://assets.leetcode.com/uploads/2018/12/29/bst_cameras_02.png
