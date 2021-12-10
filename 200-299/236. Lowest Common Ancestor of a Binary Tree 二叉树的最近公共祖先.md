
作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)


题目地址：https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/description/

## 题目描述

Given a binary tree, find the ``lowest common ancestor (LCA)`` of two given nodes in the tree.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

Given the following binary tree:  root = [3,5,1,6,2,0,8,null,null,7,4]

![在这里插入图片描述](https://assets.leetcode.com/uploads/2018/12/14/binarytree.png)

Example 1:

    Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
    Output: 3
    Explanation: The LCA of of nodes 5 and 1 is 3.

Example 2:

    Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
    Output: 5
    Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself
                 according to the LCA definition.

Note:

- All of the nodes' values will be unique.
- p and q are different and both values will exist in the binary tree.

## 题目大意

在一棵普通的二叉树中，找出两个节点的最小公共祖先。

## 解题方法

如果是BST的话，那就很简单了。可以参考一下[【LeetCode】235. Lowest Common Ancestor of a Binary Search Tree 解题报告（Java & Python）][1]的做法。

最低公共祖先的定义是，在一个二叉树中，我们能找到的最靠近叶子的节点，该节点同时是p和q的祖先节点。注意，如果p或者q本身也可以作为自己的祖先。

如果用递归的话，最重要的还是明白递归函数的作用是什么。这个题里面lowestCommonAncestor(root, p, q)函数的作用是判断p和q在root树中最低的公共祖先是什么，返回值是公共祖先。

这个题的模式叫做devide and conquer.  如果当前节点等于其中的p和q某一个节点，那么找到了节点，返回该节点，否则在左右子树分别寻找。

左右子树两个返回的是什么呢？按照该递归函数的定义，即找到了左子树和右子树里p和q的公共祖先，注意祖先可以是节点自己。然后根据左右侧找到的节点做进一步的判断。

如果左右侧查找的结果都不为空，说明分别找到了p和q，那么LCA就是当前节点。否则就在不为空的那个结果就是所求。

python代码如下：

```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if not root or p == root or q == root:
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if left and right:
            return root
        return left if left else right
```

## 日期

2018 年 6 月 22 日 —— 这周的糟心事终于完了
2019 年 1 月 9 日 —— 时不我待

  [1]: https://blog.csdn.net/fuxuemingzhu/article/details/51290289
