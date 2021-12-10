作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)

[LeetCode]

题目地址：[https://leetcode.com/problems/minimum-depth-of-binary-tree/](https://leetcode.com/problems/minimum-depth-of-binary-tree/)

Total Accepted: 70767 Total Submissions: 243842 Difficulty: Easy


## 题目描述

Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

Note: A leaf is a node with no children.

Example:

Given binary tree [3,9,20,null,null,15,7],

	    3
	   / \
	  9  20
	    /  \
	   15   7

return its minimum depth = 2.

## 题目大意

求根节点到最近的叶子节点的高度。

## 解题方法

### DFS

运用递归，递归当前和 左子树和右子树的深度，某节点的左右子树都是空的时候，说明是叶子。计算根节点到此叶子的深度。

注意：如果是叶子，那么此叶子的深度是1.

同时注意：如果有一方的某一子树为空，那么它的深度为0，但不应该进入树的深度的计算当中去。

Better solution:用HashMap存储已经遍历过的树，减少空间复杂度。实现效率的提高。

1. 当root为空的时候直接返回0，因为MIN赋值很大，所以如果不单独预判的话会返回MIN
1. 判断树的深度应该到叶子节点，也就是左右子结点都为空的那个结点
1. 树的深度的根节点深度为1

递归解法如下：

```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root: return 0
        que = collections.deque()
        que.append(root)
        depth = 1
        while que:
            size = len(que)
            for _ in range(size):
                node = que.popleft()
                if not node: continue
                if not node.left and not node.right:
                    return depth
                que.append(node.left)
                que.append(node.right)
            depth += 1
        return depth
```

### BFS

其实BFS更简单，因为发现这层有个叶子的话，就直接返回就行了。

```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root: return 0
        left = self.minDepth(root.left)
        right = self.minDepth(root.right)
        if not left:
            return right + 1
        if not right:
            return left + 1
        return 1 + min(left, right)
```

## 日期

2015/9/17 10:49:04 
2018 年 11 月 24 日 —— 周六快乐
