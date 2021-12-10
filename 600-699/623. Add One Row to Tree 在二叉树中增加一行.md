# 【LeetCode】623. Add One Row to Tree 解题报告（Python）

标签（空格分隔）： LeetCode

---

题目地址：https://leetcode.com/problems/add-one-row-to-tree/description/

## 题目描述：

Given the root of a binary tree, then value v and depth d, you need to add a row of nodes with value v at the given depth d. The root node is at depth 1.

The adding rule is: given a positive integer depth d, for each NOT null tree nodes N in depth d-1, create two tree nodes with value v as N's left subtree root and right subtree root. And N's original left subtree should be the left subtree of the new left subtree root, its original right subtree should be the right subtree of the new right subtree root. If depth d is 1 that means there is no depth d-1 at all, then create a tree node with value v as the new root of the whole original tree, and the original tree is the new root's left subtree.

Example 1:

    Input: 
    
    A binary tree as following:

           4
         /   \
        2     6
       / \   / 
      3   1 5   
    
    v = 1
    
    d = 2
    
    Output: 
    
           4
          / \
         1   1
        /     \
       2       6
      / \     / 
     3   1   5   

Example 2:

    Input: 
    
    A binary tree as following:
    
          4
         /   
        2    
       / \   
      3   1    
    
    v = 1
    
    d = 3
    
    Output: 

          4
         /   
        2
       / \    
      1   1
     /     \  
    3       1

Note:

- The given d is in range [1, maximum depth of the given tree + 1].
- The given binary tree has at least one tree node.

    
## 题目大意

新添一层值为v的节点到二叉树的第d层。原来二叉树的该层节点设置成新层的子节点。


## 解题方法

采用的是递归的解法。其实仔细读题是有很大的作用的，题目中说了很清楚了，如果d是1的话，新建节点，原来的root设成该节点的左边节点。如果d是2的话，就给root节点新建出左右节点，把原来的root子节点设置成新子节点的子节点即可～～

代码：

```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def addOneRow(self, root, v, d):
        """
        :type root: TreeNode
        :type v: int
        :type d: int
        :rtype: TreeNode
        """
        if not root: return root
        if d == 1:
            left = TreeNode(v)
            left.left = root
            root = left
        elif d == 2:
            left = TreeNode(v)
            right = TreeNode(v)
            left.left = root.left
            right.right = root.right
            root.left = left
            root.right = right
        else:
            self.addOneRow(root.left, v, d - 1)
            self.addOneRow(root.right, v, d - 1)
        return root
```

方法二： 循环。

待续。

## 日期

2018 年 3 月 21 日 ———— 啊，耽误了一天没刷题。。


  [1]: http://blog.csdn.net/fuxuemingzhu/article/details/51291406