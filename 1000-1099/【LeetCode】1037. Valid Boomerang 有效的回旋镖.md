作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)


题目地址：https://leetcode.com/problems/valid-boomerang/

## 题目描述

A boomerang is a set of 3 points that are all distinct and not in a straight line.

Given a list of three points in the plane, return whether these points are a boomerang.

Example 1:

    Input: [[1,1],[2,3],[3,2]]
    Output: true

Example 2:

    Input: [[1,1],[2,2],[3,3]]
    Output: false
 

Note:

1. `points.length == 3`
1. `points[i].length == 2`
1. `0 <= points[i][j] <= 100`
 
## 题目大意

判断三个点是否不重叠，并且不在一个直线上。

## 解题方法

### 中学数学题

不重叠很好说，三个点两两判断即可。

判断三个点是不是在一个直线上，那么三个点中任意两个点的连线之斜率是否相等（或者不存在）。用数学公式表示就是dx1 * dy2 == dx2 * dy1则在一条直线上。

C++代码如下：

```cpp
class Solution {
public:
    bool isBoomerang(vector<vector<int>>& points) {
        if (points[0][0] == points[1][0] && points[0][1] == points[1][1])
            return false;
        if (points[0][0] == points[2][0] && points[0][1] == points[2][1])
            return false;
        if (points[1][0] == points[2][0] && points[1][1] == points[2][1])
            return false;
        int dx1 = points[1][0] - points[0][0];
        int dy1 = points[1][1] - points[0][1];
        int dx2 = points[2][0] - points[1][0];
        int dy2 = points[2][1] - points[1][1];
        return dx1 * dy2 != dx2 * dy1;
    }
};
```

## 日期

2019 年 8 月 31 日 —— 赶在月底做个题
