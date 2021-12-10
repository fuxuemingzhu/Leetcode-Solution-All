
- 作者：    负雪明烛
- id：      fuxuemingzhu
- 个人博客：[http://fuxuemingzhu.cn/](http://fuxuemingzhu.cn/)

---
@[TOC](目录)


题目地址：https://leetcode-cn.com/problems/logger-rate-limiter/

## 题目描述

Design a logger system that receive stream of messages along with its timestamps, each message should be printed if and only if it is not printed in the last 10 seconds.

Given a message and a timestamp (in seconds granularity), return true if the message should be printed in the given timestamp, otherwise returns false.

It is possible that several messages arrive roughly at the same time.

Example:

    Logger logger = new Logger();
    
    // logging string "foo" at timestamp 1
    logger.shouldPrintMessage(1, "foo"); returns true; 
    
    // logging string "bar" at timestamp 2
    logger.shouldPrintMessage(2,"bar"); returns true;
    
    // logging string "foo" at timestamp 3
    logger.shouldPrintMessage(3,"foo"); returns false;
    
    // logging string "bar" at timestamp 8
    logger.shouldPrintMessage(8,"bar"); returns false;
    
    // logging string "foo" at timestamp 10
    logger.shouldPrintMessage(10,"foo"); returns false;
    
    // logging string "foo" at timestamp 11
    logger.shouldPrintMessage(11,"foo"); returns true;


## 题目大意

请你设计一个日志系统，可以流式接收日志以及它的时间戳。

该日志会被打印出来，需要满足一个条件：当且仅当日志内容 在过去的 10 秒钟内没有被打印过。

给你一条日志的内容和它的时间戳（粒度为秒级），如果这条日志在给定的时间戳应该被打印出来，则返回 true，否则请返回 false。

要注意的是，可能会有多条日志在同一时间被系统接收。

## 解题方法

### 字典

使用一个字典，保存如果10秒内没有被打印过的消息的时间戳。每个消息到达的时候，查找是否在字典中出现过，如果时间戳的间隔小于10秒，则直接返回false.

C++代码如下：

```cpp
class Logger {
public:
    /** Initialize your data structure here. */
    Logger() {
    }
    
    /** Returns true if the message should be printed in the given timestamp, otherwise returns false.
        If this method returns false, the message will not be printed.
        The timestamp is in seconds granularity. */
    bool shouldPrintMessage(int timestamp, string message) {
        if (m_.count(message) && timestamp - m_[message] < 10) {
            return false;
        }
        m_[message] = timestamp;
        return true;
    }
private:
    unordered_map<string, int> m_;
};

/**
 * Your Logger object will be instantiated and called as such:
 * Logger* obj = new Logger();
 * bool param_1 = obj->shouldPrintMessage(timestamp,message);
 */
```


## 日期

2019 年 9 月 17 日 —— 听了hulu宣讲会，觉得hulu的压力不大
