
- 作者：    负雪明烛
- id：      fuxuemingzhu
- 个人博客：[http://fuxuemingzhu.cn/](http://fuxuemingzhu.cn/)

---
@[TOC](目录)


题目地址：https://leetcode-cn.com/problems/moving-average-from-data-stream/

## 题目描述

Given a stream of integers and a window size, calculate the moving average of all integers in the sliding window.

Example:

    MovingAverage m = new MovingAverage(3);
    m.next(1) = 1
    m.next(10) = (1 + 10) / 2
    m.next(3) = (1 + 10 + 3) / 3
    m.next(5) = (10 + 3 + 5) / 3


## 题目大意

计算一个固定大小的滑动窗口中的平均数。

## 解题方法

### 队列

一个固定大小的队列，每次插入数据之前判断队列是否已满，删除队列的头部元素，在队列的尾部插入元素即可。由于每次都求和比较耗时，因此可以使用一个sum变量保存队列里面元素的和。

C++代码如下：

```cpp
class MovingAverage {
public:
    /** Initialize your data structure here. */
    MovingAverage(int size) {
        cap = size;
    }
    
    double next(int val) {
        if (que.size() >= cap) {
            sum -= que.front();
            que.pop_front();
        }
        que.push_back(val);
        sum += val;
        return (double) sum / que.size();
    }
private:
    deque<int> que;
    int cap = 0;
    int count = 0;
    long long sum = 0;
};

/**
 * Your MovingAverage object will be instantiated and called as such:
 * MovingAverage* obj = new MovingAverage(size);
 * double param_1 = obj->next(val);
 */
```


## 日期

2019 年 9 月 18 日 —— 今日又是九一八
