
作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)

题目地址：https://leetcode.com/problems/insert-into-a-binary-search-tree/description/

## 题目描述

Given the root node of a binary search tree (BST) and a value to be inserted into the tree, insert the value into the BST. Return the root node of the BST after the insertion. It is guaranteed that the new value does not exist in the original BST.

Note that there may exist multiple valid ways for the insertion, as long as the tree remains a BST after insertion. You can return any of them.

For example, 

    Given the tree:
            4
           / \
          2   7
         / \
        1   3
    And the value to insert: 5

You can return this binary search tree:

         4
       /   \
      2     7
     / \   /
    1   3 5

This tree is also valid:

         5
       /   \
      2     7
     / \   
    1   3
         \
          4


## 题目大意

向BST中插入新的val节点。

## 解题方法

题目中也已经说了，BST插入节点可能存在多个方案，只需要返回其中的一个就好。

所以我使用的就是最基本的建立BST的过程，新的val值进来之后，从根节点开始，依次判断，得到对应的位置，新建立节点并插入就好。使用递归做的，很简单。

代码如下：

```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def insertIntoBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        if not root:
            node = TreeNode(val)
            return node
        if val < root.val:
            if not root.left:
                node = TreeNode(val)
                root.left = node
            else:
                self.insertIntoBST(root.left, val)
        else:
            if not root.right:
                node = TreeNode(val)
                root.right = node
            else:
                self.insertIntoBST(root.right, val)
        return root
```

二刷的时候，写了更简单的方法，我现在对递归的认识是，一定要明白函数返回的是什么，能在当前节点进行判断的，绝对不把子节点放进来！

```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def insertIntoBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        if not root:
            return TreeNode(val)
        if val > root.val:
            root.right = self.insertIntoBST(root.right, val)
        if val < root.val:
            root.left = self.insertIntoBST(root.left, val)
        return root
```

C++版本如下：

```cpp
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    TreeNode* insertIntoBST(TreeNode* root, int val) {
        if (!root) return new TreeNode(val);
        if (val < root->val) root->left = insertIntoBST(root->left, val);
        if (val > root->val) root->right = insertIntoBST(root->right, val);
        return root;
    }
};
```

## 日期

2018 年 9 月 4 日 ———— 迎接明媚的阳光！
