
作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)

题目地址：[https://leetcode.com/problems/minimum-absolute-difference-in-bst/#/description][1]


## 题目描述


Given a binary search tree with non-negative values, find the minimum absolute difference between values of any two nodes.

Example:

	Input:
	
	   1
	    \
	     3
	    /
	   2
	
	Output:
	1

	Explanation:
	The minimum absolute difference is 1, which is the difference between 2 and 1 (or between 2 and 3).
	 

Note: There are at least two nodes in this BST.

## 题目大意    

判断一个BST中任意两个节点之间的差的绝对值的最小值。

## 解题方法

### Java解法

找出BST中两个节点的最小差距值。

第一遍没有思路，第二次看就想到了中序遍历，BST的中序遍历是有序。应该可以通过数组保存的形式，但是看了别人的做法，发现直接用个外部的变量就能保存最小的值。另外还要一个prev保存上一个节点。

为什么是当前的值-上一个节点的值呢？因为我们的遍历是有序的，所以当前节点比前一个节点大，这样相减就可以保证结果是正的。

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
    int minDiff = Integer.MAX_VALUE;
    TreeNode prev = null;
    
    public int getMinimumDifference(TreeNode root) {
        inOrder(root);
        return minDiff;
    }

    public void inOrder(TreeNode root){
        if(root == null){
            return;
        }
        inOrder(root.left);
        if(prev !=null) minDiff= Math.min(minDiff, root.val - prev.val);
        prev = root;
        inOrder(root.right);
    }
}
```

### Python解法

二刷，python。

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.res = float("inf")
        self.prev = None
        self.inOrder(root)
        return self.res

    def inOrder(self, root):
        if not root: return
        self.inOrder(root.left)
        if self.prev:
            self.res = min(self.res, root.val - self.prev.val)
        self.prev = root
        self.inOrder(root.right)
```

## 日期

2017 年 4 月 8 日 
2018 年 11 月 14 日 —— 很严重的雾霾

  [1]: https://leetcode.com/problems/minimum-absolute-difference-in-bst/#/description
