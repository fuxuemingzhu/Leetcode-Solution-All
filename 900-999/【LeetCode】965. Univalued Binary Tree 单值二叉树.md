

作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)


题目地址：https://leetcode.com/problems/univalued-binary-tree/


## 题目描述

A binary tree is ``univalued`` if every node in the tree has the same value.

Return ``true`` if and only if the given tree is univalued.

 

Example 1:

![此处输入图片的描述][1]

    Input: [1,1,1,1,1,null,1]
    Output: true

Example 2:

![此处输入图片的描述][2]

    Input: [2,2,2,5,2]
    Output: false
 

Note:

1. The number of nodes in the given tree will be in the range [1, 100].
1. Each node's value will be an integer in the range [0, 99].

## 题目大意

问二叉树的每个节点的值是不是都是一样的。


## 解题方法

### BFS

可以使用BFS或者DFS.这个题我直接花了3分钟写了个简单版本的BFS就能通过了。使用队列保存每个节点，用val保存root节点的值。如果弹出的数字不等于val不等于root节点就立刻返回false。如果全部判断完成之后仍然没有返回false，说明所有的数字都等于root，返回true.

python代码如下：

```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isUnivalTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        q = collections.deque()
        q.append(root)
        val = root.val
        while q:
            node = q.popleft()
            if not node:
                continue
            if val != node.val:
                return False
            q.append(node.left)
            q.append(node.right)
        return True
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
    bool isUnivalTree(TreeNode* root) {
        queue<TreeNode*> q;
        q.push(root);
        int val = root->val;
        while (!q.empty()) {
            TreeNode* node = q.front(); q.pop();
            if (!node) continue;
            if (node->val != val) 
                return false;
            q.push(node->left);
            q.push(node->right);
        }
        return true;
    }
};
```

### DFS

DFS代码很简单，我就不解释了。

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
    bool isUnivalTree(TreeNode* root) {
        return dfs(root, root->val);
    }
    bool dfs(TreeNode* root, int val) {
        if (!root) return true;
        if (root->val != val) return false;
        return dfs(root->left, val) && dfs(root->right, val);
    }
};
```

## 日期

2018 年 12 月 30 日 —— 周赛差强人意


  [1]: https://assets.leetcode.com/uploads/2018/12/28/unival_bst_1.png
  [2]: https://assets.leetcode.com/uploads/2018/12/28/unival_bst_2.png
  [3]: https://blog.csdn.net/fuxuemingzhu/article/details/82620422
