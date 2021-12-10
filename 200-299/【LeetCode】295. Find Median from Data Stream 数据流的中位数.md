
作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)


题目地址：https://leetcode.com/problems/find-median-from-data-stream/

## 题目描述

Median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value. So the median is the mean of the two middle value.

For example,

    [2,3,4], the median is 3
    
    [2,3], the median is (2 + 3) / 2 = 2.5

Design a data structure that supports the following two operations:

- `void addNum(int num)` - Add a integer number from the data stream to the data structure.
- `double findMedian()` - Return the median of all elements so far.
 

Example:

    addNum(1)
    addNum(2)
    findMedian() -> 1.5
    addNum(3) 
    findMedian() -> 2
 

Follow up:

1. If all integer numbers from the stream are between 0 and 100, how would you optimize it?
1. If 99% of all integer numbers from the stream are between 0 and 100, how would you optimize it?
 
## 题目大意

求一个数据流的中位数。

## 解题方法

### 大根堆+小根堆

让我们找到一个无线数据流中的中位数。心路历程如下：

- 我们如果能排序，就能找到中位数  ==> 排序时间复杂度太高，不可
- 把数据集划分成两部分，一半比中位数小，一半比中位数大 ==> 数据分为两部分
- 只需要知道比中位数小的那部分的最大值和比中位数大的那部分的最小值 ==> 大根堆和小根堆

所以，使用了两个堆：lesser表示比中位数小的那部分，因为要找出这部分的最大值，所以需要是大根堆；larger表示比中位数大的那部分，因为要找出这部分的最小值，所以需要时小根堆。

约定：如果数据流长度是偶数，则lesser的数字个数和larger相等；如果数据流长度是奇数，则多余的那个数字放到lesser中。即lesser.size() - larger.size() <= 1。

每个数字进来的时候，先放入lesser中，把lesser中的最大值拿出来放到larger中，此时larger会和less一样多，或者larger比lesser多一个。当larger比lesser多一个时，把larger中的最小值拿出来放到lesser中，从而保证lesser.size() - larger.size() <= 1;。

如果lesser和larger两者数据个数相等，则中位数是lesser中的最大值和larger中的最小值的平均值；如果lesser比larger多一个，那么中位数是lesser中的最大值。

注意C++中，priority_queue默认是大根堆，小根堆的定义方法是`priority_queue<double, vector<double>, greater<double>>`。

C++代码如下：

```cpp
class MedianFinder {
public:
    /** initialize your data structure here. */
    MedianFinder() {
    }
    
    void addNum(int num) {
        lesser.push(num);
        larger.push(lesser.top());
        lesser.pop();
        if (larger.size() > lesser.size()) {
            lesser.push(larger.top());
            larger.pop();
        }
    }
    
    double findMedian() {
        return lesser.size() == larger.size() ? (lesser.top() + larger.top()) / 2 : lesser.top();
    }
private:
    // 存放比中位数小的数字，大根堆
    priority_queue<double> lesser;
    // 存放比中位数大的数字，小根堆
    priority_queue<double, vector<double>, greater<double>> larger;
};

/**
 * Your MedianFinder object will be instantiated and called as such:
 * MedianFinder* obj = new MedianFinder();
 * obj->addNum(num);
 * double param_2 = obj->findMedian();
 */
```

参考资料：https://www.cnblogs.com/grandyang/p/4896673.html

## 日期

2019 年 9 月 15 日 —— 中秋假期的最后一天啦，刷题加油~


  [1]: https://blog.csdn.net/fuxuemingzhu/article/details/100828798
  [2]: https://www.cnblogs.com/grandyang/p/6620334.html
