作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)


题目地址：https://leetcode.com/problems/max-points-on-a-line/description/


## 题目描述

Given n points on a 2D plane, find the maximum number of points that lie on the same straight line.

Example 1:

    Input: [[1,1],[2,2],[3,3]]
    Output: 3
    Explanation:
    ^
    |
    |        o
    |     o
    |  o  
    +------------->
    0  1  2  3  4

Example 2:

    Input: [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
    Output: 4
    Explanation:
    ^
    |
    |  o
    |     o        o
    |        o
    |  o        o
    +------------------->
    0  1  2  3  4  5  6


## 题目大意

判断最多有多少个点在同一直线上。

## 解题方法

### 字典+最大公约数

这个题是个Hard题，而且通过率非常低。其实做法一点都不难。

我们想想如何判断三个点是否在一个直线上？初中知识告诉我们，两点确定一个直线。如果已经确定一个点，那么只需要计算另外两个点和当前点的斜率是否相等即可。当然如果另外两个点当中如果有和当前点重合的就不能直接求斜率了，这种情况重合的两个点无论怎么样都会和第三个点共线的。

在计算斜率的时候需要用到技巧，因为如果两个点的横坐标重合了，那么斜率是无穷大；如果斜率是浮点数，还会涉及到浮点数精度问题。所以使用了最大公约数这个技巧。我们不要直接计算斜率，而是相当于最简分式的形式，使用pair或者Python中的tuple，保存已经化为最简分数的两个数值，然后使用字典来统计这个pair出现了多少次。

最后的结果是共线并且不重合的点的最大个数+重叠的点的个数。

时间复杂度是O(N^2)，空间复杂度是O(N)。

```python
# Definition for a point.
# class Point(object):
#     def __init__(self, a=0, b=0):
#         self.x = a
#         self.y = b

class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[Point]
        :rtype: int
        """
        N = len(points)
        res = 0
        for i in range(N):
            lines = collections.defaultdict(int)
            duplicates = 1
            for j in range(i + 1, N):
                if points[i].x == points[j].x and points[i].y == points[j].y:
                    duplicates += 1
                    continue
                dx = points[i].x - points[j].x
                dy = points[i].y - points[j].y
                delta = self.gcd(dx, dy)
                lines[(dx / delta, dy / delta)] += 1
            res = max(res, (max(lines.values()) if lines else 0) + duplicates)
        return res
                
    def gcd(self, x, y):
        return x if y == 0 else self.gcd(y, x % y)
```


## 日期

2018 年 11 月 10 日 —— 这么快就到双十一了？？


  [1]: https://assets.leetcode.com/uploads/2018/10/12/island.png
  [2]: https://charlesliuyx.github.io/2018/10/11/%E3%80%90%E7%9B%B4%E8%A7%82%E7%AE%97%E6%B3%95%E3%80%91Egg%20Puzzle%20%E9%B8%A1%E8%9B%8B%E9%9A%BE%E9%A2%98/
