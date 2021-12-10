# 【LeetCode】731. My Calendar II 解题报告（Python）

作者： 		负雪明烛 
id：				fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---

题目地址：https://leetcode.com/problems/my-calendar-ii/description/

## 题目描述：

Implement a MyCalendarTwo class to store your events. A new event can be added if adding the event will not cause a triple booking.

Your class will have one method, ``book(int start, int end)``. Formally, this represents a booking on the half open interval [start, end), the range of real numbers x such that start <= x < end.

A triple booking happens when three events have some non-empty intersection (ie., there is some time that is common to all 3 events.)

For each call to the method MyCalendar.book, return true if the event can be added to the calendar successfully without causing a triple booking. Otherwise, return false and do not add the event to the calendar.

Your class will be called like this: ``MyCalendar cal = new MyCalendar(); MyCalendar.book(start, end)``

Example 1:

    MyCalendar();
    MyCalendar.book(10, 20); // returns true
    MyCalendar.book(50, 60); // returns true
    MyCalendar.book(10, 40); // returns true
    MyCalendar.book(5, 15); // returns false
    MyCalendar.book(5, 10); // returns true
    MyCalendar.book(25, 55); // returns true
    Explanation: 
    The first two events can be booked.  The third event can be double booked.
    The fourth event (5, 15) can't be booked, because it would result in a triple booking.
    The fifth event (5, 10) can be booked, as it does not use time 10 which is already double booked.
    The sixth event (25, 55) can be booked, as the time in [25, 40) will be double booked with the third event;
    the time [40, 50) will be single booked, and the time [50, 55) will be double booked with the second event.

Note:

- The number of calls to MyCalendar.book per test case will be at most 1000.
- In calls to MyCalendar.book(start, end), start and end are integers in the range [0, 10^9].

## 题目大意

每个日程都有一个开始和结束的时间，同一个时刻最多只能做两件事，当某个时间段内有第三件事出现的时候，就添加日程失败。求每次book的时候能否成功。

## 解题方法

使用暴力解法。

使用两个list分别保存已经预定了的区间和已经重叠了的区间。（深刻理解你定义的东西是什么，只有理解了才能做题）

判断区间重叠的方式是两个区间的起点的最大值 < 两个区间的终点的最小值。

那么，当一个新的区间到达的时候，先要对已经重叠的区间进行一个遍历，如果发现重叠，那么直接失败。

否则代表能添加成功，添加成功的含义是，当前区间不和任何overlaped里区间有交集。所以，更新已经重叠的区间的方式是找到和当前区间重叠的区间，然后添加到overlaped里。最后把当前区间放到booked里。

注意，在寻找新的重叠区间的时候，需要对所有的已经预定的区间进行遍历，也就是说我们当前的这个区间有可能和多个已经预定的区间重叠，要把多个重叠区间都放到overlaped里去。

时间复杂度是O(N^2)，空间复杂度是O(N).

代码如下：

```python
class MyCalendarTwo(object):

    def __init__(self):
        # 每个被book了的区间
        self.booked = list()
        # 每个重叠了的区间
        self.overlaped = list()

    def book(self, start, end):
        """
        :type start: int
        :type end: int
        :rtype: bool
        """
        for os, oe in self.overlaped:
            if max(os, start) < min(oe, end):
                return False
        for bs, be in self.booked:
            ss = max(bs, start)
            ee = min(be, end)
            if ss < ee:
                self.overlaped.append((ss, ee))
        self.booked.append((start, end))
        return True


# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)
```

参考资料：

https://www.youtube.com/watch?v=rRMdxFA-8G4

## 日期

2018 年 9 月 23 日 —— 今天是实验室第一个打卡的
