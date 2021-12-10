# 【LeetCode】435. Non-overlapping Intervals 解题报告（Python）

作者： 		负雪明烛 
id：				fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---

题目地址：https://leetcode.com/problems/non-overlapping-intervals/description/

## 题目描述：

Given a collection of intervals, find the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.

Note:

1. You may assume the interval's end point is always bigger than its start point.
1. Intervals like [1,2] and [2,3] have borders "touching" but they don't overlap each other.

Example 1:

    Input: [ [1,2], [2,3], [3,4], [1,3] ]
    
    Output: 1
    
    Explanation: [1,3] can be removed and the rest of intervals are non-overlapping.

Example 2:

    Input: [ [1,2], [1,2], [1,2] ]
    
    Output: 2
    
    Explanation: You need to remove two [1,2] to make the rest of intervals non-overlapping.

Example 3:

    Input: [ [1,2], [2,3] ]
    
    Output: 0
    
    Explanation: You don't need to remove any of the intervals since they're already non-overlapping.


## 题目大意

给出了一些区间，求最少需要移除多少个区间才能保证所有的区间不重叠。如果两个区间的起始点与终点重复，不认为是重叠。

## 解题方法

看到区间最值题一般想到排序+贪心。这个题和[452. Minimum Number of Arrows to Burst Balloons][1]挺相似。

这个题的做法也不难，这么思考：我们尽量移除那些覆盖最广的区间。

先对所有区间的起点进行排序，然后进行遍历，如果新的区间起点比老的区间终点小的话，说明有重叠，需要移除区间，移除哪个区间呢？当然是终点最靠后的终点。

我们使用last指针指向上个保留下来的节点，如果intervals[i].end < intervals[last].end，则代表新的区间终点更靠前，所以使用第i个节点代表last，也就是说移除了上面的那个last。然后统计移除了多少次区间即可。

时间复杂度是O(nlogn + n)，空间复杂度是O(1).

代码如下：

```python3
# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        if not intervals: return 0
        intervals.sort(key = lambda x : x.start)
        last = 0
        res = 0
        for i in range(1, len(intervals)):
            if intervals[last].end > intervals[i].start:
                if intervals[i].end < intervals[last].end:
                    last = i
                res += 1
            else:
                last = i
        return res
```

参考资料：

http://www.cnblogs.com/grandyang/p/6017505.html

## 日期

2018 年 9 月 16 日 ———— 天朗气清，惠风和畅


  [1]: https://blog.csdn.net/fuxuemingzhu/article/details/79888836