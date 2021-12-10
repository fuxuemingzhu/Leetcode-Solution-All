# 【LeetCode】106. Construct Binary Tree from Inorder and Postorder Traversal 解题报告（Python）

标签： LeetCode

---

题目地址：https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/description/

## 题目描述：

Given inorder and postorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.

    For example, given
    
    inorder = [9,3,15,20,7]
    postorder = [9,15,7,20,3]
    Return the following binary tree:
    
        3
       / \
      9  20
        /  \
       15   7


## 题目大意

根据中序遍历和后序遍历重建二叉树。

## 解题方法

这个是套路题，我没有完全记住每一步是多少，而是根据树的样子和两个数组进行分析，得出切片的位置。

后序遍历的最后一个元素一定是根节点，在中序遍历中找出此根节点的位置序号。中序遍历序号左边的是左孩子，右边的是右孩子。再根据左孩子和右孩子的长度对后序遍历进行切片即可。

```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        if not inorder or not postorder: return None
        val = postorder[-1]
        root = TreeNode(val)
        index = inorder.index(val)
        root.left = self.buildTree(inorder[:index], postorder[:index])
        root.right = self.buildTree(inorder[index+1:], postorder[index:-1])
        return root
```

## 日期

2018 年 3 月 12 日 


  [1]: http://img.blog.csdn.net/20160101111128525