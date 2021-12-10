
作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)

题目地址：https://leetcode.com/problems/exclusive-time-of-functions/description/

## 题目描述

Given the running logs of n functions that are executed in a nonpreemptive single threaded CPU, find the exclusive time of these functions.

Each function has a unique id, start from ``0`` to ``n-1``. A function may be called recursively or by another function.

A log is a string has this format : ``function_id:start_or_end:timestamp``. For example, ``"0:start:0"`` means function 0 starts from the very beginning of time 0. ``"0:end:0"`` means function 0 ends to the very end of time 0.

Exclusive time of a function is defined as the time spent within this function, the time spent by calling other functions should not be considered as this function's exclusive time. You should return the exclusive time of each function sorted by their function id.

Example 1:

    Input:
    n = 2
    logs = 
    ["0:start:0",
     "1:start:2",
     "1:end:5",
     "0:end:6"]
    Output:[3, 4]
    Explanation:
    Function 0 starts at time 0, then it executes 2 units of time and reaches the end of time 1. 
    Now function 0 calls function 1, function 1 starts at time 2, executes 4 units of time and end at time 5.
    Function 0 is running again at time 6, and also end at the time 6, thus executes 1 unit of time. 
    So function 0 totally execute 2 + 1 = 3 units of time, and function 1 totally execute 4 units of time.

Note:

1. Input logs will be sorted by timestamp, NOT log id.
2. Your output should be sorted by function id, which means the 0th element of your output corresponds to the exclusive time of function 0.
1. Two functions won't start or end at the same time.
1. Functions could be called recursively, and will always end.
1. 1 <= n <= 100



## 题目大意

求一个函数调用栈中各个函数各自的执行时间。这是个不能争夺资源的系统，同时只能运行一个函数。

给的数据包括函数的数量，以及各自的调用和结束的时间。

需要注意的是，开始时间是在时间片的开头，结束时间是在时间片的结尾。

## 解题方法

### 栈
这个题很好想到思路使用栈，因为我们已经知道了操作系统里面的函数调用确实就是用栈实现的。

因为同时只能运行一个函数，所以就是一个后进先出的栈。给出的调用日志一定会满足我们说的栈的条件的。

下面的解析应该能看明白。

首先要弄明白一点：当遍历到logs中的某个字符串时，无论它是begin还是end，当前位于栈顶的元素都会占用 “当前字符串的timePoint-之前字符串的timePoint”(或+1) 时间。

因为如果当前遍历到的字符串是start，那么栈顶元素就是之前start了还没结束的function，在 当前时间点 和 上一个时间点 之间的这段时间，是被栈顶元素占用的，占用了 “当前字符串的timePoint-之前字符串的timePoint” 时间。

如果当前遍历到的字符串是end，那么栈顶元素就是 当前字符串的function (前面一个字符串刚push进了该function的start) ，那么在 当前时间点 和 上一个时间点 之间的这段时间，也肯定是被栈顶元素占用的，占用 “当前字符串的timePoint-之前字符串的timePoint +1 ” 时间 (比之前多加了一个end时间点)。   

举个例子来说明：

    functionId:   0   1   2   2   1   0
    begin/end:    {   {   {   }   }   }
    timeItem:     0   1   2   3   4   5

0 被push进栈后，接下来遍历到 1 start 1，那么 0~1 的时间是被栈顶元素 0 占用的。接下来 1 被push进栈，遍历到 2 start 2，那么 1~2 的时间是被栈顶元素 1 占用的。接下来 2 被push进栈，遍历到 2 end 3，那么 2~3 的时间是被栈顶元素 2 占用的。接下来pop出 2 ，遍历到 1 end 4，那么3~4的时间是栈顶元素 1 占用的。接下来pop出 1 ，遍历到 0 end 5，那么 4~5 的时间是栈顶元素 0 占用的。

所以算法的关键在于：拿到上一个log的 start/stop time 设为prev，再拿到当前 log 的 start/stop time ，计算出两个time之间的时间差。注意prevTime表示的是当前这个操作结束之后的这一秒的开始时间，即如果是start那么就是这秒的开始时间，如果是end那么就是下一秒的开始时间。

摘自：http://blog.csdn.net/huanghanqian/article/details/77160234

```python
class Solution(object):
    def exclusiveTime(self, n, logs):
        """
        :type n: int
        :type logs: List[str]
        :rtype: List[int]
        """
        res = [0] * n
        stack = []
        prevTime = 0
        for log in logs:
            idx, type, time = log.split(':')
            if type == 'start':
                if stack:
                    res[stack[-1]] += int(time) - prevTime
                stack.append(int(idx))
                prevTime = int(time)
            else:
                res[stack[-1]] += int(time) - prevTime + 1
                stack.pop()
                prevTime = int(time) + 1
        return res
```

## 日期

2018 年 3 月 13 日 
2019 年 3 月 23 日 —— 时隔一年还是没有bug free
