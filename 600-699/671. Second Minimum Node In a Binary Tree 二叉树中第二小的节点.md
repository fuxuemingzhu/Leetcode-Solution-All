
作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)

题目地址：[https://leetcode.com/problems/second-minimum-node-in-a-binary-tree/description/][1]


## 题目描述

Given a non-empty special binary tree consisting of nodes with the non-negative value, where each node in this tree has exactly two or zero sub-node. If the node has two sub-nodes, then this node's value is the smaller value among its two sub-nodes.

Given such a binary tree, you need to output the second minimum value in the set made of all the nodes' value in the whole tree.

If no such second minimum value exists, output -1 instead.

    Example 1:
    Input: 
        2
       / \
      2   5
         / \
        5   7
    
    Output: 5
    Explanation: The smallest value is 2, the second smallest value is 5.

Example 2:

    Input: 
        2
       / \
      2   2
    
    Output: -1
    Explanation: The smallest value is 2, but there isn't any second smallest value.

## 题目大意

找二叉树中的第二小的结点值。并且给该二叉树做了一些限制，比如对于任意一个结点，要么其没有子结点，要么就同时有两个子结点，而且父结点值是子结点值中较小的那个，当然两个子结点值可以相等。

## 解题方法

### 找出所有值再求次小值

使用了一个中序遍历，把所有的值放入到set里，然后我们先找最小值，然后删除掉它之后，再求一次最小值就是次小值。

```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findSecondMinimumValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.res = set()
        self.inOrder(root)
        if len(self.res) <= 1:
            return -1
        min1 = min(self.res)
        self.res.remove(min1)
        return min(self.res)

    def inOrder(self, root):
        if not root:
            return
        self.inOrder(root.left)
        self.res.add(root.val)
        self.inOrder(root.right)
```

### 遍历时求次小值

因为根节点的值一定是比两个子树的值小的，所以我们知道了所有的值的最小值一定是root的值。如何找到第二小的值呢？可以使用一个变量，时刻保存现在遇到的比最小值大并且比次小值小的值作为第二小的值。

```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findSecondMinimumValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root: return -1
        self.res = float("inf")
        self.min = root.val
        self.inOrder(root)
        return self.res if self.res != float("inf") else -1

    def inOrder(self, root):
        if not root:
            return
        self.inOrder(root.left)
        if self.min < root.val < self.res:
            self.res = root.val
        self.inOrder(root.right)
```

## 日期


2018 年 1 月 31 日 
2018 年 11 月 19 日 —— 周一又开始了

  [1]: https://leetcode.com/problems/second-minimum-node-in-a-binary-tree/description/
