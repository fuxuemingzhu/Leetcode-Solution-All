
- 作者：    负雪明烛
- id：      fuxuemingzhu
- 个人博客：[http://fuxuemingzhu.cn/](http://fuxuemingzhu.cn/)

---
@[TOC](目录)


题目地址：https://leetcode-cn.com/problems/meeting-rooms/

## 题目描述

Given an array of meeting time intervals consisting of start and end times `[[s1,e1],[s2,e2],...] (si < ei)`, find the minimum number of conference rooms required.

Example 1:

    Input: [[0, 30],[5, 10],[15, 20]]
    Output: 2

Example 2:

    Input: [[7,10],[2,4]]
    Output: 1

## 题目大意

给定一个会议时间安排的数组，每个会议时间都会包括开始和结束的时间 [[s1,e1],[s2,e2],...] (si < ei)，为避免会议冲突，同时要考虑充分利用会议室资源，请你计算至少需要多少间会议室，才能满足这些会议安排。

## 解题方法

### 排序+堆

这个做法参考了官方解答，先对所有的区间按照开始时间进行排序，使用小根堆保存每个会议的结束时间，堆的大小表示了现在已经占用了多少个会议室。

思路是，我们要申请会议室的时候，先看是不是可以释放会议室，将已经占用的会议室释放。

遍历判断每个区间的开始时间是否大于等于小根堆中最小元素（最早结束时间），如果大于等于，说明堆里面有个会议要结束了，将其弹出，代表释放了一个会议室；否则，说明堆里面的已经在使用的会议室没有空闲，只能新增加一个会议室。

由于优先占用释放的会议室，所以最后堆里面的元素个数表示总的需要占用多少个会议室。

C++代码如下：

```cpp
class Solution {
public:
    int minMeetingRooms(vector<vector<int>>& intervals) {
        sort(intervals.begin(), intervals.end(), [](vector<int>& a, vector<int>&b) {return a[0] < b[0];});
        priority_queue<int, vector<int>, greater<int>> que;
        for (vector<int>& interval : intervals) {
            if (!que.empty() && interval[0] >= que.top()) {
                que.pop();
            }
            que.push(interval[1]);
        }
        return que.size();
    }
};
```

参考资料：https://leetcode-cn.com/problems/meeting-rooms-ii/solution/hui-yi-shi-ii-by-leetcode/

## 日期

2019 年 9 月 17 日 —— 听了hulu宣讲会，觉得hulu的压力不大
