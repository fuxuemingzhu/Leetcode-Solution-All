# 【LeetCode】640. Solve the Equation 解题报告（Python）

标签（空格分隔）： LeetCode

作者： 		负雪明烛 
id：				fuxuemingzhu
个人博客：	http://fuxuemingzhu.me/

---

题目地址：https://leetcode.com/problems/solve-the-equation/description/

## 题目描述：

Solve a given equation and return the value of x in the form of string "x=#value". The equation contains only '+', '-' operation, the variable x and its coefficient.

If there is no solution for the equation, return "No solution".

If there are infinite solutions for the equation, return "Infinite solutions".

If there is exactly one solution for the equation, we ensure that the value of x is an integer.

Example 1:

    Input: "x+5-3+x=6+x-2"
    Output: "x=2"

Example 2:

    Input: "x=x"
    Output: "Infinite solutions"

Example 3:

    Input: "2x=x"
    Output: "x=0"

Example 4:

    Input: "2x+3x-6x=x+2"
    Output: "x=-1"

Example 5:

    Input: "x=x+2"
    Output: "No solution"

## 题目大意

求解一元线性方程，求得时候注意是否有解或者无穷解等条件。

## 解题方法

这种题本质都是用python实现一个数学操作，本身并不难，但是很烦！

这个题我的做法是先把式子分为左右式，如果式子以负号开头，给它替换成'0-'，然后把所有的-换成+，这样的目的是可以直接按照+去split字符串得到每个数字。然后判断数字是否包含x呀，来求出左边的x的数目，左边数字的和，右边x的数目，右边数字的和。底下实现所谓的移动分式，把x都移到左边，把数字都移动到右边。最后再根据题目的要求求解或者返回特殊情况即可。

```python
class Solution(object):
    def solveEquation(self, equation):
        """
        :type equation: str
        :rtype: str
        """
        left, right = equation.split('=')
        if left[0] == '-':
            left = '0' + left
        if right[0] == '-':
            right = '0' + right
        left = left.replace('-', '+-')
        right = right.replace('-', '+-')
        left_x, left_val, right_x, right_val = 0, 0, 0, 0
        for num in left.split('+'):
            if 'x' in num:
                if num == 'x':
                    left_x += 1
                elif num == '-x':
                    left_x -= 1
                else:
                    left_x += int(num[:-1])
            else:
                left_val += int(num)
        for num in right.split('+'):
            if 'x' in num:
                if num == 'x':
                    right_x += 1
                elif num == '-x':
                    right_x -= 1
                else:
                    right_x += int(num[:-1])
            else:
                right_val += int(num)
        left_x -= right_x
        right_val -= left_val
        if left_x != 0 and right_val == 0:
            return "x=0"
        elif left_x != 0 and right_val != 0:
            return 'x=' + str(right_val / left_x)
        elif left_x == 0 and right_val == 0:
            return "Infinite solutions"
        elif left_x == 0 and right_val != 0:
            return "No solution"
```


## 日期

2018 年 6 月 11 日 ———— 今天学科三在路上跑的飞快～