# 【LeetCode】729. My Calendar I 解题报告

标签（空格分隔）： LeetCode

---

题目地址：https://leetcode.com/problems/my-calendar-i/description/


## 题目描述：

Implement a MyCalendar class to store your events. A new event can be added if adding the event will not cause a double booking.

Your class will have the method, ``book(int start, int end)``. Formally, this represents a booking on the half open interval ``[start, end)``, the range of real numbers x such that ``start <= x < end``.

A double booking happens when two events have some non-empty intersection (ie., there is some time that is common to both events.)

For each call to the method ``MyCalendar.book``, return true if the event can be added to the calendar successfully without causing a double booking. Otherwise, return false and do not add the event to the calendar.

Your class will be called like this: ``MyCalendar cal = new MyCalendar(); MyCalendar.book(start, end)``

    Example 1:
    MyCalendar();
    MyCalendar.book(10, 20); // returns true
    MyCalendar.book(15, 25); // returns false
    MyCalendar.book(20, 30); // returns true
    Explanation: 
    The first event can be booked.  The second can't because time 15 is already booked by another event.
    The third event can be booked, as the first event takes every time less than 20, but not including 20.

Note:

The number of calls to MyCalendar.book per test case will be at most 1000.
In calls to MyCalendar.book(start, end), start and end are integers in the range [0, 10^9].

## 解题方法

方法一：

这个题第一感觉很简单，但是却不知道该怎么做。看了别人的解答，发现BST用的恰到好处。

当第一次调用book的时候，初始化root节点。之后再book的时候，根据start,end判断是否和当前节点的时间段有交叉，如果有交叉就返回False；如果没有交叉，那么就一直向下寻找到叶子节点，到了叶子节点仍然没有交叉的话，就新建节点。

代码乍一看挺长的，但是明白了``book_helper``函数之后，其实很简单。

```python
class Node(object):
    def __init__(self, s, e):
        self.s = s
        self.e = e
        self.left = None
        self.right = None

class MyCalendar(object):

    def __init__(self):
        self.root = None
        
    def book_helper(self, s, e, node):
        if node.e <= s:
            if node.right:
                return self.book_helper(s, e, node.right)
            else:
                node.right = Node(s, e)
                return True
        elif node.s >= e:
            if node.left:
                return self.book_helper(s, e, node.left)
            else:
                node.left = Node(s, e)
                return True
        else:
            return False
        
    def book(self, start, end):
        """
        :type start: int
        :type end: int
        :rtype: bool
        """
        if not self.root:
            self.root = Node(start, end)
            return True
        else:
            return self.book_helper(start, end, self.root)


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)
```

## Date

2018 年 2 月 24 日 


  [1]: http://img.blog.csdn.net/20150926195427474