作者： 		负雪明烛 
id：				fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---

题目地址：https://leetcode.com/problems/rectangle-overlap/description/

## 题目描述：

A rectangle is represented as a list ``[x1, y1, x2, y2]``, where ``(x1, y1)`` are the coordinates of its bottom-left corner, and ``(x2, y2)`` are the coordinates of its top-right corner.

Two rectangles overlap if the area of their intersection is positive.  To be clear, two rectangles that only touch at the corner or edges do not overlap.

Given two (axis-aligned) rectangles, return whether they overlap.

    Example 1:
    
    Input: rec1 = [0,0,2,2], rec2 = [1,1,3,3]
    Output: true
    
    Example 2:
    
    Input: rec1 = [0,0,1,1], rec2 = [1,0,2,1]
    Output: false

Notes:

1. Both rectangles rec1 and rec2 are lists of 4 integers.
1. All coordinates in rectangles will be between -10^9 and 10^9.

## 题目大意

判断两个矩形区域是否相交。矩形的表示方法是[x1, y1, x2, y2]， (x1, y1)是矩形左下角点的坐标，(x2, y2)是矩形右上角的坐标。

## 解题方法

###  方法一：直接比较

求解方法有点烧脑。我在没有画图的情况下想清楚了，所以很快就写出来了。

把rec2当做基准的一个矩形。把rec1跟rec2进行比较。

先判断不想交的情况：

1. rec1的x2小于rec2的x1；此时rec1在rec2的左边。
2. rec1的y2小于rec2的y1；此时rec1在rec2的下边。
3. rec2的x2小于rec1的x1；此时rec1在rec2的右边
4. rec2的y2小于rec1的y1；此时rec1在rec2的上边。

取not代表相交的情况。

```python
class Solution:
    def isRectangleOverlap(self, rec1, rec2):
        """
        :type rec1: List[int]
        :type rec2: List[int]
        :rtype: bool
        """
        rec1_x1, rec1_y1, rec1_x2, rec1_y2 = rec1
        rec2_x1, rec2_y1, rec2_x2, rec2_y2 = rec2
        return not (rec1_x1 >= rec2_x2 or rec1_x2 <= rec2_x1 or rec1_y1 >= rec2_y2 or rec1_y2 <= rec2_y1)
```

### 方法二：求相交部分

这个做法和[223. Rectangle Area](https://blog.csdn.net/fuxuemingzhu/article/details/82973125)一样，直接根据相对的x, y的大小比较来找出相交部分。如果以x, y为相交部分都大于0的话，那么相交。

![在这里插入图片描述](https://img-blog.csdnimg.cn/20200318114705923.jpeg?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2Z1eHVlbWluZ3podQ==,size_16,color_FFFFFF,t_70)

```python
class Solution(object):
    def isRectangleOverlap(self, rec1, rec2):
        """
        :type rec1: List[int]
        :type rec2: List[int]
        :rtype: bool
        """
        [A, B, C, D], [E, F, G, H] = rec1, rec2
        x, y = (min(C, G) - max(A, E)), (min(D, H) - max(B, F))
        return x > 0 and y > 0
```

## 日期

2018 年 5 月 27 日 ———— 周末的天气很好～
