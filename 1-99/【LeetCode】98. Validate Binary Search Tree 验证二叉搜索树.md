
作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)


题目地址：[https://leetcode.com/problems/validate-binary-search-tree/#/description][1]


## 题目描述

Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

 - The left subtree of a node contains only nodes with keys less than the node's key.
 - The right subtree of a node contains only nodes with keys greater than the node's key.
 - Both the left and right subtrees must also be binary search trees.

Example 1:

	Input:
	    2
	   / \
	  1   3
	Output: true

Example 2:

	    5
	   / \
	  1   4
	     / \
	    3   6
	Output: false
	Explanation: The input is: [5,1,4,null,null,3,6]. The root node's value
	             is 5 but its right child's value is 4.

## 题目大意
判断一棵树是不是BST。

## 解题方法

### 递归

很显然，二叉树的题目可以使用递归进行解决。

根据BST的定义，左子树的值要在(min,mid)之间，右子树的值在(mid,max)之间，这个mid值并不是中位数而是当前节点的值。

定义一个辅助函数，要给这个辅助函数传入当前要判断的节点，当前要判断的这个节点的取值下限和取值上限。然后使用递归即可，每次要计算下一个节点的时候都要根据这个节点是左孩子还是右孩子对其取值的区间进行更新。

```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.valid(root, float('-inf'), float('inf'))
        
    def valid(self, root, min, max):
        if not root: return True
        if root.val >= max or root.val <= min:
            return False
        return self.valid(root.left, min, root.val) and self.valid(root.right, root.val, max)
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
    bool isValidBST(TreeNode* root) {
        if (!root)
            return true;
        return helper(root, LONG_MIN, LONG_MAX);
    }
    
    bool helper(TreeNode* root, long minVal, long MaxVal) {
        if (!root)
            return true;
        if (root->val >= MaxVal || root->val <= minVal)
            return false;
        return helper(root->left, minVal, root->val) && helper(root->right, root->val, MaxVal);
    }
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
    public boolean isValidBST(TreeNode root) {
        return isValid(root, Long.MIN_VALUE, Long.MAX_VALUE);
    }
    public boolean isValid(TreeNode root, long min, long max){
        if(root == null){
            return true;
        }
        long mid = root.val;
        if(mid <= min || mid >= max){
            return false;
        }
        return isValid(root.left, min, mid) && isValid(root.right, mid, max);
    }
}
```

### BST的中序遍历是有序的

众所周知，BST最重要的性质就是：BST的中序遍历是有序的。所以这个题能不能通过这个性质来解决呢？答案是肯定的。

也就是说，已知一个二叉树的中序遍历是有序的，能判断这个二叉树是BST吗？加上一个条件就可以，这个条件就是该中序遍历不能包含重复元素。

准确的证明我没想好，不过我们可以想象一下，中序遍历不就是左孩子－根节点－右孩子的这个顺序遍历么，如果每个子树都满足左孩子<根节点<右孩子，那就应该是个BST吧。

python代码如下：

```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        res = []
        self.inOrder(root, res)
        return res == sorted(res) and len(res) == len(set(res))
        
    def inOrder(self, root, res):
        if not root: return []
        l = self.inOrder(root.left, res)
        if l:
            res.extend(l)
        res.append(root.val)
        r = self.inOrder(root.right, res)
        if r:
            res.extend()
```

下面是C++对这个题的解法，并没有使用上面python的做法，而是用一个变量维护前面遍历到的节点，在BST的中序遍历中，每个位置的元素都应该大于前面遍历到的节点。代码如下：

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
    bool isValidBST(TreeNode* root) {
        prev_ = nullptr;
        return inOrder(root);
    }
private:
    TreeNode* prev_;
    bool inOrder(TreeNode* root) {
        if (!root) return true;
        if (!inOrder(root->left)) return false;
        if (prev_ && root->val <= prev_->val) return false;    
        prev_ = root;
        return inOrder(root->right);
    }
};
```

参考资料：http://zxi.mytechroad.com/blog/tree/leetcode-98-validate-binary-search-tree/

## 日期

2017 年 4 月 17 日 
2018 年 3 月 23 日 —— 科目一考了100分哈哈哈哈～嗝～
2019 年 1 月 19 日 —— 有好几天没有更新文章了

  [1]: https://leetcode.com/problems/validate-binary-search-tree/#/description
