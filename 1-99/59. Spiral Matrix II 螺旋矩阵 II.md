
作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)

题目地址：https://leetcode.com/problems/spiral-matrix-ii/description/

## 题目描述

Given an integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.

    For example,
    Given n = 3,
    
    You should return the following matrix:
    [
     [ 1, 2, 3 ],
     [ 8, 9, 4 ],
     [ 7, 6, 5 ]
    ]

## 题目大意

顺时针由内向内螺旋状把1～n^2这些数字生成二维矩阵。

## 解题方法

明显是[54. Spiral Matrix][1]的翻版，54题让我们打印，这个题让我们生成。因此其实是一样的套路，都是同样的方式进行遍历。

这个题由于没有给matrix，所以自己生成一个正方形的矩阵，然后把54题的读取matrix的值改为给matrix当前位置填写值即可。

### 维护四个边界和运动方向

螺旋填充，一定会在遍历的时候更改方向。在什么时候更改方向呢？在最外圈运动的时候是到达边界的时候。但是当移动到Example 1中4的位置时，要向右移动（而不是向上），那么相当于上边界已经移动了第二行。

同理，我们推断：

我们维护四个边界left, right, up, down，表示尚未走过的、可以移动的矩阵范围，起始时四个边界即矩阵的边界。当每次遇到新的边界的时候，需要把移动方向顺时针旋转90度，同时把刚刚走过的那个边界线（这条边界线上所有元素已经遍历过）需要向矩阵内移动，即缩小了边界。当所有的位置都被遍历了一次，则停止。

python代码如下，核心是每次遇到新的边界时，顺时针修改移动方向，并且将老边界内移。


### 保存已经走过的位置

一个比较蠢的实现方式：使用一个二维数组保存哪些走过了。这样遍历的时候，如果发现走过了就停止。因为while断开了，所以在当前的循环方向上要回退一格，然后移动行、列。


```python
class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        visited = [[0] * n for _ in range(n)]
        matrix = [[0] * n for _ in range(n)]
        self.row, self.col = 0, 0
        self.curr = 1
        def spiral():
            move = False
            while self.col < n and not visited[self.row][self.col]:
                matrix[self.row][self.col] = self.curr
                self.curr += 1
                visited[self.row][self.col] = 1
                self.col += 1
                move = True
            self.col -= 1
            self.row += 1
            while self.row < n and not visited[self.row][self.col]:
                matrix[self.row][self.col] = self.curr
                self.curr += 1
                visited[self.row][self.col] = 1
                self.row += 1
                move = True
            self.row -= 1
            self.col -= 1
            while self.col >= 0  and not visited[self.row][self.col]:
                matrix[self.row][self.col] = self.curr
                self.curr += 1
                visited[self.row][self.col] = 1
                self.col -= 1
                move = True
            self.col += 1
            self.row -= 1
            while self.row >= 0 and not visited[self.row][self.col]:
                matrix[self.row][self.col] = self.curr
                self.curr += 1
                visited[self.row][self.col] = 1
                self.row -= 1
                move = True
            self.row += 1
            self.col += 1
            if move:
                spiral()
        spiral()
        return matrix
```

## 日期

2018 年 3 月 13 日 
2019 年 9 月 13 日 —— 一年半后的做法明显变得简单了~

  [1]: http://blog.csdn.net/fuxuemingzhu/article/details/79541501
