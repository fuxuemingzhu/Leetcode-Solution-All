
- 作者：    负雪明烛
- id：      fuxuemingzhu
- 个人博客：[http://fuxuemingzhu.cn/](http://fuxuemingzhu.cn/)

---
@[TOC](目录)


题目地址：https://leetcode-cn.com/problems/sum-of-digits-in-the-minimum-number/

## 题目描述

Given an array `A` of positive integers, let `S` be the sum of the digits of the minimal element of `A`.

Return 0 if S is odd, otherwise return 1.

Example 1:

    Input: [34,23,1,24,75,33,54,8]
    Output: 0
    Explanation: 
    The minimal element is 1, and the sum of those digits is S = 1 which is odd, so the answer is 0.

Example 2:

    Input: [99,77,33,66,55]
    Output: 1
    Explanation: 
    The minimal element is 33, and the sum of those digits is S = 3 + 3 = 6 which is even, so the answer is 1.

Note:

1. 1 <= A.length <= 100
1. 1 <= A[i].length <= 100


## 题目大意

给你一个正整数的数组 A。
然后计算 S，使其等于数组 A 当中最小的那个元素各个数位上数字之和。
最后，假如 S 所得计算结果是 奇数 的请你返回 0，否则请返回 1。


## 解题方法

### 遍历

先找出最小的数字，然后求其各位数字的和。

C++代码如下：

```cpp
class Solution {
public:
    int sumOfDigits(vector<int>& A) {
        int min_num = INT_MAX;
        for (int a : A) {
            min_num = min(min_num, a);
        }
        int k = 0;
        int s = 0;
        while (min_num != 0) {
            s += min_num % 10;
            k++;
            min_num /= 10;
        }
        return 1 - (s & 1);
    }
};
```

## 日期

2019 年 9 月 18 日 —— 今日又是九一八


  [1]: https://blog.csdn.net/fuxuemingzhu/article/details/100977773
