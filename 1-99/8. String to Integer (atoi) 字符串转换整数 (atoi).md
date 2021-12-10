
作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/
公众号：负雪明烛
本文关键词：字符串转整数，atoi，题解，Leetcode, 力扣，Python, C++, Java

---
@[TOC](目录)


题目地址：https://leetcode-cn.com/problems/string-to-integer-atoi/

# 题目描述
Implement the `myAtoi(string s)` function, which converts a string to a 32-bit signed integer (similar to C/C++'s atoi function).

The algorithm for `myAtoi(string s)` is as follows:

1. Read in and ignore any leading whitespace.
2. Check if the next character (if not already at the end of the string) is '-' or '+'. Read this character in if it is either. This determines if the final result is negative or positive respectively. Assume the result is positive if neither is present.
3. Read in next the characters until the next non-digit charcter or the end of the input is reached. The rest of the string is ignored.
4. Convert these digits into an integer (i.e. "123" -> 123, "0032" -> 32). If no digits were read, then the integer is 0. Change the sign as necessary (from step 2).
5. If the integer is out of the 32-bit signed integer range [-231, 231 - 1], then clamp the integer so that it remains in the range. Specifically, integers less than -231 should be clamped to -231, and integers greater than 231 - 1 should be clamped to 231 - 1.
6. Return the integer as the final result.

Note:

1. Only the space character `' '` is considered as whitespace character.
2. Assume we are dealing with an environment which could only store integers within the `32-bit` signed integer range: `[−231,  231 − 1]`. If the numerical value is out of the range of representable values, `INT_MAX (231 − 1)` or `INT_MIN (−231)` is returned.

Example 1:

    Input: "42"
    Output: 42

Example 2:

    Input: "   -42"
    Output: -42
    Explanation: The first non-whitespace character is '-', which is the minus sign.
                 Then take as many numerical digits as possible, which gets 42.

Example 3:

    Input: "4193 with words"
    Output: 4193
    Explanation: Conversion stops at digit '3' as the next character is not a numerical digit.

Example 4:

    Input: "words and 987"
    Output: 0
    Explanation: The first non-whitespace character is 'w', which is not a numerical 
                 digit or a +/- sign. Therefore no valid conversion could be performed.

Example 5:

    Input: "-91283472332"
    Output: -2147483648
    Explanation: The number "-91283472332" is out of the range of a 32-bit signed integer. Thefore INT_MIN (−231) is returned.

# 题目大意

请你来实现一个 atoi 函数，使其能将字符串转换成整数。

首先，该函数会根据需要丢弃无用的开头空格字符，直到寻找到第一个非空格的字符为止。接下来的转化规则如下：

1. 如果第一个非空字符为正或者负号时，则将该符号与之后面尽可能多的连续数字字符组合起来，形成一个有符号整数。
2. 假如第一个非空字符是数字，则直接将其与之后连续的数字字符组合起来，形成一个整数。
3. 该字符串在有效的整数部分之后也可能会存在多余的字符，那么这些字符可以被忽略，它们对函数不应该造成影响。

# 解题方法

这个题是我一直“珍藏”没做的题，因为我知道这个题的坑比较多。这次算是认真的做了一次。

重点还是理解题目给了什么规则：去除起始的空格；判断正负号；找第一个开始的数字开始，到第一个非数字字符处停止。

在这种字符串处理的题目中，我一般都是选用Python大法结合正则表达式，特别是正则表达式是大杀器。

做法：
1. 去除开始和结尾的所有空字符，使用`.strip()`方法
2. 使用正则表达式找出`"+"`, `"-"`, 数字 开始，到第一个非数字字符处停止的数字。该正则是 `"^[+-]?\d+"`，可以用 http://tool.chinaz.com/regex/ 进行校验。
3. 把数字转成整数(使用Python的`int()`函数，Python的int可以表示出无限大的数字，不用担心越界)。
4. 如果超出了题目说的`INT_MAX`和`INT_MIN`的边界，则返回`INT_MAX`和`INT_MIN`。

# 代码

Python代码如下。

```python
import re
class Solution(object):
    def myAtoi(self, num):
        """
        :type str: str
        :rtype: int
        """
        num = num.strip()
        if not num:
            return 0
        res = re.findall(r"^[+-]?\d+", num)
        if not res:
            return 0
        res = int(res[0])
        return max(min(res, 2 ** 31 - 1), -2 ** 31)
```

 **欢迎关注[负雪明烛的刷题博客](https://blog.csdn.net/fuxuemingzhu)，leetcode刷题800多，每道都讲解了详细写法！**

# 日期

2020 年 4 月 3 日 —— 这几天怎么啥都不想干
