# 【LeetCode】718. Maximum Length of Repeated Subarray 解题报告（Python）

标签（空格分隔）： LeetCode

作者： 		负雪明烛 
id：				fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---

题目地址：https://leetcode.com/problems/maximum-length-of-repeated-subarray/description/

## 题目描述：

Given two integer arrays A and B, return the maximum length of an subarray that appears in both arrays.

Example 1:

    Input:
    A: [1,2,3,2,1]
    B: [3,2,1,4,7]
    Output: 3
    
    Explanation: 
    The repeated subarray with maximum length is [3, 2, 1].

Note:

1. 1 <= len(A), len(B) <= 1000
1. 0 <= A[i], B[i] < 100


## 题目大意

求最长重复子数组。那么如果我们将数组换成字符串，实际这道题就是求Longest Common Substring的问题了。


## 解题方法

这个题显然是DP。一定注意，必须连续才行！那么dp数组中每个不为0的位置，一定是两者相等的地方。

比如，对于这两个数组[1,2,2]和[3,1,2]，我们的dp数组为：

      3 1 2
    1 0 1 0
    2 0 0 2
    2 0 0 1

所以递推关系为，dp[i][j] = dp[i-1][j-1]，当A[i]== B[j]。如果不等的话，dp[i][j]为0.

刚开始理解成了最长子序列Longest Common Subsequence问题了。耽误了不少时间……

代码如下：

```python
class Solution:
    def findLength(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        m, n = len(A), len(B)
        dp = [[0 for j in range(n + 1)] for i in range(m + 1)]
        max_len = 0
        for i in range(m + 1):
            for j in range(n + 1):
                if i == 0 or j == 0:
                    dp[i][j] = 0
                elif A[i - 1] == B[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                    max_len = max(max_len, dp[i][j])
        return max_len
```

换一种方式写，可能更好理解吧，毕竟少了一行和一列空的0.

```python
class Solution:
    def findLength(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        m, n = len(A), len(B)
        dp = [[0 for j in range(n)] for i in range(m)]
        max_len = 0
        for i in range(m):
            for j in range(n):
                if A[i] == B[j]:
                    if i == 0 or j == 0:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = dp[i - 1][j - 1] + 1
                    max_len = max(max_len, dp[i][j])
        return max_len
```



参考资料：
http://www.cnblogs.com/grandyang/p/7801533.html

## 日期

2018 年 9 月 11 日 ———— 天好阴啊
