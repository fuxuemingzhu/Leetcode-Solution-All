
作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)

题目地址：[https://leetcode.com/problems/find-mode-in-binary-search-tree/#/description][1]


## 题目描述

Given a binary search tree (BST) with duplicates, find all the mode(s) (the most frequently occurred element) in the given BST.

Assume a BST is defined as follows:

- The left subtree of a node contains only nodes with keys less than or equal to the node's key.
- The right subtree of a node contains only nodes with keys greater than or equal to the node's key.
- Both the left and right subtrees must also be binary search trees.

For example:

	Given BST [1,null,2,2],
	
	   1
	     \
	      2
	     /
	    2
	
	return [2].

Note: If a tree has more than one mode, you can return them in any order.

Follow up: Could you do that without using any extra space? (Assume that the implicit stack space incurred due to recursion does not count).

## 题目大意

找出一个BST中出现次数最多的节点们。

## 解题方法

见到BST就想到中序遍历。这个题中的BST是可以包含相同的元素的，题目的要求就是找出相同的元素出现次数最多的是哪几个。那么就可以先进行中序遍历得到有序的排列，如果两个相邻的元素相同，那么这个就是连续的，找出连续最多的即可。题目思路就是BST的中序遍历加上最长连续相同子序列。

如果使用附加空间的话，可以使用hash保存每个节点出现的次数。

```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root: return []
        self.count = collections.Counter()
        self.inOrder(root)
        freq = max(self.count.values())
        res = []
        for item, c in self.count.items():
            if c == freq:
                res.append(item)
        return res
        
    def inOrder(self, root):
        if not root:
            return 
        self.inOrder(root.left)
        self.count[root.val] += 1
        self.inOrder(root.right)
```

题目建议不要用附加空间hash等，方法是计算了两次，一次是统计最大的模式出现的次数，第二次的时候构建出来了数组，然后把出现次数等于最大模式次数的数字放到数组的对应位置。

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
    public int[] findMode(TreeNode root) {
        inOrder(root);
        modes = new int[modeCount];
        currCount = 0;
        modeCount = 0;
        inOrder(root);
        return modes;
    }
    
    int currVal = 0;
    int currCount = 0;
    int maxCount = 0;
    int modeCount = 0;
    
    int[] modes;
    
    public void handleValue(int val){
        if(currVal != val){
            currVal = val;
            currCount = 0;
        }
        currCount++;
        if(currCount > maxCount){
            maxCount = currCount;
            modeCount = 1;
        }else if (currCount == maxCount){
            if(modes != null){
                modes[modeCount] = currVal;
            }
            modeCount++;
        }
    }
    
    public void inOrder(TreeNode root){
        if(root == null){
            return;
        }
        inOrder(root.left);
        handleValue(root.val);
        inOrder(root.right);
    }
}
```

## 日期

2017 年 5 月 3 日 
2018 年 11 月 23 日 —— 这就星期五了？？

  [1]: https://leetcode.com/problems/find-mode-in-binary-search-tree/#/description
