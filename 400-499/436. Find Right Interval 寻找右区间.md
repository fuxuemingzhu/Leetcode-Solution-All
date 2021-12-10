# 【LeetCode】436. Find Right Interval 解题报告（Python）

标签（空格分隔）： LeetCode

作者： 		负雪明烛 
id：				fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---

题目地址：https://leetcode.com/problems/find-right-interval/description/

## 题目描述：

Given a set of intervals, for each of the interval i, check if there exists an interval j whose start point is bigger than or equal to the end point of the interval i, which can be called that j is on the "right" of i.

For any interval i, you need to store the minimum interval j's index, which means that the interval j has the minimum start point to build the "right" relationship for interval i. If the interval j doesn't exist, store -1 for the interval i. Finally, you need output the stored value of each interval as an array.

Note:

- You may assume the interval's end point is always bigger than its start point.
- You may assume none of these intervals have the same start point.

Example 1:
    
    Input: [ [1,2] ]
    
    Output: [-1]
    
    Explanation: There is only one interval in the collection, so it outputs -1.

Example 2:

    Input: [ [3,4], [2,3], [1,2] ]
    
    Output: [-1, 0, 1]
    
    Explanation: There is no satisfied "right" interval for [3,4].
    For [2,3], the interval [3,4] has minimum-"right" start point;
    For [1,2], the interval [2,3] has minimum-"right" start point.

Example 3:

    Input: [ [1,4], [2,3], [3,4] ]
    
    Output: [-1, 2, -1]
    
    Explanation: There is no satisfied "right" interval for [1,4] and [3,4].
    For [2,3], the interval [3,4] has minimum-"right" start point.


## 题目大意

给了一堆区间，找出每个区间右边最近的区间。不允许重合，每个区间的起始点不重复。如果不存在就返回-1.

## 解题方法

这个题主要是要使用二叉搜索，我发现我对这个理解的不够深入。

做法还是很容易理解的，因为可以使用一个字典保存每个区间的索引，因为每个区间的起点都是不同的，所以可以使用这个开始点当做区间的标记。

对起始点进行排序之后（为什么要排序？因为我们要使用二分查找），遍历每个区间，找出比这个区间的结尾大的第一个区间的起点值，然后根据这个起点值再找到这个区间的索引。

这也就是lowwer_found和higher_fount。我要补一补这方面的内容了。

代码如下：

```python
# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def findRightInterval(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[int]
        """
        n = len(intervals)
        start_map = {interval.start : i for i, interval in enumerate(intervals)}
        start_list = [interval.start for interval in intervals]
        res = []
        start_list.sort()
        for interval in intervals:
            pos = self.higher_find(start_list, interval.end)
            res.append(start_map[start_list[pos]] if pos != -1 else -1)
        return res
    
    def higher_find(self, array, v):
        lo, hi = 0, len(array) - 1
        first = -1
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if array[mid] >= v:
                hi = mid - 1
                first = mid
            else:
                lo = mid + 1
        return first
                
```


参考资料：

https://leetcode.com/problems/find-right-interval/discuss/156832/Python-O(n*log(n))-O(n)-slow-AF

## 日期

2018 年 9 月 13 日 ———— 越刷越受挫