

- 作者：    负雪明烛
- id：      fuxuemingzhu
- 个人博客：[http://fuxuemingzhu.cn/](http://fuxuemingzhu.cn/)

---
@[TOC](目录)

题目地址：https://leetcode.com/problems/maximum-level-sum-of-a-binary-tree/

## 题目描述

Given the root of a binary tree, the level of its root is 1, the level of its children is 2, and so on.

Return the smallest `level X` such that the sum of all the values of nodes at `level X` is maximal.

Example 1:

![此处输入图片的描述][1]

    Input: [1,7,0,7,-8,null,null]
    Output: 2
    Explanation: 
    Level 1 sum = 1.
    Level 2 sum = 7 + 0 = 7.
    Level 3 sum = 7 + -8 = -1.
    So we return the level with the maximum sum which is level 2.

Note:

1. The number of nodes in the given tree is between 1 and 10^4.
1. `-10^5 <= node.val <= 10^5`


## 题目大意

二叉树中一层的节点和最大的时候的最小层号。

## 解题方法

### BFS

这个题考的是层次遍历，可以有两种做法，分别是BFS和DFS，类似题目是[102. Binary Tree Level Order Traversal][2]。这里使用的是BFS。

BFS需要一个队列存放当前层的所有叶子节点，然后出队列并且对这一层的所有叶子节点求和。

题目要求的是最大的和出现的最小层号，所以做个判断，如果当前层的和大于之前层，那么修改结果的层号。

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
    int maxLevelSum(TreeNode* root) {
        int res_sum = INT_MIN;
        int res_level = 1;
        queue<TreeNode*> que;
        que.push(root);
        int level = 1;
        while (!que.empty()) {
            int size = que.size();
            int level_sum = 0;
            while (size --) {
                TreeNode* cur = que.front(); que.pop();
                if (!cur) continue;
                level_sum += cur->val;
                que.push(cur->left);
                que.push(cur->right);
            }
            if (level_sum > res_sum) {
                res_sum = level_sum;
                res_level = level;
            }
            level ++;
        }
        return res_level;
    }
};
```

## 日期

2019 年 9 月 27 日 —— 昨天面快手，竟然是纯刷题


  [1]: https://assets.leetcode.com/uploads/2019/05/03/capture.JPG
  [2]: https://blog.csdn.net/fuxuemingzhu/article/details/79616156
