
作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)

题目地址：[https://leetcode.com/problems/remove-linked-list-elements/description/][1]


## 题目描述

Remove all elements from a linked list of integers that have value val.

Example

	Given: 1 --> 2 --> 6 --> 3 --> 4 --> 5 --> 6, val = 6
	Return: 1 --> 2 --> 3 --> 4 --> 5

## 题目大意

把单链表中值等于val的节点全部去掉。

## 解题方法

### 双指针

做一个判断，走的快的指针如果节点的值一直等于val就一直走；否则快慢指针一起向后走。

```java
/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
public class Solution {
    public ListNode removeElements(ListNode head, int val) {
        if(head == null){
            return null;
        }
        ListNode fakehead = new ListNode(-1);
        fakehead.next = head;
        ListNode pre = fakehead;
        ListNode curr = pre.next;
        while(curr != null){
            if(curr.val == val){
                pre.next = curr.next;
            }else{
                pre = curr;
            }
            curr = curr.next;
        }
        return fakehead.next;
    }
}
```

Python解法如下：

```python
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        dummy = ListNode(-1)
        dummy.next = head
        pre = dummy
        cur = head
        while cur:
            if cur.val == val:
                pre.next = cur.next
            else:
                pre = pre.next
            cur = cur.next
        return dummy.next
```

### 递归

感觉递归不好写出来。递归函数返回的是删除了val的链表，所以，head.next就是这个链表，然后判断是否相等，如果相等应该返回的是下一个节点，这个节点就不要了。

Java代码如下。

```java
public ListNode removeElements(ListNode head, int val) {
        if (head == null) return null;
        head.next = removeElements(head.next, val);
        return head.val == val ? head.next : head;
}
```

Python代码如下：

```python
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        if not head: return None
        head.next = self.removeElements(head.next, val)
        return head.next if head.val == val else head
```

## 日期

2017 年 8 月 17 日 
2018 年 11 月 24 日 —— 周六快乐

  [1]: https://leetcode.com/problems/remove-linked-list-elements/description/
