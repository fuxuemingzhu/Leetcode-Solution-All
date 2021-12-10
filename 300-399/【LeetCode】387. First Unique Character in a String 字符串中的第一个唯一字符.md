作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)


题目地址：https://leetcode.com/problems/first-unique-character-in-a-string/description/


## 题目描述

Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

Examples:

    s = "leetcode"
    return 0.
    
    s = "loveleetcode",
    return 2.

Note: You may assume the string contain only lowercase letters.


## 题目大意

找出字符串中第一个只出现了1次的字符。

## 解题方法

首先做个字符出现次数的统计，然后再次遍历，找出只出现了一次的第一个字符。


```python
class Solution:
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = collections.Counter(s)
        for i, c in enumerate(s):
            if count[c] == 1:
                return i
        return -1
```

## 日期

2018 年 11 月 16 日 —— 又到周五了！
