- 作者：    负雪明烛
- id：      fuxuemingzhu
- 个人博客：[http://fuxuemingzhu.cn/](http://fuxuemingzhu.cn/)

---
@[TOC](目录)


题目地址：https://leetcode.com/problems/binary-tree-postorder-traversal/

## 题目描述

Given a binary tree, return the postorder traversal of its nodes' values.

Example:

    Input: [1,null,2,3]
       1
        \
         2
        /
       3
    
    Output: [3,2,1]

Follow up: Recursive solution is trivial, could you do it iteratively?
    

## 题目大意

二叉树的后序遍历。

## 解题方法

### 递归

最常见最简单的方法就是DFS。先把左右子树递归完成，然后把根节点的值也放入结果中。

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
    vector<int> postorderTraversal(TreeNode* root) {
        vector<int> res;
        if (!root) return res;
        vector<int> left = postorderTraversal(root->left);
        vector<int> right = postorderTraversal(root->right);
        res.insert(res.end(), left.begin(), left.end());
        res.insert(res.end(), right.begin(), right.end());
        res.push_back(root->val);
        return res;
    }
};
```

Python代码如下：

```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        if not root: return res
        if root.left:
            res.extend(self.postorderTraversal(root.left))
        if root.right:
            res.extend(self.postorderTraversal(root.right))
        res.append(root.val)
        return res
```

### 迭代

题目中说了递归方法太琐碎，能不能用迭代方法解决呢？

由于后序遍历把根节点放到了最后，而我们在遍历的过程中，一定先获得到根节点，那么我们可以先倒序，然后再反转。

后序遍历：`左->右->根`。
我们的做法：`根->右->左`，然后再反转。

即，先把根节点放入栈中，然后把它左孩子、右孩子依次放入，这样我们下次对栈内的元素遍历得到的顺序就是从右向左的，对于栈中弹出的每个节点都是如此。

得到的顺序是`根->右子树(节点全部入栈)->左子树`的遍历方式，最后需要加一个翻转即可得到想要的后序遍历。

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
    vector<int> postorderTraversal(TreeNode* root) {
        vector<int> res;
        if (!root) return res;
        stack<TreeNode*> st;
        st.push(root);
        while (!st.empty()) {
            TreeNode* node = st.top(); st.pop();
            if (!node) continue;
            res.push_back(node->val);
            st.push(node->left);
            st.push(node->right);
        }
        reverse(res.begin(), res.end());
        return res;
    }
};
```

## 日期

2019 年 9 月 20 日 —— 是选择中国互联网式加班？还是外企式养生？
