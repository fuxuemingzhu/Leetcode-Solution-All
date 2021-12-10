
作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)

题目地址：https://leetcode.com/problems/groups-of-special-equivalent-strings/description/

## 题目描述

You are given an array A of strings.

Two strings ``S`` and ``T`` are special-equivalent if after any number of moves, ``S == T``.

A move consists of choosing two indices ``i`` and ``j`` with ``i % 2 == j % 2``, and swapping ``S[i]`` with ``S[j]``.

Now, a group of special-equivalent strings from A is a non-empty subset S of A such that any string not in S is not special-equivalent with any string in S.

Return the number of groups of special-equivalent strings from A.

 

Example 1:

    Input: ["a","b","c","a","c","c"]
    Output: 3
    Explanation: 3 groups ["a","a"], ["b"], ["c","c","c"]

Example 2:

    Input: ["aa","bb","ab","ba"]
    Output: 4
    Explanation: 4 groups ["aa"], ["bb"], ["ab"], ["ba"]

Example 3:

    Input: ["abc","acb","bac","bca","cab","cba"]
    Output: 3
    Explanation: 3 groups ["abc","cba"], ["acb","bca"], ["bac","cab"]

Example 4:

    Input: ["abcd","cdab","adcb","cbad"]
    Output: 1
    Explanation: 1 group ["abcd","cdab","adcb","cbad"]
 

Note:

1. 1 <= A.length <= 1000
1. 1 <= A[i].length <= 20
1. All A[i] have the same length.
1. All A[i] consist of only lowercase letters.

## 题目大意

可以对一个字符串的所有奇数位置或者偶数位置进行任意的调换顺序。如果两个字符串在经历了上面的操作之后，可以做到完全相等，那么就属于题目中的一个组。现在就要我们求最终分为几个组。

## 解题方法

理解了题意之后我们可以直接使用暴力的方法去求解了，毕竟是Easy的题目，没那么难。

把这个数组中所有的奇数位置和偶数位置的字符分别取出来，进行排序再合并。把合并之后的结果放入到一个set里，然后统计set中字符串的个数也就是题目中要求的组数。

代码如下：

```python
class Solution(object):
    def numSpecialEquivGroups(self, A):
        """
        :type A: List[str]
        :rtype: int
        """
        B = set()
        for a in A:
            B.add(''.join(sorted(a[0::2])) + ''.join(sorted(a[1::2])))
        return len(B)
```

参考资料：无


## 日期

2018 年 8 月 26 日 —— 珍爱生命，远离DD！
2018 年 11 月 6 日 —— 腰酸背痛要废了
