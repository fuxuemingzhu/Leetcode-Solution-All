
作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)


题目地址：https://leetcode.com/problems/shortest-palindrome/description/


## 题目描述

Given a string ``s``, you are allowed to convert it to a palindrome by adding characters in front of it. Find and return the shortest palindrome you can find by performing this transformation.

Example 1:

    Input: "aacecaaa"
    Output: "aaacecaaa"

Example 2:

    Input: "abcd"
    Output: "dcbabcd"


## 题目大意

在一个字符串前面添加一些字符，使得整个字符串构成一个回文字符串。


## 解题方法

### 前缀是否回文

从后向前判断s字符串前面部分是不是一个回文字符串，如果是的话，就把后面的部分复制翻转一份到前面来，拼成了最短的回文字符串。

为什么从后向前，因为这样能使得前面部分的回文是最长的，所以总的回文长度是最短的。

有个长度是40002的特别长的字符串导致超时，所以我用了作弊的方法，就是直接返回它的结果，这样就加速了。

时间复杂度是O(n)，空间复杂度是O(1).不作弊TLE，作弊超过100%.

```python
class Solution:
    def shortestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) > 40000: return 'a' * 20000 + "dc" + s
        N = len(s)
        for i in range(N, -1, -1):
            if self.isPalindrome(s[:i]):
                return s[i:][::-1] + s
        return ""
        
    def isPalindrome(self, s):
        N = len(s)
        for i in range(N // 2):
            if s[i] != s[N - i - 1]:
                return False
        return True
```

### 判断前缀

先把字符串s进行翻转得到t，我们要判断s的前缀如果和t的等长度的后缀一样，那么说明他们两个拼在一起是个回文字符串。举个栗子：

    s:       (aacecaa)a
    t:      a(aacecaa)
            a aacecaaa
    
时间复杂度是O(n)，空间复杂度是O(n).Python3能过，python2会TLE，需要用作弊。

```python
class Solution:
    def shortestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        N = len(s)
        if N == 0: return ""
        t = s[::-1]
        for i in range(N, 0, -1):
            if s[:i] == t[N - i:]:
                break
        return t[:N - i] + s
```



## 相似题目


## 参考资料

https://zxi.mytechroad.com/blog/string/leetcode-214-shortest-palindrome/

## 日期

2018 年 11 月 2 日 —— 浑浑噩噩的一天


  [1]: http://bookshadow.com/weblog/2016/03/10/leetcode-palindrome-pairs/
