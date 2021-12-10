作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)


题目地址：https://leetcode.com/problems/binary-prefix-divisible-by-5/

## 题目描述

Given an array ``A`` of ``0``s and ``1``s, consider ``N_i``: the ``i-th`` subarray from ```A[0]`` to ``A[i]`` interpreted as a binary number (from most-significant-bit to least-significant-bit.)

Return a list of booleans ``answer``, where ``answer[i]`` is true if and only if N_i is divisible by 5.

Example 1:

    Input: [0,1,1]
    Output: [true,false,false]
    Explanation: 
    The input numbers in binary are 0, 01, 011; which are 0, 1, and 3 in base-10.  Only the first number is divisible by 5, so answer[0] is true.

Example 2:

    Input: [1,1,1]
    Output: [false,false,false]

Example 3:

    Input: [0,1,1,1,1,1]
    Output: [true,false,false,false,true,false]

Example 4:

    Input: [1,1,1,0,1]
    Output: [false,false,false,false,false]
 

Note:

1. ``1 <= A.length <= 30000``
1. ``A[i] is 0 or 1``


## 题目大意

给出一个数组，判断数组的每个位置构成的前缀能不能被5整除。

## 解题方法

这个题肯定不能蛮力求解，最简单的方法就是利用求余的性质。我们每次只用保存前缀对5的余数，在求下一个位置的时候把``上一次的前缀×2 + 当前的数字``再模5.

求余的性质：

    ((a +b)mod p × c) mod p = ((a × c) mod p + (b × c) mod p) mod p
    (a×b) mod c=((a mod c) * (b mod c)) mod c
    (a+b) mod c=((a mod c)+ (b mod c)) mod c
    (a-b) mod c=((a mod c)- (b mod c)) mod c

所以，a扩大x倍之后模一个数字，等于((a % 5) * (x % 5)) % 5.

Python代码如下：

```python
class Solution(object):
    def prefixesDivBy5(self, A):
        """
        :type A: List[int]
        :rtype: List[bool]
        """
        res = []
        prefix = 0
        for a in A:
            prefix = (prefix * 2 + a) % 5
            res.append(prefix == 0)
        return res
```

## 日期

2019 年 4 月 5 日 —— 清明节休息一下～


  [1]: https://blog.csdn.net/fuxuemingzhu/article/details/82716042
