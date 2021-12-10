# 【LeetCode】86. Partition List 解题报告（Python）

标签（空格分隔）： LeetCode

作者： 		负雪明烛 
id：				fuxuemingzhu
个人博客：	http://fuxuemingzhu.me/

---

题目地址：https://leetcode.com/problems/partition-list/description/

## 题目描述：

Given a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.

Example:

    Input: head = 1->4->3->2->5->2, x = 3
    Output: 1->2->2->4->3->5


## 题目大意

要把一个单链表中，小于某个数字的所有节点放到前面，其余的位置都不要变化。

## 解题方法

乍一看，感觉原地做这些操作很难。但是，我们换个思路就感觉很简单了。

**做链表的题，不要省指针。**

用两个新指针，分别记录比x值小的和比x值大的，遍历原来的链表的时候根据值的大小拼接到对应的链表后面。

最后再把两个链表拼接到一起就行了。

```python
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        small = ListNode(0)
        large = ListNode(0)
        small_root, large_root = small, large
        while head:
            if head.val < x:
                small.next = head
                small = small.next
            else:
                large.next = head
                large = large.next
            temp = head.next
            head.next = None
            head = temp
        small.next  = large_root.next
        return small_root.next
```

## 日期

2018 年 6 月 24 日 ———— 今天请客吃了海底捞～


  [1]: https://blog.csdn.net/fuxuemingzhu/article/details/80786149