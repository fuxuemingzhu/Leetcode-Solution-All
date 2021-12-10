
作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)

题目地址：[https://leetcode.com/problems/1-bit-and-2-bit-characters/description/][1]


## 题目描述

We have two special characters. The first character can be represented by one bit 0. The second character can be represented by two bits (10 or 11).

Now given a string represented by several bits. Return whether the last character must be a one-bit character or not. The given string will always end with a zero.

Example 1:

    Input: 
    bits = [1, 0, 0]
    Output: True
    Explanation: 
    The only way to decode it is two-bit character and one-bit character. So the last character is one-bit character.

Example 2:

    Input: 
    bits = [1, 1, 1, 0]
    Output: False
    Explanation: 
    The only way to decode it is two-bit character and two-bit character. So the last character is NOT one-bit character.

Note:

1. 1 <= len(bits) <= 1000.
2. bits[i] is always 0 or 1.

## 题目大意

有两种字符，一种是0，一种是10或者11，现在要判断整个数组是否由这两种组成的，要求最后一位的数字必须是单个的0．

## 解题方法

### 遍历

这个题真的很简单，因为有两种字符串，一种是0，一种是10或11。即一种长度是1，一种长度是2.
所以找个指针然后遍历一遍，看看当前值是0还是1，是0走1步，是1走两步。最后如果能到达`len-1`即可。

下面是第一次提交，想到了判断最后一个字符是不是0。题目中已经明确告诉了是0，所以下面有个改进版的。

```python
"""
class Solution(object):
    def isOneBitCharacter(self, bits):
        """
        :type bits: List[int]
        :rtype: bool
        """
        pos = 0
        while pos < len(bits) - 1:
            if bits[pos] == 1:
                pos += 2
            else:
                pos += 1
        return pos == len(bits) - 1 and bits[pos] == 0
```

精简：

```python
class Solution(object):
    def isOneBitCharacter(self, bits):
        """
        :type bits: List[int]
        :rtype: bool
        """
        pos = 0
        while pos < len(bits) - 1:
            pos += 2 if bits[pos] == 1 else 1
        return pos == len(bits) - 1
```

## 日期

2018 年 1 月 22 日 
2018 年 11 月 14 日 —— 很严重的雾霾

  [1]: https://leetcode.com/problems/1-bit-and-2-bit-characters/description/
