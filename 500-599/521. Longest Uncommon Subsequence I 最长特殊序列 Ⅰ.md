
作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)

题目地址：https://leetcode.com/problems/longest-uncommon-subsequence-i/description/


## 题目描述

Given a group of two strings, you need to find the longest uncommon subsequence of this group of two strings. The longest uncommon subsequence is defined as the longest subsequence of one of these strings and this subsequence should not be any subsequence of the other strings.

A subsequence is a sequence that can be derived from one sequence by deleting some characters without changing the order of the remaining elements. Trivially, any string is a subsequence of itself and an empty string is a subsequence of any string.

The input will be two strings, and the output needs to be the length of the longest uncommon subsequence. If the longest uncommon subsequence doesn't exist, return -1.

    Example 1:
    Input: "aba", "cdc"
    Output: 3
    Explanation: The longest uncommon subsequence is "aba" (or "cdc"), 
    because "aba" is a subsequence of "aba", 
    but not a subsequence of any other strings in the group of two strings. 

Note:

1. Both strings' lengths will not exceed 100.
1. Only letters from a ~ z will appear in input strings.

## 题目大意

题意很重要啊！这个题目有点长，看了几遍没看太懂，所以一直没做。

给定一组两个的字符串，您需要找到这组两个字符串中最长的不常见的子序列。 最长的不常见的子序列被定义为这些字符串之一的最长子序列，并且该子序列不应该是其他字符串的任何子序列。 
子序列是可以通过删除一些字符而不改变剩余元素的顺序从一个序列导出的序列。 简而言之，任何字符串本身都是一个子序列，空字符串是任何字符串的子序列。 
输入将是两个字符串，输出需要是最长的不常见子序列的长度。 如果最长不常见的子序列不存在，则返回-1。

## 解题方法

题意简而言之就是求两个字符串的最长不常见子序列的长度。如果两个字符串相等，那么不存在！如果不等，长度最长的那个字符串就是最长不常见子序列。

脑筋急转弯的题目！怪不得大家对这个题踩了那么多。

```python
class Solution(object):
    def findLUSlength(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: int
        """
        return max(len(a), len(b)) if a != b else -1
```

## 日期

2018 年 2 月 28 日 
2018 年 11 月 ９ 日 —— 睡眠可以
