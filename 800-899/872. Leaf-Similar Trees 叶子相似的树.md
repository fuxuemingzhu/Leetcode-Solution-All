作者： 		负雪明烛 
id：				fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---

@[TOC](目录)

题目地址：https://leetcode.com/problems/leaf-similar-trees/description/

## 题目描述

Consider all the leaves of a binary tree.  From left to right order, the values of those leaves form a leaf value sequence.

![此处输入图片的描述][1]

For example, in the given tree above, the leaf value sequence is ``(6, 7, 4, 9, 8)``.

Two binary trees are considered leaf-similar if their leaf value sequence is the same.

Return ``true`` if and only if the two given trees with head nodes ``root1`` and ``root2`` are leaf-similar.


Note:

- Both of the given trees will have between 1 and 100 nodes.


## 题目大意

判断两棵二叉树的叶子节点从左到右的排列是否相同。

## 解题方法

### 中序遍历

一棵树从左到右的序列应该使用中序遍历，当中序遍历时，如果节点是叶子节点则放入序列之中。

所以判断两棵树的序列是否相等即可。

代码如下：

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        leaves1 = []
        leaves2 = []
        self.inOrder(root1, leaves1)
        self.inOrder(root2, leaves2)
        return leaves1 == leaves2
    
    def inOrder(self, root, leaves):
        if not root:
            return
        self.inOrder(root.left, leaves)
        if not root.left and not root.right:
            leaves.append(root.val)
        self.inOrder(root.right, leaves)
```

### 先序遍历

二刷的时候同样可以使用先序遍历，如果是叶子节点就把该节点放到结果里，否则继续查找就好了，所以最后结果保存的只有叶子节点。

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        return self.getLeafs(root1) == self.getLeafs(root2)
    
    def getLeafs(self, root):
        res = []
        if not root:
            return res
        if not root.left and not root.right:
            return [root.val]
        res.extend(self.getLeafs(root.left))
        res.extend(self.getLeafs(root.right))
        return res
```

同样地，可以使用迭代方法，而不是递归。

```python3
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        return self.preOrder(root1) == self.preOrder(root2)
        
    def preOrder(self, root):
        stack = []
        stack.append(root)
        res = []
        while stack:
            node = stack.pop()
            if not node: continue
            if not node.left and not node.right:
                res.append(node.val)
            stack.append(node.left)
            stack.append(node.right)
        return res
```

### 后序遍历

这个题也可以使用后序遍历，使用的是迭代的方式，代码如下。

```python3
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        return self.postOrder(root1) == self.postOrder(root2)
        
    def postOrder(self, root):
        stack = []
        stack.append(root)
        res = []
        while stack:
            node = stack.pop()
            if not node: continue
            stack.append(node.left)
            stack.append(node.right)
            if not node.left and not node.right:
                res.append(node.val)
        return res
```

## 日期

2018 年 8 月 16 日 —— 一个月不写题，竟然啥都不会了。。加油！
2018 年 11 月 7 日 —— 天冷加衣！

  [1]: https://s3-lc-upload.s3.amazonaws.com/uploads/2018/07/16/tree.png
