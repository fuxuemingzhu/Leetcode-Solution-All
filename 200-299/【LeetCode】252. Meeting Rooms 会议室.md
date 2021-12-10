
- 作者：    负雪明烛
- id：      fuxuemingzhu
- 个人博客：[http://fuxuemingzhu.cn/](http://fuxuemingzhu.cn/)

---
@[TOC](目录)


题目地址：https://leetcode-cn.com/problems/meeting-rooms/

## 题目描述

Given an array of meeting time intervals consisting of start and end times `[[s1,e1],[s2,e2],...] (si < ei)`, determine if a person could attend all meetings.

Example 1:

    Input: [[0,30],[5,10],[15,20]]
    Output: false

Example 2:

    Input: [[7,10],[2,4]]
    Output: true

## 题目大意

给定一个会议时间安排的数组，每个会议时间都会包括开始和结束的时间 [[s1,e1],[s2,e2],...] (si < ei)，请你判断一个人是否能够参加这里面的全部会议。

## 解题方法

### 排序

很经典的题目，按照会议结束的时间进行排序。排序之后，遍历数组，判断当前会议结束的时间是否比下一个会议开始时间**晚**，如果是，那肯定就无法参加所有的会议了。

```cpp
class Solution {
public:
    bool canAttendMeetings(vector<vector<int>>& intervals) {
        if (intervals.size() <= 1) return true;
        sort(intervals.begin(), intervals.end(),
             [](vector<int>& a, vector<int>&b) {return a[1] < b[1];});
        for (int i = 0; i < intervals.size() - 1; i++) {
            if (intervals[i][1] > intervals[i + 1][0])
                return false;
        }
        return true;
    }
};
```

## 日期

2019 年 9 月 17 日 —— 听了hulu宣讲会，觉得hulu的压力不大
