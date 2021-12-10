
作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)

---

题目地址：https://leetcode.com/problems/house-robber-iii/description/

## 题目描述

The thief has found himself a new place for his thievery again. There is only one entrance to this area, called the "root." Besides the root, each house has one and only one parent house. After a tour, the smart thief realized that "all houses in this place forms a binary tree". It will automatically contact the police if two directly-linked houses were broken into on the same night.

Determine the maximum amount of money the thief can rob tonight without alerting the police.

Example 1:

         3
        / \
       2   3
        \   \ 
         3   1
    Maximum amount of money the thief can rob = 3 + 3 + 1 = 7.

Example 2:

         3
        / \
       4   5
      / \   \ 
     1   3   1
    Maximum amount of money the thief can rob = 4 + 5 = 9.


## 题目大意

从一棵二叉树中取出一些数字，使得取得数字的和最大。取的规则是不能同时取直接相连的两个节点。

## 解题方法

这个是限定规则下的博弈过程。曾经看过左程云的视频教程，对这个过程印象比较深刻。

本题的做法，就是求``本节点+孙子更深节点``vs``儿子节点+重孙更深的节点``的比较。

道理能想明白，代码有点难写。用了dfs函数，虽然递归是自顶向下的，但是因为是不断的return，所以真正求值是从底向上的。用到了一个有两个元素的列表，分别保存了之前层的，不取节点和取节点的情况。然后遍历左右子树，求出当前节点取和不取能得到的值，再返回给上一层。注意这个里面的robcurr是当前节点能达到的最大值，所以最后返回结果的时候试试返回的root节点robcurr的值。

```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def dfs(root):
            # from bottom to top
            if not root: return [0, 0] # before layer, no robcurr, robcurr
            robleft = dfs(root.left)
            robright = dfs(root.right)
            norobcurr = robleft[1] + robright[1]
            robcurr = max(root.val + robleft[0] + robright[0], norobcurr)
            return [norobcurr, robcurr]
        return dfs(root)[1]
```

二刷的时候换了一种解法，使用的仍然是递归，不过不用返回两个值，而是直接一个值：无论用还是不用情况下，能得到的最好结果。必须使用记忆化递归，否则超时。

```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        memo = dict()
        return self.helper(root, memo)

    def helper(self, root, memo):
        if not root:
            return 0
        if root in memo:
            return memo[root]
        res = 0
        notused = self.helper(root.left, memo) + self.helper(root.right, memo)
        used = 0
        if root.left:
            used += self.helper(root.left.left, memo) + self.helper(root.left.right, memo)
        if root.right:
            used += self.helper(root.right.left, memo) + self.helper(root.right.right, memo)
        res = max(notused, used + root.val)
        memo[root] = res
        return res
```

三刷的时候，代码思路更简洁明了。递归函数增加一个变量，表示当前节点的父亲节点是否用过。根节点没有父亲节点，所以其父亲节点肯定没用过。然后我们判断在某个节点的父亲用过和没用过的情况下，当前节点能不能用，最优的结果分别是多少。

```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.d = dict()
        return self.helper(root, False)
    
    def helper(self, root, parentUsed):
        if not root: return 0
        if (root, parentUsed) in self.d:
            return self.d[(root, parentUsed)]
        res = 0
        if parentUsed:
            res = self.helper(root.left, False) + self.helper(root.right, False)
        else:
            res = max(root.val + self.helper(root.left, True) + self.helper(root.right, True), self.helper(root.left, False) + self.helper(root.right, False))
        self.d[(root, parentUsed)] = res
        return res
```

## 日期

2018 年 6 月 22 日 —— 这周的糟心事终于完了
2018 年 12 月 25 日 —— 圣诞节快乐
2019 年 3 月 23 日 —— 周末加油鸭

  [1]: https://blog.csdn.net/fuxuemingzhu/article/details/79367789
