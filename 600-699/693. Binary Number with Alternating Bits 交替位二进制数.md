
作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)

题目地址：[https://leetcode.com/problems/binary-number-with-alternating-bits/description/][1]


## 题目描述

Given a positive integer, check whether it has alternating bits: namely, if two adjacent bits will always have different values.

Example 1:

    Input: 5
    Output: True
    Explanation:
    The binary representation of 5 is: 101

Example 2:

    Input: 7
    Output: False
    Explanation:
    The binary representation of 7 is: 111.

Example 3:

    Input: 11
    Output: False
    Explanation:
    The binary representation of 11 is: 1011.

Example 4:

    Input: 10
    Output: True
    Explanation:
    The binary representation of 10 is: 1010.

## 题目大意

判断一个数的二进制表示中是不是相邻的两个数字都是不同的。

## 解题方法

### 遍历判断

想法很朴素，判断二进制数任意两个字符是否是不同的即可。

可以用相加为1来判断，也可以直接用不等来判断。

```python
class Solution(object):
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        bin_n = bin(n)[2:]
        return all(int(bin_n[i]) + int(bin_n[i+1]) == 1 for i in xrange(len(bin_n) - 1))
```

直接判断相邻的数字是不同的：

```python
class Solution(object):
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        bin_n = bin(n)[2:]
        return all(bin_n[i] != bin_n[i+1] for i in xrange(len(bin_n) - 1))
```

### 判断是否是交替模式

看别人的代码，速度更快，这是因为符合题目要求的二进制数字的模式是已知的，可以生成所有的模式，从而这个数字是否在这些模式之中。直接判断是不是在所有交替的字符串之间即可。

```python
class Solution(object):
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        b = 0b1010101010101010101010101010101010101010101010101010101010101010
        while b > 0:
            if b == n:
                return True
            b = b >> 1
        return False
```

### 位运算

又是骚操作。这个操作的是我们先使用n ^ (n - 1)，如果是01交错的二进制数字，在经历了这个操作之后，得到的全部是1的二进制数字。第二步使用与运算判断是否是全部为1.

```python
class Solution(object):
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        n ^= (n >> 1)
        return not (n & n + 1)
```

## 日期

2018 年 1 月 17 日 
2018 年 11 月 ９ 日 —— 睡眠可以

  [1]: https://leetcode.com/problems/binary-number-with-alternating-bits/description/
