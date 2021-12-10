
作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)

题目地址：https://leetcode.com/problems/decode-string/description/


## 题目描述

Given an encoded string, return it's decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; No extra white spaces, square brackets are well-formed, etc.

Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there won't be input like 3a or 2[4].

Examples:

    s = "3[a]2[bc]", return "aaabcbc".
    s = "3[a2[c]]", return "accaccacc".
    s = "2[abc]3[cd]ef", return "abcabccdcdcdef".

## 题目大意

对字符串进行解码，字符串的编码方式是数字+[字符串] == > 字符串连续重复数字次。求最后解码的字符串是多少。

## 解题方法

### 栈

看到括号匹配的题肯定想到用栈去做。

这个题，遇到'['就把之前的字符串进行进栈操作。遇到']'进行出栈操作。

curstring保存的是出栈操作完成后的字符串。

注意这一步：``curstring = prestring + prenum * curstring``，prestring是前面的字符串，prenum * curstring是这一步骤结束之后的字符串，所以是前面的字符串+现在的字符串得到目前已有的字符串。

```python
class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        curnum = 0
        curstring = ''
        stack = []
        for char in s:
            if char == '[':
                stack.append(curstring)
                stack.append(curnum)
                curstring = ''
                curnum = 0
            elif char == ']':
                prenum = stack.pop()
                prestring = stack.pop()
                curstring = prestring + prenum * curstring
            elif char.isdigit():
                curnum = curnum * 10 + int(char)
            else:
                curstring += char
        return curstring
```


## 日期

2018 年 2 月 17 日 
2019 年 1 月 2 日 —— 2019年开刷
