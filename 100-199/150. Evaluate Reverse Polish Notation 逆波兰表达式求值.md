# 【LeetCode】150. Evaluate Reverse Polish Notation 解题报告（Python）

标签： LeetCode

---

题目地址：https://leetcode.com/problems/evaluate-reverse-polish-notation/description/

## 题目描述：

Evaluate the value of an arithmetic expression in Reverse Polish Notation.

Valid operators are +, -, *, /. Each operand may be an integer or another expression.

    Some examples:
      ["2", "1", "+", "3", "*"] -> ((2 + 1) * 3) -> 9
      ["4", "13", "5", "/", "+"] -> (4 + (13 / 5)) -> 6

## 题目大意

后缀表达式转中缀表达式，并且求值。

## 解题方法

python 有个牛逼的函数，就是``eval()``，可以给它一个运算表达式，直接给你求值。中缀表达式转正常表达式很简单了，直接用栈就行。

但是！！需要注意的是，python中的'/'负数除法和c语言不太一样。在python中，(-1)/2=-1，而在c语言中，(-1)/2=0。也就是c语言中，除法是向零取整，即舍弃小数点后的数。而在python中，是向下取整的。而这道题的oj是默认的c语言中的语法，所以需要在遇到'/'的时候注意一下。

一种方式是采用负负得正的方法，用两个负号变成整数的除法，再取负。

另一种方式是使用``operator.truediv(int(a), int(b))``变成和c相同的方式。

```python
class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        operators = ['+', '-', '*', '/']
        for token in tokens:
            if token not in operators:
                stack.append(token)
            else:
                b = stack.pop()
                a = stack.pop()
                if token == '/' and int(a) * int(b) < 0:
                    res = eval('-' + '(' + '-' + a + '/' + b + ')')
                else:
                    res = eval(a + token + b)
                stack.append(str(res))
        return int(stack.pop())
```

或者：

```python
class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        operators = ['+', '-', '*', '/']
        for token in tokens:
            if token not in operators:
                stack.append(token)
            else:
                b = stack.pop()
                a = stack.pop()
                if token == '/':
                    res = int(operator.truediv(int(a), int(b)))
                else:
                    res = eval(a + token + b)
                stack.append(str(res))
        return int(stack.pop())
```

## 日期

2018 年 3 月 14 日 