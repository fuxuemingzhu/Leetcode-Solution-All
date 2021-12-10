- 作者：    负雪明烛
- id：      fuxuemingzhu
- 个人博客：[http://fuxuemingzhu.cn/](http://fuxuemingzhu.cn/)

---
@[TOC](目录)

题目地址：[https://leetcode.com/problems/binary-tree-preorder-traversal/#/description][1]


## 题目描述

Given a binary tree, return the preorder traversal of its nodes' values.

For example:
	
	Given binary tree {1,#,2,3},

       1
        \
         2
        /
       3

	return [1,2,3].

Note: Recursive solution is trivial, could you do it iteratively?

## 题目大意

求一个二叉树的先序遍历。

## 解题方法

### 递归

递归的思路就是先保存根节点的值，然后递归左子树和右子树。

python代码如下：

```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root: return []
        res = []
        res.append(root.val)
        res.extend(self.preorderTraversal(root.left))
        res.extend(self.preorderTraversal(root.right))
        return res
```

Java代码如下：

```java
public class Solution {
    List<Integer> ans = new ArrayList<Integer>();
    public List<Integer> preorderTraversal(TreeNode root) {
        preOrder(root);
        return ans;
    }
    public void preOrder(TreeNode root){
        if(root == null){
            return;
        }
        ans.add(root.val);
        preOrder(root.left);
        preOrder(root.right);
    }
}
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
    vector<int> preorderTraversal(TreeNode* root) {
        vector<int> res;
        preorder(root, res);
        return res;
    }
    void preorder(TreeNode* root, vector<int>& res) {
        if (!root) return;
        res.push_back(root->val);
        preorder(root->left, res);
        preorder(root->right, res);
    }
};
```

### 迭代

迭代版本的需要使用栈，先把右孩子进栈，再左孩子进栈。

为什么这个访问顺序呢？我们知道栈是后进先出的数据结构，所以遍历完根节点之后，把右孩子放到栈里，把左孩子放到栈里，那么下一次在出栈的时候是左孩子，所以总之就是个`根-->左-->右`先序遍历的过程了。

Python代码如下：

```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root: return []
        res = []
        stack = []
        stack.append(root)
        while stack:
            node = stack.pop()
            if not node:
                continue
            res.append(node.val)
            stack.append(node.right)
            stack.append(node.left)
        return res
```

Java代码如下：

```java
public class Solution {
    public List<Integer> preorderTraversal(TreeNode root) {
        if(root == null){
            return new ArrayList<Integer>();
        }
        List<Integer> ans = new ArrayList<Integer>();
        Stack<TreeNode> stack = new Stack<TreeNode>();
        stack.push(root);
        while(!stack.isEmpty()){
            TreeNode temp = stack.pop();
            ans.add(temp.val);
            if(temp.right != null){
                stack.push(temp.right);
            }
            if(temp.left != null){
                stack.push(temp.left);
            }
        }
        return ans;
    }
}
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
    vector<int> preorderTraversal(TreeNode* root) {
        vector<int> res;
        stack<TreeNode*> s;
        s.push(root);
        while (!s.empty()) {
            auto node = s.top(); s.pop();
            if (!node) continue;
            res.push_back(node->val);
            s.push(node->right);
            s.push(node->left);
        }
        return res;
    }
};
```

## 日期

2017 年 5 月 20 日 
2019 年 1 月 25 日 —— 这学期最后一个工作日
2019 年 9 月 20 日 —— 是选择中国互联网式加班？还是外企式养生？

  [1]: https://leetcode.com/problems/binary-tree-preorder-traversal/#/description
