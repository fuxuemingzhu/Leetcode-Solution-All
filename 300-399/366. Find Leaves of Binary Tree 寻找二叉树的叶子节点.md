

- 作者：    负雪明烛
- id：      fuxuemingzhu
- 个人博客：[http://fuxuemingzhu.cn/](http://fuxuemingzhu.cn/)

---
@[TOC](目录)

题目地址：https://leetcode-cn.com/problems/find-leaves-of-binary-tree/

## 题目描述

Given a binary tree, collect a tree's nodes as if you were doing this: Collect and remove all leaves, repeat until the tree is empty.

 

Example:

    Input: [1,2,3,4,5]
      
              1
             / \
            2   3
           / \     
          4   5    
    
    Output: [[4,5,3],[2],[1]]
     
    
    Explanation:

    1. Removing the leaves [4,5,3] would result in this tree:
    
              1
             / 
            2          
     
    
    2. Now removing the leaf [2] would result in this tree:
    
              1          
     
    
    3. Now removing the leaf [1] would result in the empty tree:
    
              []         


## 题目大意

给你一棵完全二叉树，请按以下要求的顺序收集它的全部节点：

- 依次从左到右，每次收集并删除所有的叶子节点
- 重复如上过程直到整棵树为空

## 解题方法

### DFS

我的做法比较新颖：计算每个节点的高度，依次放入高度为0,1,2,...,depth(root)的所有节点。

为什么？因为题目虽然让我们每次放入的都是叶子节点，而叶子节点的高度是0。当删除叶子节点时，会使剩余的每个节点的高度减一，此时`新的叶子节点`就是`如果不删除老叶子节点时高度为1`的节点……按照这个方法去做，就是依次放入高度为0,1,2,...,depth(root)的所有节点。

求树的高度用到了记忆化搜索，即代码中的node2depth，这是为了保存已经计算过高度的叶子节点，从而加速求树的高度的计算。

保存每个高度对应了哪些叶子节点的值，使用的是`倒排表`depth2node，其key是高度，value是该高度下对应的叶子节点的值。

DFS时遍历的方式选用的后序遍历，因为按照题目的要求，必须从左到右依次放入叶子节点，故遍历方式是`左孩子->右孩子->根节点`。

这个做法的好处是不用修改树的结构，比如做删除叶子节点的操作。

时间复杂度是O(N)，N为节点数。

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
    vector<vector<int>> findLeaves(TreeNode* root) {
        vector<vector<int>> res;
        int height = depth(root);
        for (int i = 0; i <= height; ++i) {
            res.push_back(depth2node[i]);
        }
        return res;
    }
    int depth(TreeNode* root) {
        if (!root) return -1;
        if (node2depth.count(root))
            return node2depth[root];
        int left = depth(root->left);
        int right = depth(root->right);
        int cur = max(left, right) + 1;
        depth2node[cur].push_back(root->val);
        node2depth[root] = cur;
        return cur;
    }
private:
    unordered_map<int, vector<int>> depth2node;
    unordered_map<TreeNode*, int> node2depth;
};
```

## 日期

2019 年 9 月 24 日 —— 梦见回到了小学，小学已经芳草萋萋破败不堪


  [1]: https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1569299800527&di=0791f14b34f5db98eb9acb10fbb908b1&imgtype=0&src=http://gss0.baidu.com/94o3dSag_xI4khGko9WTAnF6hhy/zhidao/pic/item/1ad5ad6eddc451da41652b3bb0fd5266d116324a.jpg
