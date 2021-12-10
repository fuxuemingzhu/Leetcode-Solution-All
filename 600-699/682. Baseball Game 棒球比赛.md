
作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)

题目地址：[https://leetcode.com/problems/baseball-game/description/][1]


## 题目描述

You're now a baseball game point recorder.

Given a list of strings, each string can be one of the 4 following types:

1. ``Integer`` (one round's score): Directly represents the number of points you get in this round.
1. ``"+"`` (one round's score): Represents that the points you get in this round are the sum of the last two ``valid`` round's points.
1. ``"D"`` (one round's score): Represents that the points you get in this round are the doubled data of the last ``valid`` round's points.
1. ``"C"`` (an operation, which isn't a round's score): Represents the last ``valid`` round's points you get were ``invalid`` and should be removed.

Each round's operation is permanent and could have an impact on the round before and the round after.

You need to return the sum of the points you could get in all the rounds.

Example 1:

    Input: ["5","2","C","D","+"]
    Output: 30
    Explanation: 
    Round 1: You could get 5 points. The sum is: 5.
    Round 2: You could get 2 points. The sum is: 7.
    Operation 1: The round 2's data was invalid. The sum is: 5.  
    Round 3: You could get 10 points (the round 2's data has been removed). The sum is: 15.
    Round 4: You could get 5 + 10 = 15 points. The sum is: 30.

Example 2:

    Input: ["5","-2","4","C","D","9","+","+"]
    Output: 27
    Explanation: 
    Round 1: You could get 5 points. The sum is: 5.
    Round 2: You could get -2 points. The sum is: 3.
    Round 3: You could get 4 points. The sum is: 7.
    Operation 1: The round 3's data is invalid. The sum is: 3.  
    Round 4: You could get -4 points (the round 3's data has been removed). The sum is: -1.
    Round 5: You could get 9 points. The sum is: 8.
    Round 6: You could get -4 + 9 = 5 points. The sum is 13.
    Round 7: You could get 9 + 5 = 14 points. The sum is 27.

Note:
1. The size of the input list will be between 1 and 1000.
1. Every integer represented in the list will be between -30000 and 30000.

## 题目大意

模拟棒球游戏，游戏规则是：

1. 如果是数字，那么代表本局得分
2. 如果是``"+"``，代表本局得分是前两局的和
3. 如果是``"C"``，代表上一轮的得分是无效的
4. 如果是``"D"``，代表本轮得分是上一轮的二倍

## 解题方法

### 使用栈模拟

这个题貌似困难，其实只要用了一个栈就很简单了。

只需要判断本局的操作，然后对应的移除栈顶、栈顶翻倍、栈顶求和、数字进栈等等。最后对栈的所有元素进行求和。

```python
class Solution(object):
    def calPoints(self, ops):
        """
        :type ops: List[str]
        :rtype: int
        """
        valid = []
        for op in ops:
            if op == 'C':
                valid.pop()
            elif op == 'D':
                valid.append(valid[-1] * 2)
            elif op == '+':
                valid.append(valid[-1] + valid[-2])
            else:
                valid.append(int(op))
        return sum(valid)
```

## 日期

2018 年 1 月 27 日 
2018 年 11 月 8 日 —— 项目进展缓慢

  [1]: https://leetcode.com/problems/baseball-game/description/
