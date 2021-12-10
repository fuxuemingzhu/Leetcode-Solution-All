- 作者：    负雪明烛
- id：      fuxuemingzhu
- 个人博客：[http://fuxuemingzhu.cn/](http://fuxuemingzhu.cn/)

---
@[TOC](目录)

题目地址：https://leetcode-cn.com/problems/design-hit-counter/

## 题目描述

Design a hit counter which counts the number of hits received in the past 5 minutes.

Each function accepts a timestamp parameter (in seconds granularity) and you may assume that calls are being made to the system in chronological order (ie, the timestamp is monotonically increasing). You may assume that the earliest timestamp starts at 1.

It is possible that several hits arrive roughly at the same time.

Example:

    HitCounter counter = new HitCounter();
    
    // hit at timestamp 1.
    counter.hit(1);
    
    // hit at timestamp 2.
    counter.hit(2);
    
    // hit at timestamp 3.
    counter.hit(3);
    
    // get hits at timestamp 4, should return 3.
    counter.getHits(4);
    
    // hit at timestamp 300.
    counter.hit(300);
    
    // get hits at timestamp 300, should return 4.
    counter.getHits(300);
    
    // get hits at timestamp 301, should return 3.
    counter.getHits(301); 

Follow up:
What if the number of hits per second could be very large? Does your design scale?

## 题目大意

设计一个敲击计数器，使它可以统计在过去5分钟内被敲击次数。

每个函数会接收一个时间戳参数（以秒为单位），你可以假设最早的时间戳从1开始，且都是按照时间顺序对系统进行调用（即时间戳是单调递增）。

在同一时刻有可能会有多次敲击。

## 解题方法

### 字典

我们需要一个数据结构大小为300，能保存时间和该时间下对应的敲击次数。我选择的是字典。

当字典的元素个数超过了300时，应该把时间最早的删除掉，C++中map使用红黑树实现的，所以begin()就是最小的元素，将其删除即可。

查找300秒内的敲击次数时，需要遍历一遍map，如果时间窗在300秒以内，累加次数。

C++代码如下：

```cpp
class HitCounter {
public:
    /** Initialize your data structure here. */
    HitCounter() {
    }
    
    /** Record a hit.
        @param timestamp - The current timestamp (in seconds granularity). */
    void hit(int timestamp) {
        if (m_.size() >= 300) {
            m_.erase(m_.begin());
        }
        m_[timestamp] ++;
    }
    
    /** Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity). */
    int getHits(int timestamp) {
        int count = 0;
        for (auto& h : m_) {
            if (h.first > timestamp - 300)
                count += h.second;
        }
        return count;
    }
private:
    map<int, int> m_;
};

/**
 * Your HitCounter object will be instantiated and called as such:
 * HitCounter* obj = new HitCounter();
 * obj->hit(timestamp);
 * int param_2 = obj->getHits(timestamp);
 */
```

## 日期

2019 年 9 月 24 日 —— 梦见回到了小学，小学已经芳草萋萋破败不堪


  [1]: https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1569299800527&di=0791f14b34f5db98eb9acb10fbb908b1&imgtype=0&src=http://gss0.baidu.com/94o3dSag_xI4khGko9WTAnF6hhy/zhidao/pic/item/1ad5ad6eddc451da41652b3bb0fd5266d116324a.jpg
