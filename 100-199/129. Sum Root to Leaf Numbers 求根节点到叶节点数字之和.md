# 【LeetCode】129. Sum Root to Leaf Numbers 解题报告（Python）

标签（空格分隔）： LeetCode

---

题目地址：https://leetcode.com/problems/sum-root-to-leaf-numbers/description/

## 题目描述：

Given a binary tree containing digits from 0-9 only, each root-to-leaf path could represent a number.

An example is the root-to-leaf path 1->2->3 which represents the number 123.

Find the total sum of all root-to-leaf numbers.
	
	For example,
	
	    1
	   / \
	  2   3
	The root-to-leaf path 1->2 represents the number 12.
	The root-to-leaf path 1->3 represents the number 13.
	
	Return the sum = 12 + 13 = 25.

## 解题方法


这个题和[Binary Tree Paths][1]一模一样，前个题是求路径，这个题是把路径按照10的倍数拼接在一起，最后求和即可。

有个技巧就是``res = 0``当做参数传给函数，那么函数最后的结果不会影响到res，但是如果把``res = [0]``即可。

代码：

```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        res = [0]
        self.dfs(root, res, root.val)
        return res[0]
        
    def dfs(self, root, res, path):
        if root.left == None and root.right == None:
            res[0] += path
        if root.left != None:
            self.dfs(root.left, res, path * 10 + root.left.val)
        if root.right != None:
            self.dfs(root.right, res, path * 10 + root.right.val)
```


## 日期

2018 年 2 月 25 日 


  [1]: http://blog.csdn.net/fuxuemingzhu/article/details/71249429