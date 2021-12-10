作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)


题目地址：https://leetcode.com/problems/reach-a-number/description/


## 题目描述

Find the nth digit of the infinite integer sequence 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ...

Note:

1. n is positive and will fit within the range of a 32-bit signed integer (n < 231).

Example 1:

    Input:
    3
    
    Output:
    3
    Example 2:
    
    Input:
    11
    
    Output:
    0
    
    Explanation:
    The 11th digit of the sequence 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ... is a 0, which is part of the number 10.

## 题目大意

找出一个连续的自然数序列中，第N``位``数字是多少。

## 解题方法

我们要得到第N位数字，如果直接暴力是超时的。正确的做法是找规律：个位数字有9个，2位数字有9*10=90个，3位数字有9*100=900个……所以我们先求出n是几位数字，然后判断第n个数字应该落在哪个自然数上，最后再求这个自然数会落在自然数的那一位上。

```python
class Solution(object):
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        _len = 1
        cnt = 9
        start = 1
        while n > _len * cnt:
            n -= _len * cnt
            _len += 1
            cnt *= 10
            start *= 10
        start += (n - 1) / _len
        return int(str(start)[(n - 1) % _len])
```


参考资料：http://www.cnblogs.com/grandyang/p/5891871.html

## 日期

2018 年 11 月 27 日 —— 最近的雾霾太可怕


  [1]: http://zxi.mytechroad.com/blog/dynamic-programming/leetcode-730-count-different-palindromic-subsequences/
