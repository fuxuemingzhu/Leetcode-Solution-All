
作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)


题目地址：https://leetcode.com/problems/n-th-tribonacci-number/

## 题目描述

The Tribonacci sequence `Tn` is defined as follows: 

`T0 = 0, T1 = 1, T2 = 1`, and `Tn+3 = Tn + Tn+1 + Tn+2` for `n >= 0`.

Given `n`, return the value of `Tn`.

Example 1:

    Input: n = 4
    Output: 4
    Explanation:
    T_3 = 0 + 1 + 1 = 2
    T_4 = 1 + 1 + 2 = 4

Example 2:

    Input: n = 25
    Output: 1389537
     

Constraints:

1. 0 <= n <= 37
2. The answer is guaranteed to fit within a 32-bit integer, ie. answer <= 2^31 - 1.


## 题目大意

费布拉奇数列的拓展，每个元素是前面三个元素的和。求第n个元素。

## 解题方法

### 动态规划

众所周知，当递归深度比较大的时候会爆栈，所以使用的动态规划去做。

这个题需要注意的是有n=0,1,2三个特殊值，其他都好说。

C++代码如下：

```cpp
class Solution {
public:
    int tribonacci(int n) {
        if (n == 0) return 0;
        if (n == 1) return 1;
        if (n == 2) return 1;
        vector<int> T(n + 1);
        T[0] = 0;
        T[1] = T[2] = 1;
        for (int i = 3; i <= n; ++i) {
            T[i] = T[i - 1] + T[i - 2] + T[i - 3];
        }
        return T[n];
    }
};
```


## 日期

2019 年 7 月 28 日 —— kickstart完败
