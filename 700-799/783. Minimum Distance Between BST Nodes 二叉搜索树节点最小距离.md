
作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)

题目地址：https://leetcode.com/problems/minimum-distance-between-bst-nodes/description/


## 题目描述

Given a Binary Search Tree (BST) with the root node root, return the minimum difference between the values of any two different nodes in the tree.

    Example :
    
    Input: root = [4,2,6,1,3,null,null]
    Output: 1
    Explanation:
    Note that root is a TreeNode object, not an array.
    
    The given tree [4,2,6,1,3,null,null] is represented by the following diagram:
    
              4
            /   \
          2      6
         / \    
        1   3  
    
    while the minimum difference in this tree is 1, it occurs between node 1 and node 2, also between node 3 and node 2.

Note:

1. The size of the BST will be between 2 and 100.
1. The BST is always valid, each node's value is an integer, and each node's value is different.

## 题目大意

求BST的两个节点之间的最小差值。

## 解题方法

### 中序遍历

看见BST想中序遍历是有序的啊~所以先进性中序遍历，得到有序列表，然后找出相邻的两个节点差值的最小值即可。

```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDiffInBST(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        vals = []
        def inOrder(root):
            if not root:
                return 
            inOrder(root.left)
            vals.append(root.val)
            inOrder(root.right)
        inOrder(root)
        return min([vals[i + 1] - vals[i] for i in xrange(len(vals) - 1)])
```

二刷的时候注意到和[530. Minimum Absolute Difference in BST](https://blog.csdn.net/fuxuemingzhu/article/details/69666671)是完全一样的题，果然同样的代码就直接通过了。。不懂这个题的意义是什么。。

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDiffInBST(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.res = float("inf")
        self.prev = None
        self.inOrder(root)
        return self.res
    
    def inOrder(self, root):
        if not root: return
        self.inOrder(root.left)
        if self.prev:
            self.res = min(self.res, root.val - self.prev.val)
        self.prev = root
        self.inOrder(root.right)
```

## 日期

2018 年 2 月 28 日 
2018 年 11 月 14 日 —— 很严重的雾霾
