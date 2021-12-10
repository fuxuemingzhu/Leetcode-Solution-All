作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)


题目地址：https://leetcode.com/problems/trim-a-binary-search-tree/description/


## 题目描述

Given a binary search tree and the lowest and highest boundaries as L and R, trim the tree so that all its elements lies in [L, R] (R >= L). You might need to change the root of the tree, so the result should return the new root of the trimmed binary search tree.

Example 1:

    Input: 
        1
       / \
      0   2
    
      L = 1
      R = 2
    
    Output: 
        1
          \
           2

Example 2:

    Input: 
        3
       / \
      0   4
       \
        2
       /
      1
    
      L = 1
      R = 3
    
    Output: 
          3
         / 
       2   
      /
     1

## 题目大意

给定[L,R]区间，进行BST裁剪。只要数值不在该区间的节点，全部都删除。返回的结果应该仍然是个BST.

## 解题方法

### 递归

想法很简单了，如果root的值比R大，说明root以及其所有右节点都不在这个区间内，向左边搜索。如果root的值比L小，，说明root以及其所有左节点都不在这个区间内，向右边搜索。如果root正好在这个区间内，那么分别对它的左右子树进行裁剪就好了。

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def trimBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: TreeNode
        """
        if not root:
            return None
        if root.val > R:
            return self.trimBST(root.left, L, R)
        elif root.val < L:
            return self.trimBST(root.right, L, R)
        else:
            root.left = self.trimBST(root.left, L, R)
            root.right = self.trimBST(root.right, L, R)
            return root
```


## 日期

2018 年 11 月 8 日 —— 项目进展缓慢


  [1]: https://assets.leetcode.com/uploads/2018/10/12/island.png
  [2]: https://charlesliuyx.github.io/2018/10/11/%E3%80%90%E7%9B%B4%E8%A7%82%E7%AE%97%E6%B3%95%E3%80%91Egg%20Puzzle%20%E9%B8%A1%E8%9B%8B%E9%9A%BE%E9%A2%98/
