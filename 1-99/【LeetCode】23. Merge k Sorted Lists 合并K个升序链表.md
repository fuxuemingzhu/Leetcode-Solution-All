
- 作者：    负雪明烛
- id：      fuxuemingzhu
- 个人博客：[http://fuxuemingzhu.cn/](http://fuxuemingzhu.cn/)
- 个人公众号：负雪明烛
- 本文关键词：合并，链表，单链表，题解，leetcode, 力扣，Python, C++, Java

---

题目地址: https://leetcode.com/problems/merge-k-sorted-lists/description/

## 题目描述：

Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.

Example:
    
    Input:
    [
      1->4->5,
      1->3->4,
      2->6
    ]
    Output: 1->1->2->3->4->4->5->6


## 题目大意

把一个链表里的k个有序链表合并成一个有序链表。

## 解题方法

### 方法一：每次遍历最小值（TLE）

这个题是[21. Merge Two Sorted Lists][1]的拓展，属于经典题目，很容易想到的方法就是每次在lists中查找最小的值，然后拼接到现在的链表尾部。需要注意的是，我们不能通过修改链表指针的方法来更新lists里的头部元素，所以只能强行赋值更新lists。

时间卡在了每次查找链表最小元素这一步，导致超时。

时间复杂度是O(N*K)，空间复杂度是O(1)。N是结果链表的长度，K是每次题目给出的链表个数。

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        head = ListNode(-1)
        move = head
        while True:
            curHead = ListNode(float('inf'))
            curIndex = -1
            for i, llist in enumerate(lists):
                if llist and llist.val < curHead.val:
                    curHead = llist
                    curIndex = i
            if curHead.val == float('inf'):
                break
            curNext = curHead.next
            move.next = curHead
            curHead.next = None
            move = curHead
            curHead = curNext
            lists[curIndex] = curHead
        return head.next
```

### 方法二：小根堆保存值和索引

这个方法是根据上面超时的情况自然想出来的，我们每次需要用的是K个链表头结点的最小值，所以把每个链表的头结点都放在一个小根堆里面。这样，每次弹出来的就是最小链表的值，然后根据这个值的索引去Lists中找到对应节点，拼接到末尾就行。

有人使用的弹出堆里面最小的值，然后重新生成新的节点的方式，这样不好。

另外，代码里需要注意的一个问题是，和方法一一样，需要更新链表的头结点才行，不能直接通过修改指针的方式修改，必须直接赋值更新。如果这个步骤少了的话，按照索引查找就一直获取的是老节点。

时间复杂度是O(N)，空间复杂度是O(1)。N是结果链表的长度，K是每次题目给出的链表个数。

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        head = ListNode(-1)
        move = head
        heap = []
        heapq.heapify(heap)
        [heapq.heappush(heap, (l.val, i)) for i, l in enumerate(lists) if l]
        while heap:
            curVal, curIndex = heapq.heappop(heap)
            curHead = lists[curIndex]
            curNext = curHead.next
            move.next = curHead
            curHead.next = None
            move = curHead
            curHead = curNext
            if curHead:
                lists[curIndex] = curHead
                heapq.heappush(heap, (curHead.val, curIndex))
        return head.next
```

### 方法三：小根堆保存值和节点

对于Python3，不能直接在堆里面保存节点，因为会造成无法比较的问题。但是对于python2就可以这么做了，所以可以直接把节点的值和节点直接保存到堆里面，这样每次弹出来的是最小的值的节点，直接使用就好了。

```python
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        head = ListNode(-1)
        move = head
        heap = []
        heapq.heapify(heap)
        [heapq.heappush(heap, (l.val, l)) for i, l in enumerate(lists) if l]
        while heap:
            curVal, curHead = heapq.heappop(heap)
            curNext = curHead.next
            move.next = curHead
            curHead.next = None
            move = curHead
            curHead = curNext
            if curHead:
                heapq.heappush(heap, (curHead.val, curHead))
        return head.next
```

时间复杂度是O(N)，空间复杂度是O(1)。N是结果链表的长度，K是每次题目给出的链表个数。

参考资料：


## 日期

2018 年 10 月 16 日 —— 下雨天还是挺舒服的


  [1]: https://blog.csdn.net/fuxuemingzhu/article/details/51291406
