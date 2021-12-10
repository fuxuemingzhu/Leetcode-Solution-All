# 【LeetCode】397. Integer Replacement 解题报告（Python） 

标签： LeetCode

---

题目地址：https://leetcode.com/problems/integer-replacement/description/

## 题目描述：

Given a positive integer n and you can do operations as follow:

1. If n is even, replace n with ``n/2``.
1. If n is odd, you can replace n with either ``n + 1`` or ``n - 1``.

What is the minimum number of replacements needed for n to become 1?

Example 1:
    
    Input:
    8
    
    Output:
    3
    
    Explanation:
    8 -> 4 -> 2 -> 1
    
Example 2:
    
    Input:
    7
    
    Output:
    4
    
    Explanation:
    7 -> 8 -> 4 -> 2 -> 1
    or
    7 -> 6 -> 3 -> 2 -> 1

## 题目大意

给了n，如果是是偶数对其/2，如果是奇数可以对其+1或-1操作，求最后将其化为1需要多少步。

## 解题方法

方法一：

递归。不过速度不快。

```python
class Solution(object):
    def integerReplacement(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1: return 0
        if n % 2 == 0:
            return 1 + self.integerReplacement(n / 2)
        else:
            return 1 + min(self.integerReplacement(n + 1), self.integerReplacement(n - 1))
```

方法二：

位运算。

当n是奇数的时候，如何决定应该加1还是减1？我们可以看这个数字的二进制。奇数的二进制一定是01或11结尾。同时，发现如果把一个奇数化为4的倍数，变成1的步骤会更少（3除外）。

    15 -> 16 -> 8 -> 4 -> 2 -> 1
    
    15 -> 14 -> 7 -> 6 -> 3 -> 2 -> 1

那么，如果结尾是01，那么应该对其-1；如果结尾是11，那么应该对其+1；

如果这个数字是3，需要对其-1。

直接迭代求解，速度很快。

代码：

```python
class Solution(object):
    def integerReplacement(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        while n > 1:
            count += 1
            if n & 1:#奇数
                if n & 2 and n != 3:#尾号是11
                    n += 1
                else:#尾号是01
                    n -= 1
            else:#偶数
                n >>= 1
        return count
```

方法二：



## 日期

2018 年 3 月 9 日 
