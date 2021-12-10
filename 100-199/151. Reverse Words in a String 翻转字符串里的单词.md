- 作者：    负雪明烛
- id：      fuxuemingzhu
- 个人博客：[http://fuxuemingzhu.cn/](http://fuxuemingzhu.cn/)

---

@[TOC](目录)

题目地址：https://leetcode.com/problems/reverse-words-in-a-string/description/

## 题目描述

Given an input string, reverse the string word by word.

Example 1:

	Input: "the sky is blue"
	Output: "blue is sky the"

Example 2:

	Input: "  hello world!  "
	Output: "world! hello"
	Explanation: Your reversed string should not contain leading or trailing spaces.

Example 3:

	Input: "a good   example"
	Output: "example good a"
	Explanation: You need to reduce multiple spaces between two words to a single space in the reversed string.

Note:

- A word is defined as a sequence of non-space characters.
- Input string may contain leading or trailing spaces. However, your reversed string should not contain leading or trailing spaces.
- You need to reduce multiple spaces between two words to a single space in the reversed string.

Follow up: For C programmers, try to solve it in-place in O(1) space.


## 题目大意

翻转字符串里面的单词。同时去掉多余的空格。

## 解题方法

字符串操作直接放弃 C++ ，一般都选择 Python。建议大家刷题的时候会 Python。

Python 的 split() 函数：

- split()的时候，多个连续空格当成分割符；
- split(' ')的时候，多个空格都要分割，每个空格分割出来空。

所以可以直接用split()函数，把多个连续空格当成分割符，进行分割。

然后再翻转字符串。

```python
class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(s.split()[::-1])
```

## 日期

2018 年 6 月 26 日 —— 早睡早起
2020 年 4 月 10 日 —— 春眠不觉晓
