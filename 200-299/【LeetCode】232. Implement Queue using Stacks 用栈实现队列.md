作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)

[LeetCode]

题目地址：[https://leetcode.com/problems/implement-queue-using-stacks/][1]

Total Accepted: 42648 Total Submissions: 125482 Difficulty: Easy


## 题目描述

Implement the following operations of a queue using stacks.

- push(x) -- Push element x to the back of queue.
- pop() -- Removes the element from in front of queue.
- peek() -- Get the front element.
- empty() -- Return whether the queue is empty.

Example:

	MyQueue queue = new MyQueue();
	
	queue.push(1);
	queue.push(2);  
	queue.peek();  // returns 1
	queue.pop();   // returns 1
	queue.empty(); // returns false

Notes:

1. You must use only standard operations of a stack -- which means only push to top, peek/pop from top, size, and is empty operations are valid.
1. Depending on your language, stack may not be supported natively. You may simulate a stack by using a list or deque (double-ended queue), as long as you use only standard operations of a stack.
1. You may assume that all operations are valid (for example, no pop or peek operations will be called on an empty queue).

## 题目大意

使用栈来实现一个队列。

## 解题方法

众所周知，需要用两个栈。只要想清楚两个栈来左右翻转就好了。

### Python解法

下面的python代码是把stack2当做是和队列顺序一样的，这样的话，如果stack2不空，那么久弹出元素就行。否则，如果stack1中有元素，那么在做push和pop的时候，需要先把stack1中的元素颠倒到stack2中。

```python
class MyQueue(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack1 = []
        self.stack2 = []

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: void
        """
        
        self.stack1.append(x)

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        if self.stack2:
            return self.stack2.pop()
        else:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
            return self.stack2.pop()

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        if self.stack2:
            return self.stack2[-1]
        else:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
            return self.stack2[-1]

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        return not self.stack1 and not self.stack2


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
```

### Java解法

注意，A栈的元素顺序和队列的元素顺序是一样的。也就是说当pop()或者peek()的时候，其实直接把最上面的元素给拿出来就好了。

```java
class MyQueue {
	Stack<Integer> stackA = new Stack<Integer>();
	Stack<Integer> stackB = new Stack<Integer>();

	// Push element x to the back of queue.
	public void push(int x) {
		if (stackA.isEmpty()) {
			stackA.push(x);
			System.out.println(stackA.toString());
			return;
		}
		while (!stackA.isEmpty()) {
			stackB.push(stackA.pop());
		}
		stackB.push(x);
		while (!stackB.isEmpty()) {
			stackA.push(stackB.pop());
		}
		System.out.println(stackA.toString());
	}

	// Removes the element from in front of queue.
	public void pop() {
		stackA.pop();
		System.out.println(stackA.toString());
	}

	// Get the front element.
	public int peek() {
		return stackA.peek();
	}

	// Return whether the queue is empty.
	public boolean empty() {
		return stackA.isEmpty();
	}
}
```

AC:113ms

## 日期

2016 年 05月 8日 
2018 年 11 月 21 日 —— 又是一个美好的开始

  [1]: https://leetcode.com/problems/implement-queue-using-stacks/
