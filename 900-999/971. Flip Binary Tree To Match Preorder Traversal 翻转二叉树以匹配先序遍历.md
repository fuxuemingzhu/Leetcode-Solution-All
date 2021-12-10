
作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)


题目地址：https://leetcode.com/problems/flip-binary-tree-to-match-preorder-traversal/


## 题目描述

Given a binary tree with N nodes, each node has a different value from {1, ..., N}.

A node in this binary tree can be flipped by swapping the left child and the right child of that node.

Consider the sequence of N values reported by a preorder traversal starting from the root.  Call such a sequence of N values the voyage of the tree.

(Recall that a preorder traversal of a node means we report the current node's value, then preorder-traverse the left child, then preorder-traverse the right child.)

Our goal is to flip the least number of nodes in the tree so that the voyage of the tree matches the voyage we are given.

If we can do so, then return a list of the values of all nodes flipped.  You may return the answer in any order.

If we cannot do so, then return the list [-1].

 

Example 1:

![此处输入图片的描述][1]

    Input: root = [1,2], voyage = [2,1]
    Output: [-1]

Example 2:

![此处输入图片的描述][2]

    Input: root = [1,2,3], voyage = [1,3,2]
    Output: [1]

Example 3:

![此处输入图片的描述][3]

    Input: root = [1,2,3], voyage = [1,2,3]
    Output: []
 

Note:

1. 1 <= N <= 100

## 题目大意

最少翻转哪些节点，能使得二叉树的前序遍历变成voyage.

## 解题方法

### 前序遍历

其实这个题不难，因为题目就说了是前序遍历，所以做法肯定还是前序遍历。我刚开始一直想不通的地方在于，题目又是返回[-1]，又是正常返回，没想好怎么做区分。其实做法就是递归函数不仅要修改res数组，还要返回表示能不能构成题目条件的bool变量。

按照lee215的说法，看到二叉树的题，很大可能就需要递归，所以直接先写出dfs函数，然后再慢慢向里面填东西。

我们定义的dfs函数意义是，我们能不能通过翻转（或者不翻转）该root节点的左右子树，得到对应v。如果能，返回true，否则返回false。

首先在递归函数中，我们对root节点进行判断，如果root不存在，这种情况不应该认为是题目输入错误，而是应该认为已经遍历到最底部了，这个时候相当于root = [], voyage = []，所以返回true;在先序遍历的时候，root节点是第一个要被遍历到的节点，如果不和voyage[0]相等，直接返回false;

这个题目的难点在于是否需要翻转一个节点的左右孩子。判断的方法其实是简单的：如果voyage第二个元素等于root的左孩子，那么说明不用翻转，直接递归调用左右孩子；否则如果voyage的第二个元素等于root的右孩子，那么还要注意一下，在左孩子存在的情况下，我们需要翻转当前的节点左右孩子。

翻转是什么概念呢？这里并没有直接交换，而是把当前遍历到的位置使用遍历i保存起来，这样voyage[i]就表示当前遍历到哪个位置了。所以dfs调用两个孩子的顺序很讲究，它体现了先序遍历先解决哪个树的问题，也就是完成了逻辑上的交换左右孩子。

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
    int i = 0;
    vector<int> res;
    vector<int> flipMatchVoyage(TreeNode* root, vector<int>& voyage) {
        res.clear();
        if (dfs(root, voyage)) {
            return res;
        }
        return {-1};
    }
    // can we get v by flip root?
    bool dfs(TreeNode* root, vector<int>& v) {
        if (!root) return true;
        if (root->val != v[i++]) return false;
        if (root->left && root->left->val == v[i]) {
            return dfs(root->left, v) && dfs(root->right, v);
        } else if (root->right && root->right->val == v[i]) {
            if (root->left)
                res.push_back(root->val);
            return dfs(root->right, v) && dfs(root->left, v);
        }
        return !root->left && !root->right;
    }
};
```

参考资料：https://leetcode.com/problems/flip-binary-tree-to-match-preorder-traversal/discuss/214216/JavaC%2B%2BPython-DFS-Solution


## 日期

2019 年 1 月 6 日 —— 打球打的腰酸背痛


  [1]: https://assets.leetcode.com/uploads/2019/01/02/1219-01.png
  [2]: https://assets.leetcode.com/uploads/2019/01/02/1219-02.png
  [3]: https://assets.leetcode.com/uploads/2019/01/02/1219-02.png
  [4]: http://blog.jobbole.com/74263/
