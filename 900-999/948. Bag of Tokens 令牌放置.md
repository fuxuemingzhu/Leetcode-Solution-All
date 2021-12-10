作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)


题目地址：https://leetcode.com/problems/bag-of-tokens/description/


## 题目描述

You have an initial power ``P``, an initial score of ``0`` points, and a bag of tokens.

Each token can be used at most once, has a value ``token[i]``, and has potentially two ways to use it.

- If we have at least ``token[i]`` power, we may play the token face up, losing ``token[i]`` power, and gaining ``1`` point.
- If we have at least ``1`` point, we may play the token face down, gaining ``token[i]`` power, and losing ``1`` point.

Return the largest number of points we can have after playing any number of tokens.

 

Example 1:

    Input: tokens = [100], P = 50
    Output: 0

Example 2:

    Input: tokens = [100,200], P = 150
    Output: 1

Example 3:

    Input: tokens = [100,200,300,400], P = 200
    Output: 2
 

Note:

1. tokens.length <= 1000
1. 0 <= tokens[i] < 10000
1. 0 <= P < 10000
 

## 题目大意

有个power，现在有两种操作：

1. 当power超过token[i]的时候，可以把token[i]进行翻转成正面，然后得到了1个点；
2. 当至少有1个点的时候，可以把任何一个token[i]进行翻转成反面，然后丢失1个点。

可以认为token在刚开始的时候既不是正面也不是反面。

问最后能获得的最多的点数是多少。

## 解题方法



### 贪心算法

使用了两个指针，左边指向翻成正面的token，右边指向翻成反面的token.

首先，对token先排序。

第一步，我们用现在所有的power把左边的都翻成正面，同时获得了一些点。这一步之后，我们使用power贪心地获得了所有的点数。

第二步，我们看右边能翻转多少个反面，这个能获得Power，所以我们使用的点数换取了更多的power.

这两步来回走的话，就能获得更多的Points。

需要注意的是，如果剩余的token只有一个的时候，我们是不把它换成power的。

```python
class Solution(object):
    def bagOfTokensScore(self, tokens, P):
        """
        :type tokens: List[int]
        :type P: int
        :rtype: int
        """
        print(tokens)
        tokens.sort()
        N = len(tokens)
        left, right = 0, N - 1
        points = 0
        remain = N
        while left < N and P >= tokens[left]:
            P -= tokens[left]
            points += 1
            left += 1
            remain -= 1
        if left == 0 or left == N: return points
        while points > 0 and remain > 1:
            P += tokens[right]
            right -= 1
            points -= 1
            remain -= 1
            while left <= right and P >= tokens[left]:
                P -= tokens[left]
                points += 1
                left += 1
                remain -= 1
        return points
```


## 日期

2018 年 11 月 24 日 —— 周日开始！一周就过去了～


  [1]: http://zxi.mytechroad.com/blog/dynamic-programming/leetcode-730-count-different-palindromic-subsequences/
