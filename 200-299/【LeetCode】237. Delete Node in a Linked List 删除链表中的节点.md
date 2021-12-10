- 作者：    负雪明烛
- id：      fuxuemingzhu
- 个人博客：[http://fuxuemingzhu.cn/](http://fuxuemingzhu.cn/)

---
@[TOC](目录)

[LeetCode]

题目地址：[https://leetcode.com/problems/delete-node-in-a-linked-list/](https://leetcode.com/problems/delete-node-in-a-linked-list/)

Total Accepted: 78258 Total Submissions: 179086 Difficulty: Easy

## 题目描述


Write a function to delete a ``node`` (except the tail) in a singly linked list, given only access to that node.

Given linked list -- head = [4,5,1,9], which looks like following:

    4 -> 5 -> 1 -> 9

Example 1:

	Input: head = [4,5,1,9], node = 5
	Output: [4,1,9]
	Explanation: You are given the second node with value 5, the linked list
	             should become 4 -> 1 -> 9 after calling your function.

Example 2:

	Input: head = [4,5,1,9], node = 1
	Output: [4,5,9]
	Explanation: You are given the third node with value 1, the linked list
	             should become 4 -> 5 -> 9 after calling your function.

Note:

1. The linked list will have at least two elements.
1. All of the nodes' values will be unique.
1. The given node will not be the tail and it will always be a valid node of the linked list.
1. Do not return anything from your function.


## 题目大意

给出了一个节点，这个节点是在一个单链表中的，并且这个节点不是最后一个节点。现在要我们删除这个节点。

## 解题方法

### 设置当前节点的值为下一个

拿到这个题时以为要从头找到这个节点前一个节点，然后删除当前节点。这个应该是正常思路。

但是，题目只给出了删除的这个节点，没有给出根节点。所以可以通过这个将当前的节点的数值改成下面的节点的值，然后删除下一个节点的方式。

链表基本操作，记待删除节点为node：

令node.val = node.next.val，node.next = node.next.next即可

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
	    public void deleteNode(ListNode node) {
	        node.val=node.next.val;
	        node.next=node.next.next;
	    }
	}
```

python代码如下：

```python
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next
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
    void deleteNode(ListNode* node) {
        node->val = node->next->val;
        node->next = node->next->next;
    }
};
```

## 日期

2016/4/30 0:39:40 
2018 年 11 月 11 日 —— 剁手节快乐
2019 年 9 月 27 日 —— 昨天面快手，竟然是纯刷题
