作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)

[LeetCode]

题目地址：[https://leetcode.com/problems/reverse-linked-list/](https://leetcode.com/problems/reverse-linked-list/)

Total Accepted: 105474 Total Submissions: 267077 Difficulty: Easy


## 题目描述


Reverse a singly linked list.

Example:

	Input: 1->2->3->4->5->NULL
	Output: 5->4->3->2->1->NULL

Follow up:

A linked list can be reversed either iteratively or recursively. Could you implement both?

## 题目大意

翻转单链表。

## 解题方法
### 迭代

迭代解法，每次找出老链表的下一个结点，插入到新链表的头结点，这样就是一个倒着的链。

举例说明：

	old->3->4->5->NULL
	new->2->1
	然后把3插入到new的后边，会变成：
	old->4->5->NULL
	new->3->2->1

Java代码如下：

```java
public ListNode reverseList(ListNode head) {
    ListNode prev = null;
    ListNode curr = head;
    while (curr != null) {
        ListNode nextTemp = curr.next;
        curr.next = prev;
        prev = curr;
        curr = nextTemp;
    }
    return prev;
}
```

二刷，python。

```python
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None or head.next == None:
            return head
        newHead = None
        while head != None:
            temp = head.next
            head.next = newHead
            newHead = head
            head = temp
        return newHead
```

三刷，python。下面的解法打败了100%.

```python
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(-1)
        while head:
            nodenext = head.next
            head.next = dummy.next
            dummy.next = head
            head = nodenext
        return dummy.next
```

四刷，C++代码如下：

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
    ListNode* reverseList(ListNode* head) {
        ListNode* dummy = new ListNode(0);
        while (head) {
            ListNode* old = dummy->next;
            ListNode* nxt = head->next;
            dummy->next = head;
            head->next = old;
            head = nxt;
        }
        return dummy->next;
    }
};
```

### 递归

递归，先把除了head以外的后面部分翻转，然后把head放到已经翻转了的链表的结尾即可。需要注意的是找到已经翻转了的链表结尾并不是遍历找的，而是通过`head.next.next = head;`这一步，原因是head.next是老链表的除了head以外的头，也就是说新链表的结尾。

> 1 → … → nk-1 → nk → nk+1 → … → nm → Ø
> 
> Assume from node nk+1 to nm had been reversed and you are at node nk.
> 
> n1 → … → nk-1 → nk → nk+1 ← … ← nm
> 
> We want nk+1’s next node to point to nk.
> 
> So,
> 
> nk.next.next = nk;
> 
> Be very careful that n1's next must point to Ø. If you forget about this, your linked list has a cycle in it. This bug could be caught if you test your code with a linked list of size 2.

Java代码如下：

```java
public ListNode reverseList(ListNode head) {
    if (head == null || head.next == null) return head;
    ListNode p = reverseList(head.next);
    head.next.next = head;
    head.next = null;
    return p;
}
```

另外一种递归解法是新增加一个函数，让其有两个参数，第一个参数表示剩余链表的头，第二个参数表示新链表的头。每次把剩余链表的头插入到新链表的头部，返回该新的头部即可，这样的翻转就更直观了。

python的递归写法。

```python
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        return self.reverse(head, None)
        
    def reverse(self, head, newHead):
        if not head:
            return newHead
        headnext = head.next
        head.next = newHead
        return self.reverse(headnext, head)
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
    ListNode* reverseList(ListNode* head) {
        return reverse(head, nullptr);
    }
    ListNode* reverse(ListNode* oldHead, ListNode* newHead) {
        if (!oldHead) return newHead;
        ListNode* nxt = oldHead->next;
        oldHead->next = newHead;
        return reverse(nxt, oldHead);
    }
};
```

## 日期

2016/5/1 12:50:33 
2018年3月11日
2018 年 11 月 11 日 —— 剁手节快乐
2019 年 9 月 17 日 —— 听了hulu宣讲会，觉得hulu的压力不大
