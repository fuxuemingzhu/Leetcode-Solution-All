
- 作者：    负雪明烛
- id：      fuxuemingzhu
- 个人博客：[http://fuxuemingzhu.cn/](http://fuxuemingzhu.cn/)

---
@[TOC](目录)


题目地址：https://leetcode-cn.com/problems/check-if-a-number-is-majority-element-in-a-sorted-array/

## 题目描述

The `k`-digit number `N` is an Armstrong number if and only if the `k`-th power of each digit sums to `N`.

Given a positive integer `N`, return true if and only if it is an Armstrong number.

Example 1:

    Input: 153
    Output: true
    Explanation: 
    153 is a 3-digit number, and 153 = 1^3 + 5^3 + 3^3.

Example 2:

    Input: 123
    Output: false
    Explanation: 
    123 is a 3-digit number, and 123 != 1^3 + 2^3 + 3^3 = 36.

Note:

1. `1 <= N <= 10^8`

## 题目大意

给你一个整数数组 A，请找出并返回在该数组中仅出现一次的最大整数。

如果不存在这个只出现一次的整数，则返回 -1。

## 解题方法

### 直接计算

先算k，然后判断即可。

C++代码如下：

```cpp
class Solution {
public:
    bool isArmstrong(int N) {
        int k = 0;
        int temp = N;
        while (temp != 0) {
            k++;
            temp /= 10;
        }
        long long res = 0;
        temp = N;
        while (temp != 0) {
            int mod = temp % 10;
            res += pow(mod, k);
            temp /= 10;
        }
        return res == N;
    }
    int pow(int N, int k) {
        int res = 1;
        while (k --) {
            res *= N;
        }
        return res;
    }
};
```

## 日期

2019 年 9 月 18 日 —— 今日又是九一八
