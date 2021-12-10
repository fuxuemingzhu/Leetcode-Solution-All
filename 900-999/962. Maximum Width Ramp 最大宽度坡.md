
作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)


题目地址：https://leetcode.com/problems/maximum-width-ramp/


## 题目描述

Given an array ``A`` of integers, a ramp is a tuple ``(i, j)`` for which ``i < j`` and ``A[i] <= A[j]``.  The width of such a ramp is ``j - i``.

Find the maximum width of a ramp in ``A``.  If one doesn't exist, return 0.

 

Example 1:

    Input: [6,0,8,2,1,5]
    Output: 4
    Explanation: 
    The maximum width ramp is achieved at (i, j) = (1, 5): A[1] = 0 and A[5] = 5.

Example 2:

    Input: [9,8,1,0,1,9,4,0,4,1]
    Output: 7
    Explanation: 
    The maximum width ramp is achieved at (i, j) = (2, 9): A[2] = 1 and A[9] = 1.
 

Note:

1. 2 <= A.length <= 50000
1. 0 <= A[i] <= 50000


## 题目大意

找出最大的j-i，使得``i<j``并且``A[i] <= A[j]``。

## 解题方法

### 单调栈

周赛的时候拿到这个题，第一想法肯定是对于每个数字都去找在它的左边，最远的那个小于等于它的数字。然后就很容易分析出，我们想要保存的是每个数字第一次出现的位置，而且依次只用保留最小的即可（数字最小才能保证距离最远）。从而就抽象出了单调栈这个数据结构。

这里用到的是单调递减栈，如果遇到一个数字，比栈顶元素更小，那么就入栈；否则就在栈里边向后找到第一个刚好小于等于它的元素，此时的距离就是最远距离。

本来想用C++语言打周赛，但是还是Python方便一点，直接用python保存位置和元素的tuple即可。

同样适用单调栈的题目有：[503. Next Greater Element II](https://blog.csdn.net/fuxuemingzhu/article/details/79463006)

python代码如下：

```python
class Solution(object):
    def maxWidthRamp(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        N = len(A)
        stack = []
        res = 0
        for i, a in enumerate(A):
            if not stack or stack[-1][1] > a:
                stack.append((i, a))
            else:
                x = len(stack) - 1
                while x >= 0 and stack[x][1] <= a:
                    res = max(res, i - stack[x][0])
                    x -= 1
        return res
```


## 日期

2018 年 12 月 23 日 —— 周赛成绩新高


  [1]: https://blog.csdn.net/fuxuemingzhu/article/details/79368360
