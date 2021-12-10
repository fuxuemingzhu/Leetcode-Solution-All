# 【LeetCode】61. Rotate List 解题报告（Python）

标签（空格分隔）： LeetCode

作者： 		负雪明烛 
id：				fuxuemingzhu
个人博客：	http://fuxuemingzhu.me/

---

题目地址：https://leetcode.com/problems/rotate-list/description/

## 题目描述：

Given a linked list, rotate the list to the right by k places, where k is non-negative.

Example 1:

    Input: 1->2->3->4->5->NULL, k = 2
    Output: 4->5->1->2->3->NULL
    Explanation:
    rotate 1 steps to the right: 5->1->2->3->4->NULL
    rotate 2 steps to the right: 4->5->1->2->3->NULL

Example 2:

    Input: 0->1->2->NULL, k = 4
    Output: 2->0->1->NULL
    Explanation:
    rotate 1 steps to the right: 2->0->1->NULL
    rotate 2 steps to the right: 1->2->0->NULL
    rotate 3 steps to the right: 0->1->2->NULL
    rotate 4 steps to the right: 2->0->1->NULL

## 题目大意

给出了链表和数字k。重复k次下面的操作：把链表最后的一个节点移动到开头。返回新的链表。

## 解题方法

首先，可以从Example 2也能看出来，存在k>len的情况，这样必须求余运算，否则肯定超时。即要求链表的长度。

其次，如果求余之后，知道了移动几次，本质上就是把链表的后面k个节点移动到开头去。注意是平移，顺序不变的。所以要找到后面的k个节点，那么需要用到[19. Remove Nth Node From End of List][1]类似的方法，用两个距离为k的指针进行平移操作，当前面的到达了末尾，那么后面的正好是倒数第k个。

找到倒数第k个之后，那么把这个节点和之前的节点断开，把后面的这段移到前面去即可。

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head or not head.next: return head
        _len = 0
        root = head
        while head:
            _len += 1
            head = head.next
        k %= _len
        if k == 0: return root
        fast, slow = root, root
        while k - 1:
            fast = fast.next
            k -= 1
        pre = slow
        while fast.next:
            fast = fast.next
            pre = slow
            slow = slow.next
        pre.next = None
        fast.next = root
        return slow
```

## 日期

2018 年 6 月 23 日 ———— 美好的周末要从刷题开始


  [1]: https://blog.csdn.net/fuxuemingzhu/article/details/80786149