

- 作者：    负雪明烛
- id：      fuxuemingzhu
- 个人博客：[http://fuxuemingzhu.cn/](http://fuxuemingzhu.cn/)

---
@[TOC](目录)

题目地址：https://leetcode.com/problems/binary-tree-maximum-path-sum/

## 题目描述

Given a **non-empty** binary tree, find the maximum path sum.

For this problem, a path is defined as any sequence of nodes from some starting node to any node in the tree along the parent-child connections. The path must contain at least one node and does not need to go through the root.

Example 1:

    Input: [1,2,3]
    
           1
          / \
         2   3
    
    Output: 6

Example 2:
    
    Input: [-10,9,20,null,null,15,7]
    
       -10
       / \
      9  20
        /  \
       15   7
    
    Output: 42

## 题目大意

找出二叉树中的最大路径和。

## 解题方法

### 递归

路径是我们可以从二叉树中任意选择1个或者多个相邻的节点而构成的。那么对于每个节点，我们是不是可以考虑他的左孩子是否考虑到路径内，右孩子是否考虑到路径内，从而产生公式：

    经过一个节点的最大路径 = max(其左孩子为顶点的最大路径, 0) + max(右孩子为顶点的最大路径, 0) + 该节点的值。

公式里对左右孩子为顶点的最大路径和0取max，是因为路径可能是负值，加入左右孩子的最大路径为负数，那么就不应该使用了。

为什么左右孩子要为顶点的时候才行呢？一条路径不应该有分叉的，所以如果想求经过一个节点的路径的话，那么左右孩子那里不能分叉，必须是以左右孩子为出发点的一条路径：

       2
       / \
      9  20
        /  \
       15   7

    最大路径是9 + 2 + 20 + 15

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
    int maxPathSum(TreeNode* root) {
        if (!root) return 0;
        maxPathToLeaf(root);
        return res;
    }
    int maxPathToLeaf(TreeNode* root) {
        if (!root) return 0;
        int left = maxPathToLeaf(root->left);
        int right = maxPathToLeaf(root->right);
        if (left < 0)
            left = 0;
        if (right < 0)
            right = 0;
        res = max(res, left + right + root->val);
        return root->val + max(left, right);
    }
private:
    int res = INT_MIN;
};
```

相似题目

[543. Diameter of Binary Tree](https://blog.csdn.net/fuxuemingzhu/article/details/70338312)

## 日期

2019 年 9 月 27 日 —— 昨天面快手，竟然是纯刷题


  [1]: https://assets.leetcode.com/uploads/2019/07/01/screen-shot-2019-07-01-at-53836-pm.png
