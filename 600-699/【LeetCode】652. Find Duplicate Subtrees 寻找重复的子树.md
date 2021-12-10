# 【LeetCode】652. Find Duplicate Subtrees 解题报告（Python）

标签（空格分隔）： LeetCode

作者： 		负雪明烛 
id：				fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---

题目地址：https://leetcode.com/problems/find-duplicate-subtrees/description/

## 题目描述：

Given a binary tree, return all duplicate subtrees. For each kind of duplicate subtrees, you only need to return the root node of any one of them.

Two trees are duplicate if they have the same structure with same node values.

Example 1:

        1
       / \
      2   3
     /   / \
    4   2   4
       /
      4
The following are two duplicate subtrees:

      2
     /
    4

and

    4

Therefore, you need to return above trees' root in the form of a list.

## 题目大意

找出一个二叉树中所有的重复子树。重复子树就是一棵子树，在大的二叉树中出现的次数不止一次。

## 解题方法

暴力解法不可取。

参考了[\[LeetCode\] Find Duplicate Subtrees 寻找重复树][1]才明白，我们要找到一个重复的子树，可以把树和hash结合起来啊！

每一棵子树，都能把它的结构使用先序遍历或者后序遍历保存下来，然后把这个结构保存在hash表格里面，这样当我们下次再遇到这个树的结构的时候，就能很容易查表得知，然后放到结果res中。

代码如下：

```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findDuplicateSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: List[TreeNode]
        """
        res = []
        m = collections.defaultdict(int)
        self.helper(root, m, res)
        return res
        
    def helper(self, root, m, res):
        if not root:
            return '#'
        path = str(root.val) + ',' + self.helper(root.left, m, res) + ',' + self.helper(root.right, m, res)
        if m[path] == 1:
            res.append(root) 
        m[path] += 1
        return path
```

## 日期

2018 年 7 月 15 日 ———— 昨天火锅+啤酒，今天要加班了。。


  [1]: http://www.cnblogs.com/grandyang/p/7500082.html