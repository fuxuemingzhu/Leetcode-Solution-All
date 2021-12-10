
作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)

题目地址：https://leetcode.com/problems/longest-palindromic-subsequence/description/

# 题目描述

Given a string s, find the longest palindromic subsequence's length in s. You may assume that the maximum length of s is 1000.

Example 1:

    Input:
    
    "bbbab"
    Output:
    4
    One possible longest palindromic subsequence is "bbbb".
    
Example 2:

    Input:
    
    "cbbd"
    Output:
    2
    One possible longest palindromic subsequence is "bb".

# 题目大意

找出一个字符串中最长的回文序列的长度。注意序列可以是不连续的，而子字符串是连续的。

​

# 解题思路


做完昨天的每日一题 [446. 等差数列划分 II - 子序列](https://leetcode-cn.com/problems/arithmetic-slices-ii-subsequence/) 之后，相信大家对于子序列问题的套路已经更加了解了。子序列问题不能用滑动窗口了，可以用动态规划来解决。子序列问题的经典题目就是 [300. 最长递增子序列](https://leetcode-cn.com/problems/longest-increasing-subsequence/)，务必掌握。
​

先从整体思路说起。
​

子序列问题，由于是数组中的非连续的一个序列，使用动态规划求解时，避免不了二重循环：第一重循环是求解动态规划的每一个状态 $dp[i], (0 <= i <= N)$ ，第二重循环是向前寻找上一个子序列的结尾 $j ,(0 <= j < i)$$ 来和 $i$ 一起构成满足题意的新的子序列。


- 对于「**最长递增子序列**」问题，我们对 $i, j$ 的要求是 $nums[i] > nums[j]$，即递增；
- 对于「**能构成等差数列的子序列**」问题，我们对 $i, j$ 的要求是 $num[i]$ 可以在 $nums[j]$ 的基础上构成等差数列。
- 对于「**最长回文子序列**」问题，我们对 $i, j$ 本身的取值没有要求，但是希望能够成最长的回文子串。

​

在动态规划问题中，我们找到一个符合条件的 $j$ ，然后就可以通过状态转移方程由 $dp[j]$ 推导出 $dp[i]$ 。


然后，我理一下本题的解法。
​

当已知一个序列是回文时，在其首尾添加元素后的序列存在两种情况：

1. 首尾元素相等，则最长回文的长度 + 2；
1. 首尾元素不相等，则最长回文序列长度为 仅添加首元素时的最长回文长度 与 仅添加尾元素时的最长回文长度 的最大值。



**状态定义**： $dp[i][j]$ 表示 $s[i…j]$ 中的最长回文序列长度。
​

**状态转移方程**：

1. $i > j$，$dp[i][j] = 0$；
1. $i == j$，$dp[i][j] = 1$；
1. $i < j$ 且 $s[i] == s[j]$，$dp[i][j] = dp[i + 1][j - 1] + 2$；
1. $i < j$ 且 $s[i]！= s[j]$，$dp[i][j] = max(dp[i + 1][j]，dp[i][j - 1])$；



**遍历顺序**：
从状态转移方程可以看出，计算 $dp[i][j]$ 时需要用到 $dp[i+1][j - 1]$ 和 $dp[i + 1][j]$，所以对于 $i$ 的遍历应该从后向前；对于 $j$ 的遍历应该从前向后。
​

**返回结果**：
最后返回 $dp[0][s.length() - 1]$。


# 代码


提供了三种语言的代码。


java 代码
```java
class Solution {
    public int longestPalindromeSubseq(String s) {
        int size = s.length();
        int[][] dp = new int[size][size];
        for(int i = size - 1; i >= 0; i--){
            dp[i][i] = 1;
            for(int j = i + 1; j < size; j++){
                if(s.charAt(i) == s.charAt(j)){
                    dp[i][j] = dp[i + 1][j - 1] + 2;
                }else{
                    dp[i][j] = Math.max(dp[i + 1][j], dp[i][j - 1]);
                }
            }
        }
        return dp[0][size - 1];
    }
}
```

C++代码：
```cpp
class Solution {
public:
    int longestPalindromeSubseq(string s) {
        int size = s.size();
        vector<vector<int>> dp(size, vector<int>(size, 0));
        for(int i = size - 1; i >= 0; i--){
            dp[i][i] = 1;
            for(int j = i + 1; j < size; j++){
                if(s[i] == s[j]){
                    dp[i][j] = dp[i + 1][j - 1] + 2;
                }else{
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1]);
                }
            }
        }
        return dp[0][size - 1];
    }
};
```

python 代码：
```python
class Solution:
    def longestPalindromeSubseq(self, s):
        n = len(s)
        dp = [[0] * n for _ in range(n)]
        for i in range(n - 1, -1, -1):
            dp[i][i] = 1
            for j in range(i + 1, n):
                if s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1] + 2
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
        return dp[0][n - 1]
```

- 时间复杂度：$O(N^2)$
- 空间复杂度：$O(N^2)$

​

​

# 刷题心得


子序列的动态规划解法：两重循环。其实就看对于每个 $i$，当找到满足题目要求的 $j$ 的时候，状态转移方程怎么变化。
​



参考：http://blog.csdn.net/camellhf/article/details/70337501

# 日期

2018 年 3 月 15 日 --雾霾消散，春光明媚
2021 年 8 月 12 日——对面在装修，很吵


  [1]: http://blog.csdn.net/fuxuemingzhu/article/details/79529337
