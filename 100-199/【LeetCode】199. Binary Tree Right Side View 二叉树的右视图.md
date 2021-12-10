# 【LeetCode】199. Binary Tree Right Side View 解题报告（Python）

标签： LeetCode

---

题目地址：https://leetcode.com/problems/binary-tree-right-side-view/description/

## 题目描述：

Given a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

    For example:
    Given the following binary tree,
    
       1            <---
     /   \
    2     3         <---
     \     \
      5     4       <---
    
    You should return [1, 3, 4].


## 题目大意

打印出二叉树每层的最右边的元素。

## 解题方法

这个题就是[102. Binary Tree Level Order Traversal][1]翻版啊！上个题是要直接打印每层的元素，这个是要每层元素的最右边元素，所以可以使用之前的解法，然后再把每层的给取出来嘛～～

递归解法：

```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        self.levelOrder(root, 0, res)
        return [level[-1] for level in res]
        
    def levelOrder(self, root, level, res):
        if not root: return
        if len(res) == level: res.append([])
        res[level].append(root.val)
        if root.left: self.levelOrder(root.left, level + 1, res)
        if root.right: self.levelOrder(root.right, level + 1, res)
```

非递归解法，使用队列。

这个解题的技巧在于，queue其实也可以用[-1]直接找到这个层的最后一个元素。

每次进行while循环，都是开始了新的一层，for循环的巧妙在于，直接遍历队列中已有的元素，也就是上层的元素。这样的话就直接把上层的遍历完了，新的层也加入了队列。

```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        if not root: return res
        queue = collections.deque()
        queue.append(root)
        while queue:
            res.append(queue[-1].val)
            for i in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return res
```

## 日期

2018 年 3 月 14 日 --霍金去世日


  [1]: http://blog.csdn.net/fuxuemingzhu/article/details/49102937