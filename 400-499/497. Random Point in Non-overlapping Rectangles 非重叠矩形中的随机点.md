作者： 		负雪明烛 
id：				fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---

题目地址: https://leetcode.com/problems/random-point-in-non-overlapping-rectangles/description/

## 题目描述：

Given a list of **non-overlapping** axis-aligned rectangles ``rects``, write a function ``pick`` which randomly and uniformily picks an **integer point** in the space covered by the rectangles.

Note:

1. An integer point is a point that has integer coordinates. 
1. A point on the perimeter of a rectangle is included in the space covered by the rectangles. 
1. ``i``th rectangle = ``rects[i]`` = ``[x1,y1,x2,y2]``, where ``[x1, y1]`` are the integer coordinates of the bottom-left corner, and ``[x2, y2]`` are the integer coordinates of the top-right corner.
1. length and width of each rectangle does not exceed ``2000``.
1. ``1 <= rects.length <= 100``
1. ``pick`` return a point as an array of integer coordinates ``[p_x, p_y]``
1. ``pick`` is called at most ``10000`` times.

Example 1:

Input: 

    ["Solution","pick","pick","pick"]
    [[[[1,1,5,5]]],[],[],[]]
    Output: 
    [null,[4,1],[4,1],[3,3]]

Example 2:

    Input: 
    ["Solution","pick","pick","pick","pick","pick"]
    [[[[-2,-2,-1,-1],[1,0,3,0]]],[],[],[],[],[]]
    Output: 
    [null,[-1,-2],[2,0],[-2,-1],[3,0],[-2,-2]]

Explanation of Input Syntax:

The input is two lists: the subroutines called and their arguments. Solution's constructor has one argument, the array of rectangles rects. pick has no arguments. Arguments are always wrapped with a list, even if there aren't any.

## 题目大意

给出了几个不重叠的长方形，按照覆盖面积随机在这些长方形中随机取横纵坐标都是整数的点。

## 解题方法

既然看到不重叠了，而且明显同一长方形内部的整数点被选择的概率相同，不同长方形内部的点被选择的概率等于该长方形的面积。那么我们肯定想到的是首先按照面积随机选择一个长方形，然后再在长方形中随机选择一个整数点就ok了。

所以，怎么按照面积选点呢？于是[528. Random Pick with Weight][1]就派到用场了。思想是把PDF转换成CDF，然后再随机选择点，找到这个点的upper_bound。整体的思路还是挺新颖的，所以一定得先把528题做出来才能做这个题。

这个题的做法基本一致，我提交错误好几次，最后通过思考题目给出的测试用例找到了原因。看题目给的第二个测试用例中，有个长方形是``[1, 0, 3, 0]``，这个面积不是0么？但是题目也认为这个是有3个整数点的长方形。所以求面积的方式得改啊，这个题不是简单的求长方形的面积，而是求长方形中整数点的个数，计算方式是``(x2 - x1 + 1) * (y2 - y1 + 1)``。

初始化的时间复杂度是O(N)，每次查询的时间复杂度是O(logN)，空间复杂度是O(N)。

```python
class Solution(object):

    def __init__(self, rects):
        """
        :type rects: List[List[int]]
        """
        self.rects = rects
        self.N = len(rects)
        areas = [(x2 - x1 + 1) * (y2 - y1 + 1) for x1, y1, x2, y2 in rects]
        self.preSum = [0] * self.N
        self.preSum[0] = areas[0]
        for i in range(1, self.N):
            self.preSum[i] = self.preSum[i - 1] + areas[i]
        self.total = self.preSum[-1]

    def pickRect(self):
        rand = random.randint(0, self.total - 1)
        return bisect.bisect_right(self.preSum, rand)

    def pickPoint(self, rect):
        x1, y1, x2, y2 = rect
        x = random.randint(x1, x2)
        y = random.randint(y1, y2)
        return x, y
        
    def pick(self):
        """
        :rtype: List[int]
        """
        rectIndex = self.pickRect()
        rect = self.rects[rectIndex]
        return self.pickPoint(rect)
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(rects)
# param_1 = obj.pick()
```


参考资料：

https://blog.csdn.net/fuxuemingzhu/article/details/81807215


## 日期

2018 年 10 月 16 日 —— 雨后天晴霾散


  [1]: https://blog.csdn.net/fuxuemingzhu/article/details/81807215
