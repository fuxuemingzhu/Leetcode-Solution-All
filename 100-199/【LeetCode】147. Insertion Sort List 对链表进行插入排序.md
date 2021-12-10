# 【LeetCode】147. Insertion Sort List 解题报告（Python）

标签（空格分隔）： LeetCode

作者： 		负雪明烛 
id：				fuxuemingzhu
个人博客：	http://fuxuemingzhu.me/

---

题目地址：https://leetcode.com/problems/insertion-sort-list/description/

## 题目描述：

Sort a linked list using insertion sort.

![此处输入图片的描述][1]


A graphical example of insertion sort. The partial sorted list (black) initially contains only the first element in the list.
With each iteration one element (red) is removed from the input data and inserted in-place into the sorted list
 

Algorithm of Insertion Sort:

Insertion sort iterates, consuming one input element each repetition, and growing a sorted output list.
At each iteration, insertion sort removes one element from the input data, finds the location it belongs within the sorted list, and inserts it there.
It repeats until no input elements remain.

Example 1:

    Input: 4->2->1->3
    Output: 1->2->3->4

Example 2:

    Input: -1->5->3->4->0
    Output: -1->0->3->4->5


## 题目大意

使用插入排序，对链表进行排序。

## 解题方法

这个算链表里边的难题了，其实就是模拟题目中图的过程，稍微有点复杂的就是指针的操作。参考了：[链表插入排序][2]里的做法，链表操作多用几个指针就方便很多了。

```python
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next: return head
        root = TreeNode(0)
        root.next = head
        while head.next:
            if head.val <= head.next.val:
                head = head.next
            else:
                temp = head.next
                q = root
                head.next = head.next.next
                while q.next and q.next.val < temp.val:
                    q = q.next
                temp.next = q.next
                q.next = temp
        return root.next
```

## 日期

2018 年 6 月 23 日 ———— 美好的周末要从刷题开始


  [1]: https://upload.wikimedia.org/wikipedia/commons/0/0f/Insertion-sort-example-300px.gif
  [2]: https://blog.csdn.net/happyaaaaaaaaaaa/article/details/51619973