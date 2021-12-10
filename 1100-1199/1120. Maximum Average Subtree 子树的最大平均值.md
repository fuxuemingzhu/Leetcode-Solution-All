
- 作者：    负雪明烛
- id：      fuxuemingzhu
- 个人博客：[http://fuxuemingzhu.cn/](http://fuxuemingzhu.cn/)

---
@[TOC](目录)

题目地址：https://leetcode-cn.com/problems/maximum-average-subtree/

## 题目描述

Given the root of a binary tree, find the maximum average value of any subtree of that tree.

(A subtree of a tree is any node of that tree plus all its descendants. The average value of a tree is the sum of its values, divided by the number of nodes.)

Example 1:

    Input: [5,6,1]
    Output: 6.00000
    Explanation: 
    For the node with value = 5 we have and average of (5 + 6 + 1) / 3 = 4.
    For the node with value = 6 we have and average of 6 / 1 = 6.
    For the node with value = 1 we have and average of 1 / 1 = 1.
    So the answer is 6 which is the maximum.

Note:

1. The number of nodes in the tree is between 1 and 5000.
1. Each node will have a value between 0 and 100000.
1. Answers will be accepted as correct if they are within 10^-5 of the correct answer.


## 题目大意

给出一个二进制数组 data，你需要通过交换位置，将数组中 任何位置 上的 1 组合到一起，并返回所有可能中所需 最少的交换次数。

## 解题方法

### DFS

1. 给每个节点定义一个`pair<int, int>`，第一个位置表示以该节点为根的子树值的和，第二个位置表示子树的节点数；
2. 自顶向上的累加每个节点的这两个数值；
3. 子树平均数是和/节点，使用一个全局变量来存储；
3. 使用字典做记忆化搜索，用来加速


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
    double maximumAverageSubtree(TreeNode* root) {
        double res = -1;
        dfs(root, res);
        return res;
    }
    pair<int, int> dfs(TreeNode* root, double& min_avg) {
        if (!root) return {0, 0};
        if (m_.count(root)) return m_[root];
        pair<int, int> left = dfs(root->left, min_avg);
        pair<int, int> right = dfs(root->right, min_avg);
        pair<int, int> cur;
        cur.first += left.first + right.first + root->val;
        cur.second += left.second + right.second + 1;
        min_avg = max(min_avg, (double)cur.first / cur.second);
        m_[root] = cur;
        return cur;
    }
private:
    // 节点 : 子树的和，子树的节点数
    unordered_map<TreeNode*, pair<int, int>> m_;
};
```

## 日期

2019 年 9 月 23 日 —— 昨夜睡的早，错过了北京的烟火
