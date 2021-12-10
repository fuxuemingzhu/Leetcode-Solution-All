
作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)

题目地址：https://leetcode.com/problems/construct-quad-tree/description/

## 题目描述

We want to use quad trees to store an N x N boolean grid. Each cell in the grid can only be true or false. The root node represents the whole grid. For each node, it will be subdivided into four children nodes until the values in the region it represents are all the same.

Each node has another two boolean attributes : ``isLeaf`` and ``val. isLeaf`` is true if and only if the node is a leaf node. The val attribute for a leaf node contains the value of the region it represents.

Your task is to use a quad tree to represent a given grid. The following example may help you understand the problem better:

Given the 8 x 8 grid below, we want to construct the corresponding quad tree:

![此处输入图片的描述][1]

It can be divided according to the definition above:


![此处输入图片的描述][2]
 

The corresponding quad tree should be as following, where each node is represented as a (isLeaf, val) pair.

For the non-leaf nodes, val can be arbitrary, so it is represented as *.

![此处输入图片的描述][3]

Note:

1. N is less than 1000 and guaranteened to be a power of 2.
1. If you want to know more about the quad tree, you can refer to its wiki.


## 题目大意

题目很长，但是不要害怕。题目所说的四分树，其实就是平面上的一种集合结构。把一个边长为2的幂的正方形均分成4块，然后再均分到不能均分为止即为叶子节点。类似于树结构，这是一个平面结构。

## 解题方法

首先，这种结构和树结构非常类似，肯定使用递归求解。重要的是如何判断此树结构如何判断叶子节点、val。

所以定义了一个新的函数，如果一个正方形中所有的数字都是0，则val是False，否则val是True。

判断leaf的方法是看看格子里的所有的值是不是相同的，如果全是0或者1那么就是leaf，否则就不是。

本来应该是两个函数，但是我用一个函数有3个返回值就实现了。

其他的难点就在把正方形进行切分成四块了，这个不是难点。

代码如下：

```python3
"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""
class Solution:
    def construct(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: Node
        """
        isLeaf = self.isQuadTree(grid)
        _len = len(grid)
        if isLeaf == None:
            mid = _len // 2
            topLeftGrid = [[grid[i][j] for j in range(mid)] for i in range(mid)]
            topRightGrid = [[grid[i][j] for j in range(mid, _len)] for i in range(mid)]
            bottomLeftGrid = [[grid[i][j] for j in range(mid)] for i in range(mid, _len)]
            bottomRightGrid = [[grid[i][j] for j in range(mid, _len)] for i in range(mid, _len)]
            node = Node(True, False, self.construct(topLeftGrid), self.construct(topRightGrid), 
                        self.construct(bottomLeftGrid), self.construct(bottomRightGrid))
        elif isLeaf == False:
            node = Node(False, True, None, None, None, None)
        else:
            node = Node(True, True, None, None, None, None)
        return node
        
    def isQuadTree(self, grid):
        _len = len(grid)
        _sum = 0
        for i in range(_len):
            _sum += sum(grid[i])
        if _sum == _len ** 2:
            return True
        elif _sum == 0:
            return False
        else:
            return None
```

---
二刷，换了一种写法，也是递归。

```python
"""
# Definition for a QuadTree node.
class Node(object):
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""
class Solution(object):
    def construct(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: Node
        """
        N = len(grid)
        if N == 1:
            return Node(grid[0][0] == 1, True, None, None, None, None)
        topLeftSum = sum([grid[i][j] for i in range(N/2) for j in range(N/2)])
        topRightSum = sum([grid[i][j] for i in range(N/2) for j in range(N/2, N)])
        bottomLeftSum = sum([grid[i][j] for i in range(N/2, N) for j in range(N/2)])
        bottomRightSum = sum(grid[i][j] for i in range(N/2, N) for j in range(N/2, N))
        node = Node(False, False, None, None, None, None)
        if topLeftSum == topRightSum == bottomLeftSum == bottomRightSum:
            if topLeftSum == 0:
                node.isLeaf = True
                node.val = False
            elif topLeftSum == (N / 2) ** 2:
                node.isLeaf = True
                node.val = True
        if node.isLeaf:
            return node
        node.val = True
        node.topLeft = self.construct([[grid[i][j] for j in range(N/2)] for i in range(N/2)])
        node.topRight = self.construct([[grid[i][j] for j in range(N/2, N)] for i in range(N/2)])
        node.bottomLeft = self.construct([[grid[i][j] for j in range(N/2)] for i in range(N/2, N)])
        node.bottomRight = self.construct([[grid[i][j] for j in range(N/2, N)] for i in range(N/2, N)])
        return node
```

## 日期

2018 年 8 月 19 日 —— 天阴阴，地潮潮，这种天气真舒服
2018 年 11 月 13 日 —— 时间有点快

  [1]: https://s3-lc-upload.s3.amazonaws.com/uploads/2018/02/01/962_grid.png
  [2]: https://s3-lc-upload.s3.amazonaws.com/uploads/2018/02/01/962_grid_divided.png
  [3]: https://s3-lc-upload.s3.amazonaws.com/uploads/2018/02/01/962_quad_tree.png
