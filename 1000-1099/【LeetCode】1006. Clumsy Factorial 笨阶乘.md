作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)


题目地址：https://leetcode.com/problems/clumsy-factorial/

## 题目描述

Normally, the factorial of a positive integer ``n`` is the product of all positive integers less than or equal to ``n``.  For example, ``factorial(10) = 10 * 9 * 8 * 7 * 6 * 5 * 4 * 3 * 2 * 1``.

We instead make a clumsy factorial: using the integers in decreasing order, we swap out the multiply operations for a fixed rotation of operations: multiply (*), divide (/), add (+) and subtract (-) in this order.

For example, ``clumsy(10) = 10 * 9 / 8 + 7 - 6 * 5 / 4 + 3 - 2 * 1``.  However, these operations are still applied using the usual order of operations of arithmetic: we do all multiplication and division steps before any addition or subtraction steps, and multiplication and division steps are processed left to right.

Additionally, the division that we use is floor division such that ``10 * 9 / 8`` equals ``11``.  This guarantees the result is an integer.

``Implement the clumsy`` function as defined above: given an integer ``N``, it returns the clumsy factorial of ``N``.
 

Example 1:

    Input: 4
    Output: 7
    Explanation: 7 = 4 * 3 / 2 + 1

Example 2:

    Input: 10
    Output: 12
    Explanation: 12 = 10 * 9 / 8 + 7 - 6 * 5 / 4 + 3 - 2 * 1

Note:

1. 1 <= N <= 10000
1. -2^31 <= answer <= 2^31 - 1  (The answer is guaranteed to fit within a 32-bit integer.)

## 题目大意

常规的阶乘是从N到1各个数字连乘，但是这个题设计了一个新的函数：笨拙阶乘。做法是把N到1各个数字依次使用乘、除、加、减的循环进行连接。最终的结果也是按照普通的四则运算来做。求一个数的笨拙阶乘的结果是多少。

## 解题方法

### 直接eval

很惭愧，我作弊了，用的python的函数eval，直接表达式求值就可以了。

Python代码如下：

```python
class Solution(object):
    def clumsy(self, N):
        """
        :type N: int
        :rtype: int
        """
        cl = ""
        ops = ["*", "/", "+", "-"]
        op = 0
        for n in range(N, 0, -1):
            if n != 1:
                cl += str(n) + ops[op % 4]
            else:
                cl += "1"
            op += 1
        return eval(cl)
```


## 日期

2019 年 3 月 10 日 —— 周赛进了第一页！


  [1]: https://assets.leetcode.com/uploads/2019/02/19/113_sample.png
  [2]: https://blog.csdn.net/fuxuemingzhu/article/details/80787528
