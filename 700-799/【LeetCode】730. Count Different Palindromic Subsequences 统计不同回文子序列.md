作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)


题目地址：https://leetcode.com/problems/count-different-palindromic-subsequences/description/


## 题目描述

Given a string S, find the number of different non-empty palindromic subsequences in S, and return that number modulo ``10^9 + 7``.

A subsequence of a string S is obtained by deleting 0 or more characters from S.

A sequence is palindromic if it is equal to the sequence reversed.

Two sequences ``A_1, A_2, ...`` and ``B_1, B_2, ...`` are different if there is some ``i`` for which ``A_i != B_i``.

Example 1:

    Input: 
    S = 'bccb'
    Output: 6
    Explanation: 
    The 6 different non-empty palindromic subsequences are 'b', 'c', 'bb', 'cc', 'bcb', 'bccb'.
    Note that 'bcb' is counted only once, even though it occurs twice.

Example 2:

    Input: 
    S = 'abcdabcdabcdabcdabcdabcdabcdabcddcbadcbadcbadcbadcbadcbadcbadcba'
    Output: 104860361
    Explanation: 
    There are 3104860382 different non-empty palindromic subsequences, which is 104860361 modulo 10^9 + 7.

Note:

- The length of S will be in the range [1, 1000].
- Each character S[i] will be in the set {'a', 'b', 'c', 'd'}.

## 题目大意

求一个字符串的有多少个回文子序列。


## 解题方法

### 记忆化搜索

这个题太难了，我也只是抄了[花花酱的答案][1]，花花有个40分钟的视频，讲得非常清楚，强烈大家看看。

```python
class Solution:
    def countPalindromicSubsequences(self, S):
        """
        :type S: str
        :rtype: int
        """
        def count(S, i, j):
            if i > j: return 0
            if i == j: return 1
            if self.m_[i][j]:
                return self.m_[i][j]
            if S[i] == S[j]:
                ans = count(S, i + 1, j - 1) * 2
                l = i + 1
                r = j - 1
                while l <= r and S[l] != S[i]: l += 1
                while l <= r and S[r] != S[i]: r -= 1
                if l > r: ans += 2
                elif l == r: ans += 1
                else: ans -= count(S, l + 1, r - 1)
            else:
                ans = count(S, i + 1, j) + count(S, i, j - 1) - count(S, i + 1, j - 1)
            
            self.m_[i][j] = ans % (10 ** 9 + 7)
            return self.m_[i][j]
        
        n = len(S)
        self.m_ = [[None for _ in range(n)] for _ in range(n)]
        return count(S, 0, n - 1)
```

### 动态规划

待补


## 日期

2018 年 11 月 17 日 —— 美妙的周末，美丽的天气


  [1]: http://zxi.mytechroad.com/blog/dynamic-programming/leetcode-730-count-different-palindromic-subsequences/
