
作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)

题目地址：https://leetcode.com/problems/spiral-matrix/description/

## 题目描述

Given a matrix of `m x n` elements (m rows, n columns), return all elements of the matrix in spiral order.

Example 1:

	Input:
	[
	 [ 1, 2, 3 ],
	 [ 4, 5, 6 ],
	 [ 7, 8, 9 ]
	]
	Output: [1,2,3,6,9,8,7,4,5]

Example 2:

	Input:
	[
	  [1, 2, 3, 4],
	  [5, 6, 7, 8],
	  [9,10,11,12]
	]
	Output: [1,2,3,4,8,12,11,10,9,5,6,7]

## 题目大意

顺时针螺旋着打印二维矩阵。

## 解题方法
### 维护四个边界和运动方向
螺旋打印，一定会在遍历的时候更改方向。在什么时候更改方向呢？在最外圈运动的时候是到达边界的时候。但是当移动到Example 1中4的位置时，要向右移动（而不是向上），那么相当于上边界已经移动了第二行。

同理，我们推断：

我们维护四个边界left, right, up, down，表示尚未走过的、可以移动的矩阵范围，起始时四个边界即矩阵的边界。当每次遇到新的边界的时候，需要把移动方向顺时针旋转90度，同时把刚刚走过的那个边界线（这条边界线上所有元素已经遍历过）需要**向矩阵内**移动，即缩小了边界。当所有的位置都被遍历了一次，则停止。

python代码如下，核心是每次遇到新的边界时，顺时针修改移动方向，并且将老边界内移。

```python
class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix or not matrix[0]: return []
        M, N = len(matrix), len(matrix[0])
        left, right, up, down = 0, N - 1, 0, M - 1
        res = []
        x, y = 0, 0
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        cur_d = 0
        while len(res) != M * N:
            res.append(matrix[x][y])
            if cur_d == 0 and y == right:
                cur_d += 1
                up += 1
            elif cur_d == 1 and x == down:
                cur_d += 1
                right -= 1
            elif cur_d == 2 and y == left:
                cur_d += 1
                down -= 1
            elif cur_d == 3 and x == up:
                cur_d += 1
                left += 1
            cur_d %= 4
            x += dirs[cur_d][0]
            y += dirs[cur_d][1]
        return res
```


### 保存已经走过的位置
一个比较蠢的实现方式：使用一个二维数组保存哪些走过了。这样遍历的时候，如果发现走过了就停止。因为while断开了，所以在当前的循环方向上要回退一格，然后移动行、列。

真的比较蠢 23333

```python
class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix or not matrix[0]: return []
        m, n = len(matrix), len(matrix[0])
        visited = [[0] * n for _ in range(m)]
        res = []
        self.row, self.col = 0, 0
        def spiral():
            move = False
            while self.col < n and not visited[self.row][self.col]:
                res.append(matrix[self.row][self.col])
                visited[self.row][self.col] = 1
                self.col += 1
                move = True
            self.col -= 1
            self.row += 1
            while self.row < m and not visited[self.row][self.col]:
                res.append(matrix[self.row][self.col])
                visited[self.row][self.col] = 1
                self.row += 1
                move = True
            self.row -= 1
            self.col -= 1
            while self.col >= 0  and not visited[self.row][self.col]:
                res.append(matrix[self.row][self.col])
                visited[self.row][self.col] = 1
                self.col -= 1
                move = True
            self.col += 1
            self.row -= 1
            while self.row >= 0 and not visited[self.row][self.col]:
                res.append(matrix[self.row][self.col])
                visited[self.row][self.col] = 1
                self.row -= 1
                move = True
            self.row += 1
            self.col += 1
            if move:
                spiral()
        spiral()
        return res
```

## 日期

2018 年 3 月 13 日 
2019 年 9 月 13 日   —— 一年半后的做法明显变得简单了~


  [1]: http://blog.csdn.net/fuxuemingzhu/article/details/79488113
