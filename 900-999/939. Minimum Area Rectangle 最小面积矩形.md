
作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)


题目地址：https://leetcode.com/problems/minimum-area-rectangle/description/


## 题目描述

Given a set of points in the xy-plane, determine the minimum area of a rectangle formed from these points, with sides parallel to the ``x`` and ``y`` axes.

If there isn't any rectangle, return 0.

Example 1:

    Input: [[1,1],[1,3],[3,1],[3,3],[2,2]]
    Output: 4

Example 2:

    Input: [[1,1],[1,3],[3,1],[3,3],[4,1],[4,3]]
    Output: 2
 

Note:

1. ``1 <= points.length <= 500``
1. ``0 <= points[i][0] <= 40000``
1. ``0 <= points[i][1] <= 40000``
1. All points are distinct.


## 题目大意

给了很多点，找出这些点中，任意选择4个点，形成一个长方形，要求长方形的边必须平行与坐标轴。求最小面积的长方形的面积是多少。

## 解题方法

### 确定对角线，找另外两点（4sum）

周赛的第三题，超时了很多次，确实需要优秀的解法才能通过。

最原始的想法就是，我们找出和坐标轴平行的三个点，来确定第四个点。这么做的话，时间复杂度是O(N^3)，果然超时了。这说明我对4sum理解还不够深刻啊！两天前刚做过的[454. 4Sum II][2]，做法就是确定两个数字的和，然后看剩余的两个数字的和是否存在即可。也就是说4sum的时间复杂度只有O(N^2)。

这个题正确的做法是先确定对角线两个点！题目要求所有的边必须平行坐标轴，就是告诉我们只用确定对角线两个元素，剩余的两个点可以直接求出来即可！因此不需要确定3个点的O(N^3)的遍历。

所以啊，还是需要活学活用才行啊！

题目应该说清楚：面积为0的不算长方形。这样我们才能做两个对角线点不重合的判断。

时间复杂度是O(N^2)，空间复杂度是O(N)。

Python代码如下：

```python
class Solution(object):
    def minAreaRect(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        points = map(tuple, points)
        points.sort()
        pset = set(points)
        N = len(points)
        res = float('inf')
        for i in range(N - 1):
            p1 = points[i]
            for j in range(i + 1, N):
                p4 = points[j]
                if p4[0] == p1[0] or p4[1] == p1[1]:
                    continue
                p2 = (p1[0], p4[1])
                p3 = (p4[0], p1[1])
                if p2 in pset and p3 in pset:
                    res = min(res, abs(p3[0] - p1[0]) * abs(p2[1] - p1[1]))
        return res if res != float("inf") else 0
```

C++代码如下：

```cpp
class Solution {
public:
    int minAreaRect(vector<vector<int>>& points) {
        set<pair<int, int>> pset;
        const int N = points.size();
        for (auto p : points) {
            pset.insert(make_pair(p[0], p[1]));
        }
        int res = INT_MAX;
        for (int i = 0; i < N; ++i) {
            for (int j = i + 1; j < N; ++j) {
                auto p1 = points[i];
                auto p2 = points[j];
                if (p1[0] == p2[0] || p1[1] == p2[1])
                    continue;
                pair<int, int> p3 = {p1[0], p2[1]};
                pair<int, int> p4 = {p2[0], p1[1]};
                if (pset.count(p3) && pset.count(p4))
                    res = min(res, abs((p2[1] - p1[1]) * (p2[0] - p1[0])));
            }
        }
        return res == INT_MAX ? 0 : res;
    }
};
```

在上面的C++做法中使用的是pair做set的索引，由于题目给出的point的坐标是有范围的，所以可以使用``40000 * p[0] + p[1]``作为确定一个点的方式。

```cpp
class Solution {
public:
    int minAreaRect(vector<vector<int>>& points) {
        set<int> pset;
        const int N = points.size();
        for (auto p : points) {
            pset.insert(40000 * p[0] + p[1]);
        }
        int res = INT_MAX;
        for (int i = 0; i < N; ++i) {
            for (int j = i + 1; j < N; ++j) {
                auto p1 = points[i];
                auto p2 = points[j];
                if (p1[0] == p2[0] || p1[1] == p2[1])
                    continue;
                vector<int> p3 = {p1[0], p2[1]};
                vector<int> p4 = {p2[0], p1[1]};
                if (pset.count(40000 * p3[0] + p3[1]) && pset.count(40000 * p4[0] + p4[1]))
                    res = min(res, abs((p2[1] - p1[1]) * (p2[0] - p1[0])));
            }
        }
        return res == INT_MAX ? 0 : res;
    }
};
```

### 字典保存出现的x值,y值的点

另一个高效的算法是使用字典进行保存。这样的话，如果我们确定了一个点(x,y)，那么可以快速找到和它相同x坐标或者y坐标的所有点，然后只用遍历这些点就行了。

具体做法是，使用两个字典xdict和ydict，保存每个x,y对应的坐标。然后对相同的x进行O(N^2)的遍历。这时相当于确定了相同x的两个点，然后对相同的y再进行遍历，这样确定了第三个点。第四个点不用遍历，可以直接查找是不是在所有的点中出现了即可。

最坏时间复杂度是O(N^3)，空间复杂度是O(N)。


```python
class Solution(object):
    def minAreaRect(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        points = map(tuple, points)
        points.sort()
        xdict, ydict = collections.defaultdict(list), collections.defaultdict(list)
        pset = set()
        res = float("inf")
        for point in points:
            xdict[point[0]].append(point)
            ydict[point[1]].append(point)
            pset.add(point)
        for x1 in xdict.keys():
            if len(xdict[x1]) == 1:
                continue
            for i in range(len(xdict[x1]) - 1):
                p1 = xdict[x1][i]
                for j in range(i + 1, len(xdict[x1])):
                    p2 = xdict[x1][j]
                    for p3 in ydict[p1[1]]:
                        if p3 != p1:
                            if (p3[0], p2[1]) in pset:
                                res = min(res, abs((p3[0] - p1[0]) * (p2[1] - p1[1])))
        return res if res != float("inf") else 0
```


## 日期

2018 年 11 月 11 日 —— 剁手节快乐


  [1]: https://assets.leetcode.com/uploads/2018/10/12/island.png
  [2]: https://blog.csdn.net/fuxuemingzhu/article/details/79473739
