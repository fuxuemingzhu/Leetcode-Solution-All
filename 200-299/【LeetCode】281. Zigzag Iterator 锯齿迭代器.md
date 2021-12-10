

- 作者：    负雪明烛
- id：      fuxuemingzhu
- 个人博客：[http://fuxuemingzhu.cn/](http://fuxuemingzhu.cn/)

---
@[TOC](目录)

题目地址：https://leetcode-cn.com/problems/zigzag-iterator/

## 题目描述

Given two 1d vectors, implement an iterator to return their elements alternately.

Example:

    Input:
    v1 = [1,2]
    v2 = [3,4,5,6] 
    
    Output: [1,3,2,4,5,6]
    
    Explanation: By calling next repeatedly until hasNext returns false, 
                 the order of elements returned by next should be: [1,3,2,4,5,6].

Follow up: What if you are given k 1d vectors? How well can your code be extended to such cases?

Clarification for the follow up question:

    The "Zigzag" order is not clearly defined and is ambiguous for k > 2 cases. If "Zigzag" does not look right to you, replace "Zigzag" with "Cyclic". For example:
    
    Input:
    [1,2,3]
    [4,5,6,7]
    [8,9]
    
    Output: [1,4,8,2,5,9,3,6,7].

## 题目大意

给出两个一维的向量，请你实现一个迭代器，交替返回它们中间的元素。

## 解题方法

### deque

看出题目的含义，有点类似于我们从不同链表中依次读取头部并删除头部的操作。所以可以使用数据结构来模拟这个操作，因此我们需要一个比较高效的能从头部删除元素的数据结构，比如双端队列deque。

具体做法是使用变量cur标识应该读取哪个deque，然后读取并删除该deque的头部，再修改变量cur。

C++代码如下：

```cpp
class ZigzagIterator {
public:
    ZigzagIterator(vector<int>& v1, vector<int>& v2) {
        d1 = deque<int>(v1.begin(), v1.end());
        d2 = deque<int>(v2.begin(), v2.end());
        if (v1.empty())
            cur = 1;
        else
            cur = 0;
    }

    int next() {
        int val = 0;
        if (cur == 0) {
            val = d1.front(); d1.pop_front();
            if (!d2.empty())
                cur = 1;
        } else if (cur == 1) {
            val = d2.front(); d2.pop_front();
            if (!d1.empty())
                cur = 0;
        }
        return val;
    }

    bool hasNext() {
        return !d1.empty() || !d2.empty();
    }
private:
    deque<int> d1, d2;
    int cur = 0;
};

/**
 * Your ZigzagIterator object will be instantiated and called as such:
 * ZigzagIterator i(v1, v2);
 * while (i.hasNext()) cout << i.next();
 */
```

## 日期

2019 年 9 月 24 日 —— 梦见回到了小学，小学已经芳草萋萋破败不堪


  [1]: https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1569299800527&di=0791f14b34f5db98eb9acb10fbb908b1&imgtype=0&src=http://gss0.baidu.com/94o3dSag_xI4khGko9WTAnF6hhy/zhidao/pic/item/1ad5ad6eddc451da41652b3bb0fd5266d116324a.jpg
