
作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)


题目地址：https://leetcode.com/problems/consecutive-numbers-sum/


## 题目描述

Given a positive integer ``N``, how many ways can we write it as a sum of consecutive positive integers?

Example 1:

    Input: 5
    Output: 2
    Explanation: 5 = 5 = 2 + 3

Example 2:

    Input: 9
    Output: 3
    Explanation: 9 = 9 = 4 + 5 = 2 + 3 + 4

Example 3:

    Input: 15
    Output: 4
    Explanation: 15 = 15 = 8 + 7 = 4 + 5 + 6 = 1 + 2 + 3 + 4 + 5

Note: ``1 <= N <= 10 ^ 9``.

## 题目大意

问给定一个数字N，有多少种把它展开成连续正整数之和的方案。

## 解题方法

### 数学方法

有些题会让人陷入常规做法不能自拔，比如这个题就可能想成回溯或者O(M*N)的循环。事实上可以通过数学方法进行优化。

因为是连续正整数之和，所以可以使用数列求和公式直接求和，把O(M*N)的方案降到O(M)。

由``N = a + (a + 1) + (a + 2) + (a + 3) + ... + (a + i)``得，
 
 ``N = a * (i + 1) + (i * (i + 1)) / 2``，其中，``a > 0``并且`` i>= 0``。

所以，我们先求出prod = (i * (i + 1)) / 2 ， 如果这个数字大于N了，就立刻结束。否则，remain = N - prod ==> a * (i + 1). 所以，remain应该能够整除(i + 1)，而且余数为a > 0。

这个题用python代码会超时，改用C++就能通过。

C++代码如下：

```cpp
class Solution {
public:
    int consecutiveNumbersSum(int N) {
        int res = 0;
        for (int i = 0; i < N; i++) {
            int prod = (i + 1) * i / 2;
            if (prod > N) break;
            int remain = N - prod;
            if (remain % (i + 1) != 0)
                continue;
            if (remain / (i + 1) > 0)
                res ++;
        }
        return res;
    }
};
```


## 日期

2019 年 1 月 5 日 —— 美好的周末又开始了


  [1]: https://assets.leetcode.com/uploads/2018/10/12/8-queens.png
  [2]: https://blog.csdn.net/fuxuemingzhu/article/details/79517109
