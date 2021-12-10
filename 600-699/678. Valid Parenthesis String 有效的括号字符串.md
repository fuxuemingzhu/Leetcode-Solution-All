# 【LeetCode】678. Valid Parenthesis String 解题报告（Python）

标签（空格分隔）： LeetCode

作者： 		负雪明烛 
id：				fuxuemingzhu
个人博客：	http://fuxuemingzhu.me/

---

题目地址：https://leetcode.com/problems/valid-parenthesis-string/description/

## 题目描述：

Given a string containing only three types of characters: '(', ')' and '*', write a function to check whether this string is valid. We define the validity of a string by these rules:

1. Any left parenthesis '(' must have a corresponding right parenthesis ')'.
1. Any right parenthesis ')' must have a corresponding left parenthesis '('.
1. Left parenthesis '(' must go before the corresponding right parenthesis ')'.
1. '*' could be treated as a single right parenthesis ')' or a single left parenthesis '(' or an empty string.
1. An empty string is also valid.

Example 1:

    Input: "()"
    Output: True

Example 2:

    Input: "(*)"
    Output: True

Example 3:

    Input: "(*))"
    Output: True

Note:

1. The string size will be in the range [1, 100].

## 题目大意

判断一个括号表达是是否合法，其中包含了``*``号，``*``可以表示(,)或者空字符。

## 解题方法

看到括号表达式第一感觉肯定是栈了。但是由于``*``的存在，导致这么做并不合理。

又是我绞尽脑汁也做不出来的题，果然还是[书影博客][1]浅显易懂啊！真大神，我跟着学习了不少。

这个思路是这样的：用一个set集合来记录这个表达式中左括号``能``比右括号多的个数。注意，是能够。因此，如果遇到左括号，集合里面的每个元素应该+1；遇到右括号，如果集合里边的>0的元素可以-1；如果遇到``*``，应该+1，-1或者不运算。看最后这个集合``能否``包含0，即左括号的个数等于右括号的个数。

那这个算法怎么判断的")("呢？巧妙的地方就在于，只有set里面大于0的元素才去-1；因此刚开始set只有0元素，所以)不算数。所以这个方法真的很巧妙。

```python
class Solution(object):
    def checkValidString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        old_set = set([0])
        for c in s:
            new_set = set()
            if c == '(':
                for t in old_set:
                    new_set.add(t + 1)
            elif c == ')':
                for t in old_set:
                    if t > 0:
                        new_set.add(t - 1)
            elif c == '*':
                for t in old_set:
                    new_set.add(t + 1)
                    new_set.add(t)
                    if t > 0:
                        new_set.add(t - 1)
            old_set = new_set
        return 0 in old_set
```

## 日期

2018 年 6 月 13 日 ———— 腾讯赛圆满结束！两个月修得正果哈哈～～


  [1]: http://bookshadow.com/weblog/2017/09/17/leetcode-valid-parenthesis-string/