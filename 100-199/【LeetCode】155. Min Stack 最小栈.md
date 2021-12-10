- 作者：    负雪明烛
- id：      fuxuemingzhu
- 个人博客：[http://fuxuemingzhu.cn/](http://fuxuemingzhu.cn/)

---
@[TOC](目录)

题目地址：https://leetcode.com/problems/min-stack/description/


## 题目描述

Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

- push(x) -- Push element x onto stack.
- pop() -- Removes the element on top of the stack.
- top() -- Get the top element.
- getMin() -- Retrieve the minimum element in the stack.

Example:

	MinStack minStack = new MinStack();
	minStack.push(-2);
	minStack.push(0);
	minStack.push(-3);
	minStack.getMin();   --> Returns -3.
	minStack.pop();
	minStack.top();      --> Returns 0.
	minStack.getMin();   --> Returns -2.

## 解题方法

### 栈同时保存当前值和最小值


题目要求在常数时间内获得栈中的最小值，因此不能在`getMin()`的时候再去计算最小值，最好应该在`push`或者`pop`的时候就已经计算好了当前栈中的最小值。

前排的众多题解中，基本都讲了「辅助栈」的概念，这是一种常见的思路，但是有没有更容易懂的方法呢？

可以用一个栈，这个栈同时保存的是每个数字进栈的时候的**值与栈内最小值**。即每次新元素 `x` 入栈的时候保存一个元组：**（当前值 x，栈内最小值）**。

这个元组是一个整体，同时进栈和出栈。即栈顶同时有值和栈内最小值，`top()`函数是获取栈顶的**当前值**，即栈顶元组的第一个值； `getMin()`函数是获取**栈内最小值**，即栈顶元组的第二个值；`pop()`函数时删除栈顶的元组。

每次新元素入栈时，要求新的栈内最小值：比较当前新插入元素 x 和 当前栈内最小值（即栈顶元组的第二个值）的大小。

1. 新元素入栈：当栈为空，保存元组 `(x, x)`；当栈不空，保存元组 `(x, min(此前栈内最小值， x)))`
2. 出栈：删除栈顶的元组。

```python
class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        if not self.stack:
            self.stack.append((x, x))
        else:
            self.stack.append((x, min(x, self.stack[-1][1])))
        

    def pop(self):
        """
        :rtype: void
        """
        self.stack.pop()
        

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1][0]
        

    def getMin(self):
        """
        :rtype: int
        """
        return self.stack[-1][1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
```

### 辅助栈

#### 同步栈

也可以使用一个辅助栈，专门保存到目前为止的最小值。

所谓「同步栈」是指，辅助栈存储的最小值的`push`和`pop`完全与保存元素栈保持同步。

```python
class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min = []
        

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.stack.append(x)
        if not self.min:
            self.min.append(x)
        else:
            self.min.append(min(self.min[-1], x))

    def pop(self):
        """
        :rtype: void
        """
        self.stack.pop()
        self.min.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.min[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
```

C++代码如下：

```cpp
class MinStack {
public:
    /** initialize your data structure here. */
    MinStack() {
    }
    
    void push(int x) {
        if (!mins.empty() && x > mins.top()) {
            mins.push(mins.top());
        } else {
            mins.push(x);
        }
        values.push(x);
    }
    
    void pop() {
        values.pop();
        mins.pop();
    }
    
    int top() {
        return values.top();
    }
    
    int getMin() {
        return mins.top();
    }
private:
    stack<int> values;
    stack<int> mins;
};

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack* obj = new MinStack();
 * obj->push(x);
 * obj->pop();
 * int param_3 = obj->top();
 * int param_4 = obj->getMin();
 */
```

#### 不同步栈

也使用一个辅助栈，但这个辅助栈与元素的插入不是同步的。

1. 当插入元素 x **小于等于**辅助栈的栈顶元素时，才把 x 插入到辅助栈的栈顶。
2. 当弹出的元素 x **等于**辅助栈的栈顶元素时，才把辅助栈的栈顶也弹出。

因此该辅助栈是一个单调递减栈。

C++ 代码如下：

```cpp
class MinStack {
public:
    /** initialize your data structure here. */
    MinStack() {
    }
    
    void push(int x) {
        st.push(x);
        if (min_values.size() == 0) {
            min_values.push(x);
        } else {
            if (x <= min_values.top()) {
                min_values.push(x);
            }
        }
    }
    
    void pop() {
        int cur = st.top();
        st.pop();
        if (cur == min_values.top()) {
            min_values.pop();
        }
    }
    
    int top() {
        return st.top();
    }
    
    int getMin() {
        return min_values.top();
    }
private:
    stack<int> st;
    stack<int> min_values;
};

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack* obj = new MinStack();
 * obj->push(x);
 * obj->pop();
 * int param_3 = obj->top();
 * int param_4 = obj->getMin();
 */
```

## 日期

2018 年 2 月 4 日 
2018 年 11 月 24 日 —— 周六快乐
2019 年 9 月 18 日 —— 今日又是九一八
