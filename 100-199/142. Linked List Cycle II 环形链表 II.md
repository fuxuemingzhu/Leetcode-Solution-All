
作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)

题目地址：https://leetcode.com/problems/linked-list-cycle-ii/description/

## 题目描述


Given a linked list, return the node where the cycle begins. If there is no cycle, return ``null``.

To represent a cycle in the given linked list, we use an integer ``pos`` which represents the position (0-indexed) in the linked list where tail connects to. If pos is -1, then there is no cycle in the linked list.

Note: Do not modify the linked list.
 
Example 1:

	Input: head = [3,2,0,-4], pos = 1
	Output: tail connects to node index 1
	Explanation: There is a cycle in the linked list, where tail connects to the second node.

![在这里插入图片描述](https://imgconvert.csdnimg.cn/aHR0cHM6Ly9hc3NldHMubGVldGNvZGUuY29tL3VwbG9hZHMvMjAxOC8xMi8wNy9jaXJjdWxhcmxpbmtlZGxpc3QucG5n)

Example 2:

	Input: head = [1,2], pos = 0
	Output: tail connects to node index 0
	Explanation: There is a cycle in the linked list, where tail connects to the first node.

![在这里插入图片描述](https://imgconvert.csdnimg.cn/aHR0cHM6Ly9hc3NldHMubGVldGNvZGUuY29tL3VwbG9hZHMvMjAxOC8xMi8wNy9jaXJjdWxhcmxpbmtlZGxpc3RfdGVzdDIucG5n)

Example 3:

	Input: head = [1], pos = -1
	Output: no cycle
	Explanation: There is no cycle in the linked list.

![在这里插入图片描述](https://imgconvert.csdnimg.cn/aHR0cHM6Ly9hc3NldHMubGVldGNvZGUuY29tL3VwbG9hZHMvMjAxOC8xMi8wNy9jaXJjdWxhcmxpbmtlZGxpc3RfdGVzdDMucG5n)
 

Follow up:

- Can you solve it without using extra space?



## 题目大意

找出单链表是否有环，如果有环返回环的入口，否则返回None.

## 解题方法

### 双指针

做过之前判断一个单链表中是否有环的题，我们知道可以通过一个指针走两步，一个指针走一步的方式，看两者是否相遇即可。这个题是之前的拓展。

如图所示，两个指针同时从直线起点开始，这个圈是顺时针方向走的，即走的顺序是S-O-x-c-O-x。

![此处输入图片的描述][1]

感谢评论区指正，如果SO线段的长度a足够长，而圈很小的时候，当两者相遇时，快指针多走的可能不止一圈。下面要证明如果相遇之后，慢指针回到原点继续走再相遇的点在O点。

1. 首先要证明的是，两指针相遇时，慢指针还没有走完整个链表。
	- 当慢指针没走完一圈时，显然成立
	- 假设慢指针走完了一圈之后相遇，可以假定快指针在O的前一个位置，慢指针走一圈回到了O点，此时快指针走了两圈又回到了O的前一个位置，所以在慢指针走玩一圈之前就已经相遇。

2. 快慢指针在x处第一次汇合，xo之间距离为x，假如快指针走了n圈，快指针走过的路程为a+x+n*(c + x)，慢指针走过的路程为a+x，所以a+x+n*(c + x) = 2(a+x),所以a + x = n*(c + x)，也就是SOx之间的距离等于n圈的长度，所以令慢指针从起点开始一次一步，快指针从x开始顺时针方向转也一次一步，同时前进，则慢指针走a时，快指针走了n*(c+x) - x的长度，则必会在O处相遇！

同时注意题目中说了，有可能不存在环，所以要进行判断。

二刷的时候提交错误了几次，原因在于判断fast == slow的时候写错位置了。应该写在移动指针之后，而不是在while循环刚开始的时候就判断。因为刚开始就判断的话，那么底下移动之后，可能直接就退出while了，没有做是否相等的判断。

```python
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        slow, fast = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                break
        if not fast or not fast.next:
            return None
        slow = head
        while slow != fast:
            slow = slow.next
            fast = fast.next
        return fast
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
    ListNode *detectCycle(ListNode *head) {
        if (!head) return nullptr;
        ListNode* fast = head;
        ListNode* slow = head;
        while (fast && fast->next) {
            fast = fast->next->next;
            slow = slow->next;
            if (slow == fast) 
                break;
        }
        if (!fast || !fast->next || slow != fast) return nullptr;
        slow = head;
        while (slow != fast) {
            slow = slow->next;
            fast = fast->next;
        }
        return fast;
    }
};
```

### set

其实也可以简单一点，如果我们保存走过的每个位置不就好了吗？所以，对于Python来说，可以直接把对象放到set中去，这样，当我们再次遍历到已经访问过的节点时，说明有了环，直接返回该节点即可。

```python
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head: return None
        visited = set()
        while head:
            if head in visited:
                return head
            visited.add(head)
            head = head.next
        return None
```

对于C++来说，有set和unordered_set两种集合，这里使用unordered_set，里面存放的内容是指向节点的指针，放指针一是可以成功存放，第二是如果已经遍历过了某个节点就相当于遍历过了这个指针。

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
    ListNode *detectCycle(ListNode *head) {
        if (!head) return nullptr;
        unordered_set<ListNode*> visited;
        while (head) {
            if (visited.count(head))
                return head;
            visited.insert(head);
            head = head->next;
        }
        return nullptr;
    }
};
```

参考资料：

http://blog.csdn.net/monkeyduck/article/details/50439840
https://blog.csdn.net/l294265421/article/details/50478818

## 日期

2018 年 3 月 12 日 
2019 年 1 月 11 日 —— 小光棍节？

  [1]: https://img-blog.csdn.net/20160101111128525
