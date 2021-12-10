
作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)

题目地址：[https://leetcode.com/problems/two-sum-iv-input-is-a-bst/description/][1]


## 题目描述

Given a Binary Search Tree and a target number, return true if there exist two elements in the BST such that their sum is equal to the given target.

Example 1:

    Input: 
        5
       / \
      3   6
     / \   \
    2   4   7
    
    Target = 9
    
    Output: True

Example 2:

    Input: 
        5
       / \
      3   6
     / \   \
    2   4   7
    
    Target = 28
    
    Output: False

## 题目大意

判断一个BST中是否存在两个节点的和等于指定的K.

## 解题方法

### 方法一：BFS

这个题又让我学到了，原来bfs还可以这么写。

原来认为bfs是通过append和pop(0)的方式进行计算的，这个答案把pop(0)的方式进行了简化，直接使用for就可以完成列表遍历，如果列表改变了也没问题。

使用set()保存已经遍历了的数字，作为存储。

比如下面用例的结果如下：
用例：

    [5,3,6,2,4,null,7]
    9

结果：

    5
    [5, 3, 6]
    3
    [5, 3, 6, 2, 4]
    6

```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        if not root: return False
        bfs, s = [root], set()
        for i in bfs:
            print i.val
            if k - i.val in s : return True
            s.add(i.val)
            if i.left : bfs.append(i.left)
            if i.right : bfs.append(i.right)
            print([b.val for b in bfs])
        return False
```

二刷的时候，使用BFS的标准写法，如下：

```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        que = collections.deque()
        que.append(root)
        res = set()
        while que:
            size = len(que)
            for _ in range(size):
                node = que.popleft()
                if not node:
                    continue
                if k - node.val in res:
                    return True
                res.add(node.val)
                que.append(node.left)
                que.append(node.right)
        return False
```

### 方法二：DFS

直接使用DFS进行判断也可以。这里又有两种写法，第一种是中序遍历成有序数组，然后进行一个2sum操作；另一种是在DFS的过程中就进行判断，如果找到即停止。

中序遍历解法如下：

```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        res = self.inOrder(root)
        resset = set(res)
        for num in res:
            if k != 2 * num and k - num in resset:
                return True
        return False
    
    def inOrder(self, root):
        if not root:
            return []
        res = []
        res.extend(self.inOrder(root.left))
        res.append(root.val)
        res.extend(self.inOrder(root.right))
        return res
```

DFS过程中进行判断：

```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        res = set()
        def inOrder(root):
            if not root:
                return False
            if k - root.val in res:
                return True
            res.add(root.val)
            return inOrder(root.left) or inOrder(root.right)
        return inOrder(root)
```


## 日期

2018 年 1 月 21 日 
2018 年 11 月 11 日 —— 剁手节快乐

  [1]: https://leetcode.com/problems/two-sum-iv-input-is-a-bst/description/
