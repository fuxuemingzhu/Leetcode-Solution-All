
作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/
公众号：负雪明烛
本文关键词：回文数，回文，题解，Leetcode, 力扣，Python, C++, Java

---
@[TOC](目录)

题目地址：[https://leetcode.com/problems/palindrome-number/#/description][1]


## 题目描述

Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.

Example 1:

	Input: 121
	Output: true

Example 2:

	Input: -121
	Output: false
	Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

Example 3:

	Input: 10
	Output: false
	Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

Follow up:

- Coud you solve it without converting the integer to a string?

## 题目大意

判断一个数字是不是回文数字。

## 解题方法

### 判断回文字符串

可以先转化成字符串，然后判断这个字符串是不是回文串。

```python
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0: return False
        x = str(x)
        N = len(x)
        for i in range(N / 2):
            if x[i] != x[N - 1 - i]:
                return False
        return True
```

### 翻转数字

这个题的意思很简单就是判断一个数字是不是回文数，这个和一个字符串是不是回文的方法不一样。可以通过重新构建一个数字，和之前的数字的顺序是反着的，最后看两个数字是不是相等即可。

注意，常量空间不算附加空间。

```java
public class Solution {
    public boolean isPalindrome(int x) {
		if (x < 0) return false;
        int y = x;
        int res = 0;
        while(y > 0){
            res = res * 10 + y % 10;
            y /= 10;
        }
        return x == res;
    }
}
```

## 日期

2017 年 5 月 7 日 
2018 年 11 月 22 日 —— 感恩节快乐～

  [1]: https://leetcode.com/problems/arranging-coins/#/description
