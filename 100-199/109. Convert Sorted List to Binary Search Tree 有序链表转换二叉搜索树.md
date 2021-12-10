# 【LeetCode】109. Convert Sorted List to Binary Search Tree 解题报告（Python）

标签（空格分隔）： LeetCode

作者： 		负雪明烛 
id：				fuxuemingzhu
个人博客：	http://fuxuemingzhu.me/

---

题目地址：https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree/description/

## 题目描述：

Given a singly linked list where elements are sorted in ascending order, convert it to a height balanced BST.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

Example:

Given the sorted linked list: [-10,-3,0,5,9],

One possible answer is: [0,-3,9,-10,null,5], which represents the following height balanced BST:

          0
         / \
       -3   9
       /   /
     -10  5

## 题目大意

把一个单链表转成二叉平衡树。二叉平衡树是左右子树的高度差最多为1.

## 解题方法

这个题目和[108. Convert Sorted Array to Binary Search Tree][1]基本一模一样啊！所以毫无疑问地，我把链表转成了数组，然后再用108题的做法就过了。

而且这个题神奇的地方在于，使用python2超时，但是使用Python3就通过了。以后还是尽量用python3比较好吧。。

哦对，python3要用地板除。

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        nums = []
        while head:
            nums.append(head.val)
            head = head.next
        return self.helper(nums)
        
    def helper(self, nums):
        if not nums: return None
        _len = len(nums)
        mid = _len // 2
        root = TreeNode(nums[mid])
        root.left = self.helper(nums[:mid])
        root.right = self.helper(nums[mid+1:])
        return root
```

## 日期

2018 年 6 月 23 日 ———— 美好的周末要从刷题开始


  [1]: https://blog.csdn.net/fuxuemingzhu/article/details/70665213