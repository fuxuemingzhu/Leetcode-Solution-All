- 作者：    负雪明烛
- id：      fuxuemingzhu
- 个人博客：[http://fuxuemingzhu.cn/](http://fuxuemingzhu.cn/)
- 个人公众号：负雪明烛
- 本文关键词：合并，有序链表，递归，迭代，题解，leetcode, 力扣，Python, C++, Java

---
@[TOC](目录)

题目地址：[https://leetcode.com/problems/merge-two-sorted-lists/](https://leetcode.com/problems/merge-two-sorted-lists/)


## 题目描述


Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

Example:

	Input: 1->2->4, 1->3->4
	Output: 1->1->2->3->4->4

## 题目大意

把两个有序列表合并成一个有序列表。

## 解题方法

### 迭代

直接自己定义一个链表的头，循环两个链表，每次把两个链表头部较小的那个节点放到结尾。最后不要忘了如果链表有剩余，应该拼接起来。

#### Python解法
这个题有个升级版本[23. Merge k Sorted Lists](https://blog.csdn.net/fuxuemingzhu/article/details/83068632)，比这题有意思，可以看看。

```python
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
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

#### C++解法

C++注意全部是指针操作，要用指针操作符。

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
    ListNode* mergeTwoLists(ListNode* l1, ListNode* l2) {
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

#### Java解法



```java
/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { liebiaoval = x; }
 * }
 */
public class Solution {
    public ListNode mergeTwoLists(ListNode l1, ListNode l2) {
        ListNode head=new ListNode(0);
        ListNode move=head;
        while(l1!=null && l2!=null){
            if(l1.val<=l2.val){
                move.next=l1;
                l1=l1.next;
            }else{
                move.next=l2;
                l2=l2.next;
            }
            move=move.next;
        }
        if(l1!=null){
            move.next=l1;
        }else{
            move.next=l2;
        }
        
        return head.next;
    }
}
```
AC:1ms


### 递归

递归很好写了，这个函数是把两个有序的merge，所以找到当前的小的节点，然后把后面的继续merge就好了。

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1 and not l2:
            return None
        elif not l1:
            return l2
        elif not l2:
            return l1
        if l1.val <= l2.val:
            node = l1
            node.next = self.mergeTwoLists(l1.next, l2)
        else:
            node = l2
            node.next= self.mergeTwoLists(l1, l2.next)
        return node
```


## 日期

2016/5/1 19:35:14 
2018 年 3 月 11 日
2018 年 11 月 18 日 —— 出去玩了一天，腿都要废了
2019 年 1 月 11 日 —— 小光棍节？
