作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)


[LeetCode]

题目地址：[https://leetcode.com/problems/remove-duplicates-from-sorted-list/](https://leetcode.com/problems/remove-duplicates-from-sorted-list/)

Total Accepted: 114584 Total Submissions: 311665 Difficulty: Easy


## 题目描述



Given a sorted linked list, delete all duplicates such that each element appear only once.

Example 1:

	Input: 1->1->2
	Output: 1->2

Example 2:

	Input: 1->1->2->3->3
	Output: 1->2->3

## 题目大意

删除有序列表中的重复节点。

## 解题方法
### 判断相邻节点是否相等

如果下一个元素和这个元素的值相等。这个元素的下个元素就等于下个元素的下个元素。再循环就好了。

在找到不同的元素之前，当前元素不走。找到之后再走。

Java代码如下：

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
    public ListNode deleteDuplicates(ListNode head) {
        ListNode move=head;
        while(move!=null && move.next!=null){
            if(move.next.val == move.val){
                move.next=move.next.next;
            }else{
                move=move.next;
            }
        }
        
        return head;
        
    }
}
```

这个做法的Python解法如下：

```python
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head: return None
        prev, cur = head, head.next
        while cur:
            if cur.val == prev.val:
                prev.next = cur.next
            else:
                prev = cur
            cur = cur.next
        return head
```

C++版本如下：

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
    ListNode* deleteDuplicates(ListNode* head) {
        if (!head || !head->next) return head;
        ListNode* prev = head;
        ListNode* cur = head->next;
        while (cur) {
            if (prev->val == cur->val) {
                prev->next = cur->next;
            } else {
                prev = cur;
            }
            cur = cur->next;
        }
        return head;
    }
};
```

### 使用set

二刷， python

二刷第一遍没看清，不知道是个已经排序了的linkedlist，所以，用了set。没想到这个方法竟然更快点。

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next: return head
        val_set = set()
        val_set.add(head.val)
        root = ListNode(0)
        root.next = head
        while head and head.next:
            if head.next.val in val_set:
                head.next = head.next.next
            else:
                head = head.next
                val_set.add(head.val)
        return root.next
```

### 使用列表
使用一个类似于栈的列表，把每个链表节点向里面放，如果遇到了同样的元素那么“退栈”，只放入最后一个节点。可以这样做的原因是给出的链表是已经排序的，因此相等的节点会连续存在。

python代码如下：

```python
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next: return head
        deque = []
        move = head
        while move:
            while deque and deque[-1].val == move.val:
                deque.pop()
            deque.append(move)
            move = move.next
        for i in range(len(deque) - 1):
            deque[i].next = deque[i + 1]
        return deque[0]
```
### 递归

递归解法还不是那么好想的，需要返回的是当前节点或者下一个节点，也就是说如果重复的时候，舍弃掉当前节点。

```python
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next: return head
        head.next = self.deleteDuplicates(head.next)
        return head if head.val != head.next.val else head.next
```

## 日期

2016/5/1 15:05:24 
2018 年 6 月 23 日 —— 美好的周末要从刷题开始
2018 年 11 月 20 日 —— 真是一个好天气
2019 年 9 月 16 日 —— 秋高气爽
