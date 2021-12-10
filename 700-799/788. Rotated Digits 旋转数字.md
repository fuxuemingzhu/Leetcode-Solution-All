
作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)

题目地址：https://leetcode.com/problems/rotated-digits/description/


## 题目描述

X is a good number if after rotating each digit individually by 180 degrees, we get a valid number that is different from X. A number is valid if each digit remains a digit after rotation. 0, 1, and 8 rotate to themselves; 2 and 5 rotate to each other; 6 and 9 rotate to each other, and the rest of the numbers do not rotate to any other number.

Now given a positive number N, how many numbers X from 1 to N are good?

    Example:
    Input: 10
    Output: 4
    Explanation: 
    There are four good numbers in the range [1, 10] : 2, 5, 6, 9.
    Note that 1 and 10 are not good numbers, since they remain unchanged after rotating.

Note:

1. N  will be in range [1, 10000].

## 题目大意

在[1,N]双闭区间中，有多少个数字，将其倒影之后和自身不同。

## 解题方法

重要的是理解题意，就好比下面的这个倒影，要求倒影和自身不同，但倒影也必须是数字：

![此处输入图片的描述][1]

可以总结出以下的要求：

1. 该数字中不含``[3, 4, 7]``，否则其倒影不是数字。
2. 该数字中必须包含``[2, 5, 6, 9]``中的至少一个，否则倒影和原数字相同

最后的结果是有多少个，遍历之后很容易得到答案。

```python
class Solution(object):
    def rotatedDigits(self, N):
        """
        :type N: int
        :rtype: int
        """
        valid = [2, 5, 6, 9]
        nonValid = [3, 4, 7]
        def isGood(num):
            for y in nonValid:
                if str(y) in str(num):
                    return False
            return any(str(x) in str(num) for x in valid)
        return sum(map(int, [isGood(n) for n in range(1, N + 1)]))
```

二刷，基于同样的思想，写了一个更简洁的代码。

```python
class Solution(object):
    def rotatedDigits(self, N):
        """
        :type N: int
        :rtype: int
        """
        dmap = {"0" : "0", "1" : "1", "8" : "8", "2" : "5", "5" : "2", "6" : "9", "9" : "6"}
        res = 0
        for num in range(1, N + 1):
            numlist = list(str(num))
            if any(x in numlist for x in ["3", "4", "7"]):
                continue
            numRotate = map(lambda x : dmap[x], numlist)
            if numRotate == numlist:
                continue
            res += 1
        return res
```

看了别人的提交，发现了一个更简单的思路，就是我们不需要把翻转后的数字构建出来，我们只需要找出特定的字符是否在字符串中即可。比如，如果数字包含``["3", "4", "7"]``，那么肯定不可以。如果数字包含``["2", "5", "6", "9"]``，那么一定可以。如果这些数字都不包含，那么就是翻转之后是自身的数字，就不能计算到结果里。


```python
class Solution(object):
    def rotatedDigits(self, N):
        """
        :type N: int
        :rtype: int
        """
        dmap = {"0" : "0", "1" : "1", "8" : "8", "2" : "5", "5" : "2", "6" : "9", "9" : "6"}
        res = 0
        for num in range(1, N + 1):
            if any(x in str(num) for x in ["3", "4", "7"]):
                continue
            if any(x in str(num) for x in ["2", "5", "6", "9"]):
                res += 1
        return res
```

## 日期

2018 年 2 月 26 日 
2018 年 11 月 11 日 —— 剁手节快乐

  [1]: http://bpic.588ku.com/element_pic/00/00/07/125784e23ebbd9a.jpg
