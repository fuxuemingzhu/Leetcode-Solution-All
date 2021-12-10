# 【LeetCode】143. Reorder List 解题报告（Python）

标签（空格分隔）： LeetCode

作者： 		负雪明烛 
id：				fuxuemingzhu
个人博客：	http://fuxuemingzhu.me/

---

题目地址：https://leetcode.com/problems/reorder-list/description/

## 题目描述：

Given a singly linked list L: L0→L1→…→Ln-1→Ln,
reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…

You may not modify the values in the list's nodes, only nodes itself may be changed.

Example 1:

    Given 1->2->3->4, reorder it to 1->4->2->3.

Example 2:

    Given 1->2->3->4->5, reorder it to 1->5->2->4->3.


## 题目大意

把一个链表的前半部分正序，后半部分逆序，然后一个一个的连接起来。

## 解题方法

就像题目大意里面说的，需要三步。其实这个题对链表的考察非常的巧妙和详细了，可以说是三个题目了。

代码有点长，就是按照三步来写的。题目要求不能返回新节点，这个也提高了难度。

参考了：[\[leetcode\]Reorder List @ Python][1]

```python
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        if head and head.next and head.next.next:
            #find mid
            fast, slow = head, head
            while fast.next and fast.next.next:
                fast = fast.next.next
                slow = slow.next
            head1 = head
            head2 = slow.next
            slow.next = None

            # reverse linked list head2     
            dummy = ListNode(0)
            dummy.next = head2
            p = head2.next
            head2.next = None
            while p:
                temp = p
                p = p.next
                temp.next = dummy.next
                dummy.next = temp
            head2 = dummy.next
            
            # merge two linked list head1 and head2
            p1 = head1
            p2 = head2
            while p2:
                temp1 = p1.next
                temp2 = p2.next
                p1.next = p2
                p2.next = temp1
                p1 = temp1
                p2 = temp2
```

## 日期

2018 年 6 月 25 日 ———— 新的一周，不要再想烦心事了。


  [1]: https://www.cnblogs.com/zuoyuan/p/3700846.html