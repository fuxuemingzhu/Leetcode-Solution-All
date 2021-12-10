

- 作者：    负雪明烛
- id：      fuxuemingzhu
- 个人博客：[http://fuxuemingzhu.cn/](http://fuxuemingzhu.cn/)

---
@[TOC](目录)


题目地址：https://leetcode-cn.com/problems/max-stack/

## 题目描述

Design a max stack that supports push, pop, top, peekMax and popMax.

1. `push(x)` -- Push element x onto stack.
1. `pop()` -- Remove the element on top of the stack and return it.
1. `top()` -- Get the element on the top.
1. `peekMax()` -- Retrieve the maximum element in the stack.
1. `popMax()` -- Retrieve the maximum element in the stack, and remove it. If you find more than one maximum elements, only remove the top-most one.

Example 1:

    MaxStack stack = new MaxStack();
    stack.push(5); 
    stack.push(1);
    stack.push(5);
    stack.top(); -> 5
    stack.popMax(); -> 5
    stack.top(); -> 1
    stack.peekMax(); -> 5
    stack.pop(); -> 1
    stack.top(); -> 5

Note:

1. `-1e7 <= x <= 1e7`
1. Number of operations won't exceed 10000.
1. The last four operations won't be called when stack is empty.

## 题目大意

设计一个最大栈，支持 push、pop、top、peekMax 和 popMax 操作。

## 解题方法

### 双栈

这个题最大的难点在与popMax操作，即要求可以弹出栈中的最大值。

我们使用双栈，一个存放所有的数值，一个存放到当前数值为止的最大值。当要弹出最大值的时候，需要一个辅助的栈，存放数值栈中不是最大值的那些数字，弹出最大值之后，再把辅助栈中的所有元素Push到栈中。

C++代码如下：

```cpp
class MaxStack {
public:
    /** initialize your data structure here. */
    MaxStack() {
    }
    
    void push(int x) {
        if (!maxVals.empty() && x < maxVals.top()) {
            maxVals.push(maxVals.top());
        } else {
            maxVals.push(x);
        }
        values.push(x);
    }
    
    int pop() {
        int val = values.top();
        values.pop();
        maxVals.pop();
        return val;
    }
    
    int top() {
        return values.top();
    }
    
    int peekMax() {
        int maxv = maxVals.top();
        return maxv;
    }
    
    int popMax() {
        int maxv = maxVals.top();
        stack<int> temp;
        while (!values.empty() && values.top() != maxv) {
            temp.push(values.top());
            values.pop();
            maxVals.pop();
        }
        values.pop();
        maxVals.pop();
        while (!temp.empty()) {
            push(temp.top());
            temp.pop();
        }
        return maxv;
    }
private:
    stack<int> values;
    stack<int> maxVals;
};

/**
 * Your MaxStack object will be instantiated and called as such:
 * MaxStack* obj = new MaxStack();
 * obj->push(x);
 * int param_2 = obj->pop();
 * int param_3 = obj->top();
 * int param_4 = obj->peekMax();
 * int param_5 = obj->popMax();
 */
```

## 日期

2019 年 9 月 19 日 —— 举杯邀明月，对影成三人


  [1]: https://blog.csdn.net/fuxuemingzhu/article/details/100977773
