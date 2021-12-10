
作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)

题目地址：[https://leetcode.com/problems/merge-two-binary-trees/description/][1]


## 题目描述

Given two binary trees and imagine that when you put one of them to cover the other, some nodes of the two trees are overlapped while the others are not.

You need to merge them into a new binary tree. The merge rule is that if two nodes overlap, then sum node values up as the new value of the merged node. Otherwise, the NOT null node will be used as the node of new tree.

Example 1:

    Input: 
    	Tree 1                     Tree 2                  
              1                         2                             
             / \                       / \                            
            3   2                     1   3                        
           /                           \   \                      
          5                             4   7                  
    Output: 
    Merged tree:
    	     3
    	    / \
    	   4   5
    	  / \   \ 
    	 5   4   7

## 题目大意

将两个二叉树进行merge操作。操作方式是把两个树进行重叠，如果重叠部分都有值，那么这个新节点是他们的值的和；如果重叠部分没有值，那么新的节点就是他们两个当中不为空的节点。

## 解题方法

### 递归

如果两个树都有节点的话就把两个相加，左右孩子为两者的左右孩子。

否则选不是空的节点当做子节点。

时间复杂度是O(N1+N2)，空间复杂度O(N)。N = t1 的 t2交集。

```python
class Solution:
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        if t1 and t2:
            newT = TreeNode(t1.val +  t2.val)
            newT.left = self.mergeTrees(t1.left, t2.left)
            newT.right = self.mergeTrees(t1.right, t2.right)
            return newT
        else:
            return t1 or t2
```

也可以换一种写法，没有任何区别：

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        if not t2:
            return t1
        if not t1:
            return t2
        newT = TreeNode(t1.val + t2.val)
        newT.left = self.mergeTrees(t1.left, t2.left)
        newT.right = self.mergeTrees(t1.right, t2.right)
        return newT
```

## 日期

2018 年 1 月 13 日 
2018 年 11 月 3 日 —— 雾霾的周六


  [1]: https://leetcode.com/problems/merge-two-binary-trees/description/
