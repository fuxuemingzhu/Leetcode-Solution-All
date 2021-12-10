作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)


题目地址：https://leetcode.com/problems/minimum-increment-to-make-array-unique/description/


## 题目描述

Given two sequences ``pushed`` and ``popped`` **with distinct values**, return ``true`` if and only if this could have been the result of a sequence of push and pop operations on an initially empty stack.
 

Example 1:

    Input: pushed = [1,2,3,4,5], popped = [4,5,3,2,1]
    Output: true
    Explanation: We might do the following sequence:
    push(1), push(2), push(3), push(4), pop() -> 4,
    push(5), pop() -> 5, pop() -> 3, pop() -> 2, pop() -> 1

Example 2:

    Input: pushed = [1,2,3,4,5], popped = [4,3,5,1,2]
    Output: false
    Explanation: 1 cannot be popped before 2.
 

Note:

1. ``0 <= pushed.length == popped.length <= 1000``
1. ``0 <= pushed[i], popped[i] < 1000``
1. ``pushed`` is a permutation of ``popped``.
1. ``pushed`` and ``popped`` have distinct values.
 

## 题目大意

给出了一个栈的输入数字，按照这个顺序输入到栈里，能不能得到一个对应的栈的输出序列。


## 解题方法

### 模拟过程

我使用的方法异常简单粗暴，直接模拟这个过程。

题目已知所有的数字都是不同的。我们在模拟这个弹出的过程中，进行一个判断，如果这个弹出的数字和栈顶数字是吻合的，那么栈就要把已有的数字弹出来。如果栈是空的，或者栈顶数字和弹出的数字不等，那么我们应该把pushed数字一直往里放，直到相等为止。

最后，如果栈的入栈序列能得到这个出栈序列，那么栈应该是空的。


```python
class Solution(object):
    def validateStackSequences(self, pushed, popped):
        """
        :type pushed: List[int]
        :type popped: List[int]
        :rtype: bool
        """
        stack = []
        N = len(pushed)
        pi = 0
        for i in range(N):
            if stack and popped[i] == stack[-1]:
                stack.pop()
            else:
                while pi < N and pushed[pi] != popped[i]:
                    stack.append(pushed[pi])
                    pi += 1
                pi += 1
        return not stack
```

使用C++代码如下，思路和上面一样，其实可以简化代码。2018 年 12 月 7 日 —— 恩，12月又过去一周了


```cpp
class Solution {
public:
    bool validateStackSequences(vector<int>& pushed, vector<int>& popped) {
        bool canbe = true;
        int N = pushed.size();
        stack<int> s;
        int pi = 0;
        for (int i = 0; i < N; i++) {
            s.push(pushed[i]);
            while (!s.empty() && s.top() == popped[pi]) {
                s.pop();
                pi++;
            }
        }
        return s.empty();
    }
};
```


## 日期

2018 年 11 月 24 日 —— 周日开始！一周就过去了～
2018 年 12 月 7 日 —— 恩，12月又过去一周了


  [1]: http://zxi.mytechroad.com/blog/dynamic-programming/leetcode-730-count-different-palindromic-subsequences/
