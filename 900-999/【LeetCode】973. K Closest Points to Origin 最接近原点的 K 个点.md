
作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)

题目地址：https://leetcode.com/problems/k-closest-points-to-origin/


## 题目描述

We have a list of ``points`` on the plane.  Find the ``K`` closest points to the origin ``(0, 0)``.

(Here, the distance between two points on a plane is the Euclidean distance.)

You may return the answer in any order.  The answer is guaranteed to be unique (except for the order that it is in.)

 

Example 1:

    Input: points = [[1,3],[-2,2]], K = 1
    Output: [[-2,2]]
    Explanation: 
    The distance between (1, 3) and the origin is sqrt(10).
    The distance between (-2, 2) and the origin is sqrt(8).
    Since sqrt(8) < sqrt(10), (-2, 2) is closer to the origin.
    We only want the closest K = 1 points from the origin, so the answer is just [[-2,2]].

Example 2:

    Input: points = [[3,3],[5,-1],[-2,4]], K = 2
    Output: [[3,3],[-2,4]]
    (The answer [[-2,4],[3,3]] would also be accepted.)
 

Note:

1. ``1 <= K <= points.length <= 10000``
1. ``-10000 < points[i][0] < 10000``
1. ``-10000 < points[i][1] < 10000``

## 题目大意

找出离原点``(0, 0)``最近的K个点。

## 解题方法

### 小根堆

经典的TopK，这个题的做法很多，最常见的就是使用小根堆。因为这是周赛，为了节省时间，我就直接使用了python的小根堆。

首先把每个元素距离原点的距离和该坐标组成tuple放到list里面，这样构建堆的时候，会按照第一个元素自动排序。提供了nsmallest方法直接取出最小的K个tuple，然后把坐标返回即可。

关于TopK，可以[看拜托，面试别再问我TopK了！！！](https://mp.weixin.qq.com/s/FFsvWXiaZK96PtUg-mmtEw)

python代码如下：

```python
class Solution(object):
    def kClosest(self, points, K):
        """
        :type points: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        """
        dis = []
        for p in points:
            d = math.sqrt(p[0] ** 2 + p[1] ** 2)
            dis.append((d, p))
        heapq.heapify(dis)
        return [d[1] for d in heapq.nsmallest(K, dis)]
```


## 日期

2019 年 1 月 13 日 —— 时间太快了


  [1]: https://assets.leetcode.com/uploads/2018/12/29/bst_cameras_01.png
  [2]: https://assets.leetcode.com/uploads/2018/12/29/bst_cameras_02.png
