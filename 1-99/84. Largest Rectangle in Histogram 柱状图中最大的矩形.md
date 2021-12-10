作者： 		负雪明烛 
id：				fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)

题目地址: https://leetcode.com/problems/largest-rectangle-in-histogram/description/

## 题目描述

Given n non-negative integers representing the histogram's bar height where the width of each bar is 1, find the area of largest rectangle in the histogram.

![此处输入图片的描述][1]


Above is a histogram where width of each bar is 1, given height = [2,1,5,6,2,3].

 ![此处输入图片的描述][2]

The largest rectangle is shown in the shaded area, which has area = 10 unit.

 

Example:

    Input: [2,1,5,6,2,3]
    Output: 10

## 题目大意

计算一堆矩形能够成的面积最大的一块是多少。

## 解题方法
### 单调栈

这个题是**单调栈**的运用，使用一个**单调递增栈**来维护已经出现了的矩形高度。

1. 如果后面新来的元素高度比栈顶元素高，那么需要入栈，因为面积最大的元素会出现在后面。
2. 如果后面新来的元素高度比栈顶元素小，那么需要弹出栈里的元素，并且，每次弹出的时候都要对计算目前的宽度，相乘得到面积。

栈里保存索引的方式是需要掌握的，保存索引的方式在最小值栈结构中也有运用。

每次求栈内矩形的宽度的时候，其实是求其位置到最右边的距离。注意即将入栈的元素索引 `i` 是一直不变的，另外栈里的每个元素的索引可以认为是矩形的右边界。

[Leetcode #84 Largest Rectangle in Histogram][3]图文并茂，讲得很清楚。

最坏时间复杂度是O(N^2)，最优时间复杂度是O(N)，空间复杂度是O(N)。

```python
class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        stack = list()
        res = 0
        heights.append(0)
        N = len(heights)
        for i in range(N):
            if not stack or heights[i] > heights[stack[-1]]:
                stack.append(i)
            else:
                while stack and heights[i] <= heights[stack[-1]]:
                    h = heights[stack[-1]]
                    stack.pop()
                    w = i if not stack else i - stack[-1] - 1
                    res = max(res, h * w)
                stack.append(i)
        return res
```


参考资料：

https://www.cnblogs.com/boring09/p/4231906.html

## 日期

2018 年 10 月 9 日 —— 今天降温7度，注意保暖


  [1]: https://leetcode.com/static/images/problemset/histogram.png
  [2]: https://leetcode.com/static/images/problemset/histogram_area.png
  [3]: https://www.cnblogs.com/boring09/p/4231906.html
