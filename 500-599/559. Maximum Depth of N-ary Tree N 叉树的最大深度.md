
作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)

题目地址：https://leetcode.com/problems/maximum-depth-of-n-ary-tree/description/

## 题目描述

Given a n-ary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

For example, given a ``3-ary`` tree:

 
![此处输入图片的描述][1]

 
We should return its max depth, which is 3.

Note:

1. The depth of the tree is at most 1000.
1. The total number of nodes is at most 5000.


## 题目大意

N叉树的高度。

## 解题方法

### DFS

首先得明白，这个N叉树是什么样的数据结构定义的。val是节点的值，children是一个列表，这个列表保存了其所有节点。

求一个树的高度，完全可以转换成一个递归问题。树的高度= 1 + 子树最大高度。


代码如下：

```python
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        if not root:
            return 0
        if not root.children:
            return 1
        depth = 1 + max(self.maxDepth(child) for child in root.children)
        return depth
```

### BFS

求高度的话，让我们想到了BFS，这样做的道理是我们从根节点开始，每向下走一步，那么深度就增加1，相当于层次遍历，当遍历结束的时候，就得到了树的高度。

```python
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        if not root: return 0
        depth = 0
        que = collections.deque()
        que.append(root)
        while que:
            size = len(que)
            for i in range(size):
                node = que.popleft()
                for child in node.children:
                    que.append(child)
            depth += 1
        return depth
```

## 日期

2018 年 7 月 12 日 —— 天阴阴地潮潮，已经连着两天这样了
2018 年 11 月 6 日 —— 腰酸背痛要废了

  [1]: https://leetcode.com/static/images/problemset/NaryTreeExample.png
