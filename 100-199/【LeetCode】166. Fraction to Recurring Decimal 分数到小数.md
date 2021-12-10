# 【LeetCode】166. Fraction to Recurring Decimal 解题报告（Python）

标签（空格分隔）： LeetCode

作者： 		负雪明烛 
id：				fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---

题目地址：https://leetcode.com/problems/fraction-to-recurring-decimal/description/

## 题目描述：

Given two integers representing the numerator and denominator of a fraction, return the fraction in string format.

If the fractional part is repeating, enclose the repeating part in parentheses.

Example 1:

    Input: numerator = 1, denominator = 2
    Output: "0.5"

Example 2:

    Input: numerator = 2, denominator = 1
    Output: "2"

Example 3:

    Input: numerator = 2, denominator = 3
    Output: "0.(6)"


## 题目大意

计算两个整数的除法，结果可能是小数。如果是循环小数，那么就把循环的部分用括号括起来。

## 解题方法

复习一下整数除法，用长除式的时候，不断地得到当前除法的商和余数，然后给余数部分补零继续做除法。当我们遇到了一个余数，而且这个余数在前面已经出现过了，那么就是出现了循环了。

所以，我们需要一个dict来保存出现过的余数，以及得出这个余数时候，结果出现的位置。所以再次得到这个余数的时候，就查出来了上次出现了的位置，中间这一段就是循环小数部分。

另外特别注意的是，这个题目支持负数除法，所以最好的方法全部转化为正整数的除法，先判断结果的符号，然后把结果变成正数。


代码如下：

```python
class Solution:
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        d = dict()
        div, mod = self.divmod(numerator, denominator)
        if mod == 0:
            return str(div)
        ans = "-" if ((numerator > 0) ^ (denominator > 0)) else ""
        div, mod, denominator = abs(div), abs(mod), abs(denominator)
        ans += str(div) + "."
        d[mod] = len(ans)
        while mod:
            mod *= 10
            div, mod = self.divmod(mod, denominator)
            ans += str(div)
            if mod in d:
                index = d[mod]
                ans = ans[:index] + "(" + ans[index:] + ")"
                break
            else:
                d[mod] = len(ans)
        return ans

    def divmod(self, a, b):
        q = int(a / b)   # I'm using 3.x
        r = a - b * q
        return (q, r)
```

上面的代码自定义了divmod是因为python的divmod是向下取整，这样的话对于负数不友好。既然按照上面的思路先转化为正数再算，就可以使用原生的divmod。代码如下：

```python
class Solution:
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        if numerator == 0: return "0"
        d = dict()
        ans = "-" if ((numerator > 0) ^ (denominator > 0)) else ""
        numerator, denominator = abs(numerator), abs(denominator)
        div, mod = divmod(numerator, denominator)
        if mod == 0: return ans + str(div)
        ans += str(div) + "."
        d[mod] = len(ans)
        while mod:
            mod *= 10
            div, mod = divmod(mod, denominator)
            ans += str(div)
            if mod in d:
                index = d[mod]
                ans = ans[:index] + "(" + ans[index:] + ")"
                break
            else:
                d[mod] = len(ans)
        return ans
```

## 日期

2018 年 9 月 8 日 ———— 美好的周末，从刷题开始


  [1]: https://leetcode.com/static/images/problemset/diagonal_traverse.png
  [2]: https://blog.csdn.net/fuxuemingzhu/article/details/82390672