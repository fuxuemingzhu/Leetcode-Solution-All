
作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)


[LeetCode]

题目地址：[https://leetcode.com/problems/sum-of-left-leaves/][1]

 - Difficulty: Easy

## 题目大意

Find the sum of all left leaves in a given binary tree.

    Example:

        3
       / \
      9  20
        /  \
       15   7
    
    There are two left leaves in the binary tree, with values 9 and 15 respectively. Return 24.

## 题目大意

求一个二叉树中所有的左叶子节点的和。

## 解题方法

### 递归

Java解法是这样的。

这个方法很直白很简单，用递归判断是不是左叶子，然后求和即可。我的第一次A过的代码是这样的。

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
    int sum=0;
    public int sumOfLeftLeaves(TreeNode root) {
        if(root==null){
            return 0;
        }
        if(root.left!=null){
            if(root.left.left==null && root.left.right==null){//根的左边节点是叶子
                sum += root.left.val;//加上左叶子的值
            }
            sumOfLeftLeaves(root.left);//循环左叶子
        }
        if(root.right!=null){
            sumOfLeftLeaves(root.right);//循环右叶子
        }

        return sum;
    }
}
```
AC：8 ms

看了高票解答之后，感觉自己还可以精简下代码。如下。

```java
public class Solution {
    public int sumOfLeftLeaves(TreeNode root) {
        if(root==null){
            return 0;
        }
        int sum=0;
        if(root.left!=null){
            if(root.left.left==null && root.left.right==null){
                sum += root.left.val;
            }else{
                sum += sumOfLeftLeaves(root.left);
            }
        }
        
        sum += sumOfLeftLeaves(root.right);

        return sum;
    }
}
```

AC:9 ms

Python解法是这样的。

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root: return 0
        self.sum = 0
        self.inOrder(root)
        return self.sum

    def inOrder(self, root):
        if not root: return 
        if root.left:
            self.inOrder(root.left)
            if not root.left.left and not root.left.right:
                self.sum += root.left.val
        if root.right:
            self.inOrder(root.right)
```

### 迭代

对于树的问题，一般都可以使用递归和迭代两种解法。这个题用迭代的话，需要用栈，总体代码和递归基本一样的。

Python解法如下：

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root: return 0
        stack = []
        stack.append(root)
        leftsum = 0
        while stack:
            node = stack.pop()
            if not node: continue
            if node.left:
                if not node.left.left and not node.left.right:
                    leftsum += node.left.val
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return leftsum
```

## 日期

2017 年 1 月 7 日 
2018 年 11 月 14 日 —— 很严重的雾霾

  [1]: https://leetcode.com/problems/sum-of-left-leaves/
