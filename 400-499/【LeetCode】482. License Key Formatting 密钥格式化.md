
作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)

题目地址：[https://leetcode.com/problems/license-key-formatting/description/][1]


## 题目描述

You are given a license key represented as a string S which consists only alphanumeric character and dashes. The string is separated into N+1 groups by N dashes.

Given a number K, we would want to reformat the strings such that each group contains exactly K characters, except for the first group which could be shorter than K, but still must contain at least one character. Furthermore, there must be a dash inserted between two groups and all lowercase letters should be converted to uppercase.

Given a non-empty string S and a number K, format the string according to the rules described above.

Example 1:

	Input: S = "5F3Z-2e-9-w", K = 4
	
	Output: "5F3Z-2E9W"
	
	Explanation: The string S has been split into two parts, each part has 4 characters.
	Note that the two extra dashes are not needed and can be removed.

Example 2:

	Input: S = "2-5g-3-J", K = 2
	
	Output: "2-5G-3J"

	Explanation: The string S has been split into three parts, each part has 2 characters except the first part as it could be shorter as mentioned above.

Note:
1. The length of string S will not exceed 12,000, and K is a positive integer.
1. String S consists only of alphanumerical characters (a-z and/or A-Z and/or 0-9) and dashes(-).
1. String S is non-empty.

## 题目大意

现在有一些用``-``分割的字符串，需要重新安排，使得除了第一个之外，其他的``-``分割的字符串长度都是K。另外需要全部转成大写字符。

## 解题方法

注意，这个题的意思是 右边的序列要都是K个的，最左边如果不够就不够了，剩多少写多少。

首先计算第一个应该占据了多少个字符，然后看后面的应该是等长的。并且和原来的-的划分情况是无关的。每个片的个数都要是K。
字符串切片结束的长度大于自身长度也可以。

```python
class Solution(object):
    def licenseKeyFormatting(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        S = S.upper()
        groups = ''.join(S.split('-'))
        bias = len(groups) % K
        devides = len(groups) / K
        answer = groups[:bias]
        answer += '-' if bias != 0 else ''
        for i in range(devides):
            answer += groups[i*K+bias : (i+1)*K+bias] + '-'
        return answer[:-1]
```

二刷的时候，写的Python代码如下：

```python
class Solution(object):
    def licenseKeyFormatting(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        res = []
        s = "".join(S.split("-")).upper()
        N = len(s)
        if N % K != 0:
            res.append(s[: N % K])
        for i in range(N % K, N, K):
            res.append(s[i : i + K])
        return "-".join(res)
```


## 日期

2018 年 2 月 1 日 
2018 年 11 月 22 日 —— 感恩节快乐～

  [1]: https://leetcode.com/problems/license-key-formatting/description/
