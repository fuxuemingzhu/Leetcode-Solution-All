
作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)


题目地址：https://leetcode.com/problems/reverse-linked-list-ii/description/

## 题目描述

Reverse a linked list from position m to n. Do it in one-pass.

Note: 1 ≤ m ≤ n ≤ length of list.

Example:

    Input: 1->2->3->4->5->NULL, m = 2, n = 4
    Output: 1->4->3->2->5->NULL

## 题目大意

把单链表中第m--n个元素进行翻转。

## 解题方法

### 迭代

其实就是翻转链表的而变形题目了。进行一次遍历，把第m到n个元素进行翻转，即依次插入到第m个节点的头部。

这个题还是有意思的。建议后面再多做几遍。

Python代码如下：

```python
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        count = 1
        root = ListNode(0)
        root.next = head
        pre = root
        while pre.next and count < m:
            pre = pre.next
            count += 1
        if count < m:
            return head
        mNode = pre.next
        curr = mNode.next
        while curr and count < n:
            next = curr.next
            curr.next = pre.next
            pre.next = curr
            mNode.next = next
            curr = next
            count += 1
        return root.next
```

C++代码如下：

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
    ListNode* reverseBetween(ListNode* head, int m, int n) {
        int pos = 1;
        ListNode* dummy = new ListNode(0);
        dummy->next = head;
        ListNode* pre = dummy;
        ListNode* cur = head;
        while (cur && pos < m) {
            pre = pre->next;
            cur = cur->next;
            pos ++;
        }
        ListNode* tailNode = cur;
        while (cur && pos <= n) {
            ListNode* nxt = cur->next;
            cur->next = pre->next;
            pre->next = cur;
            tailNode->next = nxt;
            cur = nxt;
            pos ++;
        }
        return dummy->next;
    }
};
```

### 递归

递归解法虽然简单，但是需要对程序有深刻的认识。所以写起来并不简单。理解下面这个解法之前，最好把[206. Reverse Linked List](https://blog.csdn.net/fuxuemingzhu/article/details/51290121#_138)的递归解法弄懂。

首先要记住这个reverseBetween()函数的意义：翻转链表中的[m,n]区间的元素，并且返回新链表的头结点。

1. 那么，如果m==n，则不用翻转，直接返回原来的头即可。
2. 如果m!=1的时候，该节点不用翻转，继续翻转后面的节点。
3. 如果m==1，该节点至n节点需要翻转，使用递归先把后面的翻转，此时head->next指向了**翻转部分**链表的结尾，把head插入到**翻转部分**链表的结尾即可。

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
    ListNode* reverseBetween(ListNode* head, int m, int n) {
        if (m == n)
            return head;
        if (m != 1) {
            head->next = reverseBetween(head->next, m - 1, n - 1);
            return head;
        } else {
            ListNode* newHead = reverseBetween(head->next, 1, n - 1);
            ListNode* reversedTail = head->next->next;
            head->next->next = head;
            head->next = reversedTail;
            return newHead;
        }
    }
};
```

## 日期

2018 年 6 月 24 日 ———— 今天请客吃了海底捞～


  [1]: https://blog.csdn.net/fuxuemingzhu/article/details/80786149
