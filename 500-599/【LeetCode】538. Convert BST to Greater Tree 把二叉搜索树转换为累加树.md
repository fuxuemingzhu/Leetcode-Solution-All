
作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)

题目地址：[https://leetcode.com/problems/convert-bst-to-greater-tree/description/][1]


## 题目描述

Given a Binary Search Tree (BST), convert it to a Greater Tree such that every key of the original BST is changed to the original key plus sum of all keys greater than the original key in BST.

Example:
    
    Input: The root of a Binary Search Tree like this:
                  5
                /   \
               2     13
    
    Output: The root of a Greater Tree like this:
                 18
                /   \
              20     13

## 题目大意

把BST的每个节点的值重新设置为所有比它值大的节点的值的和。

## 解题方法

### 递归

这个题要把每个节点变为比该节点值大（包含）的所有节点之和。

这个题的动机是我们应该先修改数值比较大的节点，然后修改数值比较小的节点。这样做，才能保证，我们只需要一次遍历，就把每个节点的值修改成了比它值更大的所有节点的和。

BST的右子树都比该节点大，所以修改次序是右-->中-->左。用一个变量储存遍历过程中所有有节点之和就得到了所有的比当前把该节点的值更大的和，然后修改为该变量的值即可。


```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        self.sum = 0
        def afterOrder(cur):
            if not cur: return
            afterOrder(cur.right)
            self.sum += cur.val
            cur.val = self.sum
            afterOrder(cur.left)
        afterOrder(root)
        return root
```

## 日期

2018 年 1 月 22 日 
2018 年 11 月 13 日 —— 时间有点快

  [1]: https://leetcode.com/problems/convert-bst-to-greater-tree/description/
