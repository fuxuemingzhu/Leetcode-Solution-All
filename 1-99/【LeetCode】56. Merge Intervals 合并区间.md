
作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)

题目地址：[https://leetcode.com/problems/merge-intervals/#/description][1]


## 题目描述

Given a collection of intervals, merge all overlapping intervals.

Example 1:

	Input: [[1,3],[2,6],[8,10],[15,18]]
	Output: [[1,6],[8,10],[15,18]]
	Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].

Example 2:

	Input: [[1,4],[4,5]]
	Output: [[1,5]]
	Explanation: Intervals [1,4] and [4,5] are considered overlapping.

## 题目大意

这个题目意思是在数轴上有多个区间，如果能合并成更大区间的就合并在一起。

## 解题方法

首先按照每个区间的start排序，然后遍历。

用start,end两个指针记录当前的区间的开始和结束，之后的工作就是比较每一个区间的开始是否小于等于上个区间的end值，如果小于等于说明有重叠、可以合并成更大区间，这个时候要选择当前的区间end和上个区间end的最大值作为新的end完成区间合并。如果当前区间的start大于上个区间的end，那么两个区间不能合并，故以start和end为开始和结束构建区间的放到结果list中。如此遍历所有，最后一个区间也要同样放到结果list中。

python代码如下：

```python
# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        N = len(intervals)
        if not N: return []
        intervals.sort(key = lambda x : x.start)
        res = []
        start = intervals[0].start
        end = intervals[0].end
        for it in intervals:
            if it.start <= end:
                end = max(end, it.end)
            else:
                cur = Interval(start, end)
                res.append(cur)
                start = it.start
                end = it.end
        res.append(Interval(start, end))
        return res
```

Java代码如下：

```java
/**
 * Definition for an interval.
 * public class Interval {
 *     int start;
 *     int end;
 *     Interval() { start = 0; end = 0; }
 *     Interval(int s, int e) { start = s; end = e; }
 * }
 */
public class Solution {
    public List<Interval> merge(List<Interval> intervals) {
		if (intervals.size() <= 1) {
			return intervals;
		}
		Collections.sort(intervals, new Comparator<Interval>() {
			@Override
			public int compare(Interval o1, Interval o2) {
				return o1.start - o2.start;
			}
		});
		int start = intervals.get(0).start;
		int end = intervals.get(0).end;
		List<Interval> answer = new ArrayList<Interval>();
		for (Interval interval : intervals) {
			if (interval.start <= end) {
				end = Math.max(end, interval.end);
			} else {
				answer.add(new Interval(start, end));
				start = interval.start;
				end = interval.end;
			}
		}
		answer.add(new Interval(start, end));
		return answer;  
    }
}
```

C++代码如下：

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
    vector<Interval> merge(vector<Interval>& intervals) {
        const int N = intervals.size();
        vector<Interval> res;
        if (N == 0) return res;
        sort(intervals.begin(), intervals.end(), [](Interval a, Interval b){
            return a.start < b.start;
        });
        int start = intervals[0].start;
        int end = intervals[0].end;
        for (auto& it : intervals) {
            if (it.start <= end) {
                end = max(it.end, end);
            } else {
                res.push_back(Interval(start, end));
                start = it.start;
                end = it.end;
            }
        }
        res.push_back(Interval(start, end));
        return res;
    }
};
```

## 日期

2017 年 4 月 4 日 
2019 年 1 月 9 日 —— 抓紧时间学习啊！

  [1]: https://leetcode.com/problems/merge-intervals/#/description
