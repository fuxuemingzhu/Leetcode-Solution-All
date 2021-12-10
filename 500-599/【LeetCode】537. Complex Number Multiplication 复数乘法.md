
作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)

题目地址：https://leetcode.com/problems/complex-number-multiplication/description/

## 题目描述

Given two strings representing two complex numbers.

You need to return a string representing their multiplication. Note i2 = -1 according to the definition.

Example 1:

    Input: "1+1i", "1+1i"
    Output: "0+2i"
    Explanation: (1 + i) * (1 + i) = 1 + i2 + 2 * i = 2i, and you need convert it to the form of 0+2i.

Example 2:

    Input: "1+-1i", "1+-1i"
    Output: "0+-2i"
    Explanation: (1 - i) * (1 - i) = 1 + i2 - 2 * i = -2i, and you need convert it to the form of 0+-2i.

Note:

1. The input strings will not have extra blank.
1. The input strings will be given in the form of a+bi, where the integer a and b will both belong to the range of [-100, 100]. And the output should be also in this form.

## 解题方法

方法一：

求两个复数的乘积。这个题中已经说明了一定会存在+号，这就是留个我们根据格式化的表达读取数字的实虚部用的。

另外，注意字符串的格式化时，后面所有的变量必须用括号括起来才行，也就是tuple型。


```python
class Solution(object):
    def complexNumberMultiply(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        num1 = map(int, a[:-1].split('+'))
        num2 = map(int, b[:-1].split('+'))
        real = num1[0] * num2[0] - num1[1] * num2[1]
        virtual = num1[0] * num2[1] + num1[1] * num2[0]
        return "%d+%di" % (real, virtual)
```

C++处理的字符串的时候稍微麻烦了一些。

```cpp
class Solution {
public:
    string complexNumberMultiply(string a, string b) {
        int ap = a.find('+');
        int ar = stoi(a.substr(0, ap));
        int ai = stoi(a.substr(ap + 1, a.size() - 1));
        int bp = b.find('+');
        int br = stoi(b.substr(0, bp));
        int bi = stoi(b.substr(bp + 1, b.size() - 1));
        string ansr = to_string(ar * br - ai * bi);
        string ansi = to_string(ar * bi + ai * br);
        return ansr + '+' + ansi + 'i';
    }
};
```

## 日期

2018 年 2 月 5 日 
2018 年 12 月 4 日 —— 周二啦！
