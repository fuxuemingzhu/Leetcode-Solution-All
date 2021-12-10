
作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)


题目地址：https://leetcode.com/problems/flip-equivalent-binary-trees/description/


## 题目描述

For a binary tree T, we can define a flip operation as follows: choose any node, and swap the left and right child subtrees.

A binary tree X is flip equivalent to a binary tree Y if and only if we can make X equal to Y after some number of flip operations.

Write a function that determines whether two binary trees are flip equivalent.  The trees are given by root nodes root1 and root2.

 

Example 1:

    Input: root1 = [1,2,3,4,5,6,null,null,null,7,8], root2 = [1,3,2,null,6,4,5,null,null,null,null,8,7]
    Output: true
    Explanation: We flipped at nodes with values 1, 3, and 5.
 
![此处输入图片的描述][1]


Note:

1. Each tree will have at most 100 nodes.
1. Each value in each tree will be a unique integer in the range [0, 99].
 

## 题目大意

两棵二叉树，判断他们对某些节点的左右子树进行互换之后，能不能相等。

## 解题方法

### 递归

这个题优美的递归，让我们不禁感叹编程真的简化了这个世界。

题目中我们不确定翻转了哪些节点，首先我们可以知道如果两个树都是空树，那么可以互相得到。如果两个数有一个是空，另一个不空，那么一定不能互相得到。如果两个树的节点的值不等，也不能互相得到。

重点来了：我们现在已经确定了两个树都不空，企鹅值相等，如何确定它们的子树们是否翻转相等呢？首先，我们来回顾一下flipEquiv函数的含义：判断两个树在进行翻转/不进行翻转的情况下，能不能相等。所以，我们不确定两个子树的状况，只需要对两个子树进行翻转/不翻转两种状态判断即可。如果进行翻转，那么root1的左子树可以通过root2的右子树得到，同时root1的左子树通过root2的右子树得到；如果不进行翻转，那么root1和root2的对应左右子树通过操作应该也能互相得到。

```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def flipEquiv(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        if not root1 and not root2: return True
        if not root1 and root2: return False
        if root1 and not root2: return False
        if root1.val != root2.val: return False
        return (self.flipEquiv(root1.left, root2.right) and self.flipEquiv(root1.right, root2.left)) or (self.flipEquiv(root1.left, root2.left) and self.flipEquiv(root1.right, root2.right))
```


## 日期

2018 年 12 月 2 日 —— 又到了周日


  [1]: https://assets.leetcode.com/uploads/2018/11/29/tree_ex.png
