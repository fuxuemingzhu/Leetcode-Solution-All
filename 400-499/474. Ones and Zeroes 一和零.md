# 【LeetCode】474. Ones and Zeroes 解题报告（Python）

作者： 		负雪明烛 
id：				fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---

题目地址：https://leetcode.com/problems/ones-and-zeroes/description/

## 题目描述：

n the computer world, use restricted resource you have to generate maximum benefit is what we always want to pursue.

For now, suppose you are a dominator of m 0s and n 1s respectively. On the other hand, there is an array with strings consisting of only 0s and 1s.

Now your task is to find the maximum number of strings that you can form with given m 0s and n 1s. Each 0 and 1 can be used at most once.

Note:

1. The given numbers of 0s and 1s will both not exceed 100
1. The size of given string array won't exceed 600.

Example 1:

    Input: Array = {"10", "0001", "111001", "1", "0"}, m = 5, n = 3
    Output: 4

    Explanation: This are totally 4 strings can be formed by the using of 5 0s and 3 1s, which are “10,”0001”,”1”,”0”

Example 2:

    Input: Array = {"10", "0", "1"}, m = 1, n = 1
    Output: 2
    
    Explanation: You could form "10", but then you'd have nothing left. Better form "0" and "1".

## 题目大意

我们现在从数组中每个字符串都有一些0和1，问给了m个0，n个1，从数组中取出最多的字符串，这些字符串中1和0的出现次数之和不超过m，n.

## 解题方法

看到这个题第一个感觉是贪心，但是想了想，无论是贪心少的还是贪心多的，都会影响到后面选取的变化，所以不行。

遇到这种求最多或最少的次数的，并且不用求具体的解决方案，一般都是使用DP。

这个DP很明白了，定义一个数组dp[m+1][n+1]，代表m个0, n个1能组成的最长字符串。遍历每个字符串统计出现的0和1得到zeros和ones，所以第dp[i][j]的位置等于dp[i][j]和dp[i - zeros][j - ones] + 1。其中dp[i - zeros][j - ones]表示如果取了当前的这个字符串，那么剩下的可以取的最多的数字。

这个题用Counter竟然不通过，使用两个常量去做统计居然就行了。

时间复杂度有点难计算，大致是O(MN * L), L 是数组长度，空间复杂度是O(MN).

代码如下：

```python
class Solution(object):
    def findMaxForm(self, strs, m, n):
        """
        :type strs: List[str]
        :type m: int
        :type n: int
        :rtype: int
        """
        # m个0, n个1能组成的最长字符串
        dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        for str in strs:
            zeros, ones = 0, 0
            for c in str:
                if c == "0":
                    zeros += 1
                elif c == "1":
                    ones += 1
            for i in range(m, zeros - 1, -1):
                for j in range(n, ones - 1, -1):
                    dp[i][j] = max(dp[i][j], dp[i - zeros][j - ones] + 1)
        return dp[m][n]
```

参考资料：

http://www.cnblogs.com/grandyang/p/6188893.html
https://kingsfish.github.io/2017/07/23/Leetcode-474-Ones-and-Zeros/

## 日期

2018 年 9 月 23 日 —— 今天是实验室第一个打卡的
