- 作者：    负雪明烛
- id：      fuxuemingzhu
- 个人博客：[http://fuxuemingzhu.cn/](http://fuxuemingzhu.cn/)

---
@[TOC](目录)

题目地址：https://leetcode.com/problems/delete-node-in-a-bst/description/

## 题目描述

Given a root node reference of a BST and a key, delete the node with the given key in the BST. Return the root node reference (possibly updated) of the BST.

Basically, the deletion can be divided into two stages:

- Search for a node to remove.
- If the node is found, delete the node.

Note: Time complexity should be O(height of tree).

Example:

    root = [5,3,6,2,4,null,7]
    
    key = 3
    
        5
       / \
      3   6
     / \   \
    2   4   7
    
    Given key to delete is 3. So we find the node with value 3 and delete it.
    
    One valid answer is [5,4,6,2,null,null,7], shown in the following BST.
    
        5
       / \
      4   6
     /     \
    2       7
    
    Another valid answer is [5,2,6,null,4,null,7].
    
        5
       / \
      2   6
       \   \
        4   7
    
## 题目大意

删除二叉树中指定一节点，并调整二叉树，使得结果的二叉树仍然满足BST的条件。

## 解题方法
### 迭代

这个题的解法并不是固定的，删除之后的二叉树也不止一种。比如可以有下面两种主要的方法：

1. 被删除节点没有左子树：返回其右子树
2. 被删除节点节点没有右子树：返回其左子树
3. 被删除节点既有左子树，又有右子树：
    1）查找到其右子树的最小值的节点，替换掉被删除的节点，并删除找到的最小节点
    2）查找到其左子树的最大值的节点，替换掉被删除的节点，并删除找到的最大节点

下面的做法是查找右子树的最小值节点的方法，最小节点就是右子树中的最靠左边的节点。代码使用的递归，最核心的是找到该节点之后的操作，特别是把值进行交换一步很重要，因为我们并没有删除了该最小值节点，所以把最小值的节点赋值成要查找的节点，然后在之后的操作中将会把它删除。

Python代码如下：

```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
        if not root: return None
        if root.val == key:
            if not root.right:
                left = root.left
                return left
            else:
                right = root.right
                while right.left:
                    right = right.left
                root.val, right.val = right.val, root.val
        root.left = self.deleteNode(root.left, key)
        root.right = self.deleteNode(root.right, key)
        return root
```

删除查找到左子树中最大值的方法，左子树的最大值是左子树的最靠右边的节点，使用迭代找到该值，然后和root节点的值进行交换。递归左右子树，这个被交换的值会在后面被删除掉。

C++代码如下：

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
    TreeNode* deleteNode(TreeNode* root, int key) {
        if (!root) return nullptr;
        if (root->val == key) {
            if (!root->left) {
                return root->right;
            } else {
                TreeNode* left = root->left;
                while (left->right) {
                    left = left->right;
                }
                swap(left->val, root->val);
            }
        }
        root->left = deleteNode(root->left, key);
        root->right = deleteNode(root->right, key);
        return root;
    }
};
```

## 日期

2018 年 3 月 23 日 —— 科目一考了100分哈哈哈哈～嗝～
2019 年 9 月 27 日 —— 昨天面快手，竟然是纯刷题

  [1]: http://blog.csdn.net/fuxuemingzhu/article/details/51291406
