
作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)

题目地址：https://leetcode.com/problems/palindromic-substrings/description/

## 题目描述

Given a string, your task is to count how many palindromic substrings in this string.

The substrings with different start indexes or end indexes are counted as different substrings even they consist of same characters.

Example 1:

    Input: "abc"
    Output: 3
    Explanation: Three palindromic strings: "a", "b", "c".

Example 2:

    Input: "aaa"
    Output: 6
    Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".

Note:
1. The input string length won't exceed 1000.

## 题目大意

判断子字符串有多少个回文。

## 解题方法

### 方法一：暴力循环

看到字符的长度只有1000，首先用暴力解法。双重循环，得到所有的子字符串，然后判断是不是回文。

时间复杂度基本是O(N^3)，超过1%的提交。

代码：

```python
class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = 0
        for i in xrange(len(s)):
            for j in xrange(i, len(s)):
                if s[i:j + 1] == s[i:j + 1][::-1]:
                    count += 1
        return count
```

### 方法二：固定起点向后找

index从0到len进行遍历。对于每个单个的字符，其本身是一个回文。然后对回文长度是奇数的情况进行遍历：使用left和right双指针，往两边走，判断总长度是3,5,7……的子串是不是回文（left指针和right指针指向的字符相等）。再对回文是偶数的情况同样的进行遍历。最后求和即可。

比较巧妙的一种思想，不要怕代码长，其实没啥。

```python
class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = 0
        for i in xrange(len(s)):
            count += 1
            #回文长度是奇数的情况
            left = i - 1
            right = i + 1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                count += 1
                left -= 1
                right += 1
            #回文长度是偶数的情况
            left = i
            right = i + 1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                count += 1
                left -= 1
                right += 1
        return count
```

### 方法三：动态规划

动态规划的思想是，我们先确定所有的回文，即 ``string[start:end] ``是回文. 当我们要确定``string[i:j]`` 是不是回文的时候，要确定：

1. ``string[i]`` 等于 ``string[j]``吗?
1. ``string[i+1:j-1]``是回文吗?

单个字符是回文；两个连续字符如果相等是回文；如果有3个以上的字符，需要两头相等并且去掉首尾之后依然是回文。

Python代码如下：

```python
class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        count = 0
        start, end, maxL = 0, 0, 0
        dp = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(i):
                dp[j][i] = (s[j] == s[i]) & ((i - j < 2) | dp[j + 1][i - 1])
                if dp[j][i]:
                    count += 1
            dp[i][i] = 1
            count += 1
        return count
```

二刷的Python代码如下：

```python
class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = 0
        N = len(s)
        dp = [[False] * N for _ in range(N)]
        for l in range(1, N + 1): # step size
            for i in range(N - l + 1):
                j = i + l - 1
                if l == 1 or (l == 2 and s[i] == s[j]) or (l >= 3 and s[i] == s[j] and dp[i + 1][j - 1]):
                    dp[i][j] = True
                    count += 1
        return count
```

C++代码如下：

```cpp
class Solution {
public:
    int countSubstrings(string s) {
        const int N = s.size();
        vector<vector<int>> dp(N, vector<int>(N, false));
        int count = 0;
        for (int l = 1; l <= N; l ++) {
            for (int i = 0; i <= N - l; i ++) {
                int j = i + l - 1;
                if (l == 1 || (l == 2 && s[i] == s[j]) || (l >= 3 && s[i] == s[j] && dp[i + 1][j - 1])) {
                    count ++;
                    dp[i][j] = true;
                }
            }
        }
        return count;
    }
};
```


## 日期

2018 年 3 月 3 日 
2018 年 12 月 10 日 —— 又是周一！

  [1]: http://blog.csdn.net/fuxuemingzhu/article/details/79359540
