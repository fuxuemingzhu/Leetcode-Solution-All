
作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)

题目地址：https://leetcode.com/problems/quad-tree-intersection/description/

## 题目描述

A quadtree is a tree data in which each internal node has exactly four children: ``topLeft``, ``topRight``, ``bottomLeft`` and ``bottomRight``. Quad trees are often used to partition a two-dimensional space by recursively subdividing it into four quadrants or regions.

We want to store True/False information in our quad tree. The quad tree is used to represent a N * N boolean grid. For each node, it will be subdivided into four children nodes until the values in the region it represents are all the same. Each node has another two boolean attributes : isLeaf and val. isLeaf is true if and only if the node is a leaf node. The val attribute for a leaf node contains the value of the region it represents.

For example, below are two quad trees A and B:

    A:
    +-------+-------+   T: true
    |       |       |   F: false
    |   T   |   T   |
    |       |       |
    +-------+-------+
    |       |       |
    |   F   |   F   |
    |       |       |
    +-------+-------+
    topLeft: T
    topRight: T
    bottomLeft: F
    bottomRight: F
    
    B:               
    +-------+---+---+
    |       | F | F |
    |   T   +---+---+
    |       | T | T |
    +-------+---+---+
    |       |       |
    |   T   |   F   |
    |       |       |
    +-------+-------+
    topLeft: T
    topRight:
         topLeft: F
         topRight: F
         bottomLeft: T
         bottomRight: T
    bottomLeft: T
    bottomRight: F
     
    
Your task is to implement a function that will take two quadtrees and return a quadtree that represents the logical OR (or union) of the two trees.
    
    A:                 B:                 C (A or B):
    +-------+-------+  +-------+---+---+  +-------+-------+
    |       |       |  |       | F | F |  |       |       |
    |   T   |   T   |  |   T   +---+---+  |   T   |   T   |
    |       |       |  |       | T | T |  |       |       |
    +-------+-------+  +-------+---+---+  +-------+-------+
    |       |       |  |       |       |  |       |       |
    |   F   |   F   |  |   T   |   F   |  |   T   |   F   |
    |       |       |  |       |       |  |       |       |
    +-------+-------+  +-------+-------+  +-------+-------+

Note:

1. Both A and B represent grids of size N * N.
1. N is guaranteed to be a power of 2.
1. If you want to know more about the quad tree, you can refer to its wiki.
1. The logic OR operation is defined as this: "A or B" is true if A is true, or if B is true, or if both A and B are true.


## 题目大意

四叉树的题目。一个节点有四个分叉，在平面上的表示就是一个正方形的四个等分正方形。如果两个四叉树的或运算定义为每个分叉的或运算。如果某个节点的所有分叉都是同样的数值，需要合并成一个节点。

## 解题方法

树的题目一般都是用递归来做。这个题有意思的地方在于，需要进行节点的合并操作。

首先，可以做个简单的递归分析：如果一个节点是True，那么无论和什么样的节点进行或运算都是True.如果一个节点是False，那么无论和什么样的节点进行或运算都是什么样的节点。

新节点的四个分叉都分别进行或运算即可。最后判断如果四个分叉都是同样的数值，那么就合并。

这里体现了这个题目有意思的地方，并不需要输出结果和答案完全一致。答案判定的规则是，如果某节点是叶子节点就不去判断它的四个分叉了，所以我的输出里四个分叉没有设置为None，但是都同样通过了。另外，如果一个节点不是叶子节点的话，就不去判断它的val了。

这样的检测方法省了不少事，代码里面就没有写置None的过程。

比如：

    {"$id":"1","bottomLeft":{"$id":"4","bottomLeft":null,"bottomRight":null,"isLeaf":true,"topLeft":null,"topRight":null,"val":true},"bottomRight":{"$id":"5","bottomLeft":null,"bottomRight":null,"isLeaf":true,"topLeft":null,"topRight":null,"val":true},"isLeaf":false,"topLeft":{"$id":"2","bottomLeft":null,"bottomRight":null,"isLeaf":true,"topLeft":null,"topRight":null,"val":false},"topRight":{"$id":"3","bottomLeft":null,"bottomRight":null,"isLeaf":true,"topLeft":null,"topRight":null,"val":false},"val":false}
    {"$id":"1","bottomLeft":{"$id":"4","bottomLeft":null,"bottomRight":null,"isLeaf":true,"topLeft":null,"topRight":null,"val":false},"bottomRight":{"$id":"5","bottomLeft":null,"bottomRight":null,"isLeaf":true,"topLeft":null,"topRight":null,"val":true},"isLeaf":false,"topLeft":{"$id":"2","bottomLeft":null,"bottomRight":null,"isLeaf":true,"topLeft":null,"topRight":null,"val":true},"topRight":{"$id":"3","bottomLeft":null,"bottomRight":null,"isLeaf":true,"topLeft":null,"topRight":null,"val":true},"val":false}


我的输出是：

    {"$id":"1","bottomLeft":{"$id":"4","bottomLeft":null,"bottomRight":null,"isLeaf":true,"topLeft":null,"topRight":null,"val":true},"bottomRight":{"$id":"5","bottomLeft":null,"bottomRight":null,"isLeaf":true,"topLeft":null,"topRight":null,"val":true},"isLeaf":true,"topLeft":{"$id":"2","bottomLeft":null,"bottomRight":null,"isLeaf":true,"topLeft":null,"topRight":null,"val":true},"topRight":{"$id":"3","bottomLeft":null,"bottomRight":null,"isLeaf":true,"topLeft":null,"topRight":null,"val":true},"val":true}

答案是：

    {"$id":"1","bottomLeft":null,"bottomRight":null,"isLeaf":true,"topLeft":null,"topRight":null,"val":true}

代码如下：

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
    def intersect(self, q1, q2):
        """
        :type q1: Node
        :type q2: Node
        :rtype: Node
        """
        if q1.isLeaf:
            return q1 if q1.val else q2
        if q2.isLeaf:
            return q2 if q2.val else q1
        
        q1.topLeft = self.intersect(q1.topLeft, q2.topLeft)
        q1.topRight = self.intersect(q1.topRight, q2.topRight)
        q1.bottomLeft = self.intersect(q1.bottomLeft, q2.bottomLeft)
        q1.bottomRight = self.intersect(q1.bottomRight, q2.bottomRight)
        
        if q1.topLeft.isLeaf and q1.topRight.isLeaf and q1.bottomLeft.isLeaf and q1.bottomRight.isLeaf:
            if q1.topLeft.val == q1.topRight.val == q1.bottomLeft.val == q1.bottomRight.val:
                q1.isLeaf = True
                q1.val = q1.topLeft.val
        return q1
```

参考资料：

https://leetcode.com/problems/quad-tree-intersection/discuss/157532/Java-concise-code-beat-100

## 日期

2018 年 9 月 3 日 —— 新学期开学第一天！
2018 年 11 月 24 日 —— 周六快乐
