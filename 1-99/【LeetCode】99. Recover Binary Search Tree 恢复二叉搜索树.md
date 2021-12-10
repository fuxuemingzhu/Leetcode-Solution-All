# 【LeetCode】99. Recover Binary Search Tree 解题报告（Python）

标签（空格分隔）： LeetCode

---

题目地址：https://leetcode.com/problems/recover-binary-search-tree/description/

## 题目描述：

Two elements of a binary search tree (BST) are swapped by mistake.

Recover the tree without changing its structure.

Note:
A solution using O(n) space is pretty straight forward. Could you devise a constant space solution?

    
## 题目大意

删除二叉树中指定一节点，并调整二叉树，使得结果的二叉树仍然满足BST的条件。

## 解题方法

同学们，看到BST就想什么？对，中序遍历是有序的。

那么，如果其中两个被交换了，那么中序遍历的结果一定也就不对了。比如：

    [1, 2, 3, 4, 5, 6]  ==>  [1, 5, 3, 4, 2, 6]

那么，可以看出5这个数字比后面的3大，说明他被打乱了；另外2这个数字，比前面的数字4小，所以他也被打乱了。

所以，可以通过先进行中序遍历得到所有的，然后再查找哪些乱了，再复原，时间复杂度O(n)。

但是，中序遍历的操作不需要完全完成。在中序遍历的过程中，用一个指针保存上个节点，那么当前节点值应该小于前一个节点的值。否则就存在乱序。

第一个乱序的数字是pre，第二个乱序的数字是root，所以用两个指针分别保存。

代码：

```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        self.pre, self.first, self.second = None, None, None
        self.inOrder(root)
        self.first.val, self.second.val = self.second.val, self.first.val

    def inOrder(self, root):
        if not root: return
        self.inOrder(root.left)
        if self.pre and self.pre.val > root.val:
            if not self.first:
                self.first = self.pre
            self.second = root
        self.pre = root
        self.inOrder(root.right)
```

## 日期

2018 年 3 月 23 日 ———— 科目一考了100分哈哈哈哈～嗝～


  [1]: http://blog.csdn.net/fuxuemingzhu/article/details/51291406