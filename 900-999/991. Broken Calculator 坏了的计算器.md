作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)


题目地址：https://leetcode.com/problems/broken-calculator/


## 题目描述

On a broken calculator that has a number showing on its display, we can perform two operations:

- **Double**: Multiply the number on the display by 2, or;
- **Decrement**: Subtract 1 from the number on the display.

Initially, the calculator is displaying the number ``X``.

Return the minimum number of operations needed to display the number ``Y``.

Example 1:

    Input: X = 2, Y = 3
    Output: 2
    Explanation: Use double operation and then decrement operation {2 -> 4 -> 3}.

Example 2:

    Input: X = 5, Y = 8
    Output: 2
    Explanation: Use decrement and then double {5 -> 4 -> 8}.

Example 3:

    Input: X = 3, Y = 10
    Output: 3
    Explanation:  Use double, decrement and double {3 -> 6 -> 5 -> 10}.

Example 4:
    
    Input: X = 1024, Y = 1
    Output: 1023
    Explanation: Use decrement operations 1023 times.
 

Note:

1. ``1 <= X <= 10^9``
1. ``1 <= Y <= 10^9``


## 题目大意

有一个坏掉了的计算器，只能对现在正在显示的数字进行两种操作：

1. 翻倍
2. 减1

已知初始化的时候计算器显示的数字是X，问最少需要多少步操作才能得到目标数字Y。

## 解题方法

这个题第一感觉肯定是BFS，但是很显然数字的取值范围太大，BFS会超时。

那么这个题就是个数学问题了……下面的内容摘自[演员的自我修养][1]：

1. 首先我们发现x要么乘2要么减1，如果x初始就比y大，那么只能一直做减法！

2. 在x小于y的情况下：

- 如果y是奇数，那么最后一个操作一定是减1（显然）
- 如果y是偶数呢？最后操作一定是乘2吗？答案是yes!

因为对于某个x现在要变为y可能是``先乘2再做若干次减``法，也可能是先``做若干次减法再乘2``
第一种用式子表示为``1 + 2*x-y``，第二种用式子表示为``x-y/2 + 1``
显然式子2的结果永远小于等于式子1的结果！

所以，我们想要最小化次数一定是先减法再乘2，也就是y为偶数时，最后的操作一定是乘2。

那么这里我们就从y开始反推，是奇数就加1，是偶数就除2，一直到y小于等于x为止！

python代码如下：

```python
class Solution(object):
    def brokenCalc(self, X, Y):
        """
        :type X: int
        :type Y: int
        :rtype: int
        """
        if X > Y: return X - Y
        res = 0
        while X < Y:
            if Y % 2 == 1:
                Y += 1
                res += 1
            Y //= 2
            res += 1
        return res + X - Y
```

## 日期

2019 年 2 月 21 日 —— 一放假就再难抓紧了


  [1]: https://buptwc.com/2019/02/10/Leetcode-991-Broken-Calculator/
  [2]: https://zhanghuimeng.github.io/post/leetcode-991-broken-calculator/
