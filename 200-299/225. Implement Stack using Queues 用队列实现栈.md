
作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)


题目地址：[https://leetcode.com/problems/implement-stack-using-queues/#/description][1]


## 题目描述


Implement the following operations of a stack using queues.

- push(x) -- Push element x onto stack.
- pop() -- Removes the element on top of the stack.
- top() -- Get the top element.
- empty() -- Return whether the stack is empty.

Example:

	MyStack stack = new MyStack();
	
	stack.push(1);
	stack.push(2);  
	stack.top();   // returns 2
	stack.pop();   // returns 2
	stack.empty(); // returns false

Notes:

1. You must use only standard operations of a queue -- which means only push to back, peek/pop from front, size, and is empty operations are valid.
1. Depending on your language, queue may not be supported natively. You may simulate a queue by using a list or deque (double-ended queue), as long as you use only standard operations of a queue.
1. You may assume that all operations are valid (for example, no pop or top operations will be called on an empty stack).

## 题目大意

金庸队列的操作实现一个栈。

## 解题方法

一个队列就可以解决，不需要两个队列的。

每次新元素进队列的时候，先把当前的数字进入队列，然后把它前面的所有的元素翻转一下，翻到了它的后面。

Java代码如下：

```java
public class MyStack {
    Queue<Integer> queue;
    /** Initialize your data structure here. */
    public MyStack() {
        queue = new LinkedList<Integer>();
    }
    
    /** Push element x onto stack. */
    public void push(int x) {
        queue.add(x);
        for(int i = 0; i < queue.size() -1; i++){
            queue.add(queue.poll());
        }
    }
    
    /** Removes the element on top of the stack and returns that element. */
    public int pop() {
        return queue.poll();
    }
    
    /** Get the top element. */
    public int top() {
        return queue.peek();
    }
    
    /** Returns whether the stack is empty. */
    public boolean empty() {
        return queue.isEmpty();
    }
}

/**
 * Your MyStack object will be instantiated and called as such:
 * MyStack obj = new MyStack();
 * obj.push(x);
 * int param_2 = obj.pop();
 * int param_3 = obj.top();
 * boolean param_4 = obj.empty();
 */
```

Python代码如下：

```python
class MyStack(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.que = collections.deque()

    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: void
        """
        self.que.append(x)
        for i in range(len(self.que) - 1):
            self.que.append(self.que.popleft())
            
    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        return self.que.popleft()
    
    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        return self.que[0]

    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        return not self.que

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
```

## 日期

2017 年 5 月 21 日 
2018 年 11 月 24 日 —— 周六快乐

  [1]: https://leetcode.com/problems/implement-stack-using-queues/#/description
