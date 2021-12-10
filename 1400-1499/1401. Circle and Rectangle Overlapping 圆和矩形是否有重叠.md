
- 作者：    负雪明烛
- id：      fuxuemingzhu
- 个人博客：[http://fuxuemingzhu.cn/](http://fuxuemingzhu.cn/)

---
@[TOC](目录)


题目地址：https://leetcode-cn.com/problems/circle-and-rectangle-overlapping/

# 题目描述

给你一个以 `(radius, x_center, y_center)` 表示的圆和一个与坐标轴平行的矩形 `(x1, y1, x2, y2)`，其中 `(x1, y1)` 是矩形左下角的坐标，`(x2, y2)` 是右上角的坐标。

如果圆和矩形有重叠的部分，请你返回 `True` ，否则返回 `False` 。

换句话说，请你检测是否 存在 点 `(xi, yi)` ，它既在圆上也在矩形上（两者都包括点落在边界上的情况）。

示例 1：

![在这里插入图片描述](https://imgconvert.csdnimg.cn/aHR0cHM6Ly9hc3NldHMubGVldGNvZGUtY24uY29tL2FsaXl1bi1sYy11cGxvYWQvdXBsb2Fkcy8yMDIwLzA0LzA0L3NhbXBsZV80XzE3MjgucG5n?x-oss-process=image/format,png)
    输入：radius = 1, x_center = 0, y_center = 0, x1 = 1, y1 = -1, x2 = 3, y2 = 1
    输出：true
    解释：圆和矩形有公共点 (1,0) 

示例 2：

![在这里插入图片描述](https://imgconvert.csdnimg.cn/aHR0cHM6Ly9hc3NldHMubGVldGNvZGUtY24uY29tL2FsaXl1bi1sYy11cGxvYWQvdXBsb2Fkcy8yMDIwLzA0LzA0L3NhbXBsZV8yXzE3MjgucG5n?x-oss-process=image/format,png)

    输入：radius = 1, x_center = 0, y_center = 0, x1 = -1, y1 = 0, x2 = 0, y2 = 1
    输出：true

示例 3：

![在这里插入图片描述](https://imgconvert.csdnimg.cn/aHR0cHM6Ly9hc3NldHMubGVldGNvZGUtY24uY29tL2FsaXl1bi1sYy11cGxvYWQvdXBsb2Fkcy8yMDIwLzA0LzA0L3NhbXBsZV82XzE3MjgucG5n?x-oss-process=image/format,png)

    输入：radius = 1, x_center = 1, y_center = 1, x1 = -3, y1 = -3, x2 = 3, y2 = 3
    输出：true

示例 4：

    输入：radius = 1, x_center = 1, y_center = 1, x1 = 1, y1 = -3, x2 = 2, y2 = -1
    输出：false
 

提示：

1. `1 <= radius <= 2000`
1. `-10^4 <= x_center, y_center, x1, y1, x2, y2 <= 10^4`
1. `x1 < x2`
1. `y1 < y2`


# 题目大意

要判断一个圆和另一个矩形是否有交点。

# 解题方法

## 利用公式

求矩形和圆是否相交的方法看：“怎样判断平面上一个矩形和一个圆形是否有重叠？ - Milo Yip的回答 - 知乎
https://www.zhihu.com/question/24251545/answer/27184960”。

总结一下：

1. 首先把矩形中心移动到坐标原点
2. 把圆形移动到第一象限
3. 求矩形和圆形的最短距离（可能是矩形的一个边，也可能是顶点）
4. 比较该最短距离和圆的半径

C++代码如下。

```cpp
class Solution {
public:
    bool checkOverlap(int radius, int x_center, int y_center, int x1, int y1, int x2, int y2) {
        float rec_x_center = (x1 + x2) / 2;
        float rec_y_center = (y1 + y2) / 2;
        vector<float> v = {fabs(x_center - rec_x_center), fabs(y_center - rec_y_center)};
        vector<float> h = {x2 - rec_x_center, y2 - rec_y_center};
        vector<float> u = {max(v[0] - h[0], 0.0f), max(v[1] - h[1], 0.0f)};
        return u[0] * u[0] + u[1] * u[1] <= radius * radius;
    }
};
```


 **欢迎关注[负雪明烛的刷题博客](https://blog.csdn.net/fuxuemingzhu)，leetcode刷题800多，每道都讲解了详细写法！**

# 日期

2020 年 4 月 5 日 —— 好久不打周赛了

