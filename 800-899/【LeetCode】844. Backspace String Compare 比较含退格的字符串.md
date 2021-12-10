
作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)

题目地址：https://leetcode.com/problems/backspace-string-compare/description/

## 题目描述

Given two strings S and T, return if they are equal when both are typed into empty text editors. # means a backspace character.

Example 1:

    Input: S = "ab#c", T = "ad#c"
    Output: true
    Explanation: Both S and T become "ac".

Example 2:

    Input: S = "ab##", T = "c#d#"
    Output: true
    Explanation: Both S and T become "".

Example 3:

    Input: S = "a##c", T = "#a#c"
    Output: true
    Explanation: Both S and T become "c".

Example 4:

    Input: S = "a#c", T = "b"
    Output: false
    Explanation: S becomes "c" while T becomes "b".

Note:

1. 1 <= S.length <= 200
1. 1 <= T.length <= 200
1. S and T only contain lowercase letters and '#' characters.

Follow up:

- Can you solve it in O(N) time and O(1) space?


## 题目大意

在一个空白的编辑器里连续输入两段字符，其中#代表退格，要求最后两段字符是否相同。

有个Follow up，问我们能不能使用O(n)的时间复杂度和O(1)的空间复杂度。

## 解题方法

### 字符串切片

字符串题对于Python而言都不算题。就是按照题目要求做一遍就好了。

遇到#，字符串不为空，就删除最后一个字符。如果不是#号，就拼接到字符串的最后。把两个字符串都求出来，然后比较就好。

注意，我不小心踏进了一个坑，因为看到两个连续的if，就把它们合并在一起了，其实不行的：

```python
if s == '#':
    if ans_S:
        ans_S = ans_S[:-1]
```

我给改成了：

```python
if s == '#' and ans_S:
        ans_S = ans_S[:-1]
```

这样看着好看了，其实是错的。因为如果字符串是空的，那么输入#号，会把这个#号拼接到字符串上去。

Follow up的要求暂时不会。

代码如下：

```python
class Solution(object):
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        ans_S = ""
        ans_T = ""
        for s in S:
            if s == '#':
                if ans_S:
                    ans_S = ans_S[:-1]
            else:
                ans_S += s
        for t in T:
            if t == '#':
                if ans_T:
                    ans_T = ans_T[:-1]
            else:
                ans_T += t
        return ans_S == ans_T
                
```

### 栈

使用一个栈的话，可以完美处理这个问题，遇到#退栈就好了，唯一需要注意的时候如果栈是空的时候，不能退栈。


```python
class Solution(object):
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        stackS, stackT = [], []
        for s in S:
            if s != "#":
                stackS.append(s)
            elif stackS:
                stackS.pop()
        for t in T:
            if t != "#":
                stackT.append(t)
            elif stackT:
                stackT.pop()
        return stackS == stackT
```

## 日期

2018 年 6 月 10 日 —— 等了两天的腾讯比赛复赛B的数据集，结果人家在复赛刚开始就给了。。


  [1]: https://blog.csdn.net/fuxuemingzhu/article/details/80471765
