- 作者：    负雪明烛
- id：      fuxuemingzhu
- 个人博客：[http://fuxuemingzhu.cn/](http://fuxuemingzhu.cn/)
- 个人公众号：负雪明烛
- 本文关键词：链表, 删除节点，双指针，题解，leetcode, 力扣，Python, C++, Java


---
@[TOC](目录)

题目地址：https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/

## 题目描述


Given a linked list, remove the ``n-th`` node from the end of list and return its head.

Example:

	Given linked list: 1->2->3->4->5, and n = 2.
	
	After removing the second node from the end, the linked list becomes 1->2->3->5.

Note:

1. Given n will always be valid.

Follow up:

- Could you do this in one pass?


## 题目大意

删除一个单链表的倒数第n个节点。

## 解题方法
### 双指针

先来分析一下这个题埋的坑吧。
第一，首先要判断这个n是不是有效，如果n超出链表长度怎么办，还好题目给了n是有效的。
第二，如果要删除头结点怎么办？估计很多人栽在了这个上面。
第三，题目说的是单链表没错，但是是否有环呢？当有环的时候，没有倒数第n个节点，你让我怎么办？很遗憾，题目没有说明这一点，我认为这是题目不严谨的地方。

具体到解法，这个题肯定是使用快慢指针啊，两个之间的距离是n，所以当快指针指向结尾的时候，慢指针正好指向了倒数第n个。因为要删除慢指针的位置，所以需要一个pre指针记录一下前面的那个节点的位置。

由于有可能删除首节点，所以使用哑结点当做新的头可以解决。

Python代码如下：

```python
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        root = ListNode(0)
        root.next = head
        fast, slow, pre = root, root, root
        while n - 1:
            fast = fast.next
            n -= 1
        while fast.next:
            fast = fast.next
            pre = slow
            slow = slow.next
        pre.next = slow.next
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
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        ListNode* dummy = new ListNode(0);
        dummy->next = head;
        ListNode* prev = dummy;
        ListNode* cur = dummy;
        while (n--) {
            cur = cur->next;
        }
        while (cur && cur->next) {
            cur = cur->next;
            prev = prev->next;
        }
        prev->next = prev->next->next;
        return dummy->next;
    }
};
```

## 日期

2018 年 6 月 23 日 —— 美好的周末要从刷题开始
2019 年 1 月 10 日 —— 加油
2019 年 9 月 27 日 —— 昨天面快手，竟然是纯刷题

  [1]: https://upload.wikimedia.org/wikipedia/commons/0/0f/Insertion-sort-example-300px.gif
  [2]: https://blog.csdn.net/happyaaaaaaaaaaa/article/details/51619973
