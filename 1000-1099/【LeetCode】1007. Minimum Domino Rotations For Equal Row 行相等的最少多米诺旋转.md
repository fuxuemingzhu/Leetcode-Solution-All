作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)


题目地址：https://leetcode.com/problems/minimum-domino-rotations-for-equal-row/

## 题目描述

In a row of dominoes, ``A[i]`` and ``B[i]`` represent the top and bottom halves of the ``i``-th domino.  (A domino is a tile with two numbers from 1 to 6 - one on each half of the tile.)

We may rotate the ``i``-th domino, so that ``A[i]`` and ``B[i]`` swap values.

Return the minimum number of rotations so that all the values in ``A`` are the same, or all the values in ``B`` are the same.

If it cannot be done, return ``-1``.


Example 1:

![此处输入图片的描述][1]

    Input: A = [2,1,2,4,2,2], B = [5,2,6,2,3,2]
    Output: 2
    Explanation: 
    The first figure represents the dominoes as given by A and B: before we do any rotations.
    If we rotate the second and fourth dominoes, we can make every value in the top row equal to 2, as indicated by the second figure.

Example 2:

    Input: A = [3,5,1,2,3], B = [3,6,3,3,4]
    Output: -1
    Explanation: 
    In this case, it is not possible to rotate the dominoes to make one row of values equal.
     

Note:

1. 1 <= A[i], B[i] <= 6
1. 2 <= A.length == B.length <= 20000

## 题目大意

有一排多米诺骨牌，A, B分别代表每个牌的正反面。现在要求我们翻转其中的一部分骨牌，使得正反面对调，能不能让A或者B出现完全相同的点数？如果可以的话，需要返回最少的翻转次数。如果不可以，需要返回-1.

## 解题方法

### 遍历一遍

我们需要对这个题做分析：先把A,B两面的数字做一个统计，如果出现最多的点数<牌的个数，那么无论如何都无法翻转成功。如果出现最多的点数=牌的个数，那么这个时候需要保证每一个牌的都有且只有一面的点数是这个最多的点数。如果出现最多的点数>牌的个数，那么需要保证每个牌都至少有一面是这个数字，此时两面都是这个数字的话，就不用翻转。

所以：

如果两面相等都等于出现最多的数字target，不用翻转。

我们需要使用两个数字分别表示向该面翻转的次数。如果只有一面等于target，就把向另一面翻转的次数+1.

在任何时候，只要这个牌的正反面有一面不是出现最多的数字，那么一定返回-1.

我们最终只需要返回两个方向翻转的次数的最小值即可。

下面做一下讨论：为什么只用统计出现最多的数字就行，为什么出现次数第二多的次数一定没有机会？

1.如果出现最多的数字的次数<长度，无论第一第二都不行。
2.如果出现最多的次数=长度，这个时候第二多次数如果等于N，那么两者效果一样，如果第二多次数如果小于N，那么不可能。
3.如果出现最多的次数>N，这个时候一定会出现某些牌的正反面都是该最多的数字。此时第二多的数字没有机会。

总之，只需要判断出现最多的数字即可。

Python代码如下：

```python
class Solution(object):
    def minDominoRotations(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        N = len(A)
        count = collections.Counter(A + B)
        if count.most_common(1)[0][1] < N:
            return -1
        target = count.most_common(1)[0][0]
        a_swap = 0
        b_swap = 0
        for i in range(N):
            if A[i] == B[i]:
                if A[i] == target:
                    continue
                else:
                    return -1
            elif A[i] == target:
                b_swap += 1
            elif B[i] == target:
                a_swap += 1
            else:
                return -1
        return min(a_swap, b_swap)
```


## 日期

2019 年 3 月 10 日 —— 周赛进了第一页！


  [1]: https://assets.leetcode.com/uploads/2019/03/08/domino.png
