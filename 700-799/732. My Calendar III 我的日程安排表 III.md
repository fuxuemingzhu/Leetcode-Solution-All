# 【LeetCode】732. My Calendar III解题报告

标签（空格分隔）： LeetCode

---

题目地址：https://leetcode.com/problems/my-calendar-iii/description/


## 题目描述：

Implement a MyCalendarThree class to store your events. A new event can always be added.

Your class will have one method, book(int start, int end). Formally, this represents a booking on the half open interval [start, end), the range of real numbers x such that start <= x < end.

A K-booking happens when K events have some non-empty intersection (ie., there is some time that is common to all K events.)

For each call to the method MyCalendar.book, return an integer K representing the largest integer such that there exists a K-booking in the calendar.

Your class will be called like this: MyCalendarThree cal = new MyCalendarThree(); MyCalendarThree.book(start, end)

    Example 1:
    MyCalendarThree();
    MyCalendarThree.book(10, 20); // returns 1
    MyCalendarThree.book(50, 60); // returns 1
    MyCalendarThree.book(10, 40); // returns 2
    MyCalendarThree.book(5, 15); // returns 3
    MyCalendarThree.book(5, 10); // returns 3
    MyCalendarThree.book(25, 55); // returns 3
    Explanation: 
    The first two events can be booked and are disjoint, so the maximum K-booking is a 1-booking.
    The third event [10, 40) intersects the first event, and the maximum K-booking is a 2-booking.
    The remaining events cause the maximum K-booking to be only a 3-booking.
    Note that the last event locally causes a 2-booking, but the answer is still 3 because
    eg. [10, 20), [10, 40), and [5, 15) are still triple booked.
Note:

1. The number of calls to MyCalendarThree.book per test case will be at most 400.
1. In calls to MyCalendarThree.book(start, end), start and end are integers in the range [0, 10^9].

## 解题方法

看这个：https://www.cnblogs.com/FannyChung/p/7896415.html


代码：

```python
class Node(object):
    def __init__(self, start, end, c):
        self.start = start
        self.end = end
        self.count = c
        self.left = None
        self.right = None
        
class MyCalendarThree(object):
    def __init__(self):
        self.root = None
        self.maxK = 1
        
    def book_helper(self, root, start, end, c):
        if root == None:
            return Node(start, end, c)
        if start >= root.end:
            #不能写成return self.boook_helper()，因为要进行树的构建和修改，一定要赋值给root.right
            root.right = self.book_helper(root.right, start, end, c)
        elif end <= root.start:
            root.left = self.book_helper(root.left, start, end, c)
        else:
            intervals = sorted([start, end, root.start, root.end])
            root_l, root_r = root.start, root.end
            root.start, root.end = intervals[1], intervals[2]
            root.left = self.book_helper(root.left, intervals[0], intervals[1], c if start <= root_l else root.count)
            root.right = self.book_helper(root.right, intervals[2], intervals[3], c if end >= root_r else root.count)
            root.count += c
            self.maxK = max(root.count, self.maxK)
        return root

    def book(self, start, end):
        """
        :type start: int
        :type end: int
        :rtype: int
        """
        self.root = self.book_helper(self.root, start, end, 1)
        return self.maxK


# Your MyCalendarThree object will be instantiated and called as such:
# obj = MyCalendarThree()
# param_1 = obj.book(start,end)
```


## 日期

2018 年 2 月 25 日 