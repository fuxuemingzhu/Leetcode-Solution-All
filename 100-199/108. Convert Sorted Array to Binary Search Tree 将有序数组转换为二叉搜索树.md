
作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)

题目地址：[https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/#/description][1]


## 题目描述

Given an array where elements are sorted in ascending order, convert it to a height balanced BST.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

Example:

	Given the sorted array: [-10,-3,0,5,9],
	
	One possible answer is: [0,-3,9,-10,null,5], which represents the following height balanced BST:
	
	      0
	     / \
	   -3   9
	   /   /
	 -10  5

## 题目大意

把一个已经排序了的数组，变成一个高度平衡的BST。答案不唯一。

## 解题方法

### Java解法

因为BST的中序遍历是有序的，所以有序数组的中间的数字是根节点，序列中间节点左边是根节点的左子树，右边是根节点的右子树，以此类推。

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
    public TreeNode sortedArrayToBST(int[] nums) {
        return helper(nums, 0, nums.length - 1);
    }
    
    public TreeNode helper(int[] nums, int start, int end){
        if(start > end){
            return null;
        }
        int mid = (start + end) / 2;
        TreeNode node = new TreeNode(nums[mid]);
        node.left = helper(nums, start, mid - 1);
        node.right = helper(nums, mid + 1, end);
        return node;
    }
}
```

### Python解法

二刷，python

用python2的时候，最后有个特别大的测试用例，导致内存错误。。

改成Python3，并把除法改成了地板除竟然过了。。神奇。

```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums: return None
        _len = len(nums)
        mid = _len // 2
        root = TreeNode(nums[mid])
        root.left = self.sortedArrayToBST(nums[:mid])
        root.right = self.sortedArrayToBST(nums[mid+1:])
        return root
```


## 日期

2017 年 4 月 24 日 
2018 年 6 月 23 日
2018 年 11 月 16 日 —— 又到周五了！

  [1]: https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/#/description
