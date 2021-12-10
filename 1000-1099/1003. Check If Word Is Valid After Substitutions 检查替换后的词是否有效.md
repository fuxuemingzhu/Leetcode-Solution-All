作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)


题目地址：https://leetcode.com/problems/check-if-word-is-valid-after-substitutions/


## 题目描述

We are given that the string ``"abc"`` is valid.

From any valid string ``V``, we may split ``V`` into two pieces ``X`` and ``Y`` such that ``X + Y`` (``X`` concatenated with ``Y``) is equal to ``V``.  (``X`` or ``Y`` may be empty.)  Then, ``X + "abc" + Y`` is also valid.

If for example ``S = "abc"``, then examples of valid strings are: ``"abc", "aabcbc", "abcabc", "abcabcababcc"``.  Examples of invalid strings are: ``"abccba", "ab", "cababc", "bac"``.

Return ``true`` if and only if the given string ``S`` is valid.

Example 1:

    Input: "aabcbc"
    Output: true
    Explanation: 
    We start with the valid string "abc".
    Then we can insert another "abc" between "a" and "bc", resulting in "a" + "abc" + "bc" which is "aabcbc".

Example 2:

    Input: "abcabcababcc"
    Output: true
    Explanation: 
    "abcabcabc" is valid after consecutive insertings of "abc".
    Then we can insert "abc" before the last letter, resulting in "abcabcab" + "abc" + "c" which is "abcabcababcc".

Example 3:

    Input: "abccba"
    Output: false

Example 4:

    Input: "cababc"
    Output: false
 

Note:

1. ``1 <= S.length <= 20000``
1. ``S[i] is 'a', 'b', or 'c'``


## 题目大意

初始只给了一个``"abc"``字符串，然后可以在该字符串的任意位置插入一个新的``"abc"``字符串，然后继续该操作……这些步骤得到的字符串均为有效字符串。如果经过上面的操作无论如何都不能得到的字符串就是无效字符串。

问一个字符串是不是有效字符串。


## 解题方法

### 循环

好久没有做过这么简单的题目了……

如果理解了题意应该明白，每次都去插入一个``"abc"``字符串，那么到最后一步一定会有``"abc"``。所以我们如果倒着来，每次把``"abc"``进行替换成``""``，那么一定能回到最初的状态，也就是空字符串。

这个方法唯一不太好的是时间复杂度，判断"abc"是否在S中，需要O(N)的时间复杂度，替换这步的操作应该也是O(N)，所以总的时间复杂度是O(N^2)。题目给出的S的长度是20000，为什么没有超时呢？我觉得主要是替换的时候会把大量的"abc"同时替换掉了，这样每次操作就把字符串大幅变短了。

python代码如下：

```python
class Solution(object):
    def isValid(self, S):
        """
        :type S: str
        :rtype: bool
        """
        while "abc" in S:
            S = S.replace("abc", "")
        return not S
```

## 日期

2019 年 3 月 3 日 —— 3月开始，春天到了


  [1]: https://blog.csdn.net/fuxuemingzhu/article/details/85227593
