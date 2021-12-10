
作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)

题目地址：https://leetcode.com/problems/middle-of-the-linked-list/description/

## 题目描述

Given a non-empty, singly linked list with head node ``head``, return a ``middle`` node of linked list.

If there are two middle nodes, return the second middle node.

Example 1:

    Input: [1,2,3,4,5]
    Output: Node 3 from this list (Serialization: [3,4,5])
    The returned node has value 3.  (The judge's serialization of this node is [3,4,5]).
    Note that we returned a ListNode object ans, such that:
    ans.val = 3, ans.next.val = 4, ans.next.next.val = 5, and ans.next.next.next = NULL.

Example 2:

    Input: [1,2,3,4,5,6]
    Output: Node 4 from this list (Serialization: [4,5,6])
    Since the list has two middle nodes with values 3 and 4, we return the second one.
 

Note:

- The number of nodes in the given list will be between 1 and 100.


## 题目大意

给出链表中的中间节点。如果链表长度为偶数，返回的应该是中间的第二个节点。

## 解题方法

### 使用哑结点

这个题很简单，就是快慢指针两个移动即可。

需要注意的是，如果链表长度为偶数，返回的应该是中间的第二个节点。这个做的方法，是判断fast指针是指向了最末尾的None还是链表结尾的node。如果是链表结尾说明是偶数个点，如果是none说明是奇数个点。


代码如下：

```python3
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head
        slow, fast = dummy, dummy
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow.next if fast else slow
```

### 不使用哑结点

如果不使用哑结点，初始时直接将两个指针指向head能获得更快的速度。这么做的前提是题目已经告诉了节点的数量最少是1，否则如果初始化是空的话fast.next会报错。


```python3
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        slow, fast = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        return slow
```


## 日期

2018 年 8 月 16 日 —— 一个月不写题，竟然啥都不会了。。加油！
2018 年 11 月 6 日 —— 腰酸背痛要废了
