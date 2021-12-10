
作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)

题目地址：https://leetcode.com/problems/largest-triangle-area/description/

## 题目描述

You have a list of points in the plane. Return the area of the largest triangle that can be formed by any 3 of the points.

    Example:
    Input: points = [[0,0],[0,1],[1,0],[0,2],[2,0]]
    Output: 2
    
    Explanation: 
    The five points are show in the figure below. The red triangle is the largest.

![此处输入图片的描述][1]

Notes:

- 3 <= points.length <= 50.
- No points will be duplicated.
-  -50 <= points[i][j] <= 50.
- Answers within 10^-6 of the true value will be accepted as correct.

## 题目大意

给出一组二维坐标，求这些点能组成的最大三角形面积。

## 解题方法

### 三重循环

看了下数据的范围最多到50，所以O(n^3)的时间复杂度肯定能过的。所以直接使用三重遍即可。

根据坐标求三角形面积是有公式的。另外要注意的是我们再求的时候要加上绝对值符号。

![此处输入图片的描述][2]

![此处输入图片的描述][3]

```python
class Solution:
    def largestTriangleArea(self, points):
        """
        :type points: List[List[int]]
        :rtype: float
        """
        res = 0
        N = len(points)
        for i in range(N - 2):
            for j in range(i + 1, N - 1):
                for k in range(i + 2, N):
                    (x1, y1), (x2, y2), (x3, y3) = points[i], points[j], points[k]
                    res = max(res, 0.5 * abs(x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)))
        return res
```


### 组合函数

python的组合公式实现了数学中的组合运算符，节省了代码量。


```python
class Solution:
    def largestTriangleArea(self, points):
        """
        :type points: List[List[int]]
        :rtype: float
        """
        # S=(1/2)*(x1y2+x2y3+x3y1-x1y3-x2y1-x3y2)
        def f(p1, p2, p3):
            (x1, y1), (x2, y2), (x3, y3) = p1, p2, p3
            return 0.5 * abs(x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2))
        return max(f(a, b, c) for a, b, c in itertools.combinations(points, 3))
```

## 日期

2018 年 4 月 9 日 —— 天气变好，春暖花开～～
2018 年 11 月 ９ 日 —— 睡眠可以

  [1]: https://s3-lc-upload.s3.amazonaws.com/uploads/2018/04/04/1027.png
  [2]: http://www.ab126.com/d/file/geometric/2016-02-24/8127a3b9e643a0f5afb2e28c20233eee.png
  [3]: http://www.ab126.com/d/file/geometric/2016-02-24/c30dec33193122f952876e788c9bbf45.png
