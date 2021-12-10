作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)


题目地址：https://leetcode.com/problems/complement-of-base-10-integer/

## 题目描述

Every non-negative integer ``N`` has a binary representation.  For example, ``5`` can be represented as ``"101"`` in binary, ``11`` as ``"1011"`` in binary, and so on.  Note that except for ``N = 0``, there are no leading zeroes in any binary representation.

The complement of a binary representation is the number in binary you get when changing every ``1`` to a ``0`` and ``0`` to a ``1``.  For example, the complement of ``"101"`` in binary is ``"010"`` in binary.

For a given number ``N`` in base-10, return the complement of it's binary representation as a base-10 integer.

Example 1:

    Input: 5
    Output: 2
    Explanation: 5 is "101" in binary, with complement "010" in binary, which is 2 in base-10.

Example 2:

    Input: 7
    Output: 0
    Explanation: 7 is "111" in binary, with complement "000" in binary, which is 0 in base-10.

Example 3:

    Input: 10
    Output: 5
    Explanation: 10 is "1010" in binary, with complement "0101" in binary, which is 5 in base-10.
 

Note:

1. ``0 <= N < 10^9``

## 题目大意

求一个数的补码。

## 解题方法

很简单一个作弊方法，直接求二进制，然后把1改成0，把0改成1即可。

Python代码如下：

```python
class Solution(object):
    def bitwiseComplement(self, N):
        """
        :type N: int
        :rtype: int
        """
        return int("".join(map(lambda x :"0" if x == "1" else "1", bin(N)[2:])), 2)
```


## 日期

2019 年 3 月 21 日 —— 好久不刷题，重拾有点难


  [1]: https://assets.leetcode.com/uploads/2019/03/06/1266.png
  [2]: https://assets.leetcode.com/uploads/2019/03/08/domino.png
