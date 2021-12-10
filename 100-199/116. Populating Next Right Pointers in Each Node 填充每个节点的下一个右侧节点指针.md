
- 作者：    负雪明烛
- id：      fuxuemingzhu
- 个人博客：[http://fuxuemingzhu.cn/](http://fuxuemingzhu.cn/)

---
@[TOC](目录)

题目地址：https://leetcode.com/problems/populating-next-right-pointers-in-each-node/description/

## 题目描述


给定一个**完美二叉树**，其所有叶子节点都在同一层，每个父节点都有两个子节点。二叉树定义如下：

	struct Node {
	  int val;
	  Node *left;
	  Node *right;
	  Node *next;
	}
	
填充它的每个 next 指针，让这个指针指向其下一个右侧节点。如果找不到下一个右侧节点，则将 next 指针设置为 `NULL`。

初始状态下，所有 next 指针都被设置为 `NULL`。

示例：

![在这里插入图片描述](https://img-blog.csdnimg.cn/20200709111208411.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2Z1eHVlbWluZ3podQ==,size_16,color_FFFFFF,t_70)

	输入：{"$id":"1","left":{"$id":"2","left":{"$id":"3","left":null,"next":null,"right":null,"val":4},"next":null,"right":{"$id":"4","left":null,"next":null,"right":null,"val":5},"val":2},"next":null,"right":{"$id":"5","left":{"$id":"6","left":null,"next":null,"right":null,"val":6},"next":null,"right":{"$id":"7","left":null,"next":null,"right":null,"val":7},"val":3},"val":1}
	
	输出：{"$id":"1","left":{"$id":"2","left":{"$id":"3","left":null,"next":{"$id":"4","left":null,"next":{"$id":"5","left":null,"next":{"$id":"6","left":null,"next":null,"right":null,"val":7},"right":null,"val":6},"right":null,"val":5},"right":null,"val":4},"next":{"$id":"7","left":{"$ref":"5"},"next":null,"right":{"$ref":"6"},"val":3},"right":{"$ref":"4"},"val":2},"next":null,"right":{"$ref":"7"},"val":1}

	解释：给定二叉树如图 A 所示，你的函数应该填充它的每个 next 指针，以指向其下一个右侧节点，如图 B 所示。
	 

提示：

1. 你只能使用常量级额外空间。
2. 使用递归解题也符合要求，本题中递归程序占用的栈空间不算做额外的空间复杂度。


## 题目大意

把一棵完全二叉树的每层节点之间顺序连接，形成单链表。

## 解题方法

### 递归

树的问题一般都可以用递归解决。这个题中，同样可以使用dfs解决。

注意题目已经声明了是完全二叉树，从根节点开始找到任意节点，将其左孩子指向右孩子。如果该节点已经指向了同层的其他节点，说明需要连接两个子树，比如例子中的``2->3``,那么不仅要把2的左孩子4指向右孩子5，还要把2的右孩子5指向2的next节点的左孩子6。这样递归完成了，每层就是单链表了。

发现一篇文章讲得很细：http://www.cnblogs.com/yrbbest/p/4437341.html

```python
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if not root: return
        if root.right:
            root.left.next = root.right
            if root.next:
                root.right.next = root.next.left
        self.connect(root.left)
        self.connect(root.right)
        return root
```

## 日期

2018 年 3 月 14 日 --霍金去世日
