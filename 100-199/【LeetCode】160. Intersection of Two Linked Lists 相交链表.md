
作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)

题目地址：[https://leetcode.com/problems/intersection-of-two-linked-lists/description/][1]


## 题目描述

Write a program to find the node at which the intersection of two singly linked lists begins.


For example, the following two linked lists:

    A:          a1 → a2
                       ↘
                         c1 → c2 → c3
                       ↗            
    B:     b1 → b2 → b3
    begin to intersect at node c1.


Notes:

1. If the two linked lists have no intersection at all, return null.
1. The linked lists must retain their original structure after the function returns.
1. You may assume there are no cycles anywhere in the entire linked structure.
1. Your code should preferably run in O(n) time and use only O(1) memory.
Credits:
1. Special thanks to @stellari for adding this problem and creating all test cases.

## 题目大意

找出两个链表的最早公共元素。

## 解题方法

### 双指针

第一次遍历时，如果两者的非公共元素的个数正好相等，那么一定能找到相同元素；如果非公共元素个数不等，那么在一次遍历之后，两者的指针的差距就是非公共元素的个数差。这样翻转之后，指针的差距正好弥补了非公共元素的差，这样，第二次遍历要么一定相遇，要么两者没有公共元素，返回None。


```python
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if headA is None or headB is None:
            return None
        pA = headA
        pB = headB
        while pA is not pB:
            pA = headB if pA is None else pA.next
            pB = headA if pB is None else pB.next
        return pA
```

二刷的时候，感觉写的解法更为容易理解。

```python
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        len1, len2 = 0, 0
        moveA, moveB = headA, headB
        while moveA:
            len1 += 1
            moveA = moveA.next
        while moveB:
            len2 += 1
            moveB = moveB.next
        if len1 < len2:
            for _ in range(len2 - len1):
                headB = headB.next
        else:
            for _ in range(len1 - len2):
                headA = headA.next
        while headA and headB and headA != headB:
            headA = headA.next
            headB = headB.next
        return headA
```

### 栈

因为后面的元素是相等的，所以使用栈把相等元素都弹出来，那么不等元素就是所求。

```python
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        stack1, stack2 = [], []
        while headA:
            stack1.append(headA)
            headA = headA.next
        while headB:
            stack2.append(headB)
            headB = headB.next
        pre = None
        while stack1 and stack2:
            s1 = stack1.pop()
            s2 = stack2.pop()
            if s1 != s2:
                return pre
            else:
                pre = s1
        return pre
```


## 日期

2017 年 8 月 27 日 
2018 年 11 月 26 日 —— 11月最后一周！

  [1]: https://leetcode.com/problems/intersection-of-two-linked-lists/description/
