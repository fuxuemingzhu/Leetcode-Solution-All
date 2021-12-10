作者： 		负雪明烛 
id：				fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---

题目地址: https://leetcode.com/problems/maximal-rectangle/description/

## 题目描述：

Given a 2D binary matrix filled with 0's and 1's, find the largest rectangle containing only 1's and return its area.

Example:

    Input:
    [
      ["1","0","1","0","0"],
      ["1","0","1","1","1"],
      ["1","1","1","1","1"],
      ["1","0","0","1","0"]
    ]
    Output: 6

## 题目大意

给出了一个二维的数组，求在这里面能够成的最大的矩形面积是多少。


## 解题方法

本以为会和[221. Maximal Square][1]做法一样使用DP解决，可是感觉状态转移方程太复杂，所以还是参考了[84. Largest Rectangle in Histogram][2]升级版的解法。

如图所示，如果把每一行的1和它上面的1连在一起，那么就可以看成一个个站里的矩形方块。那么我们的最终目的就是找出最大面积的矩形方块，所以就是第84题的做法了，使用单调栈。

![此处输入图片的描述][3]

需要注意的是，我们使用一个height数组，保存到某一层的第i个位置为止，能向上构成的矩形的高度。而且需要对每层都做一个寻找面积的操作，最终选择所有层中能够成矩形面积最大值。

时间复杂度是O(M(N+M))，空间复杂度是O(N)。

```python
class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix or not matrix[0]: return 0
        M, N = len(matrix), len(matrix[0])
        height = [0] * N
        res = 0
        for row in matrix:
            for i in range(N):
                if row[i] == '0':
                    height[i] = 0
                else:
                    height[i] += 1
            res = max(res, self.maxRectangleArea(height))
        return res            
            
    def maxRectangleArea(self, height):
        if not height: return 0
        res = 0
        stack = list()
        height.append(0)
        for i in range(len(height)):
            cur = height[i]
            while stack and cur < height[stack[-1]]:
                w = height[stack.pop()]
                h = i if not stack else i - stack[-1] - 1
                res = max(res, w * h)
            stack.append(i)
        return res
```


参考资料：

https://www.jianshu.com/p/cffdc94c9c19

## 日期

2018 年 10 月 10 日 —— 冻成狗


  [1]: https://blog.csdn.net/fuxuemingzhu/article/details/82992233
  [2]: https://blog.csdn.net/fuxuemingzhu/article/details/82977472
  [3]: https://upload-images.jianshu.io/upload_images/424375-2a5a361549e471e4.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1000/format/webp
