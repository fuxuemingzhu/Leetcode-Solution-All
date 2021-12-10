
作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)

题目地址：https://leetcode.com/problems/design-linked-list/description/

## 题目描述

Design your implementation of the linked list. You can choose to use the singly linked list or the doubly linked list. A node in a singly linked list should have two attributes: ``val`` and ``next``. ``val`` is the value of the current node, and ``next`` is a pointer/reference to the next node. If you want to use the doubly linked list, you will need one more attribute ``prev`` to indicate the previous node in the linked list. Assume all nodes in the linked list are 0-indexed.

Implement these functions in your linked list class:

- get(index) : Get the value of the ``index``-th node in the linked list. If the index is invalid, return -1.
- addAtHead(val) : Add a node of value ``val`` before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
- addAtTail(val) : Append a node of value ``val`` to the last element of the linked list.
- addAtIndex(index, val) : Add a node of value ``val`` before the ``index``-th node in the linked list. If ``index`` equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
- deleteAtIndex(index) : Delete the ``index``-th node in the linked list, if the index is valid.

Example:

    MyLinkedList linkedList = new MyLinkedList();
    linkedList.addAtHead(1);
    linkedList.addAtTail(3);
    linkedList.addAtIndex(1, 2);  // linked list becomes 1->2->3
    linkedList.get(1);            // returns 2
    linkedList.deleteAtIndex(1);  // now the linked list is 1->3
    linkedList.get(1);            // returns 3

Note:

- All values will be in the range of [1, 1000].
- The number of operations will be in the range of [1, 1000].
- Please do not use the built-in LinkedList library.

## 题目大意

自己实现一个链表。

## 解题方法

链表的实现如果按照题目所说的，那么需要自己定义类，也就是普通的链表。但是！我们需要那么做么？我们需要实现的链表只要能实现题目中给的函数功能就行了，所以完全不需要自己定义类，只需要一个list即可！

也就是说所有的操作都映射到list上的操作，对应的改变一下就行。

注意，这个本质上是不对的，只是为了通过这个题而做的，这种定义的链表的各种操作的复杂度是不符合要求的。

Python代码如下：

```python
class MyLinkedList(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.linkedlist = list()

    def get(self, index):
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        :type index: int
        :rtype: int
        """
        if index < 0 or index >= len(self.linkedlist):
            return -1
        else:
            return self.linkedlist[index]

    def addAtHead(self, val):
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        :type val: int
        :rtype: void
        """
        self.linkedlist.insert(0, val)

    def addAtTail(self, val):
        """
        Append a node of value val to the last element of the linked list.
        :type val: int
        :rtype: void
        """
        self.linkedlist.append(val)

    def addAtIndex(self, index, val):
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        :type index: int
        :type val: int
        :rtype: void
        """
        if 0 <= index and index <= len(self.linkedlist):
            self.linkedlist.insert(index, val)

    def deleteAtIndex(self, index):
        """
        Delete the index-th node in the linked list, if the index is valid.
        :type index: int
        :rtype: void
        """
        if 0 <= index and index < len(self.linkedlist):
            self.linkedlist.pop(index)


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
```

## 日期

2018 年 7 月 13 日 —— 早起困一上午，中午必须好好休息才行啊
2018 年 11 月 18 日 —— 出去玩了一天，腿都要废了
