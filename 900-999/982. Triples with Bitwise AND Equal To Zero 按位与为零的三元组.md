作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)


题目地址：https://leetcode.com/problems/triples-with-bitwise-and-equal-to-zero/


## 题目描述

Given an array of integers ``A``, find the number of triples of indices (i, j, k) such that:

- ``0 <= i < A.length``
- ``0 <= j < A.length``
- ``0 <= k < A.length``
- ``A[i] & A[j] & A[k] == 0``, where ``&`` represents the bitwise-AND operator.
 

Example 1:
    
    Input: [2,1,3]
    Output: 12
    
    Explanation: We could choose the following i, j, k triples:

    (i=0, j=0, k=1) : 2 & 2 & 1
    (i=0, j=1, k=0) : 2 & 1 & 2
    (i=0, j=1, k=1) : 2 & 1 & 1
    (i=0, j=1, k=2) : 2 & 1 & 3
    (i=0, j=2, k=1) : 2 & 3 & 1
    (i=1, j=0, k=0) : 1 & 2 & 2
    (i=1, j=0, k=1) : 1 & 2 & 1
    (i=1, j=0, k=2) : 1 & 2 & 3
    (i=1, j=1, k=0) : 1 & 1 & 2
    (i=1, j=2, k=0) : 1 & 3 & 2
    (i=2, j=0, k=1) : 3 & 2 & 1
    (i=2, j=1, k=0) : 3 & 1 & 2
     

Note:

1. 1 <= A.length <= 1000
1. 0 <= A[i] < 2^16

## 题目大意

找出给定的数组中，有多少个三元组，使得这个三元组的位与等于0.

## 解题方法

看了下数组长度是1000，大概分析下这个题目的时间复杂度是O(N^2×log(N))以下。同时注意到三元组的顺序并无要求，即同样的组合可能出现多次。

一个最省事的做法就是，先两重循环，计算任意两个数字之间的位与结果是多少，存储到字典中，字典中保存的是位与出现的次数。然后再次对数组每个位置进行遍历，同时遍历字典中的每个元素，即可分析出任意三个数字位与的结果和次数。

唯一需要注意的是字典保存的是两个数字位与后的结果出现的次数，当第三个数字和两位数字位与结果进行位与的结果是0的时候，需要次数累加。

这个时间复杂度怎么分析？注意题目给出的每个元素的大小是2^16，所以两个数字位与的结果不会超过2^16。因此，总的时间复杂度是O(N^2 + 2^16 * N).


```python
class Solution {
public:
    int countTriplets(vector<int>& A) {
        const int N = A.size();
        int res = 0;
        unordered_map<int, int> m_;
        for (int i = 0; i < N; ++i) {
            for (int j = 0; j < N; ++j) {
                ++m_[(A[i] & A[j])];
            }
        }
        for (int i = 0; i < N; ++i) {
            for (auto a : m_) {
                if ((A[i] & a.first) == 0)
                    res += a.second;
            }
        }
        return res;
    }
};
```


## 日期

2019 年 1 月 27 日 —— 这个周赛不太爽
