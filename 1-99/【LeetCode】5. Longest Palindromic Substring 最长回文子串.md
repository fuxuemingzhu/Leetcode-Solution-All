
作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/
公众号：负雪明烛
本文关键词：最长回文子串，题解，leetcode, 力扣，python, C++, java

---
@[TOC](目录)

题目地址：https://leetcode.com/problems/longest-palindromic-substring/description/

## 题目描述

Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example:

    Input: "babad"
    
    Output: "bab"
    
    Note: "aba" is also a valid answer.
 

Example:

    Input: "cbbd"
    
    Output: "bb"

## 题目大意

找出字符串中最长的回文子串。

## 解题方法

### 暴力遍历

遍历算法是我们最直观的解法，事实上也能通过OJ。我们使用的方法是两重循环确定子串的起始和结束位置，这样只要判断该子串是个回文，我们保留最长的回文即可。

代码很简单，C++版本如下：

```cpp
class Solution {
public:
    string longestPalindrome(string s) {
        const int N = s.size();
        string res;
        for (int i = 0; i < N; i++) {
            for (int j = i; j < N; j++) {
                if (j - i + 1 >= res.size() && isPalindrome(s, i, j)) {
                    res = s.substr(i, j - i + 1);
                }
            }
        }
        return res;
    }
    // [start, end]
    bool isPalindrome(string& s, int start, int end) {
        const int N = s.size();
        int l = start, r = end;
        while (l <= r) {
            if (s[l++] != s[r--]) {
                return false;
            }
        }
        return true;
    }
};
```

### 动态规划

动态规划的两个特点：第一大问题拆解为小问题，第二重复利用之前的计算结果，来解答这道题。

那如何划分小问题呢，我们可以先把所有长度最短为1的子字符串计算出来，根据起始位置从左向右，这些必定是回文。然后计算所有长度为2的子字符串，再根据起始位置从左向右。到长度为3的时候，我们就可以利用上次的计算结果：如果中心对称的短字符串不是回文，那长字符串也不是，如果短字符串是回文，那就要看长字符串两头是否一样。这样，一直到长度最大的子字符串，我们就把整个字符串集穷举完了。

我们维护一个二维数组 `dp`，其中 `dp[i][j]` 表示字符串区间 `[i, j]` 是否为回文串。

1. 当 `i = j` 时，只有一个字符，肯定是回文串；
2. 如果 `i = j + 1` ，说明是相邻字符，此时需要判断 `s[i] `是否等于 `s[j]` ；
3. 如果 `i` 和 `j` 不相邻，即 `i - j >= 2` 时，除了判断 `s[i]` 和 `s[j]` 相等之外，`dp[j + 1][i - 1]` 若为真，就是回文串。

通过以上分析，可以写出递推式如下：

```
dp[i, j] = 1                                        if i == j
         = s[i] == s[j]                             if j = i + 1
         = s[i] == s[j] && dp[i + 1][j - 1]         if j > i + 1      
```

Python 代码刚提交的时候超时了，但是使用set一下，看看是否只包含相同字符，这样就通过了！

```python
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(set(s)) == 1: return s
        n = len(s)
        start, end, maxL = 0, 0, 0
        dp = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(i):
                dp[j][i] = (s[j] == s[i]) & ((i - j < 2) | dp[j + 1][i - 1])
                if dp[j][i] and maxL < i - j + 1:
                    maxL = i - j + 1
                    start = j
                    end = i
            dp[i][i] = 1
        return s[start : end + 1]
```

C++版本代码如下，需要注意的是这里的res初始化为第一个字符：

```cpp
class Solution {
public:
    string longestPalindrome(string s) {
        const int N = s.size();
        if (N == 0) return "";
        string res = s.substr(0, 1);
        vector<vector<bool>> dp(N, vector(N, false));
        // s[j, i]
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < i; j++) {
                dp[j][i] = (s[j] == s[i]) && (i == j + 1 || dp[j + 1][i - 1]);
                if (dp[j][i] && i - j + 1 >= res.size()) {
                    res = s.substr(j, i - j + 1);
                }
            }
            dp[i][i] = true;
        }
        return res;
    }
};
```

二刷---

马拉车算法。。待续

参考：
http://www.cnblogs.com/grandyang/p/4464476.html
https://segmentfault.com/a/1190000002991199

## 日期

2018 年 3 月 15 日 —— 雾霾消散，春光明媚
2019 年 1 月 19 日 —— 有好几天没有更新文章了

  [1]: http://blog.csdn.net/fuxuemingzhu/article/details/79529337
