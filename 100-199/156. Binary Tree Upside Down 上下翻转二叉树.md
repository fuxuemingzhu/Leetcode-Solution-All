
作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	[http://fuxuemingzhu.cn/](http://fuxuemingzhu.cn/)

---
@[TOC](目录)


题目地址：https://leetcode-cn.com/problems/binary-tree-upside-down/

## 题目描述

Given a binary tree where all the `right` nodes are either leaf nodes with a sibling (a left node that shares the same parent node) or empty, flip it upside down and turn it into a tree where the original right nodes turned into left leaf nodes. Return the new root.

Example:

    Input: [1,2,3,4,5]
    
        1
       / \
      2   3
     / \
    4   5
    
    Output: return the root of the binary tree [4,5,2,#,#,3,1]
    
       4
      / \
     5   2
        / \
       3   1  


## 题目大意

给定一个二叉树，其中所有的右节点要么是具有兄弟节点（拥有相同父节点的左节点）的叶节点，要么为空，将此二叉树上下翻转并将它变成一棵树， 原来的右节点将转换成左叶节点。返回新的根。

## 解题方法

### 递归

树的做法一般都可以递归和非递归做法。递归做法说明如下：

把一棵树右旋，规律是：左孩子变成了根，右孩子变成了左子树，根节点变成了右子树。

我们先保存下来未旋转之前的左右孩子，然后对左子树递归做上面的操作，注意右孩子是叶子节点或者为空，所以不用对右孩子递归。另外由于根节点变成了右子树，需要把它的两个孩子设置为空。


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
    TreeNode* upsideDownBinaryTree(TreeNode* root) {
        if (!root || !root->left) return root;
        TreeNode* l = root->left;
        TreeNode* r = root->right;
        TreeNode* newRoot = upsideDownBinaryTree(root->left);
        l->left = r;
        l->right = root;
        root->left = nullptr;
        root->right = nullptr;
        return newRoot;
    }
};
```

### 迭代

迭代的做法比较绕。

pre保存新树的根节点;
cur保存每个节点，每次向左下方移动;
next保存cur->next;
temp保存cur->right;

所以核心语句就是修改cur->left和cur->right两句，其余语句都是在移动指针，要注意的是保存和移动的顺序不能和修改相冲突。

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
    TreeNode* upsideDownBinaryTree(TreeNode* root) {
        TreeNode* cur = root, *pre = nullptr, *temp = nullptr, *nxt = nullptr;
        while (cur) {
            nxt = cur->left;
            cur->left = temp;
            temp = cur->right;
            cur->right = pre;
            pre = cur;
            cur = nxt;
        }
        return pre;
    }
};
```

## 日期

2019 年 9 月 17 日 —— 听了hulu宣讲会，觉得hulu的压力不大
