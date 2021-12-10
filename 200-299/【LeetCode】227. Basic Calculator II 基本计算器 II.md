# 【LeetCode】227. Basic Calculator II 解题报告（Python）

标签（空格分隔）： LeetCode

作者： 		负雪明烛 
id：				fuxuemingzhu
个人博客：	http://fuxuemingzhu.me/

---

题目地址：https://leetcode.com/problems/basic-calculator-ii/description/

## 题目描述：

Implement a basic calculator to evaluate a simple expression string.

The expression string contains only non-negative integers, +, -, *, / operators and empty spaces . The integer division should truncate toward zero.

Example 1:

    Input: "3+2*2"
    Output: 7

Example 2:

    Input: " 3/2 "
    Output: 1

Example 3:

    Input: " 3+5 / 2 "
    Output: 5

Note:

- You may assume that the given expression is always valid.
- Do not use the eval built-in library function.

## 题目大意

给算数表达式求值。

## 解题方法

直接使用eval可以过。。然后算法的话，使用下下面的方法：

用num保存上一个数字，用pre_op保存上一个操作符。当遇到新的操作符的时候，需要根据pre_op进行操作。乘除的优先级高于加减。所以有以下规则：

之前的运算符是+，那么需要把之前的数字num进栈，然后等待下一个操作数的到来。
之前的运算符是-，那么需要把之前的数字求反-num进栈，然后等待下一个操作数的到来。
之前的运算符是×，那么需要立刻出栈和之前的数字相乘，重新进栈，然后等待下一个操作数的到来。
之前的运算符是/，那么需要立刻出栈和之前的数字相除，重新进栈，然后等待下一个操作数的到来。

注意比较的都是之前的操作符和操作数，现在遇到的操作符是没有什么用的。

另外，坑爹的Python地板除。。比如-3//2=2的，和c++不一样。因此真正操作的时候如果遇到负数，使用的用浮点除再取整的方式获得和c++一样的结果。


```python3
class Solution:
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []
        pre_op = '+'
        num = 0
        for i, each in enumerate(s):
            if each.isdigit():
                num = 10 * num + int(each)
            if i == len(s) - 1 or each in '+-*/':
                if pre_op == '+':
                    stack.append(num)
                elif pre_op == '-':
                    stack.append(-num)
                elif pre_op == '*':
                    stack.append(stack.pop() * num)
                elif pre_op == '/':
                    top = stack.pop()
                    if top < 0:
                        stack.append(int(top / num))
                    else:
                        stack.append(top // num)
                pre_op = each
                num = 0
        return sum(stack)

```

## 日期

2018 年 6 月 27 日 ———— 阳光明媚，心情大好，抓紧科研啊