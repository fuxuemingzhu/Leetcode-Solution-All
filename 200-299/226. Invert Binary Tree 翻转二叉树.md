作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)

题目地址:  https://leetcode.com/problems/invert-binary-tree/

## 题目描述


Invert a binary tree.

Example:

Input:

	     4
	   /   \
	  2     7
	 / \   / \
	1   3 6   9

Output:

	     4
	   /   \
	  7     2
	 / \   / \
	9   6 3   1

Trivia:

This problem was inspired by this original tweet by Max Howell:

> Google: 90% of our engineers use the software you wrote (Homebrew), but you can’t invert a binary tree on a whiteboard so f*** off.

## 题目大意

翻转二叉树。

## 解题方法

### 递归

这个题能够很好地帮助我们理解递归。

递归函数本身也是函数，调用递归函数就把它当做普通函数来看待，一定要只思考当前层的处理逻辑，明白该递归函数的输入输出是什么即可，调用的时候不要管函数内部实现。不要用肉脑 debug 递归函数的调用过程，会被绕进去。

首先来分析`invertTree(TreeNode root)`函数的定义：

1. 函数的定义是什么？
该函数可以翻转一棵二叉树，即**将二叉树中的每个节点的左右孩子都进行互换。**
2. 函数的输入是什么？
函数的输入是要被翻转的二叉树。
3. 函数的输出是什么？
返回的结果就是已经翻转后的二叉树。

然后我们来分析函数的写法：

1. 递归终止的条件
当要翻转的节点是空，停止翻转，返回空节点。
2. 返回值
虽然对 `root` 的左右子树都进行了翻转，但是翻转后的二叉树的根节点不变，故返回 `root` 节点。
3. 函数内容
`root` 节点的新的左子树：是翻转了的 `root.right` => 即 `root.left = invert(root.right)`;
`root` 节点的新的右子树：是翻转了的 `root.left` => 即 `root.right = invert(root.left)`;

至此，递归函数就写完了。在『函数内容』编写的时候，是不是把递归函数`invertTree(TreeNode root)`当做了普通函数来用？调用`invertTree(TreeNode root)`函数就是能实现翻转二叉树的目的，不需要理解函数内部怎么实现的。

最后，提醒大家避免踩一个小坑，不能直接写成下面这样的代码：

```python
root.left = invert(root.right)
root.right = invert(root.left)
```

这是因为第一行修改了`root.left`，会影响了第二行。在 Python 中，正确的写法是把两行写在同一行，就能保证 `root.left` 和 `root.right` 的修改是同时进行的。

Python 解法如下：

```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return
        root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        return root
```

### 迭代

使用迭代方法。众所周知，把递归改成迭代需要一个栈，这个题使用迭代基本就是套个模板就好了，关键步骤只有一行，那就是把两个子树进行翻转。

```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        stack = []
        stack.append(root)
        while stack:
            node = stack.pop()
            if not node:
                continue
            node.left, node.right = node.right, node.left
            stack.append(node.left)
            stack.append(node.right)
        return root
```

## 日期

2016/4/29 21:58:13 
2018 年 10 月 8 日 —— 终于开学了。
2018 年 11 月 ９ 日 —— 睡眠可以
