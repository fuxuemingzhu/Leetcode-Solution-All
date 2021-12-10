
作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)

题目地址：[https://leetcode.com/problems/binary-tree-tilt/#/description][1]


## 题目描述

Given a binary tree, return the tilt of the whole tree.

The tilt of a tree node is defined as the absolute difference between the sum of all left subtree node values and the sum of all right subtree node values. Null node has tilt 0.

The tilt of the whole tree is defined as the sum of all nodes' tilt.

Example 1:

    Input: 
             1
           /   \
          2     3
    Output: 1
    Explanation: 
    Tilt of node 2 : 0
    Tilt of node 3 : 0
    Tilt of node 1 : |2-3| = 1
    Tilt of binary tree : 0 + 0 + 1 = 1

Note:

 1. The sum of node values in any subtree won't exceed the range of 32-bit integer.
 2. All the tilt values won't exceed the range of 32-bit integer.

## 题目大意

找根节点左右子树的差值的和。

## 解题方法

### Java解法

这个题很容易想到dfs，但是怎么写呢。这个用到的是``后序遍历``，用一个res来保存左右差的结果，函数的返回值是左右子树的和加上根节点的值。这样统计之后就能求出所有左右子树的和的差值。

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
    int res = 0;
    public int findTilt(TreeNode root) {
        postOrder(root);
        return res;
    }
    public int postOrder(TreeNode root){
        if(root == null){
            return 0;
        }
        int left = postOrder(root.left);
        int right = postOrder(root.right);
        res += Math.abs(left - right);
        return left + right + root.val;
    }
}
```

### Python解法

定义的后序遍历函数返回的值是左右子树的差。如果明白了这个定义之后就知道了，我们需要一个变量，在遍历的过程中求差的和。

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findTilt(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.sums = 0
        self.postOrder(root)
        return self.sums
    
    def postOrder(self, root):
        if not root:
            return 0
        left = self.postOrder(root.left)
        right = self.postOrder(root.right)
        self.sums += abs(left - right)
        return left + right + root.val
```

## 日期

2017 年 5 月 9 日 
2018 年 11 月 16 日 —— 又到周五了！

  [1]: https://leetcode.com/problems/binary-tree-tilt/#/description
