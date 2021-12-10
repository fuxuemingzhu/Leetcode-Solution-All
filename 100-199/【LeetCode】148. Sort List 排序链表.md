
作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)

题目地址：https://leetcode.com/problems/sort-list/description/

## 题目描述

Sort a linked list in O(n log n) time using constant space complexity.

Example 1:

	Input: 4->2->1->3
	Output: 1->2->3->4

Example 2:

	Input: -1->5->3->4->0
	Output: -1->0->3->4->5
	    
## 题目大意

把单链表进行排序。

## 解题方法

这个题要求用O(nlongn)的时间复杂度和O(1)的空间复杂度。所以可以使用merge排序，但是如果是链表可以修改指针，把两个有序链表进行原地的合并。

Merge排序就是先划分成一前一后等分的两块，然后对两块分别进行排序，然后再合并两个有序序列。

第一步，如何等分地划分，可以使用快慢指针的方式，当快指针到达结尾，那么慢指针到了中间位置，把链表进行截断分成了两个。

第二步，合并有序的序列，对于单链表来说，正好用到了[Merge Two Sorted Lists][1]里的把两个链表合并的方法。

事实上，这个答案里面并不是O(1)的空间，因为，第一，添加了新的链表头的个数会随着递归的次数而不断增加，并不是常量个；第二，递归本身就不是常量空间。

Python代码如下：

```python
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next: return head
        pre, slow, fast = head, head, head
        while fast and fast.next:
            pre = slow
            slow = slow.next
            fast = fast.next.next
        pre.next = None
        l1 = self.sortList(head)
        l2 = self.sortList(slow)
        return self.mergeTwoLists(l1, l2)
    
    def mergeTwoLists(self, l1, l2):
        head = ListNode(0)
        move = head
        if not l1: return l2
        if not l2: return l1
        while l1 and l2:
            if l1.val < l2.val:
                move.next = l1
                l1 = l1.next
            else:
                move.next = l2
                l2 = l2.next
            move = move.next
        move.next = l1 if l1 else l2
        return head.next
```

C++代码如下，对于链表操作全是指针操作，真的很烦：

```cpp
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    // make the list sort.
    ListNode* sortList(ListNode* head) {
        if (!head || !head->next) return head;
        ListNode* fast = head;
        ListNode* slow = head;
        ListNode* pre = head;
        while (fast && fast->next) {
            pre = slow;
            fast = fast->next->next;
            slow = slow->next;
        }
        pre->next = nullptr;
        ListNode* l1 = sortList(head);
        ListNode* l2 = sortList(slow);
        return mergeList(l1, l2);
    }
    // merge two sort list.
    ListNode* mergeList(ListNode* l1, ListNode* l2) {
        if (!l1) return l2;
        if (!l2) return l1;
        ListNode* dummy = new ListNode(0);
        ListNode* cur = dummy;
        while (l1 && l2) {
            if (l1->val < l2->val) {
                cur->next = l1;
                l1 = l1->next;
            } else {
                cur->next = l2;
                l2 = l2->next;
            }
            cur = cur->next;
        }
        if (l1) cur->next = l1;
        else  cur->next = l2;
        return dummy->next;
    }
};
```

## 日期

2018 年 3 月 20 日 —— 阳光明媚～
2019 年 1 月 11 日 —— 小光棍节？

  [1]: http://blog.csdn.net/fuxuemingzhu/article/details/51291406
