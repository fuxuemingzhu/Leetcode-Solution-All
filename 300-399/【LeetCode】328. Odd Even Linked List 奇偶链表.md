作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)

题目地址：https://leetcode.com/problems/odd-even-linked-list/description/

## 题目描述

Given a singly linked list, group all odd nodes together followed by the even nodes. Please note here we are talking about the node number and not the value in the nodes.

You should try to do it in place. The program should run in O(1) space complexity and O(nodes) time complexity.

    Example:
    Given 1->2->3->4->5->NULL,
    return 1->3->5->2->4->NULL.

Note:

1. The relative order inside both the even and odd groups should remain as it was in the input. 
1. The first node is considered odd, the second node even and so on ...

## 题目大意

把一个链表的奇数序号的节点放在前面，偶数序号的节点放在后面。注意使用O(n)的时间复杂度和O(1)的空间。

## 解题方法

我的想法很朴素。我只用弄出来两条链不就好了吗？如果是奇数节点放到奇链，如果是偶数节点就放到偶链。最后，把偶链放到奇链的后面就好了。

注意，偶链的末尾指针要设置成空，已让单链表终止。

比如对于用例[1,2,3]，奇数链是1->3，偶链是2，而遍历完成后的偶链2仍然指向3的，所以死循环了。把尾指针设置成空就能终止了。

Python代码如下：

```python
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        odd = ListNode(0)
        even = ListNode(0)
        oddHead, evenHead = odd, even
        index = 0
        while head:
            if index & 1 == 0:
                odd.next = head
                odd = odd.next
            else:
                even.next = head
                even = even.next
            head = head.next
            index += 1
        even.next = None
        odd.next = evenHead.next
        return oddHead.next
```

C++代码如下，不过由于在函数中声明了普通指针而没有delete，会造成内存泄漏，leetcode能通过，但是面试的时候要小心。

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
    ListNode* oddEvenList(ListNode* head) {
        ListNode* oddHead = new ListNode(0);
        ListNode* evenHead = new ListNode(0);
        ListNode* odd = oddHead;
        ListNode* even = evenHead;
        int index = 1;
        while (head) {
            if (index & 1) {
                odd->next = head;
                odd = odd->next;
            } else {
                even->next = head;
                even = even->next;
            }
            head = head->next;
            ++index;
        }
        if (even->next) even->next = nullptr;
        if (evenHead->next)
            odd->next = evenHead->next;
        return oddHead->next;
    }
};
```


## 日期

2018 年 3 月 15 日 —— 雾霾消散，春光明媚
2019 年 3 月 23 日 —— 一年之后重刷此题，还是还有点生疏
