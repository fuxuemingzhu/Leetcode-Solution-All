
作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)

题目地址：https://leetcode.com/problems/search-in-a-binary-search-tree/description/

## 题目描述

Given the root node of a binary search tree (BST) and a value. You need to find the node in the BST that the node's value equals the given value. Return the subtree rooted with that node. If such node doesn't exist, you should return NULL.

For example, 

Given the tree:

        4
       / \
      2   7
     / \
    1   3

    And the value to search: 2

You should return this subtree:

      2     
     / \   
    1   3

In the example above, if we want to search the value ``5``, since there is no node with value 5, we should return ``NULL``.

## 题目大意

在一个BST中查找某值，如果找到的话，返回找到的那个节点，如果找不到就返回None.

## 解题方法

### 递归

只要是BST查找，那肯定都好说。树的查找比较简单的就是递归，如果节点是空，那么肯定没找到；节点值相等，返回这个节点；如果节点值小于要查找的值，那么在当前节点的右子树中找；否则在左子树中找。

代码如下：

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def searchBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        if not root:
            return None
        if root.val == val:
            return root
        elif root.val < val:
            return self.searchBST(root.right, val)
        else:
            return self.searchBST(root.left, val)
```

## 日期

2018 年 7 月 12 日 ———— 天阴阴地潮潮，已经连着两天这样了
2018 年 11 月 6 日 —— 腰酸背痛要废了
