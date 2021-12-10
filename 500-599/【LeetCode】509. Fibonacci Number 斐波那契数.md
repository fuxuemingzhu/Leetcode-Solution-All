
作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)


题目地址：https://leetcode.com/problems/fibonacci-number/

## 题目描述

The **Fibonacci numbers**, commonly denoted F(n) form a sequence, called the **Fibonacci sequence**, such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,

    F(0) = 0,   F(1) = 1
    F(N) = F(N - 1) + F(N - 2), for N > 1.

Given `N`, calculate ``F(N)``.

 

Example 1:

    Input: 2
    Output: 1
    Explanation: F(2) = F(1) + F(0) = 1 + 0 = 1.

Example 2:

    Input: 3
    Output: 2
    Explanation: F(3) = F(2) + F(1) = 1 + 1 = 2.

Example 3:

    Input: 4
    Output: 3
    Explanation: F(4) = F(3) + F(2) = 2 + 1 = 3.
     
Note:

1. 0 ≤ N ≤ 30.

## 题目大意

求费布拉奇数列的第N个元素是多少。

## 解题方法

### 动态规划

常见的求费布拉奇数列的方法是递归，但是估计这个题目会超时，另外太简单了我不写了。

一个常见的优化就是改成了一维的动态规划，因为每个状态只和前两个状态有关，所以我们可以依次从第0个位置推到我们想要的位置。

这个题需要注意的是N的取值范围，注意当N<=1的时候相当于终止条件，直接返回结果。

这种解法的时间复杂度是O(N)。

另外一提，费布拉奇数列是有通项公式的，可以直接用公式求出来，时间复杂度降到O(1).

Python代码如下：

```cpp
class Solution {
public:
    int fib(int N) {
        if (N <= 1) return N;
        vector<int> fibs(N + 1);
        fibs[0] = 0;
        fibs[1] = 1;
        for (int i = 2; i <= N; ++i) {
            fibs[i] = fibs[i - 1] + fibs[i - 2];
        }
        return fibs[N];
    }
};
```

## 日期

2019 年 7 月 13 日 —— 又是一个多月没刷题


  [1]: https://blog.csdn.net/fuxuemingzhu/article/details/79463006
