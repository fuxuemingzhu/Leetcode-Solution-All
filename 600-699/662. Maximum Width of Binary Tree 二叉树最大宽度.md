# 【LeetCode】662. Maximum Width of Binary Tree 解题报告（Python）

标签（空格分隔）： LeetCode

---

题目地址：https://leetcode.com/problems/maximum-width-of-binary-tree/description/

## 题目描述：

Given a binary tree, write a function to get the maximum width of the given tree. The width of a tree is the maximum width among all levels. The binary tree has the same structure as a full binary tree, but some nodes are null.

The width of one level is defined as the length between the end-nodes (the leftmost and right most non-null nodes in the level, where the null nodes between the end-nodes are also counted into the length calculation.

    Example 1:
    Input: 
    
               1
             /   \
            3     2
           / \     \  
          5   3     9 
    
    Output: 4
    Explanation: The maximum width existing in the third level with the length 4 (5,3,null,9).
    
    Example 2:
    Input: 
    
              1
             /  
            3    
           / \       
          5   3     
    
    Output: 2
    Explanation: The maximum width existing in the third level with the length 2 (5,3).
    
    Example 3:
    Input: 
    
              1
             / \
            3   2 
           /        
          5      
    
    Output: 2
    Explanation: The maximum width existing in the second level with the length 2 (3,2).
    
    Example 4:
    Input: 
    
              1
             / \
            3   2
           /     \  
          5       9 
         /         \
        6           7
    Output: 8
    Explanation:The maximum width existing in the fourth level with the length 8 (6,null,null,null,null,null,null,7).


Note: Answer will in the range of 32-bit signed integer.
    
## 题目大意

给定二叉树，求二叉树的最大宽度。二叉树某层的宽度是指其最左非空节点与最右非空节点之间的跨度。


## 解题方法

做法是层次遍历 + 完全二叉树的节点位置性质。这个性质指的是，每层都有 2 ^ (n-1)个节点。某节点的左孩子的标号是2n, 右节点的标号是2n + 1。因为这个题，中间缺少了节点的话，仍然要“认为”节点存在，所以需要使用这种标号的方法强制计算，而不是直接遍历。

遍历的方式是使用队列，其实很简单了。

代码：

```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def widthOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        queue = collections.deque()
        queue.append((root, 1))
        res = 0
        while queue:
            width = queue[-1][1] - queue[0][1] + 1
            res = max(width, res)
            for _ in range(len(queue)):
                n, c = queue.popleft()
                if n.left: queue.append((n.left, c * 2))
                if n.right: queue.append((n.right, c * 2 + 1))
        return res
```

## 日期

2018 年 3 月 21 日 ———— 啊，耽误了一天没刷题。。


  [1]: http://blog.csdn.net/fuxuemingzhu/article/details/51291406