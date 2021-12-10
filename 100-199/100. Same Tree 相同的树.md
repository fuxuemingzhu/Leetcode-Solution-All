作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)

[LeetCode]

题目地址：[https://leetcode.com/problems/same-tree/](https://leetcode.com/problems/same-tree/)

Total Accepted: 126017 Total Submissions: 291619 Difficulty: Easy


## 题目描述

Given two binary trees, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical and the nodes have the same value.

Example 1:

	Input:     1         1
	          / \       / \
	         2   3     2   3
	
	        [1,2,3],   [1,2,3]
	
	Output: true

Example 2:

	Input:     1         1
	          /           \
	         2             2
	
	        [1,2],     [1,null,2]
	
	Output: false

Example 3:

	Input:     1         1
	          / \       / \
	         2   1     1   2
	
	        [1,2,1],   [1,1,2]
	
	Output: false

## 题目大意

判断两棵二叉树是否完全相等。

## 解题方法


这道题是树的题目，属于最基本的树遍历的问题。

问题要求就是判断两个树是不是一样，基于先序，中序或者后序遍历都可以做完成，因为对遍历顺序没有要求。

这里我们主要考虑一下结束条件，如果两个结点都是null，也就是到头了，那么返回true。如果其中一个是null，说明在一棵树上结点到头，另一棵树结点还没结束，即树不相同，或者两个结点都非空，并且结点值不相同，返回false。最后递归处理两个结点的左右子树，返回左右子树递归的与结果即可。

这里使用的是先序遍历，算法的复杂度跟遍历是一致的，如果使用递归，时间复杂度是O(n)，空间复杂度是O(logn)。代码如下：

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
    public boolean isSameTree(TreeNode p, TreeNode q) {
        if(p==null && q==null){
            return true;
        }
        if(p==null || q==null){//注意是在p/q都不为空的情况下有一个为空，说明另外一个不为空
            return false;
        }
        if(p.val!=q.val){//注意是不相等返回False，相等的话需要继续进行子节点的判断
            return false;
        }
        return isSameTree(p.left,q.left) && isSameTree(p.right,q.right);
    }
}
```
AC:0ms

递归问题最终要的是终止条件！！！一定要万无一失。

----

二刷，python。

两年前的我竟然写了这么多啊，现在写一个Python版本的。

```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if not p and not q:
            return True
        if not p or not q:
            return False
        return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
```


## 日期

2016/4/30 1:17:33 
2018 年 10 月 8 日 —— 终于开学了。
2018 年 11 月 14 日 —— 很严重的雾霾
