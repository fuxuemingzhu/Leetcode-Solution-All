
作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)

题目地址：[https://leetcode.com/problems/maximum-depth-of-binary-tree/](https://leetcode.com/problems/maximum-depth-of-binary-tree/)

Total Accepted: 85334 Total Submissions: 188240 Difficulty: Easy 


## 题目描述

Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Note: A leaf is a node with no children.

Example:

Given binary tree ``[3,9,20,null,null,15,7]``,

	    3
	   / \
	  9  20
	    /  \
	   15   7

return its depth = 3.

## 题目大意

求一颗二叉树的高度。

## 解题方法

### 方法一：BFS

求树的高度，可以从根节点开始，每次向下走一层，直到所有的节点遍历结束。层数就是高度。

```python3
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        depth = 0
        que = collections.deque()
        que.append(root)
        while que:
            size = len(que)
            for _ in range(size):
                node = que.popleft()
                if not node:
                    continue
                que.append(node.left)
                que.append(node.right)
            depth += 1
        return depth - 1
```


### 方法二：DFS

运用递归，如果该节点是空，那么高度是0。否则树的高度等于 1 +　左子树和右子树高度的最大值。

```python3
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
```

## 参考资料

[559. Maximum Depth of N-ary Tree](https://blog.csdn.net/fuxuemingzhu/article/details/81021864)

[算法之二叉树各种遍历](http://blog.csdn.net/sjf0115/article/details/8645991)

[轻松搞定面试中的二叉树题目](http://blog.csdn.net/luckyxiaoqiang/article/details/7518888)

## 日期

2015/9/16 10:42:06 
2018 年 11 月 ９ 日 —— 睡眠可以
