# 【LeetCode】222. Count Complete Tree Nodes 解题报告（Python）

标签（空格分隔）： LeetCode

作者： 		负雪明烛 
id：				fuxuemingzhu
个人博客：	http://fuxuemingzhu.me/

---

题目地址：https://leetcode.com/problems/count-complete-tree-nodes/description/

## 题目描述：

Given a complete binary tree, count the number of nodes.

Note:

Definition of a complete binary tree from Wikipedia:
In a complete binary tree every level, except possibly the last, is completely filled, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.

Example:

    Input: 
        1
       / \
      2   3
     / \  /
    4  5 6
    
    Output: 6

## 题目大意

求一个完全二叉树的节点个数。

## 解题方法

我知道这个肯定有简单算法的，否则可以直接遍历去求，那样没意义。

参考了[222. Count Complete Tree Nodes][1]的做法，在此感谢。

求完全二叉树的节点数目。注意完全二叉树和满二叉树Full Binary Tree的唯一区别是，完全二叉树最后一层的节点不满，而且假设最后一层有节点，都是从左边开始。 这样我们可以利用这个性质得到下面的结论：

1. 假如左子树高度等于右子树高度，则右子树为完全二叉树，左子树为满二叉树。
1. 假如高度不等，则左字数为完全二叉树，右子树为满二叉树。
1. 求高度的时候只往左子树来找。

可以使用上面的结论得出本题的解法：

1. 先构造一个getHeight方法， 用来求出二叉树的高度。这里我们只用求从根节点到最左端节点的长度。

1. 求出根节点左子树高度leftHeight和根节点右子树高度rightHeight
- 假如两者相等，那么说明左子树是满二叉树，而右子树可能是完全二叉树。
-- 我们可以返回  2 ^ leftHeight - 1 + 1  + countNodes(root.right)
-- 这里+1是因为把根节点也算进去，化简一下就是 1 << leftHeight + countNodes(root.right)，返回结果
- 否则两者不等，说明左子树是完全二叉树，右子树是满二叉树
-- 我们可以返回 2^ rightHeight - 1 + 1 + countNodeS(root.left)
-- 化简以后得到 1 << rightHeight + countNodes(root.left)，返回结果



```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root: return 0
        nodes = 0
        left_height = self.getHeight(root.left)
        right_height = self.getHeight(root.right)
        if left_height == right_height:
            nodes = 2 ** left_height + self.countNodes(root.right)
        else:
            nodes = 2 ** right_height + self.countNodes(root.left)
        return nodes
        
        
    def getHeight(self, root):
        height = 0
        while root:
            height += 1
            root = root.left
        return height
        
```

## 日期

2018 年 6 月 23 日 ———— 美好的周末要从刷题开始


  [1]: https://www.cnblogs.com/yrbbest/p/4993469.html