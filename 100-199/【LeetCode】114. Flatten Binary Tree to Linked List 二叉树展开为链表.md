作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)

题目地址：[https://leetcode.com/problems/flatten-binary-tree-to-linked-list/#/description][1]


## 题目描述

Given a binary tree, flatten it to a linked list in-place.

For example,

Given

         1
        / \
       2   5
      / \   \
     3   4   6
The flattened tree should look like:

       1
        \
         2
          \
           3
            \
             4
              \
               5
                \
                 6

## 题目大意

把一个二叉树拉直，即按照先序遍历的顺序形成一个只有右孩子的二叉树。

## 解题方法

### 先序遍历

最简单的方法就是使用列表保存先序遍历的每个节点，然后在列表中完成操作。即，使得列表中每个元素的左孩子为空，右孩子都是下一个节点。

这个方法很简单，不过需要O(N)的空间复杂度。

python代码如下：

```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        res = []
        self.preOrder(root, res)
        for i in range(len(res) - 1):
            res[i].left = None
            res[i].right = res[i + 1]
    
    def preOrder(self, root, res):
        if not root: return
        res.append(root)
        self.preOrder(root.left, res)
        self.preOrder(root.right, res)
```

### 递归

递归一定要明白递归函数的意义，我觉得如果不清楚的弄明白递归函数的输入和输出是什么，那么不可能写出正确的代码。

这里的flatten(root)的输入是一个树的根节点，这个函数将使得该根节点下的所有孩子按照先序遍历的顺序放到其右侧。返回是空，但是这个函数运行结束后，root的指向仍然是原来的位置，即树的根节点。

所以，递归的思路就有了：把左右子树分别flatten形成两个链表，然后把根节点的左孩子放到根节点的右孩子上。把原先的根节点的右孩子拼到当前根节点链表的结尾。

图形化说明：

         1
        / \
       2   5
      / \   \
     3   4   6

变成：

         1
          \
       2   5
        \   \
     3   4   6
2是root,3是left,4是right。修改成下面这样：

再变成：

         1
          \
       2   5
        \   \
         3   6
          \   
           4       
再变成：

         1
          \   
           2   
            \   
             3   
              \   
               4    
                \
                 5
                  \
                   6

python代码：

```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        if not root: return
        left = root.left
        right = root.right
        root.left = None
        self.flatten(left)
        self.flatten(right)
        root.right = left
        cur = root
        while root.right:
            root = root.right
        root.right = right
```

C++代码：

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
    void flatten(TreeNode* root) {
        if (!root) return;
        TreeNode* left = root->left;
        TreeNode* right = root->right;
        root->left = nullptr;
        flatten(left);
        flatten(right);
        root->right = left;
        TreeNode* cur = root;
        while (cur->right)
            cur = cur->right;
        cur->right = right;
    }
};
```

Java代码：

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
    public void flatten(TreeNode root) {
        if(root == null){
            return;
        }
        TreeNode left = root.left;
        TreeNode right = root.right;
        root.left = null;
        flatten(left);
        flatten(right);
        root.right = left;
        TreeNode cur = root;
        while(cur.right != null){
            cur = cur.right;
        }
        cur.right = right;
    }
}
```

## 日期

2017 年 4 月 19 日 
2019 年 1 月 7 日 —— 新的一周开始啦啦啊

  [1]: https://leetcode.com/problems/flatten-binary-tree-to-linked-list/#/description
