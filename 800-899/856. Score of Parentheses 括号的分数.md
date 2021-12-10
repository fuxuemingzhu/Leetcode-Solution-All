
作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)


题目地址：https://leetcode.com/problems/score-of-parentheses/description/


## 题目描述

Given a balanced parentheses string ``S``, compute the score of the string based on the following rule:

- ``()`` has score 1
- ``AB`` has score ``A + B``, where A and B are balanced parentheses strings.
- ``(A)`` has score ``2 * A``, where A is a balanced parentheses string.
 

Example 1:

    Input: "()"
    Output: 1

Example 2:

    Input: "(())"
    Output: 2

Example 3:

    Input: "()()"
    Output: 2

Example 4:

    Input: "(()(()))"
    Output: 6
 

Note:

1. S is a balanced parentheses string, containing only ( and ).
1. 2 <= S.length <= 50

## 题目大意

括号匹配的题目，但是这个匹配题目给定了条件：如果是``()``得1分，如果``AB``形式得2分，如果``(A)``分数是2×A.求最终多少分。

## 解题方法

### 栈

括号匹配的题目一般要用到栈，这个题也是。我们用栈保存两样东西：一是左括号``(``，二是得分。这样我们在遇到``)``返回的时候，可以直接判断栈里面是左括号还是得分。如果是左括号``(``，那么得分是1，放入栈中。如果是得分，那么我们需要一直向前求和直到找到左括号为止，然后把这个得分×2，放入栈中。

由于题目给的是符合要求的括号匹配对，那么栈里面最后应该只剩下一个元素了，就是最终得分。


Python代码如下：

```python
class Solution(object):
    def scoreOfParentheses(self, S):
        """
        :type S: str
        :rtype: int
        """
        stack = []
        score = 0
        for c in S:
            if c == '(':
                stack.append("(")
            else:
                tc = stack[-1]
                if tc == '(':
                    stack.pop()
                    stack.append(1)
                else:
                    num = 0
                    while stack[-1] != '(':
                        num += stack.pop()
                    stack.pop()
                    stack.append(num * 2)
        return sum(stack)
```

如果一个栈里面只放数值的话，那么，我们可以把遇到的左括号变成0放到栈里面。我们遇到右括号的时候，把前面的数字乘以2重新放入栈的末尾，但是``()``是直接放入1的。为了防止栈为空，那么在栈开始的时候放入一个0，当把栈过了一遍之后，剩余的数字就是所求。

用官方例子说明：

For example, when counting (()(())), our stack will look like this:

[0, 0] after parsing (
[0, 0, 0] after (
[0, 1] after )
[0, 1, 0] after (
[0, 1, 0, 0] after (
[0, 1, 1] after )
[0, 3] after )
[6] after )

python代码如下：

```python
class Solution(object):
    def scoreOfParentheses(self, S):
        """
        :type S: str
        :rtype: int
        """
        stack = [0]
        score = 0
        for c in S:
            if c == '(':
                stack.append(0)
            else:
                v = stack.pop()
                stack[-1] += max(v * 2, 1)
        return sum(stack)
```

### 递归

这个递归解法，我们使用的是从两头向中间的策略。如果找到的了``()``返回1，否则向中间找有没有提前匹配好的，这个如果存在就是``AB``形式，返回的是A+B。如果不存在的话，那说明是``(A)``形式，就返回2×A.

注意，在找AB的时候，i从l开始只能循环到r - 1，最后的一个括号不能进行匹配。

![此处输入图片的描述][1]

C++代码如下：

```cpp
class Solution {
public:
    int scoreOfParentheses(string S) {
        return helper(S, 0, S.size() - 1);
    }
private:
    int helper(string& s, int l, int r) {//[l, r]
        if (r - l == 1) return 1;
        int count = 0;
        for (int i = l; i < r; i++) {
            if (s[i] == '(')
                count++;
            else
                count--;
            if (count == 0) {
                return helper(s, l, i) + helper(s, i + 1, r);
            }
        }
        return helper(s, l + 1, r - 1) * 2;
    }
};
```

### 计数

我们从左到右去统计，开放的``'('``数目为d，如果遇到一个``(``就意味着里面的``()``要加倍。当我们遇到``()``的时候，需要增加2^(d-1)到结果里面。这个方法只关注``()``。

![此处输入图片的描述][2]

C++代码如下：

```cpp
class Solution {
public:
    int scoreOfParentheses(string S) {
        int res = 0, val = 0;
        for (int i = 0; i < S.size(); i ++) {
            if (S[i] == '(')
                val++;
            else{
                val--;
                if (S[i - 1] == '(')
                    res += 1 << val;
            }
        }
        return res;
    }
};
```


## 日期

2018 年 12 月 11 日 —— 双十一已经过去一个月了，真快啊。。


  [1]: https://zxi.mytechroad.com/blog/wp-content/uploads/2018/06/856-ep198.png
  [2]: https://zxi.mytechroad.com/blog/wp-content/uploads/2018/06/856-ep198-2.png
