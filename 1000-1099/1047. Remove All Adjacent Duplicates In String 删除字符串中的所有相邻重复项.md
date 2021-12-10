作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)


题目地址：https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/

## 题目描述

Given a string ``S`` of lowercase letters, a *duplicate removal* consists of choosing two adjacent and equal letters, and removing them.

We repeatedly make duplicate removals on S until we no longer can.

Return the final string after all such duplicate removals have been made.  It is guaranteed the answer is unique.
 

Example 1:
    
    Input: "abbaca"
    Output: "ca"
    Explanation: 
    For example, in "abbaca" we could remove "bb" since the letters are adjacent and equal, and this is the only possible move.  The result of this move is that the string is "aaca", of which only "aa" is possible, so the final string is "ca".
 

Note:

1. ``1 <= S.length <= 20000``
1. ``S`` consists only of English lowercase letters.


## 题目大意

每次去除字符串中两个相邻且相等的字符，求最后剩下的字符串（结果唯一）。

## 解题方法

### 栈

两个相等的字符连续出现则都消除掉，另外题目也说了结果唯一。有点类似与括号匹配问题，所以，我们一个很容易想到栈去解决。

顺序遍历字符串，如果当前的字符和栈顶字符相同，那么出栈；否则，把结果放到栈里面。最后栈里剩余的字符串即为所求。

Python代码如下：

```python
class Solution(object):
    def removeDuplicates(self, S):
        """
        :type S: str
        :rtype: str
        """
        stack = []
        for s in S:
            if stack and s == stack[-1]:
                stack.pop()
                continue
            stack.append(s)
        return "".join(stack)
```

## 日期

2019 年 5 月 22 日 —— 一个多月不刷题了，重新捡起来


  [1]: https://blog.csdn.net/fuxuemingzhu/article/details/79463006
