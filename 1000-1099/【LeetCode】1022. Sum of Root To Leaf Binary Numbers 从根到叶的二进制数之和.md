
作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)

题目地址：https://leetcode.com/problems/sum-of-root-to-leaf-binary-numbers/

## 题目描述

Given a binary tree, each node has value ``0`` or ``1``.  Each root-to-leaf path represents a binary number starting with the most significant bit.  For example, if the path is ``0 -> 1 -> 1 -> 0 -> 1``, then this could represent ``01101`` in binary, which is ``13``.

For all leaves in the tree, consider the numbers represented by the path from the root to that leaf.

Return the sum of these numbers modulo ``10^9 + 7``.


Example 1:

![此处输入图片的描述][1]

    Input: [1,0,1,0,1,0,1]
    Output: 22
    Explanation: (100) + (101) + (110) + (111) = 4 + 5 + 6 + 7 = 22
 

Note:

1. The number of nodes in the tree is between 1 and 1000.
1. ``node.val`` is ``0`` or ``1``.


## 题目大意

二叉树的每个节点的数值有0和1，从根节点到叶子节点的一条路径就会构成了一个二进制字符串，求所有路径构成的二进制字符串转成整数的和。

## 解题方法

### DFS

最简单的方法就是把所有的路径遍历一遍，然后计算每条路径构成的二进制字符串表示的整数的最大值即可。

我认为递归最重要的是明白递归函数的定义，如果不能明白定义，那么就写不出正确的代码。

这个题定义了一个函数，查找的是在遍历这个节点之时，已经路过的路径（包括当前节点）。在其中判断如果该节点是叶子节点，那么更新所有的路径和。

Python的整数不会越界，这题中每经历过一个节点，就把之前的路径*2 + 当前的节点值当做路径表示的整数。

Python代码如下：

```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumRootToLeaf(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root: return 0
        self.res = 0
        self.dfs(root, root.val)
        return self.res

    def dfs(self, root, preSum):
        if not root.left and not root.right:
            self.res = (self.res + preSum) % (10 ** 9 + 7)
            return
        if root.left:
            self.dfs(root.left, preSum * 2 + root.left.val)
        if root.right:
            self.dfs(root.right, preSum * 2 + root.right.val)
```

## 日期

2019 年 4 月 7 日 —— 周赛bug了3次。。


  [1]: https://assets.leetcode.com/uploads/2019/04/04/sum-of-root-to-leaf-binary-numbers.png
