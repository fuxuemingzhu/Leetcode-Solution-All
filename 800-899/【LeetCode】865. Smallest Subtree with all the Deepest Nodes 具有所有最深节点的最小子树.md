
作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)

题目地址：https://leetcode.com/problems/smallest-subtree-with-all-the-deepest-nodes/description/

## 题目描述

Given a binary tree rooted at root, the depth of each node is the shortest distance to the root.

A node is deepest if it has the largest depth possible among any node in the entire tree.

The subtree of a node is that node, plus the set of all descendants of that node.

Return the node with the largest depth such that it contains all the deepest nodes in its subtree.

 

Example 1:

    Input: [3,5,1,6,2,0,8,null,null,7,4]
    Output: [2,7,4]

Explanation:

![此处输入图片的描述][1]

    We return the node with value 2, colored in yellow in the diagram.
    The nodes colored in blue are the deepest nodes of the tree.
    The input "[3, 5, 1, 6, 2, 0, 8, null, null, 7, 4]" is a serialization of the given tree.
    The output "[2, 7, 4]" is a serialization of the subtree rooted at the node with value 2.
    Both the input and output have TreeNode type.
     

Note:

1. The number of nodes in the tree will be between 1 and 500.
1. The values of each node are unique.


## 题目大意

一棵二叉树有它的最大深度，找出一个节点，这个节点包含了所有最大深度的叶子。并且这个节点最接近叶子节点。

## 解题方法

这个题貌似很复杂，而且没有思路，这就说明没有建模好。

这个题的模型其实比较左右子树的高度，如果左右子树的高度相等，说明当前节点就是要求的。这个解释是这样的：必须包含所有的最大高度的叶子，左右叶子高度相等，所以必须包含当前节点。

当左子树高度>右子树高度的时候，要求的节点在左边；反之，在右边。

所以，递归思路 + 一个pair。这个pair的思路是，保存了当前节点的深度和当前节点的最深子树节点。

如果还不明白可以看下图的右边部分，每个节点旁边都写了（高度，当前符合要求的节点）。

![这里写图片描述](https://zxi.mytechroad.com/blog/wp-content/uploads/2018/07/866-ep204.png)

```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def subtreeWithAllDeepest(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        return self.depth(root)[1]
        
    def depth(self, root):
        if not root: return 0, None
        l, r = self.depth(root.left), self.depth(root.right)
        if l[0] > r[0]:
            return l[0] + 1, l[1]
        elif l[0] < r[0]:
            return r[0] + 1, r[1]
        else:
            return l[0] + 1, root
        
```

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
    TreeNode* subtreeWithAllDeepest(TreeNode* root) {
        return getDepth(root).second;
    }
private:
    //return <max depth, max depth's node>
    pair<int, TreeNode*> getDepth(TreeNode* root) { 
        if (!root) return {-1, nullptr};
        auto l = getDepth(root->left);
        auto r = getDepth(root->right);
        return {max(l.first, r.first) + 1, (l.first == r.first) ? root : ((l.first > r.first) ? l.second : r.second)};
    }
};
```


参考资料：

https://leetcode.com/problems/smallest-subtree-with-all-the-deepest-nodes/discuss/146808/One-pass
https://www.youtube.com/watch?v=q1zk8vZIDw0


## 日期

2018 年 9 月 5 日 —— 忙碌的一天
2018 年 12 月 12 日 —— 双十二

  [1]: https://s3-lc-upload.s3.amazonaws.com/uploads/2018/07/01/sketch1.png
