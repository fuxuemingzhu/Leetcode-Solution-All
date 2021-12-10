
作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/
公众号：负雪明烛
本文关键词：整数，反转，题解，Leetcode, 力扣，Python, C++, Java

---
@[TOC](目录)

题目地址：https://leetcode.com/problems/reverse-integer/description/


# 题目描述

Given a 32-bit signed integer, reverse digits of an integer.

Example 1:
    
    Input: 123
    Output:  321

Example 2:
    
    Input: -123
    Output: -321

Example 3:
    
    Input: 120
    Output: 21

Note:

- Assume we are dealing with an environment which could only hold integers within the 32-bit signed integer range. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.

# 题目大意

把一个 int 进行翻转，如果翻转后的数值不在 int 范围内，返回0。

# 解题方法

## 转成字符串

题目要对整数进行翻转，并说明了当翻转了的整数超过了32位，就是用0替代。

这个题又让我学会了一个新的函数``bit_length()``，在python2.7以上可以对整型使用。


```python
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        n = cmp(x, 0) * int(str(abs(x))[::-1])
        return n if n.bit_length() < 32 else 0
```

二刷，同样使用字符串翻转，只不过翻转之后进行判断直接使用使用int最大值和最小值。

```py
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0: return 0
        flag = 1
        if x < 0:
            flag = -1
            x = -x
        r = int(str(x)[::-1])
        if flag == 1 and r <= 2147483647:
            return r
        elif flag == -1 and -r >= -2147483648:
            return -r
        return 0
```

C++版本的代码如下：

```cpp
class Solution {
public:
    int reverse(int x) {
        if (x == 0) return 0;
        int flag = 1;
        if (x < 0) flag = -1;
        string xs = to_string(x);
        long r = stol(string(xs.rbegin(), xs.rend()));
        if (flag == 1 && r <= INT_MAX) return r;
        if (flag == -1 && -r >= INT_MIN) return -r;
        return 0;
    }
};
```

## 数学

TODO

# 日期

2018 年 2 月 5 日 
2018 年 11 月 30 日 —— 又到了周末
2021 年 8 月 7 日
