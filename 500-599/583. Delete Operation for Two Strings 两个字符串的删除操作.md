
作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)

题目地址：https://leetcode.com/problems/delete-operation-for-two-strings/description/

## 题目描述

Given two words word1 and word2, find the minimum number of steps required to make word1 and word2 the same, where in each step you can delete one character in either string.

Example 1:

	Input: "sea", "eat"
	Output: 2
	Explanation: You need one step to make "sea" to "ea" and another step to make "eat" to "ea".

Note:

1. The length of given words won't exceed 500.
1. Characters in given words can only be lower-case letters.

    
## 题目大意

给出了两个字符串，可以删除两个字符串中的某些字符，求最少删除多少个字符之后两个字符串相等。

## 解题方法

一直觉得这一个题非常的难，所以就没做。昨天复习了一下机试指南之后，发现这个题不就是求最长公共子序列(LCS)吗？顿时豁然开朗。LCS和LIS一样是经典的动态规划问题应该背会的。这个题在机试指南的162页。

但是，别忘了一点，求出LCS后还要用两者的长度之和减去LCS的长度，才是我们应该删除的字符长度。

![这里写图片描述](https://img-blog.csdn.net/20180404191631962?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2Z1eHVlbWluZ3podQ==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)

如果还不是很明白，可以看这个题的官方解答：[https://leetcode.com/articles/delete-operation-for-two-strings/][1]，有dp的二维数组，能把变化看的非常清楚。

代码：

```python
class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        _len1, _len2 = len(word1), len(word2)
        dp = [[0] * (len(word2) + 1) for _ in range(len(word1) + 1)]
        for i in range(1, len(word1) + 1):
            for j in range(1, len(word2) + 1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i][j-1], dp[i-1][j])
        val = dp[-1][-1]
        return _len1 - val + _len2 - val
```

二刷使用的C++，发现和上面的做法有点区别。上面的做法是最长公共子序列，这个题的做法可以指直接使用要删除的序列。

这个题的做法和[712. Minimum ASCII Delete Sum for Two Strings](https://blog.csdn.net/fuxuemingzhu/article/details/79822689)很像，代码如下：

```cpp
class Solution {
public:
    int minDistance(string word1, string word2) {
        const int M = word1.size(), N = word2.size();
        vector<vector<int>> dp(M + 1, vector<int>(N + 1, 0));
        for (int i = 1; i < M + 1; i ++)
            dp[i][0] = dp[i - 1][0] + 1;
        for (int j = 1; j < N + 1; j ++)
            dp[0][j] = dp[0][j - 1] + 1;
        for (int i = 1; i < M + 1; i ++) {
            for (int j = 1; j < N + 1; j ++) {
                if (word1[i - 1] == word2[j - 1]) {
                    dp[i][j] = dp[i - 1][j - 1];
                } else {
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + 1;
                }
            }
        }
        return dp[M][N];
    }
};
```

## 日期

2018 年 4 月 4 日 —— 清明时节雪纷纷～～下雪了，惊不惊喜，意不意外？
2018 年 12 月 14 日 —— 12月过半，2019就要开始

  [1]: https://leetcode.com/articles/delete-operation-for-two-strings/
