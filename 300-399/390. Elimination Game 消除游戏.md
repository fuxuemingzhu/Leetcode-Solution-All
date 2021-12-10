# 【LeetCode】390. Elimination Game 解题报告（Python） 

标签： LeetCode

---

题目地址：https://leetcode.com/problems/elimination-game/description/

## 题目描述：

There is a list of sorted integers from 1 to n. Starting from left to right, remove the first number and every other number afterward until you reach the end of the list.

Repeat the previous step again, but this time from right to left, remove the right most number and every other number from the remaining numbers.

We keep repeating the steps again, alternating left to right and right to left, until a single number remains.

Find the last number that remains starting with a list of length n.

    Example:
    
    Input:
    n = 9,
    1 2 3 4 5 6 7 8 9
    2 4 6 8
    2 6
    6
    
    Output:
    6

## 题目大意

消除游戏。

分为两种消除的方式，第一种是从左向右，从第一个位置开始间隔着消除；第二种是从右向左，从最后一个位置开始间隔这消除。

求最后能留下的最后的结果是哪个数。

## 解题方法

看到这个题，我一定能肯定，这个题的不是使用暴力去求解的，否则没有意义。这个题的做法非常巧妙。消除的规律是同样的，只不过顺序不同，那么，可以封装成两个函数，互相调用达到目的。这是建立在这个思想上的：

> 第一次从左向右检索完，剩下，2 4 6 8， 其实这跟1 2 3
> 4的信息几乎是一样的，只是差了倍数2，所以问题就变为从右往左对规模4的问题进行操作，找到答案乘以2就行。对于从右往左，如果是1 2 3 4
> 5的话，检索完还剩2 4，同样是1 2的问题，如果是 1 2 3 4，剩 1 3，我们可以认为是1
> 2乘以2减一，总之，我们可以找到将每次的剩余子序列转化为同类子问题的方法。

这个算是分而治之的思想，很巧妙的通过2倍关系实现了递归调用。

```python
class Solution(object):
    def lastRemaining(self, n):
        """
        :type n: int
        :rtype: int
        """
        return self.leftToRight(n)
        
    def leftToRight(self, n):
        if n == 1: return 1
        if n == 2: return 2
        if n & 1 == 1:
            return 2 * self.rightToLeft((n - 1) / 2)
        else:
            return 2 * self.rightToLeft(n / 2)
        
    def rightToLeft(self, n):
        if n == 1: return 1
        if n == 2: return 1
        if n & 1 == 1:
            return 2 * self.leftToRight((n - 1) / 2)
        else:
            return 2 * self.leftToRight(n / 2) - 1
```

## 日期

2018 年 3 月 12 日 
