# 【LeetCode】452. Minimum Number of Arrows to Burst Balloons 解题报告（Python）

标签（空格分隔）： LeetCode

---

题目地址：https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/description/

## 题目描述：

There are a number of spherical balloons spread in two-dimensional space. For each balloon, provided input is the start and end coordinates of the horizontal diameter. Since it's horizontal, y-coordinates don't matter and hence the x-coordinates of start and end of the diameter suffice. Start is always smaller than end. There will be at most 104 balloons.

An arrow can be shot up exactly vertically from different points along the x-axis. A balloon with xstart and xend bursts by an arrow shot at x if xstart ≤ x ≤ xend. There is no limit to the number of arrows that can be shot. An arrow once shot keeps travelling up infinitely. The problem is to find the minimum number of arrows that must be shot to burst all balloons.

    Example:
    
    Input:
    [[10,16], [2,8], [1,6], [7,12]]
    
    Output:
    2
    
    Explanation:
    One way is to shoot one arrow for example at x = 6 (bursting the balloons [2,8] and [1,6]) and another arrow at x = 11 (bursting the other two balloons).


## 题目大意

给出了一组气球的起始和结束的坐标，现在用箭去沿着y轴方向射。最少需要多少个箭才能把所有的气球打破？

## 解题方法

这个题是贪心算法的题目，看到这种问区间重叠情况的，一般都能想到是贪心。我们把所有的区间按照右边界进行排序，因为每个气球都要被打破，因此排序得到的第一组数据我们一定要使用。可以想到，只要沿着该数据最右边界的位置进行射箭一定能打破尽可能多的气球。然后依次移动射箭的位置，进行统计即可。

```python
class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        if not points: return 0
        points.sort(key = lambda x : x[1])
        curr_pos = points[0][1]
        ans = 1
        for i in range(len(points)):
            if curr_pos >= points[i][0]:
                continue
            curr_pos = points[i][1]
            ans += 1
        return ans
```

## 日期

2018 年 4 月 10 日 ———— 风很大，很舒服～～