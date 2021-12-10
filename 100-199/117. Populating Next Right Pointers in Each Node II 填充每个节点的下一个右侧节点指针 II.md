# 【LeetCode】117. Populating Next Right Pointers in Each Node II 解题报告（Python）

标签： LeetCode

---

题目地址：https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/description/

## 题目描述：

Follow up for problem "Populating Next Right Pointers in Each Node".

What if the given tree could be any binary tree? Would your previous solution still work?

Note:

You may only use constant extra space.

For example,

    Given the following binary tree,
    
             1
           /  \
          2    3
         / \    \
        4   5    7
    
    After calling your function, the tree should look like:
    
             1 -> NULL
           /  \
          2 -> 3 -> NULL
         / \    \
        4-> 5 -> 7 -> NULL

## 题目大意

把一棵完全二叉树的每层节点之间顺序连接，形成单链表。

## 解题方法

跟[【LeetCode】116. Populating Next Right Pointers in Each Node 解题报告（Python）][1]很像，只不过这个题没有完全二叉树的条件，因此我们需要额外的条件。

下面这个做法没满足题目中的常数空间的要求，不过是个非递归的好做法，对完全二叉树也完全试用。做法就是把每层的节点放到一个队列里，把队列的每个元素进行弹出的时候，如果它不是该层的最后一个元素，那么把它指向队列中的后面的元素（不把后面的这个弹出）。

```python
# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        if not root: return
        queue = collections.deque()
        queue.append(root)
        while queue:
            _len = len(queue)
            for i in range(_len):
                node = queue.popleft()
                if i < _len - 1:
                    node.next = queue[0]
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
```

方法二：

constant extra space.

待续。

## 日期

2018 年 3 月 14 日 --霍金去世日


  [1]: http://blog.csdn.net/fuxuemingzhu/article/details/79559645