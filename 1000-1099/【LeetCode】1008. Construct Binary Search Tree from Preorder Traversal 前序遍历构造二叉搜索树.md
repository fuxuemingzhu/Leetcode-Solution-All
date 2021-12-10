
作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)


题目地址：https://leetcode.com/problems/construct-binary-search-tree-from-preorder-traversal/

## 题目描述

Return the root node of a binary search tree that matches the given ``preorder`` traversal.

(Recall that a binary search tree is a binary tree where for every node, any descendant of ``node.left`` has a ``value < node.val``, and any descendant of node.right has a ``value > node.val``.  Also recall that a preorder traversal displays the value of the node first, then traverses ``node.left``, then traverses ``node.right``.)

Example 1:
    
    Input: [8,5,1,7,10,12]
    Output: [8,5,10,1,7,null,12]

![此处输入图片的描述][1]

Note: 

1. 1 <= preorder.length <= 100
1. The values of preorder are distinct.

## 题目大意

给出了一个BST的先序遍历，求该BST。

## 解题方法

### 递归

先序遍历一定先遍历了根节点，所以出现的第一个数字一定是根。那么BST的左子树都比根节点小，而先序遍历要把左子树遍历结束才遍历右子树，所以向后找第一个大于根节点数字位置，该位置就是右子树的根节点。

做一个递归即可。

Python代码如下：

```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def bstFromPreorder(self, preorder):
        """
        :type preorder: List[int]
        :rtype: TreeNode
        """
        if not preorder: return None
        root = TreeNode(preorder[0])
        N = len(preorder)
        i = 1
        while i < N:
            if preorder[i] > preorder[0]:
                break
            i += 1
        root.left = self.bstFromPreorder(preorder[1:i])
        root.right = self.bstFromPreorder(preorder[i:])
        return root
```


## 日期

2019 年 3 月 10 日 —— 周赛进了第一页！


  [1]: https://assets.leetcode.com/uploads/2019/03/06/1266.png
  [2]: https://assets.leetcode.com/uploads/2019/03/08/domino.png
