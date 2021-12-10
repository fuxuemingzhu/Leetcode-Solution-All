

- 作者：    负雪明烛
- id：      fuxuemingzhu
- 个人博客：[http://fuxuemingzhu.cn/](http://fuxuemingzhu.cn/)

---
@[TOC](目录)


题目地址：https://leetcode-cn.com/problems/convex-polygon/

## 题目描述

Given a list of points that form a polygon when joined sequentially, find if this polygon is convex (Convex polygon definition).

 

Note:

1. There are at least 3 and at most 10,000 points.
1. Coordinates are in the range -10,000 to 10,000.
1. You may assume the polygon formed by given points is always a simple polygon (Simple polygon definition). In other words, we ensure that exactly two edges intersect at each vertex, and that edges otherwise don't intersect each other.
 

Example 1:

    [[0,0],[0,1],[1,1],[1,0]]
    
    Answer: True
    
Explanation: ![此处输入图片的描述][1]

Example 2:

    [[0,0],[0,10],[10,10],[10,0],[5,5]]
    
    Answer: False

Explanation:![此处输入图片的描述][2]



## 题目大意

判断一个多边形是不是凸多边形。

## 解题方法

### 计算向量夹角

借鉴了参考资料中的做法：

假设多边形的顶点是呈逆时针排列的，多边形是凸多边形的充要条件是：对于多边形的任何一条边，其下一条边必须是不朝右拐的（可以向左拐，也可以不拐）。那么如何判断下一条边是不朝右拐呢？假设假设当前边形成的向量是v1，下一条边形成的向量是v2，那么v2不朝右拐的充要条件是v1 x v2 >= 0，也就是它们形成的有向三角形的面积大于等于0，符合右手法则。

C++代码如下：

```cpp
class Solution {
public:
    bool isConvex(vector<vector<int>>& points) {
        int N = points.size();
        long pre = 0;
        for (int i = 0; i < N; ++i) {
            long cur = angle({points[i], points[(i + 1) % N], points[(i + 2) % N]});
            if (cur != 0) {
                if (cur * pre < 0)
                    return false;
                else
                    pre = cur;
            }
        }
        return true;
    }
    int angle(vector<vector<int>> A) {
        return  (A[1][0] - A[0][0]) * (A[2][1] - A[0][1]) - 
                (A[1][1] - A[0][1]) * (A[2][0] - A[0][0]);

    }
};
```

参考资料：https://blog.csdn.net/magicbean2/article/details/78593338

## 日期

2019 年 9 月 20 日 —— 是选择中国互联网式加班？还是外企式养生？


  [1]: https://assets.leetcode.com/uploads/2018/10/13/polygon_convex.png
  [2]: https://assets.leetcode.com/uploads/2018/10/13/polygon_not_convex.png
