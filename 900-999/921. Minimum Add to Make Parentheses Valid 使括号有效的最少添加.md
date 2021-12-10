
作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)


题目地址: https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/

## 题目描述

Given a string S of '(' and ')' parentheses, we add the minimum number of parentheses ( '(' or ')', and in any positions ) so that the resulting parentheses string is valid.

Formally, a parentheses string is valid if and only if:

- It is the empty string, or
- It can be written as ``AB`` (``A`` concatenated with ``B``), where ``A`` and ``B`` are valid strings, or
- It can be written as ``(A)``, where ``A`` is a valid string.

Given a parentheses string, return the minimum number of parentheses we must add to make the resulting string valid.


Example 1:

    Input: "())"
    Output: 1

Example 2:

    Input: "((("
    Output: 3

Example 3:

    Input: "()"
    Output: 0

Example 4:

    Input: "()))(("
    Output: 4
 

Note:

1. S.length <= 1000
1. S only consists of '(' and ')' characters.


## 题目大意

求最少添加几个括号才能使得整个表达式是合法的括号表达式。

## 解题方法

遇到括号匹配题一般想到用栈。这题也不例外。

同样是对字符串进行一次遍历，如果遍历到的位置是左括号，那么要进行判断：

1. 如果栈顶是右括号，那么说明判断前面字符串缺少了几个括号
2. 否则，需要直接进栈

如果遍历到的位置是右括号，那么直接进栈。

我花了半个小时才把这个题做出来啊，错误的地方就在于左括号的判断上。第一，判断前面缺少几个括号的时候，我把栈所有的元素全部退栈了，这样就错误了，因为可能前面部分匹配，再往前的左括号需要等待后面的右括号来了之后才能判断。所以，这个问题的解决方法是如果cnt == 0，就不再退栈了。第二，我把stack.append('(')写错位置了，事实上，只要出现新的左括号，这个左括号一定进栈。由于我太愚蠢了，把进栈这步放在了对栈的判断里面，这样就导致了不符合栈的判断条件的地方就没把左括号放进去。。这个是不应该犯的错误。

时间复杂度是O(N)，空间复杂度是O(N)。

```python
class Solution(object):
    def minAddToMakeValid(self, S):
        """
        :type S: str
        :rtype: int
        """
        if not S: return 0
        stack = []
        res = 0
        for i, s in enumerate(S):
            if '(' == s:
                if stack and (stack[-1] == ')'):
                    cnt = 0
                    while stack:
                        if stack.pop() == ')':
                            cnt -= 1
                        else:
                            cnt += 1
                        if cnt == 0:
                            break
                    res += abs(cnt)
                stack.append('(')
            else:
                stack.append(')')
        cnt = 0
        while stack:
            if stack.pop() == ')':
                cnt -= 1
            else:
                cnt += 1
        res += abs(cnt)
        return res
```

二刷使用了更简单的方法，直接把左括号进栈，遇到右括号时，如果栈里有左括号就弹出，否则需要加上右括号的个数。最后还要加上栈里面左括号的个数。

```python
class Solution(object):
    def minAddToMakeValid(self, S):
        """
        :type S: str
        :rtype: int
        """
        res = 0
        stack = []
        for c in S:
            if c == '(':
                stack.append('(')
            else:
                if stack:
                    stack.pop()
                else:
                    res += 1
        return res + len(stack)
```

C++代码还是长一点。

```cpp
class Solution {
public:
    int minAddToMakeValid(string S) {
        stack<char> s;
        int res = 0;
        for (auto c : S) {
            if (c == '(') {
                s.push('(');
            } else {
                if (!s.empty()) {
                    s.pop();
                } else {
                    res ++;
                }
            }
        }
        return res + s.size();
    }
};
```

## 日期

2018 年 10 月 14 日 —— 周赛做出来3个题，开心
2018 年 12 月 2 日 —— 又到了周日
