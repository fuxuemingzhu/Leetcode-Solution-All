作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)

[LeetCode]

题目地址：[https://leetcode.com/problems/symmetric-tree/][1]

Total Accepted: 106639 Total Submissions: 313969 Difficulty: Easy


## 题目描述

Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

	    1
	   / \
	  2   2
	 / \ / \
	3  4 4  3

But the following [1,2,2,null,3,null,3] is not:

	    1
	   / \
	  2   2
	   \   \
	   3    3
Note:

1. Bonus points if you could solve it both recursively and iteratively.

## 题目大意

判断一棵二叉树是不是镜像二叉树。

## 解题方法

### DFS

如果一个树是对称的，那么意味着左右子树是镜像的。就像判断回文一样，每层的 左右两边对称位置 的节点是镜像的。


			     1
			   /   \
	  left->  2     2  <-right
			 / \   / \
			3   4  4  3


定义新函数`isMirror(left, right)`，该函数的意义是判断`left` 和 `right`是不是对称的子树。
1. 当`left` 和 `right`的值相等的时候，需要判断下一层是否是对称的。
3. 在递归判断下一层的时候的时候，需要判断的是 `left.left` 和 `right.right`这两棵树是不是对称的，以及 `left.right`和`right.left` 这两棵树是不是对称的。

代码只是上面的思路的实现，可以用递归来完成。递归最重要的是 要明白函数的定义、输入、输出，如果这些没明白一定会把自己绕进去。另外递归的时候应该把递归函数当做黑盒使用，即不需要知道此函数内部怎么实现的，但是调用这个递归函数就是能达到某个功能。这样会帮助理解递归。

本题提醒了我们：在递归的过程中不一定只有一个参数，也可以同时传了两个参数，每次递归的时候同时改变两个采纳数。

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
    public boolean isSymmetric(TreeNode root) {
        return isMirror(root,root);
    }
    
    public boolean isMirror(TreeNode left,TreeNode right){
        if(left == null && right == null)   return true;
        if(left == null || right == null)   return false;
        return (left.val == right.val) && isMirror(left.left,right.right) && isMirror(left.right,right.left);
    }
}
```
AC:1ms

二刷的时候写的Python解法如下：

```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root: return True
        return self.isMirror(root.left, root.right)
        
    def isMirror(self, left, right):
        if not left and not right: return True
        if not left or not right: return False
        return left.val == right.val and self.isMirror(left.left, right.right) and self.isMirror(left.right, right.left)
```

### BFS

BFS 使用一个队列，把要判断是否为镜像的节点放在一起。

在队列中同时取出两个节点`left, right`，判断这两个节点的值是否相等，然后把他们的孩子中按照`(left.left, right.right)` 一组，`(left.right, right.left)`一组放入队列中。

BFS做法需要把所有的节点都检查完才能确定返回结果`True`，除非提前遇到不同的节点值而终止返回`False`。

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
    public boolean isSymmetric(TreeNode root) {
        Queue<TreeNode> q = new LinkedList<>();
        q.add(root);
        q.add(root);
        while(!q.isEmpty()){
            TreeNode left=q.poll();
            TreeNode right=q.poll();
            if(left==null && right==null)   continue;
            if(left==null || right==null)   return false;
            if(left.val != right.val)   return false;
            q.add(left.left);
            q.add(right.right);
            q.add(left.right);
            q.add(right.left);
        }
        return true;
    }
    
}
```

AC:3ms

二刷的时候的Python解法如下：

```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root: return True
        que = collections.deque()
        que.append(root.left)
        que.append(root.right)
        while que:
            left, right = que.popleft(), que.popleft()
            if not left and not right:
                continue
            if not left or not right:
                return False
            if left.val != right.val:
                return False
            que.append(left.left)
            que.append(right.right)
            que.append(left.right)
            que.append(right.left)
        return True
```

一种便于理解的BFS做法，把要判断的是否对称节点作为tuple一起放入队列中：

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        queue = collections.deque()
        queue.append((root, root))
        while queue:
            left, right = queue.popleft()
            if not left and not right:
                continue
            if not left or not right:
                return False
            if left.val != right.val:
                return False
            queue.append((left.left, right.right))
            queue.append((left.right, right.left))
        return True
```

## 日期

2016 年 05月 8日 
2018 年 11 月 19 日 —— 周一又开始了
2020 年 5 月 31 日 —— 准备组织每日一题的分享

  [1]: https://leetcode.com/problems/symmetric-tree/
