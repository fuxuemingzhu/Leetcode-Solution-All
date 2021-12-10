
作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)

题目地址：https://leetcode.com/problems/minimum-ascii-delete-sum-for-two-strings/description/

## 题目描述

Given two strings s1, s2, find the lowest ASCII sum of deleted characters to make two strings equal.

Example 1:
    
    Input: s1 = "sea", s2 = "eat"
    Output: 231
    
    Explanation: Deleting "s" from "sea" adds the ASCII value of "s" (115) to the sum.
    Deleting "t" from "eat" adds 116 to the sum.
    At the end, both strings are equal, and 115 + 116 = 231 is the minimum sum possible to achieve this.
    
Example 2:
    
    Input: s1 = "delete", s2 = "leet"
    Output: 403
    
    Explanation: Deleting "dee" from "delete" to turn the string into "let",
    adds 100[d]+101[e]+101[e] to the sum.  Deleting "e" from "leet" adds 101[e] to the sum.
    At the end, both strings are equal to "let", and the answer is 100+101+101+101 = 403.
    If instead we turned both strings into "lee" or "eet", we would get answers of 433 or 417, which are higher.

Note:

1. 0 < s1.length, s2.length <= 1000.
1. All elements of each string will have an ASCII value in [97, 122].

## 题目大意

给出两个字符串，可以在每个字符串中删除一些字符，得到相等的字符串。求删除的字符的ASCII最小和。

## 解题方法

看到玩字符串+最优问题，一定是DP没错了。我们已经做过了求LCS的问题，当时的dp的结果是个数。这个题改成ASCII就好。思路和我们[583. Delete Operation for Two Strings][1]基本一致。

583这个题的做法是求个数，所以每个位置如果相等的话，就+1，而这个题求ASCII，所以相等的话加上ASCII。

对于 DP 的问题，最重要的是找到合适的状态和状态转移方程。其实直接使用LCS的ASCII之和作为状态就行了。 

题目所求为使得两个字符串 ascii 和相同的最小删除字符 ascii 和，所以我们设 dp[i][j] 为 s1 前 i 个字符与 s2 前 j 个字符得到LCS所需的ASCII和。 

那么我们开始构造转移方程： 

对于 s1[0...i−1] 和 s2[0...j−1] 的 LCS的ASCII的和应该是这样的：

1. 若 s1[i−1]==s2[j−1] ，则 dp[i][j]=C[i−1][j−1] + ord(s1[i-1])
1. 若不相等，则 s1[i−1], s2[j−1] 选择删除一个，
dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

这里应该还是比较容易理解的，即LCS的字符数不变。

最终的结果和583一样，要把所有的和减去LCS的和。

代码：

```python
class Solution(object):
    def minimumDeleteSum(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: int
        """
        l1, l2 = len(s1), len(s2)
        dp = [[0] * (l2 + 1) for _ in range(l1 + 1)]
        for i in range(1, l1 + 1):
            for j in range(1, l2 + 1):
                if s1[i - 1] == s2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + ord(s1[i - 1])
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        result = sum(map(ord, s1 + s2)) - dp[-1][-1] * 2
        return result
```

C++版本的char直接转成int就是得到了ASCII码，所以简单一点。

C++代码如下：

```cpp
class Solution {
public:
    int minimumDeleteSum(string s1, string s2) {
        const int M = s1.size(), N = s2.size();
        vector<vector<int>> dp(M + 1, vector<int>(N + 1, 0));
        for (int i = 1; i < M + 1; i ++)
            dp[i][0] = dp[i - 1][0] + s1[i - 1];
        for (int j = 1; j < N + 1; j ++)
            dp[0][j] = dp[0][j - 1] + s2[j - 1];
        for (int i = 1; i < M + 1; i ++) {
            for (int j = 1; j < N + 1; j ++) {
                if (s1[i - 1] == s2[j - 1]) {
                    dp[i][j] = dp[i - 1][j - 1];
                } else {
                    dp[i][j] = min(dp[i - 1][j] + s1[i - 1], dp[i][j - 1] + s2[j - 1]);
                }
            }
        }
        return dp[M][N];
    }
};
```

参考：
1. https://blog.csdn.net/bowen_wu_sysu/article/details/78428635
1. https://leetcode.com/problems/delete-operation-for-two-strings/discuss/103214/Java-DP-Solution-(Longest-Common-Subsequence)

## 日期

2018 年 4 月 4 日 —— 清明时节雪纷纷～～下雪了，惊不惊喜，意不意外？
2018 年 12 月 14 日 —— 12月过半，2019就要开始

  [1]: https://blog.csdn.net/fuxuemingzhu/article/details/79821305
