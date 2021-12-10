

作者： 		负雪明烛 
id：				fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)

题目地址：https://leetcode.com/problems/to-lower-case/description/

## 题目描述：

Implement function ToLowerCase() that has a string parameter str, and returns the same string in lowercase.

## 题目大意

把字符串的大写字母全都转化成小写。

## 解题方法

### ASIIC码操作

当然可以直接使用lower()函数，直接能过。但是，毕竟是让你实现么，所以动手写一下。

主要是判断字符处在'A'~'Z'之间，如果这样的话，就把它转成小写字符就行。其他的字符都不要改变。

代码如下：

```python
class Solution:
    def toLowerCase(self, str):
        """
        :type str: str
        :rtype: str
        """
        res = ""
        for s in str:
            if ord(s) >= ord('A') and ord(s) <= ord('Z'):
                res += chr(ord(s) - ord('A') + ord('a'))
            else:
                res += s
        return res
```

## 日期

2018 年 7 月 12 日 ———— 天阴阴地潮潮，已经连着两天这样了
