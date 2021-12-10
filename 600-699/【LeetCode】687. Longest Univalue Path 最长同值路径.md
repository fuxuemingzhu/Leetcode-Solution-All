
作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)

题目地址：[https://leetcode.com/problems/longest-univalue-path/description/][1]


## 题目描述

Given a binary tree, find the length of the longest path where each node in the path has the same value. This path may or may not pass through the root.

Note: The length of path between two nodes is represented by the number of edges between them.

Example 1:
    
    Input:
    
                  5
                 / \
                4   5
               / \   \
              1   1   5

    Output:
    
    2

Example 2:
    
    Input:
    
                  1
                 / \
                4   5
               / \   \
              4   4   5

    Output:
    
    2

Note: The given binary tree has not more than 10000 nodes. The height of the tree is not more than 1000.

## 题目大意

求一个二叉树中，相等数值的节点之间的路径最长是多少。

## 解题方法

### DFS

基本思想就是dfs，求一个顶点到所有根节点的路径，时刻保留相等元素的最大值。相等元素的最大值是左右子树的相等元素的最大值+1，所以是递归。

定义的DFS函数是获得在通过root节点的情况下，最长单臂路径。其中更新的res是左右臂都算上的。所以这个题和普通的题是有点不一样。

可以见[LeetCode 687. Longest Univalue Path](http://zxi.mytechroad.com/blog/tree/leetcode-687-longest-univalue-path/)解法。


![在这里插入图片描述](https://zxi.mytechroad.com/blog/wp-content/uploads/2017/10/687-ep78-1.png)


```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        longest = [0]
        def dfs(root):
            if not root:
                return 0
            left_len, right_len = dfs(root.left), dfs(root.right)
            left = left_len + 1 if root.left and root.left.val == root.val else 0
            right = right_len + 1 if root.right and root.right.val == root.val else 0
            longest[0] = max(longest[0], left + right)
            return max(left, right)
        dfs(root)
        return longest[0]
```

---

二刷，python写法，思路和上面相同。

```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root: return 0
        self.res = 0
        self.getPath(root)
        return self.res
    
    def getPath(self, root):
        if not root: return 0
        left = self.getPath(root.left)
        right = self.getPath(root.right)
        pl, pr = 0, 0
        if root.left and root.left.val == root.val: pl = 1 + left
        if root.right and root.right.val == root.val: pr = 1 + right
        self.res = max(self.res, pl + pr)
        return max(pl, pr)
```

C++版本的如下：

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
    int longestUnivaluePath(TreeNode* root) {
        if(root == nullptr) return 0;
        int res = 0;
        getPath(root, res);
        return res;
    }
private:
    int getPath(TreeNode* root, int &res){
        if(root == nullptr) return 0;
        int l = getPath(root->left, res);
        int r = getPath(root->right, res);
        int pl = 0, pr = 0;
        if(root->left && (root->left->val == root->val)) pl = l + 1;
        if(root->right && (root->right->val == root->val)) pr = r + 1;
        res = max(res, pl + pr);
        return max(pl, pr);
    }
};
```

## 日期

2018 年 2 月 3 日 
2018 年 11 月 24 日 —— 周日开始！一周就过去了～

  [1]: https://leetcode.com/problems/longest-univalue-path/description/
