
作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)

---

题目地址：https://leetcode.com/problems/count-numbers-with-unique-digits/description/

## 题目描述

Given a non-negative integer n, count all numbers with unique digits, x, where 0 ≤ x < 10^n.

Example:
Given n = 2, return 91. (The answer should be the total numbers in the range of 0 ≤ x < 100, excluding ``[11,22,33,44,55,66,77,88,99]``)

Credits:
Special thanks to @memoryless for adding this problem and creating all test cases.


## 题目大意

给出了一个n，找出n位的10进制数中，有多少个数字是不包含重复数字的。

## 解题方法

这个题明显不能用暴力解法，想都不用想。

还是找规律吧：

1. 如果n = 1，那么可以有10个数字不同（0～9）
2. 如果n >= 2，那么第一位可以是1～9共9个数字，第二位可以是出去第一位的数字+0共9个数字，之后的每位数字都必须不能使用前面已经用过的数字所以依次递减。即9,9,8,7,...,1
3. n位数字中由不同的数字构成的数字，是比它小的各位数字所能构成的该条件的数字求和。

使用循环求解，根据数字的位数，来求这个位数的能够满足条件的个数。ans是小于等于n位的求和。

如果看不明白代码，可以这么理解：题目要求的是0 ≤ x < 10^n的x个数，那么x可以为1位数，2位数……n位数。当x为1位数的时候有10个结果；当x为2位数的时候，有9*9个结果；当x为3位数的时候，有9*9*8个结果……也就是说当x为n位数的时候，有9*9*...*(11 - n个结果)，其中n必须小于等于10了（11位数字不可能每一位都不相同）。最后求和就好。

Python代码如下：

```python
class Solution(object):
    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        nums = [9, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        ans, product = 1, 1
        for i in range(min(n, 10)):
            product *= nums[i]
            ans += product
        return ans
```

C++代码如下：

```cpp
class Solution {
public:
    int countNumbersWithUniqueDigits(int n) {
        int count[]= {9,9,8,7,6,5,4,3,2,1};
        int res = 1, prod = 1;
        for (int i = 0; i < min(10, n); i ++) {
            prod *= count[i];
            res += prod;
        }
        return res;
    }
};
```

## 日期

2018 年 6 月 2 日 —— 周末在学习
2018 年 12 月 20 日 —— 感冒害的我睡不着
