作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)


题目地址：https://leetcode.com/problems/check-completeness-of-a-binary-tree/


## 题目描述

Given a binary tree, determine if it is a complete binary tree.

Definition of a complete binary tree from Wikipedia:

- In a complete binary tree every level, except possibly the last, is completely filled, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.

 

Example 1:

![此处输入图片的描述][1]

    Input: [1,2,3,4,5,6]
    Output: true
    Explanation: Every level before the last is full (ie. levels with node-values {1} and {2, 3}), and all nodes in the last level ({4, 5, 6}) are as far left as possible.

Example 2:

![此处输入图片的描述][2]

    Input: [1,2,3,4,5,null,7]
    Output: false
    Explanation: The node with value 7 isn't as far left as possible.
 
Note:

1. The tree will have between 1 and 100 nodes.

## 题目大意

判断一个二叉树是不是完全二叉树。


## 解题方法

### BFS

这个题可以使用DFS或者BFS先找出二叉树的层次遍历。之后的判断中，使用DFS比较麻烦一些。

使用BFS的话层次遍历比较简单，因为我们从每层的从左到右进行遍历，如果某一层已经出现None之后，后面还有非空叶子节点的话，那么就不是完全二叉树。

代码如下：

```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isCompleteTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root: return True
        res = []
        que = collections.deque()
        que.append(root)
        hasNone = False
        while que:
            size = len(que)
            for i in range(size):
                node = que.popleft()
                if not node:
                    hasNone = True
                    continue
                if hasNone:
                    return False
                que.append(node.left)
                que.append(node.right)
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
    bool isCompleteTree(TreeNode* root) {
        queue<TreeNode*> q;
        q.push(root);
        while (!q.empty()) {
            TreeNode* node = q.front(); q.pop();
            if (!node) break;
            q.push(node->left);
            q.push(node->right);
        }
        while (!q.empty()) {
            TreeNode* node = q.front(); q.pop();
            if (node)
                return false;
        }
        return true;
    }
};
```

### DFS

思路是，除了最后一层之外，其余的层必须都是满二叉树，最后一层左边只能全部是非空叶子节点，如果出现None之后，后面不能再有非空叶子节点了。


```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isCompleteTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root: return True
        res = []
        self.getlevel(res, 0, root)
        depth = len(res) - 1
        for d in range(depth):
            if d != depth - 1:
                if None in res[d] or len(res[d]) != (2 ** d):
                    return False
            else:
                ni = -1
                for i, n in enumerate(res[d]):
                    if n == None:
                        if ni == -1:
                            ni = i
                    else:
                        if ni != -1:
                            return False
        return True
                

    def getlevel(self, res, level, root):
        if level >= len(res):
            res.append([])
        if not root:
            res[level].append(None)
        else:
            res[level].append(root.val)
            self.getlevel(res, level + 1, root.left)
            self.getlevel(res, level + 1, root.right)
```



## 日期

2018 年 12 月 16 日 —— 周赛好难


  [1]: https://assets.leetcode.com/uploads/2018/12/15/complete-binary-tree-1.png
  [2]: https://assets.leetcode.com/uploads/2018/12/15/complete-binary-tree-2.png
  [3]: https://zxi.mytechroad.com/blog/wp-content/uploads/2018/12/952-ep232.png
