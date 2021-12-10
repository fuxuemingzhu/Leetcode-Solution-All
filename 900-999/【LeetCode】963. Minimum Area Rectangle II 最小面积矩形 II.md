

作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)


题目地址：https://leetcode.com/problems/minimum-area-rectangle-ii/


## 题目描述

Given a set of points in the xy-plane, determine the minimum area of ``any`` rectangle formed from these points, with sides ``not necessarily parallel`` to the x and y axes.

If there isn't any rectangle, return 0.


Example 1:

![此处输入图片的描述][1]
    
    Input: [[1,2],[2,1],[1,0],[0,1]]
    Output: 2.00000
    Explanation: The minimum area rectangle occurs at [1,2],[2,1],[1,0],[0,1], with an area of 2.

Example 2:

![此处输入图片的描述][2]

    Input: [[0,1],[2,1],[1,1],[1,0],[2,0]]
    Output: 1.00000
    Explanation: The minimum area rectangle occurs at [1,0],[1,1],[2,1],[2,0], with an area of 1.

Example 3:

![此处输入图片的描述][3]

    Input: [[0,3],[1,2],[3,1],[1,3],[2,1]]
    Output: 0
    Explanation: There is no possible rectangle to form from these points.

Example 4:

![此处输入图片的描述][4]

    Input: [[3,1],[1,1],[0,1],[2,1],[3,3],[3,2],[0,2],[2,3]]
    Output: 2.00000
    Explanation: The minimum area rectangle occurs at [2,1],[2,3],[3,3],[3,1], with an area of 2.
 

Note:

1. 1 <= points.length <= 50
1. 0 <= points[i][0] <= 40000
1. 0 <= points[i][5] <= 40000
1. All points are distinct.
1. Answers within 10^-5 of the actual value will be accepted as correct.


## 题目大意

给定一组坐标，找出四个顶点使其能构成长方形，求最小的长方形的面积。注意，边有可能不和x,y轴平行。

## 解题方法

### 线段长+线段中心+字典

前面有个平行于坐标轴的长方形题目，那个题目是固定对角线的两个点就能找出剩余两个点了，但是这个题可以不和坐标轴平行，那么问题就变大了。。

想来想去还是用长方形的性质，不过很显然仍然是和对象线有关的性质：

1. 长方形的两条对角线长度相等；
2. 长方形的两条对角线互相平分（中点重合）；

注意，如果满足上面两个条件的四边形就是长方形。

用上了这两个性质之后，题目从``点``的处理直接变成了``线段``的处理，时间复杂度降到了O(N^2).

具体做法是，我们求出任意两个点构成的线段的长度（的平方）、线段的中心坐标，然后用字典保存成``（长度，中心点x，中心点y）：[(线段1起点，线段1终点)， (线段2起点，线段2终点)……]``。把这个字典弄好了之后，我们需要对字典做一次遍历，依次遍历相同长度和中心点的两个线段构成的长方形的面积，保留最小值就好了。

知道两条对角线坐标，求长方形的面积，方法是找两条临边，然后相乘即可。

python代码如下：

```python
class Solution(object):
    def minAreaFreeRect(self, points):
        """
        :type points: List[List[int]]
        :rtype: float
        """
        N = len(points)
        # (l^2, x#, y#) : [(0,1), (1,2)]
        d = collections.defaultdict(list)
        for i in range(N - 1):
            pi = points[i]
            for j in range(i + 1, N):
                pj = points[j]
                l = (pi[0] - pj[0]) ** 2 + (pi[1] - pj[1]) ** 2
                x = (pi[0] + pj[0]) / 2.0
                y = (pi[1] + pj[1]) / 2.0
                d[(l, x, y)].append((i, j))
        res = float("inf")
        for l in d.values():
            M = len(l)
            for i in range(M - 1):
                p0, p2 = points[l[i][0]], points[l[i][1]]
                for j in range(i + 1, M):
                    p1, p3 = points[l[j][0]], points[l[j][1]]
                    d1 = math.sqrt((p0[0] - p1[0]) ** 2 + (p0[1] - p1[1]) ** 2)
                    d2 = math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)
                    area = d1 * d2
                    res = min(res, area)
        return 0 if res == float('inf') else res
```


## 日期

2018 年 12 月 23 日 —— 周赛成绩新高


  [1]: https://assets.leetcode.com/uploads/2018/12/21/1a.png
  [2]: https://assets.leetcode.com/uploads/2018/12/22/2.png
  [3]: https://assets.leetcode.com/uploads/2018/12/22/3.png
  [4]: https://assets.leetcode.com/uploads/2018/12/21/4c.png
  [5]: https://blog.csdn.net/fuxuemingzhu/article/details/79368360
  [6]: https://blog.csdn.net/fuxuemingzhu/article/details/79368360
  [7]: https://blog.csdn.net/fuxuemingzhu/article/details/79368360
