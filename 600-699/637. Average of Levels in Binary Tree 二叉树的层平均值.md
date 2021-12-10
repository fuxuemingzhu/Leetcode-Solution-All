
作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)

题目地址：[https://leetcode.com/submissions/detail/136579829/][1]


## 题目描述

Given a non-empty binary tree, return the average value of the nodes on each level in the form of an array.

Example 1:

    Input:
        3
       / \
      9  20
        /  \
       15   7
    Output: [3, 14.5, 11]

	Explanation:
	The average value of nodes on level 0 is 3,  on level 1 is 14.5, and on level 2 is 11. Hence return [3, 14.5, 11].

Note:

1. The range of node's value is in the range of 32-bit signed integer.

## 题目大意

求二叉树每层的所有节点的平均值

## 解题方法

### 方法一：DFS

这个题需要保存每层的节点的和以及每层的节点数。采用``DFS``的方式，把每个节点进行遍历，把这个节点加到对应层中去。每层使用两个数字，第一个数字保存所有节点的和，第二个数字保存有多少个节点。

注意一个小问题，节点为空的时候要return，否则下面node为None，出现错误。

```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        info = [] # the first element is sum of the level,the second element is nodes in this level
        def dfs(node, depth=0):
            if not node:
                return
            if len(info) <= depth:
                info.append([0, 0])
            info[depth][0] += node.val
            info[depth][1] += 1
            # print(info)
            dfs(node.left, depth + 1)
            dfs(node.right, depth + 1)
        dfs(root)
        return [s / float(c) for s,c in info]
```

二刷。直接使用数组保存每层所有节点的值，最后需要做个求平均数的处理。

```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        res = []
        self.getLevel(root, 0, res)
        return [sum(line) / float(len(line)) for line in res]
    
    def getLevel(self, root, level, res):
        if not root:
            return
        if level >= len(res):
            res.append([])
        res[level].append(root.val)
        self.getLevel(root.left, level + 1, res)
        self.getLevel(root.right, level + 1, res)
```

### 方法二：BFS

其实层次遍历使用BFS比使用DFS更加简单高效。因为每层遍历结束之后，已经知道了这一行的所有数字，所以可以直接求平均数，然后放入到结果中去，而不用最后才求平均数了。

```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        que = collections.deque()
        res = []
        que.append(root)
        while que:
            size = len(que)
            row = []
            for _ in range(size):
                node = que.popleft()
                if not node:
                    continue
                row.append(node.val)
                que.append(node.left)
                que.append(node.right)
            if row:
                res.append(sum(row) / float(len(row)))
        return res
```


## 日期

2018 年 1 月 17 日 
2018 年 11 月 ９ 日 —— 睡眠可以


  [1]: https://leetcode.com/submissions/detail/136579829/
