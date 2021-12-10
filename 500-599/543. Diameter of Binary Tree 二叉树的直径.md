
- 作者：    负雪明烛
- id：      fuxuemingzhu
- 个人博客：[http://fuxuemingzhu.cn/](http://fuxuemingzhu.cn/)


---
@[TOC](目录)

题目地址：[https://leetcode.com/problems/diameter-of-binary-tree/#/description][1]


## 题目描述

Given a binary tree, you need to compute the length of the diameter of the tree. The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

Example:
Given a binary tree 

          1
         / \
        2   3
       / \     
      4   5    
Return 3, which is the length of the path [4,2,1,3] or [5,2,1,3].

Note: The length of path between two nodes is represented by the number of edges between them.

## 题目大意

找出树的两个节点之间的最长距离。

## 解题方法

### 递归

这个题当然想到是递归。但是如何递归呢。看叶子节点的左右子树的深度都是0，那么，它的深度是0，一个树的深度是其左右子树的最大值+1。

树总的最大宽度是其左右子树高度的和中的最大值。

求最大距离的过程需要在递归里面写，所以这个步骤比较巧妙，一个递归实现了两个作用。

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
    int diameterOfBinaryTree(TreeNode* root) {
        if (!root) return 0;
        distanceToLeaf(root);
        return res - 1;
    }
    int distanceToLeaf(TreeNode* root) {
        if (!root) return 0;
        if (m.count(root)) return m[root];
        int left = distanceToLeaf(root->left);
        int right = distanceToLeaf(root->right);
        res = max(left + right + 1, res);
        int distance = max(left, right) + 1;
        m[root] = distance;
        return distance;
    }
private:
    int res = INT_MIN;
    unordered_map<TreeNode*, int> m;
};
```

Java代码如下：

```java
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
public class Solution {
    int max = 0;
    public int diameterOfBinaryTree(TreeNode root) {
        DeepOfTree(root);
        return max;
    }
    public int DeepOfTree(TreeNode root){
        if(root == null) return 0;
        int left = DeepOfTree(root.left);
        int right = DeepOfTree(root.right);
        max = Math.max(max, left + right);
        return Math.max(left, right) + 1;
    }
}
```


Python代码如下：

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        self.diameter = 0
        self.getDepth(root)
        return self.diameter
        
    def getDepth(self, root):
        if not root:
            return 0
        left = self.getDepth(root.left)
        right = self.getDepth(root.right)
        self.diameter = max(self.diameter, left + right)
        return 1 + max(left, right)
```

 相似题目

[124. Binary Tree Maximum Path Sum](https://blog.csdn.net/fuxuemingzhu/article/details/101563683)

## 日期

2017 年 4 月 21 日 
2018 年 11 月 16 日 —— 又到周五了！
2019 年 9 月 27 日 —— 昨天面快手，竟然是纯刷题

  [1]: https://leetcode.com/problems/diameter-of-binary-tree/#/description
