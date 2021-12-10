作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)

题目地址：https://leetcode.com/problems/binary-tree-pruning/description/

## 题目描述

We are given the head node root of a binary tree, where additionally every node's value is either a 0 or a 1.

Return the same tree where every subtree (of the given tree) not containing a 1 has been removed.

(Recall that the subtree of a node X is X, plus every node that is a descendant of X.)

Example 1:

    Input: [1,null,0,0,1]
    Output: [1,null,0,null,1]
![此处输入图片的描述][1]
     
    Explanation: 
    Only the red nodes satisfy the property "every subtree not containing a 1".
    The diagram on the right represents the answer.
    
    
    Example 2:
    Input: [1,0,1,0,0,0,1]
    Output: [1,null,1,null,1]
    
![此处输入图片的描述][2]
    
    Example 3:
    Input: [1,1,0,1,1,0,1,0]
    Output: [1,1,0,1,1,null,1]
    
![此处输入图片的描述][3]

Note:

1. The binary tree will have at most 100 nodes.
1. The value of each node will only be 0 or 1.


## 题目大意

把一棵树的所有不含1的子树都删除。子树的定义是自身节点和所有子节点。

## 解题方法

### 后序遍历

这个题一看还是dfs啊～习惯了新定义一个函数dfs了，但这次不需要了。我们直接把节点的左孩子和右孩子重新设置就好了。这个题是后序遍历！

一定要注意的是，**我们判断这个节点是叶子节点并且节点值是1的这个步骤要放在左右子树处理之后**。可以从Example2中看出来，如果0节点的左右子节点都是0，那么把左右节点都减去了之后，还要判断自身是不是0，然后把自己也剪了。也就是说这一步相当于后序遍历，把孩子都处理结束之后，然后再处理自身。

```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pruneTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root: return
        root.left = self.pruneTree(root.left)
        root.right = self.pruneTree(root.right)
        if not root.left and not root.right and root.val == 0:
            return None
        return root
```

C++版本代码如下：

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
    TreeNode* pruneTree(TreeNode* root) {
        if (!root) return nullptr;
        root->left = pruneTree(root->left);
        root->right = pruneTree(root->right);
        if (!root->left && !root->right)
            return root->val == 1 ? root : nullptr;
        return root;
    }
};
```

## 日期

2018 年 4 月 8 日 —— 网吧通宵了，然后睡了一天。。
2018 年 11 月 5 日 —— 打了羽毛球，有点累
2018 年 12 月 2 日 —— 又到了周日

  [1]: https://s3-lc-upload.s3.amazonaws.com/uploads/2018/04/06/1028_2.png
  [2]: https://s3-lc-upload.s3.amazonaws.com/uploads/2018/04/06/1028_1.png
  [3]: https://s3-lc-upload.s3.amazonaws.com/uploads/2018/04/05/1028.png
