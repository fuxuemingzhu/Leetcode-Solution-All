# 【LeetCode】592. Fraction Addition and Subtraction 解题报告（Python）

标签（空格分隔）： LeetCode

作者： 		负雪明烛 
id：				fuxuemingzhu
个人博客：	http://fuxuemingzhu.me/

---

题目地址：https://leetcode.com/problems/fraction-addition-and-subtraction/description/

## 题目描述：

Given a string representing an expression of fraction addition and subtraction, you need to return the calculation result in string format. The final result should be irreducible fraction. If your final result is an integer, say 2, you need to change it to the format of fraction that has denominator 1. So in this case, 2 should be converted to 2/1.

Example 1:

    Input:"-1/2+1/2"
    Output: "0/1"

Example 2:

    Input:"-1/2+1/2+1/3"
    Output: "1/3"

Example 3:

    Input:"1/3-1/2"
    Output: "-1/6"

Example 4:

    Input:"5/3+1/3"
    Output: "2/1"

Note:

1. The input string only contains '0' to '9', '/', '+' and '-'. So does the output.
1. Each fraction (input and output) has format ±numerator/denominator. If the first input fraction or the output is positive, then '+' will be omitted.
1. The input only contains valid irreducible fractions, where the numerator and denominator of each fraction will always be in the range [1,10]. If the denominator is 1, it means this fraction is actually an integer in a fraction format defined above.
1. The number of given fractions will be in the range [1,10].
1. The numerator and denominator of the final result are guaranteed to be valid and in the range of 32-bit int.

## 题目大意

求分式运算的结果。返回时应该返回最简真分数。

## 解题方法

本身解题方法就是分数的加减法。

分式的减法法则是:

1. 同分母分式相加减，只把分子相加减，分母不变；
2. 异分母分式相加减，先通分变为同分母分式，再按同分母分式相加减的法则运算；
3. 完成分式的加减运算后，若所得分式不是既约分式应约分化为既约分式。

因为这里都是用真分数形式给出的，所以加的时候把分母通分，分子扩大相应的倍数再相加就好了。刚开始我把最后化为最简分数形式放在了最后一步，这样的话会造成分式的分子分母巨大，因此超时了。放到了每次加减完成之后就可以了。

另外，我还趟了一个坑：约分的时候，需要求绝对值，否则min(ans)之后可以是负值就尴尬了。

这里可以优化的一个地方就是约分的求最大公约数GCD哈。以后再改吧。

```python
class Solution(object):
    def fractionAddition(self, expression):
        """
        :type expression: str
        :rtype: str
        """
        if expression[0] == '-':
            expression = '0/1' + expression
        expression = expression.replace('-', '+-')
        son_moms = []
        for fractions in expression.split('+'):
            son_moms.append(map(int, fractions.split('/')))
        ans = [0, 1]
        for son_mom in son_moms:
            ans[0] = ans[0] * son_mom[1] + son_mom[0] * ans[1]
            ans[1] = ans[1] * son_mom[1]
            for div in range(2, abs(min(ans))):
                while (ans[0] % div == 0) and (ans[1] % div == 0):
                    ans[0] /= div
                    ans[1] /= div
        if ans[0] == 0:
            return '0/1'
        return str(ans[0]) + "/" + str(ans[1])
```


## 日期

2018 年 6 月 11 日 ———— 今天学科三在路上跑的飞快～