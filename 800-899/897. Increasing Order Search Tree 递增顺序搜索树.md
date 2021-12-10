作者： 		负雪明烛 
id：				fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---

@[TOC](目录)

题目地址：https://leetcode.com/problems/increasing-order-search-tree/description/

## 题目描述

Given a tree, rearrange the tree in ``in-order`` so that the leftmost node in the tree is now the root of the tree, and every node has no left child and only 1 right child.

Example 1:

    Input: [5,3,6,2,4,null,8,1,null,null,null,7,9]

           5
          / \
        3    6
       / \    \
      2   4    8
     /        / \ 
    1        7   9

    Output: [1,null,2,null,3,null,4,null,5,null,6,null,7,null,8,null,9]

     1
      \
       2
        \
         3
          \
           4
            \
             5
              \
               6
                \
                 7
                  \
                   8
                    \
                     9  

Note:

1. The number of nodes in the given tree will be between 1 and 100.
1. Each node will have a unique integer value from 0 to 1000.


## 题目大意

把一棵树按照中序遍历的顺序重新安排，安排成最左侧的节点是新的数树的根节点，并且每个节点只有右子节点。

## 解题方法

### 重建二叉树

好久没做树的题目，有点生疏。使用的方式是最简单的，先中序遍历，得到顺序，然后再连接的方式。

这个做法的问题是用数组保存了整儿个中序遍历的值，然后重建了二叉树，那么空间复杂度挺大的，不是一个好方法。

时间复杂度是O(n)，空间复杂度是O(n).

代码如下：

```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def increasingBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        array = self.inOrder(root)
        if not array:
            return None
        newRoot = TreeNode(array[0])
        curr = newRoot
        for i in range(1, len(array)):
            curr.right =TreeNode(array[i])
            curr = curr.right
        return newRoot
        
    def inOrder(self, root):
        if not root:
            return []
        array = []
        array.extend(self.inOrder(root.left))
        array.append(root.val)
        array.extend(self.inOrder(root.right))
        return array
```

### 数组保存节点

在上面解法的基础上，如果不想使用保存节点的值然后重新构建每个节点的方式，那么有个更简单的方法就是我们在数组里保存节点，然后直接把数组的节点再次构成树就好了。省去了重新构造每个节点的过程。

时间复杂度是O(n)，空间复杂度是O(n).

```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def increasingBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        res = self.inOrder(root)
        if not res:
            return 
        dummy = TreeNode(-1)
        cur = dummy
        for node in res:
            node.left = node.right = None
            cur.right = node
            cur = cur.right
        return dummy.right
    
    def inOrder(self, root):
        if not root:
            return []
        res = []
        res.extend(self.inOrder(root.left))
        res.append(root)
        res.extend(self.inOrder(root.right))
        return res
```

### 中序遍历时修改指针

这个做法在上面的基础上再次缩减了空间复杂度，不再需要数组。这种做法中直接在中序遍历的过程中修改每个节点的指向。

修改指向的方式其实比较简单，使用prev指针一直指向了构造出来的这个新树的最右下边的节点，在中序遍历过程中把当前节点的左指针给设置为None，然后把当前节点放到新树的右下角，这样类似于一个越来越长的链表的构建过程。

时间复杂度是O(n)，空间复杂度是O(1).


```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def increasingBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        dummy = TreeNode(-1)
        self.prev = dummy
        self.inOrder(root)
        return dummy.right
        
    def inOrder(self, root):
        if not root:
            return None
        self.inOrder(root.left)
        root.left = None
        self.prev.right = root
        self.prev = self.prev.right
        self.inOrder(root.right)
```

## 参考资料

https://zxi.mytechroad.com/blog/tree/leetcode-897-increasing-order-search-tree/


## 日期

2018 年 9 月 3 日 ———— 新学期开学第一天！
2018 年 11 月 1 日 —— 小光棍节
