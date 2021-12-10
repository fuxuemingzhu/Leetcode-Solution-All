作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)

[LeetCode]

题目地址：[https://leetcode.com/problems/linked-list-cycle/](https://leetcode.com/problems/linked-list-cycle/)

Total Accepted: 102417 Total Submissions: 277130 Difficulty: Easy


## 题目描述


Given a linked list, determine if it has a cycle in it.

To represent a cycle in the given linked list, we use an integer pos which represents the position (0-indexed) in the linked list where tail connects to. If pos is -1, then there is no cycle in the linked list.

 

Example 1:

Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where tail connects to the second node.

![在这里插入图片描述](https://assets.leetcode.com/uploads/2018/12/07/circularlinkedlist.png)

Example 2:

	Input: head = [1,2], pos = 0
	Output: true
	Explanation: There is a cycle in the linked list, where tail connects to the first node.

![在这里插入图片描述](https://assets.leetcode.com/uploads/2018/12/07/circularlinkedlist_test2.png)

Example 3:

	Input: head = [1], pos = -1
	Output: false
	Explanation: There is no cycle in the linked list.

![在这里插入图片描述](https://assets.leetcode.com/uploads/2018/12/07/circularlinkedlist_test3.png)
 

Follow up:

Can you solve it using O(1) (i.e. constant) memory?

## 题目大意

判断单链表里是否有环。

## 解题方法

### 双指针

双指针的方法。

思路是两个指针，一个每次走两步，一个每次走一步，循环下去，只要两者能够重逢说明有环。

Java代码如下：

```java
public class Solution {
    public boolean hasCycle(ListNode head) {
        if(head==null) return false;
        ListNode fast = head;
        ListNode slow = head;
        while(slow!=null){
            if(fast.next==null || fast.next.next==null) return false;
            fast=fast.next.next;
            slow=slow.next;
            if(fast==slow) break;
        }
        return true;
    }
}
```
AC:1ms

看了官方解答之后，发现可以优化，优化如下：

```java
	public class Solution {
	    public boolean hasCycle(ListNode head) {
	        if(head==null||head.next==null) return false;
	        ListNode fast = head.next;
	        ListNode slow = head;
	        while(slow!=fast){
	            if(fast.next==null || fast.next.next==null) return false;
	            fast=fast.next.next;
	            slow=slow.next;
	        }
	        return true;
	    }
	}
```

我想的是只要走的慢的这个不为空的话，就一直走好了。 官方解答想的是两者不重合就一直走。

二刷，Python。

上python版本的。

```python
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        slow, fast = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if slow == fast:
                return True
        return False
```

三刷，python.

```python
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head: return False
        slow, fast = head, head.next
        while fast and fast.next:
            if fast == slow:
                return True
            fast = fast.next.next
            slow = slow.next
        return False
```

四刷，C++。注意C++里面全部用的是指针操作。代码如下：

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
    bool hasCycle(ListNode *head) {
        if (!head) return false;
        ListNode* fast = head;
        ListNode* slow = head;
        while (fast && fast->next) {
            fast = fast->next->next;
            slow = slow->next;
            if (fast == slow)
                return true;
        }
        return false;
    }
};
```

### 保存已经走过的路径

官方解答的HashTable的方法。记录下来哪些已经走了，只要走到之前走过的节点说明有环。

```java
public class Solution {
    public boolean hasCycle(ListNode head) {
        HashSet<ListNode> hash=new HashSet();
        while(head!=null){
            if(hash.contains(head)){
                return true;
            }else{
                hash.add(head);
            }
            head=head.next;
        }
        return false;
    }
}
```
AC:10ms


## 日期

2016/5/2 17:24:37 
2018 年 11 月 24 日 —— 周六快乐
2019 年 1 月 11 日 —— 小光棍节？
