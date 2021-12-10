- 作者：    负雪明烛
- id：      fuxuemingzhu
- 个人博客：[http://fuxuemingzhu.cn/](http://fuxuemingzhu.cn/)

---
@[TOC](目录)


题目地址：https://leetcode-cn.com/problems/equal-tree-partition/

## 题目描述

Given a binary tree with n nodes, your task is to check if it's possible to partition the tree to two trees which have the equal sum of values after removing exactly one edge on the original tree.

Example 1:

    Input:     
        5
       / \
      10 10
        /  \
       2   3
    
    Output: True
    Explanation: 
        5
       / 
      10
          
    Sum: 15
    
       10
      /  \
     2    3
    
    Sum: 15

Example 2:

    Input:     
        1
       / \
      2  10
        /  \
       2   20
    
    Output: False
    Explanation: You can't split the tree into two trees with equal sum after removing exactly one edge on the tree.

Note:

1. The range of tree node value is in the range of [-100000, 100000].
2. 1 <= n <= 10000


## 题目大意

删除二叉树中的一条边，能否使得剩余的两个树的节点之和相等？

## 解题方法

### 递归

这个题就是分割二叉树，使得分割完之后两部分和相等。那么，所有节点总的和必须是偶数。我们可以求出总和total，判断total/2是否是其中的一个子树，如果是的话就可以分割出来。

使用递归的做法，计算出每个子树的所有节点之和。这样也就知道了整个树的所有节点之和total，此total必须是偶数。然后找half = total / 2是否是某个`子树`的和。

为了防止重复计算子树的和，使用了字典保存以每个节点为根的子树的和。这样已经计算的节点可以直接查表得到其子树和。

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
    bool checkEqualTree(TreeNode* root) {
        int total = getSum(root);
        if (total & 1)
            return false;
        int half = total / 2;
        return subEqual(root->left, half) || subEqual(root->right, half);
    }
    bool subEqual(TreeNode* root, int target) {
        if (!root) return false;
        if (getSum(root) == target)
            return true;
        return subEqual(root->left, target) || subEqual(root->right, target);
    }
    int getSum(TreeNode* root) {
        if (!root) return 0;
        if (m.count(root))
            return m[root];
        int res = root->val + getSum(root->left) + getSum(root->right);
        m[root] = res;
        return res;
    }
private:
    unordered_map<TreeNode*, int> m;
};
```


参考资料：https://leetcode-cn.com/problems/equal-tree-partition/solution/java-di-gui-by-zxy0917-16/

## 日期

2019 年 9 月 21 日 —— 莫生气，我若气病谁如意


  [1]: https://assets.leetcode.com/uploads/2018/10/12/bstdlloriginalbst.png
  [2]: https://assets.leetcode.com/uploads/2018/10/12/bstdllreturndll.png
  [3]: https://assets.leetcode.com/uploads/2018/10/12/bstdllreturnbst.png
  [4]: https://blog.csdn.net/fuxuemingzhu/article/details/79294461
