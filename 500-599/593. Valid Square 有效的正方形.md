# 【LeetCode】593. Valid Square 解题报告（Python）

作者： 		负雪明烛 
id：				fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---

题目地址：https://leetcode.com/problems/valid-square/description/

## 题目描述：

Given the coordinates of four points in 2D space, return whether the four points could construct a square.

The coordinate (x,y) of a point is represented by an integer array with two integers.

Example:

    Input: p1 = [0,0], p2 = [1,1], p3 = [1,0], p4 = [0,1]
    Output: True

Note:

1. All the input integers are in the range [-10000, 10000].
1. A valid square has four equal sides with positive length and four equal angles (90-degree angles).
1. Input points have no order.

## 题目大意

给出4个点，看能不能构成正方形。

## 解题方法

数学问题还得数学好才行。我们想一想，肯定要按照边来判断。一个四边形有6条边，如果是正方形的话需要满足，4条相等的短边，以及两边相等的对角线边。

所以我们计算一下边的长度，然后判断一下是否只有两类边即可。注意四边形没有长度为0的边。

时间复杂度是O(1)，空间复杂度是O(1).

代码如下：

```python
class Solution(object):
    def validSquare(self, p1, p2, p3, p4):
        """
        :type p1: List[int]
        :type p2: List[int]
        :type p3: List[int]
        :type p4: List[int]
        :rtype: bool
        """
        def d(point1, point2):
            return (point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2
        s = set([d(p1, p2), d(p1, p3), d(p1, p4), d(p2, p3), d(p2, p4), d(p3, p4)])
        return 0 not in s and len(s) == 2
```

参考资料：

https://leetcode.com/problems/valid-square/discuss/103442/C++-3-lines-(unordered_set)

## 日期

2018 年 9 月 20 日 —— 趁年轻多读书
