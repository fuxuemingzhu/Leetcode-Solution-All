作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)


题目地址：https://leetcode.com/problems/flip-string-to-monotone-increasing/description/

## 题目描述

A string of ``'0'``s and ``'1'``s is monotone increasing if it consists of some number of ``'0'``s (possibly 0), followed by some number of ``'1'``s (also possibly 0.)

We are given a string S of ``'0'``s and ``'1'``s, and we may flip any ``'0'`` to a ``'1'`` or a ``'1'`` to a ``'0'``.

Return the minimum number of flips to make ``S`` monotone increasing.

 

Example 1:

    Input: "00110"
    Output: 1
    Explanation: We flip the last digit to get 00111.

Example 2:

    Input: "010110"
    Output: 2
    Explanation: We flip to get 011111, or alternatively 000111.

Example 3:
    
    Input: "00011000"
    Output: 2
    Explanation: We flip to get 00000000.
     

Note:

1. 1 <= S.length <= 20000
1. S only consists of '0' and '1' characters.

## 题目大意

一个字符串中有0有1，问最少翻转多少个字符能够使得这个字符串编程一个单调递增的字符串。

## 解题方法

### Prefix计算

周赛第二题，这个题还是有点难度的，不好想。

常规的做法是，我们使用Prefix数组保存每个位置之前的1有多少个。因为我们最终的目标是变成前面是0后面是1的字符串，所以，可以通过过一遍数组，要把遍历到的位置前面都变0后面都变1，需要计算每个位置前面有多少个1加上后面有多少个0。因为前面的1要翻转成0，后面的0要翻转成1.

总之，只需要先求出每个位置前面的1的个数是多少，那么，再次遍历，求每个位置前面的1个数和后面0个数的和的最小值即可。

使用的是P数组保存每个位置前面1的个数。那么后面0的个数是：总的0的个数(即，总个数减去总的1的个数） - 前面0的个数（即，现在的位置索引减去前面1的个数）。

时间复杂度是O(N)，空间复杂度是O(N).

```python
class Solution(object):
    def minFlipsMonoIncr(self, S):
        """
        :type S: str
        :rtype: int
        """
        N = len(S)
        P = [0] # how many ones
        res = float('inf')
        for s in S:
            P.append(P[-1] + int(s))
        return min(P[i] + (N - P[-1]) - (i - P[i]) for i in range(len(P)))
```

### 动态规划

工位对面的大师想出来的方法，我自愧不如啊，看了很久还要请教一下才能勉强弄懂出来的样子。

这个题和买卖股票有点类似，都需要使用一个二维dp数组，分别保存的是以0结尾或者以1结尾的字符串需要翻转的最小次数。

为了方便，给dp数组多了一个空间，表示最前面的字符串还没有开始的时候，肯定不需要做任何翻转。

那么，当我们遍历到字符串的i位置时:

1. 如果这个位置的字符是``'0'``，那么：

- 当前以0结尾的dp数组等于前面的以0结尾的dp，即不需要做任何操作，此时前面必须是0结尾;
- 当前以1结尾的dp数组等于Min(前面的以0结尾的dp + 1，前面的以1结尾的dp + 1)。这里的含义是一种情况为前面的0到前面的那个位置结束，把当前的0翻转成1；另一种情况是前面一位以1结束不变，把当前的0翻转成1。需要求这两个情况的最小值。此时前面可以以0或者1结尾。

1. 如果这个位置的字符是``'1'``，那么：

- 当前以0结尾的dp数组等于前面的以0结尾的dp + 1，即把当前的1翻转成0，此时前面只能以0结尾；
- 当前以1结尾的dp数组等于``Min(前面的以0结尾的dp，前面的以1结尾的dp)``。这里的含义是该位置以1结尾需要翻转多少次呢？当然是前面翻转0或者1的次数最小值，因为当前的1一定不用翻转，而前面无论怎么翻转都能满足条件。此时前面可以以0或者1结尾。

总结一下思路，首先一定要明白dp数组是代表以这个第二维度数字结尾的状态数，比如dp[i][0]就是第i个数字以0结尾的情况下，需要翻转的个数。然后，要明白的是如果遍历到的这个字符并没有限制死我们是否要翻转它，所以翻转不翻转都要考虑到，即这个对应位置变成1或者0两种情况下dp怎么更新。更新的方式是看前面一个状态，从前一个状态转成现在要变成的状态，需要做哪些操作，翻转次数怎么变化。

时间复杂度是O(N)，空间复杂度是O(N).

```python
class Solution(object):
    def minFlipsMonoIncr(self, S):
        """
        :type S: str
        :rtype: int
        """
        N = len(S)
        dp = [[0] * 2 for _ in range(N + 1)]
        for i in range(1, N + 1):
            if S[i - 1] == '0':
                dp[i][0] = dp[i - 1][0]
                dp[i][1] = min(dp[i - 1][1], dp[i - 1][0]) + 1
            else:
                dp[i][0] = dp[i - 1][0] + 1
                dp[i][1] = min(dp[i - 1][1], dp[i - 1][0])
        return min(dp[N][0], dp[N][1])
```

显然，上面的做法中，每次dp转移操作只和前面的一个状态有关，所以，可以优化空间复杂度到O(1)。代码如下：


```python
class Solution(object):
    def minFlipsMonoIncr(self, S):
        """
        :type S: str
        :rtype: int
        """
        N = len(S)
        dp = [0] * 2
        for i in range(1, N + 1):
            if S[i - 1] == '0':
                dp[0] = dp[0]
                dp[1] = min(dp[1], dp[0]) + 1
            else:
                dp[1] = min(dp[1], dp[0])
                dp[0] = dp[0] + 1
        return min(dp[0], dp[1])
```

## 参考资料

https://leetcode.com/problems/flip-string-to-monotone-increasing/discuss/183859/Java-DP-using-O(N)-time-and-O(1)-space

## 日期

2018 年 10 月 21 日 —— 这个周赛有点难


  [1]: https://blog.csdn.net/fuxuemingzhu/article/details/79534213
