
作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)

题目地址：https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/description/

## 题目描述

Given preorder and inorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.

For example, given

    preorder = [3,9,20,15,7]
    inorder = [9,3,15,20,7]

Return the following binary tree:

        3
       / \
      9  20
        /  \
       15   7


## 题目大意

使用先序遍历和中序遍历序列重构二叉树。

## 解题方法

### 递归
解决本题需要牢牢掌握先序遍历和中序遍历的含义，以及递归。

先序遍历：根节点，左子树的先序遍历，右子树的先序遍历。
中序遍历：左子树的中序遍历，根节点，右子树的中序遍历。

可以看出，先序遍历的开头第一个元素是**根元素**。找到根节点在中序遍历中的位置，则可以利用**根节点**将中序遍历的数组分割出左右子树。再根据左右子树的长度对先序遍历的数组切片。使用递归则可以构建出完整的树。

很多朋友不理解递归，这里多说一下怎么理解递归。首先一定要明确递归函数的定义、其输入和输出是什么，而不用明白该函数内部具体是怎么实现的。我们将递归函数当做黑盒使用，也当做普通函数使用，一定不要试图用大脑理解该递归函数内部是怎么递归的，很容易绕进去。即，我不需要知道这个函数怎么实现的，我调用这个函数就是能实现某个功能。

比如对于本题而言，`buildTree(preorder, inorder)`函数的输入是一棵树的先序遍历序列和中序遍历序列，该函数的返回值是构建好的这棵树的根节点。我们在找到`root`节点后，设定其左右子树时，依然调用`buildTree(preorder, inorder)`，此时的输入变成了`root`左右子树对应的先序遍历和中序遍历序列，该函数的返回值就是构建好的左右子树的根节点。

至此代码就写完了，我们看到构建 `root` 的左右子树时，直接使用`buildTree(preorder, inorder)`函数，只要给定正确的输入，这个函数就能给正确的输出，不用去向这个函数到底干了什么。

这样理解递归是不是更清晰了呢？

Python代码如下：

```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if not preorder or not inorder:
            return None
        root = TreeNode(preorder[0])
        index = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1:index+1], inorder[:index])
        root.right = self.buildTree(preorder[index+1:], inorder[index+1:])
        return root
```

## 日期

2018 年 6 月 22 日 —— 这周的糟心事终于完了
2019 年 1 月 8 日 —— 别熬夜，我都开始有黑眼圈了。。
2020 年 5 月 22 日 —— 这天的每日一题，熬夜写题解，也会黑眼圈。
