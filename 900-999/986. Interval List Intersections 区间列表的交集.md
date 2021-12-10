
作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)


题目地址：https://leetcode.com/problems/interval-list-intersections/


## 题目描述

Given two lists of **closed** intervals, each list of intervals is pairwise disjoint and in sorted order.

Return the intersection of these two interval lists.

(Formally, a closed interval ``[a, b]`` (with ``a <= b``) denotes the set of real numbers ``x`` with ``a <= x <= b``.  The intersection of two closed intervals is a set of real numbers that is either empty, or can be represented as a closed interval.  For example, the intersection of [1, 3] and [2, 4] is [2, 3].)

 

Example 1:

![此处输入图片的描述][1]

    Input: A = [[0,2],[5,10],[13,23],[24,25]], B = [[1,5],[8,12],[15,24],[25,26]]
    Output: [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]
    Reminder: The inputs and the desired output are lists of Interval objects, and not arrays or lists.
     

Note:

1. 0 <= A.length < 1000
1. 0 <= B.length < 1000
1. 0 <= A[i].start, A[i].end, B[i].start, B[i].end < 10^9

## 题目大意

给了两组区间，每个区间都是shaungb，求这两组区间之间的交集部分。

## 解题方法

### 双指针

这个题的做法很像merge排序的merge部分。首先复习一下Merge部分：把两个有序的数组合并成一个更大的有序数组，使用双指针从两个数组开始向后遍历，每次把较小的数字放到新的位置并将该指针后移，直到两个指针全部到达末尾。

这个题较为复杂的是一个区间包含了开始和结束两部分，两个区间的交集需要由两个区间的开始和结束共同决定。我画了一个图，说明了总的只有这6种相交的状态。

![在这里插入图片描述](https://img-blog.csdnimg.cn/2019021919441582.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2Z1eHVlbWluZ3podQ==,size_16,color_FFFFFF,t_70)

所以，对于四种相交的情况，很明显相交部分的区间的起点是A和B区间起点较大的一个，相交部分的终点是A和B区间终点较小的一个。至于接下来怎么移动指针，也可以明显看出，应该保留A和B区间结尾较大的那个，这个其实是个类似贪心的方法。保留结尾大的区间才会和另外一个区间集相交，因此应该移动的指针是结尾区间小的那个。

当两个区间不相交的时候，需要舍弃前面的那个区间，这个也是很明显的。

时间复杂度是O(M*N)。C++代码如下：


```cpp
/**
 * Definition for an interval.
 * struct Interval {
 *     int start;
 *     int end;
 *     Interval() : start(0), end(0) {}
 *     Interval(int s, int e) : start(s), end(e) {}
 * };
 */
class Solution {
public:
    vector<Interval> intervalIntersection(vector<Interval>& A, vector<Interval>& B) {
        vector<Interval> res;
        const int M = A.size();
        const int N = B.size();
        if (M == 0 || N == 0) return res;
        int ai = 0, bi = 0;
        while (ai != M && bi != N) {
            Interval a = A[ai];
            Interval b = B[bi];
            if (a.end < b.start) {
                ++ai;
            } else if (a.start > b.end) {
                ++bi;
            } else {
                res.push_back({max(a.start, b.start), min(a.end, b.end)});
                if (a.end <= b.end) {
                    ++ai;
                } else {
                    ++bi;
                }
            }
        }
        return res;
    }
};
```

## 日期

2019 年 2 月 19 日 —— 重拾状态


  [1]: https://assets.leetcode.com/uploads/2019/01/30/interval1.png
  [2]: https://images2015.cnblogs.com/blog/1024555/201612/1024555-20161218163120151-452283750.png
  [3]: https://images2015.cnblogs.com/blog/1024555/201612/1024555-20161218194508761-468169540.png
