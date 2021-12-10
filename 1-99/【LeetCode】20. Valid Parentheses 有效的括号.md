
- 作者：    负雪明烛
- id：      fuxuemingzhu
- 个人博客：[http://fuxuemingzhu.cn/](http://fuxuemingzhu.cn/)
- 个人公众号：负雪明烛
- 本文关键词：有效，括号，括号匹配，栈，题解，leetcode, 力扣，Python, C++, Java

---
@[TOC](目录)

题目地址：[https://leetcode.com/problems/valid-parentheses/#/description][1]


## 题目描述

Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.

## 题目大意

有三种括号组成的字符串，看最后的结果是否能组成正常的括号。

## 解题方法

### Java解法

第一感觉就是栈，但是怎么用呢。这个方法就是如果左边的括号出现，那么把右边的括号放到栈里，这样，如果不是左边的括号出现时，弹出右边的括号，判断栈里边最后入的那个元素和目前的右边括号是否相同。如果不同就返回false。有种可能是入栈很多左括号，右括号个数小于左括号个数，所以最后也要判断一下栈是否为空，如果是空说明左右括号个数正好匹配。

```java
public class Solution {
    public boolean isValid(String s) {
        if(s == null || (s.length() & 1) == 1){
            return false;
        }
        Stack<Character> stack = new Stack<Character>();
        for(char c : s.toCharArray()){
            if(c == '('){
                stack.push(')');
            }else if(c == '['){
                stack.push(']');
            }else if(c == '{'){
                stack.push('}');
            }else if(stack.isEmpty() || stack.pop() != c){
                return false;
            }
        }
        return stack.isEmpty();
    }
}
```

---

### Python解法

二刷，Python，使用的也是栈。

```python
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        for c in s:
            if not stack:
                stack.append(c)
            else:
                if c in ['(', '[', '{']:
                    stack.append(c)
                else:
                    top = stack.pop()
                    if (top == '(' and c != ')') or \
                        (top == '[' and c != ']') or \
                        (top == '{' and c != '}'):
                        return False
        return not stack
```

## 日期

2017 年 5 月 17 日 
2018 年 11 月 24 日 —— 周六快乐

  [1]: https://leetcode.com/problems/valid-parentheses/#/description
