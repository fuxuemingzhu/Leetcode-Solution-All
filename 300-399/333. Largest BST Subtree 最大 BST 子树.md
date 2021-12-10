

- 作者：    负雪明烛
- id：      fuxuemingzhu
- 个人博客：[http://fuxuemingzhu.cn/](http://fuxuemingzhu.cn/)

---
@[TOC](目录)


题目地址：https://leetcode-cn.com/problems/largest-bst-subtree/

## 题目描述

Given a binary tree, find the largest subtree which is a `Binary Search Tree (BST)`, where largest means subtree with largest number of nodes in it.

Note:

- A subtree must include all of its descendants.

Example:

    Input: [10,5,15,1,8,null,7]
    
       10 
       / \ 
      5  15 
     / \   \ 
    1   8   7
    
    Output: 3
    Explanation: The Largest BST Subtree in this case is the highlighted one.
                 The return value is the subtree's size, which is 3.

Follow up:
- Can you figure out ways to solve it with O(n) time complexity?


## 题目大意

找出一个树中最大的BST有多少个节点。

## 解题方法

### DFS

如果用简单的方法做，就是先判断每个树是不是BST，如果是则返回其节点个数，如果不是就递归他的左右子树，最后结果要用最大值。

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
    int largestBSTSubtree(TreeNode* root) {
        if (!root) return 0;
        int res = 0;
        if (isBST(root, INT_MIN, INT_MAX)) {
            return countNodes(root);
        }
        res = max(res, largestBSTSubtree(root->left));
        res = max(res, largestBSTSubtree(root->right));
        return res;
    }
    bool isBST(TreeNode* root, int minVal, int maxVal) {
        if (!root) return true;
        if (root->val >= maxVal)
            return false;
        if (root->val <= minVal)
            return false;
        return isBST(root->left, minVal, root->val) && isBST(root->right, root->val, maxVal);
    }
    int countNodes(TreeNode* root) {
        if (!root) return 0;
        return 1 + countNodes(root->left) + countNodes(root->right);
    }
private:
    int res = 0;
};
```

## 日期

2019 年 9 月 20 日 —— 是选择中国互联网式加班？还是外企式养生？


  [1]: https://assets.leetcode.com/uploads/2018/10/12/maze_1_example_1.png
  [2]: https://assets.leetcode.com/uploads/2018/10/13/maze_1_example_2.png
