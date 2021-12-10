
- 作者：    负雪明烛
- id：      fuxuemingzhu
- 个人博客：[http://fuxuemingzhu.cn/](http://fuxuemingzhu.cn/)

---
@[TOC](目录)

题目地址：https://leetcode.com/problems/delete-nodes-and-return-forest/

## 题目描述

Given the root of a binary tree, each node in the tree has a distinct value.

After deleting all nodes with a value in `to_delete`, we are left with a forest (a disjoint union of trees).

Return the roots of the trees in the remaining forest.  You may return the result in any order.
 

Example 1:

![此处输入图片的描述][1]

    Input: root = [1,2,3,4,5,6,7], to_delete = [3,5]
    Output: [[1,2,null,4],[6],[7]]
 

Constraints:

1. The number of nodes in the given tree is at most 1000.
1. Each node has a distinct value between 1 and 1000.
1. `to_delete`.length <= 1000
1. `to_delete` contains distinct values between 1 and 1000.


## 题目大意

删除一棵二叉树中的所有值出现在to_delete中的节点。

## 解题方法

### 递归

参考了lee215大神的答案。看到二叉树的题就想到递归呀！

一个节点被删除时有以下几个情况：

1. 如果该节点是根节点，形成左右两个子树，此时递归左右子树。
2. 如果该节点不是根节点，那么需要修改其父节点指向自己的指针为空，并且递归左右子树。

一个节点一旦被删除，那么其左右孩子就是新的树的根节点。
如果一个节点是根节点，并且不被删除的情况下，才会放入结果中。

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
    vector<TreeNode*> delNodes(TreeNode* root, vector<int>& to_delete) {
        vector<TreeNode*> res;
        helper(root, true, res, to_delete);
        return res;
    }
    void helper(TreeNode*& node, bool isRoot, vector<TreeNode*>& res, vector<int>& to_delete) {
        if (!node) return;
        bool isDel = delCurNode(node, to_delete);
        helper(node->left, isDel, res, to_delete);
        helper(node->right, isDel, res, to_delete);
        if (isRoot && !isDel) {
            res.push_back(node);
        }
        if (!isRoot && isDel) {
            node = nullptr;
        }
    }
    bool delCurNode(TreeNode* root, vector<int>& to_delete) {
        for (int val : to_delete) {
            if (root->val == val) {
                return true;
            }
        }
        return false;
    }
};
```

参考资料：https://leetcode.com/problems/delete-nodes-and-return-forest/discuss/328853/JavaC%2B%2BPython-Recursion-Solution

## 日期

2019 年 9 月 27 日 —— 昨天面快手，竟然是纯刷题


  [1]: https://assets.leetcode.com/uploads/2019/07/01/screen-shot-2019-07-01-at-53836-pm.png
