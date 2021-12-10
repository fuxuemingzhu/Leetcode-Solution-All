
作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)


题目地址：https://leetcode.com/problems/di-string-match/description/


## 题目描述

Given a string ``S`` that only contains ``"I"`` (increase) or ``"D"`` (decrease), let ``N = S.length``.

Return any permutation ``A`` of ``[0, 1, ..., N]`` such that for all ``i = 0, ..., N-1``:

- If ``S[i] == "I"``, then ``A[i] < A[i+1]``
- If ``S[i] == "D"``, then ``A[i] > A[i+1]``
 

Example 1:

    Input: "IDID"
    Output: [0,4,1,3,2]

Example 2:

    Input: "III"
    Output: [0,1,2,3]

Example 3:

    Input: "DDI"
    Output: [3,2,0,1]
 
Note:

1. 1 <= S.length <= 10000
1. S only contains characters "I" or "D".

## 题目大意

已知一个字符串只包含I和D，求[0～N]的一个排列，使得如果字符串的某个位置是I，那么数组对应的位置和后面的位置是递增的；如果字符串的某个位置是D，那么数组对应的位置和后面的位置是递减的。

## 解题方法

乍一看很难的题目，但是仔细分析一下，发现很简单的：类似于贪心策略，我们使第一个出现的I的位置对应的是0，第一个D出现的位置对应的是N，那么无论这个位置后面无论出现的是另外的哪个数字，当前的位置都能满足题设条件。我们每次遇见I都比之前的I增加1，每次遇到D都比之前的D减小1.这样会尽可能的给后面的数字让出空间。

最后还要注意的是数组比字符串多一个位置，这个位置其实就是剩下的那个数字，比如我的解法中的ni或者nd都可以。

时间复杂度是O(N)，空间复杂度是O(1)。


```python
class Solution:
    def diStringMatch(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        N = len(S)
        ni, nd = 0, N
        res = []
        for s in S:
            if s == "I":
                res.append(ni)
                ni += 1
            else:
                res.append(nd)
                nd -= 1
        res.append(ni)
        return res
```

## 日期

2018 年 11 月 18 日 —— 出去玩了一天，腿都要废了
