作者： 		负雪明烛 
id：				fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)

题目地址: https://leetcode.com/problems/powx-n/description/

## 题目描述：

Implement pow(x, n), which calculates x raised to the power n ``(x^n)``.

Example 1:

    Input: 2.00000, 10
    Output: 1024.00000

Example 2:

    Input: 2.10000, 3
    Output: 9.26100

Example 3:
    
    Input: 2.00000, -2
    Output: 0.25000
    Explanation: 2-2 = 1/22 = 1/4 = 0.25

Note:

1. ` -100.0 < x < 100.0`
1.  `n` is a `32`-bit signed integer, within the range `[−2^31, 2^31 − 1]`

## 题目大意

实现x的n次方的函数。

## 解题方法

### 递归

主要是注意n的正负，这个题比较简单了，直接递归调用就行。如果n是负数，那么相当于求 `(1/x)^(-n)`。如果n是奇数，那么结果需要单独乘以 `x`，否则就相当于求`(x^2)^(n/2)`，一直递归下去即可。

时间复杂度是O(1)，空间复杂度是O(1)。我认为这个代码是O(1)，因为n只有32位，循环次数是有上限的常数。

```python
class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n == 0:
            return 1
        if n < 0:
            x = 1 / x
            n = -n
        if n % 2:
            return x * self.myPow(x, n - 1)
        return self.myPow(x * x, n / 2)
```
C++ 代码如下：

```cpp
class Solution {
public:
    double myPow(double x, long long n) {
        if (n == 0)
            return 1;
        if (n == 1)
            return x;
        if (n < 0)
            return 1.0 / myPow(x, -n);
        if (n  % 2 == 1)
            return x * myPow(x, n - 1);
        else {
            double cur = myPow(x, n / 2);
            return cur * cur;
        }
    }
};
```

### 迭代

使用迭代的方法，这个方法叫做二分求幂。

时间复杂度是O(1)，空间复杂度是O(1)

```python
class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n == 0:
            return 1
        if n < 0:
            x = 1 / x
            n = -n
        ans = 1
        res = 1
        while n:
            if n % 2:
                ans *= x
            n >>= 1
            x *= x
        return ans
```



## 日期

2018 年 10 月 7 日 —— 假期最后一天！！
2020 年 5 月 11 日 —— 毕业前最好的假期
