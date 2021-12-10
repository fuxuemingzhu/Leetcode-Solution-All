# 【LeetCode】91. Decode Ways 解题报告（Python）

标签（空格分隔）： LeetCode

作者： 		负雪明烛 
id：				fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---

题目地址：https://leetcode.com/problems/decode-ways/description/

## 题目描述：

A message containing letters from A-Z is being encoded to numbers using the following mapping:

    'A' -> 1
    'B' -> 2
    ...
    'Z' -> 26

Given a non-empty string containing only digits, determine the total number of ways to decode it.

Example 1:

    Input: "12"
    Output: 2
    Explanation: It could be decoded as "AB" (1 2) or "L" (12).

Example 2:

    Input: "226"
    Output: 3
    Explanation: It could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).


## 题目大意

输入是一个数字字符串，如果拆分之后其中的部分数字能代表了一个英文字母，那么算作一种拆分方式。求所有共多少拆分方式。

## 解题方法

这个题目和爬楼梯的题目非常像，直接使用dp。

令， dp[i]代表解析s[:i]字符串所有可能的方式数目。

则：

    dp[i] = dp[i-1] if s[i] != '0'
           + dp[i-2] if '9' < s[i-2:i] < '27'

举例子：

对于"226"：

令dp数组为[0,0,0,0]，初始化为[1,0,0,0]；

从第一个位置开始，输入为"2"，不为"0"，所以dp数组为[1,1,0,0]；

第2个位置，输入为"2"，不为"0"，所以dp数组为[1,1,1,0]；此时前两位数字是"22"，满足区间，所以变为[1,1,2,0]；

第3个位置，输入为"6"，不为"0"，所以dp数组为[1,1,2,2]；此时前两位数字是"26"，满足区间，所以变为[1,1,2,3]。


代码如下：

```python
class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        dp = [0] * (len(s) + 1)
        dp[0] = 1
        for i in range(1, len(dp)):
            if s[i-1] != '0':
                dp[i] = dp[i-1]
            if i != 1 and '09' < s[i-2:i] < '27':
                dp[i] += dp[i-2]
        return dp[-1]
```

参考资料：

1. https://leetcode.com/problems/decode-ways/discuss/163707/Python-From-O(N)-Space-To-O(1)-Space-Solutions

## 日期

2018 年 8 月 27 日 ———— 就要开学了！


  [1]: https://blog.csdn.net/fuxuemingzhu/article/details/82113409
  [2]: https://leetcode.com/media/original_images/31_Next_Permutation.gif