
作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)

题目地址：[https://leetcode.com/problems/palindrome-linked-list/#/description][1]


## 题目描述

Given a singly linked list, determine if it is a palindrome.

Follow up:
Could you do it in O(n) time and O(1) space?

## 题目大意

判断一个链表是不是回文链表。

## 解题方法

可以用一个栈，这样的时间复杂度为O(n),空间复杂度为O(n)不符合要求。但是能通过。

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
    public boolean isPalindrome(ListNode head) {
        if(head == null || head.next == null){
            return true;
        }
        ListNode temp = head;
        Stack<Integer> stack = new Stack<Integer>();
        while(temp != null){
            stack.push(temp.val);
            temp = temp.next;
        }
        while(head != null){
            int top = stack.pop();
            if(top != head.val){
                return false;
            }
            head = head.next;
        }        
        return true;
    }
}
```

二刷，Python。

同样使用了数组，但是判断回文的时候，直接使用的双指针从头和尾向中间遍历。

```python
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        vals = []
        while head:
            vals.append(head.val)
            head = head.next
        N = len(vals)
        left, right = 0, N - 1
        while left < right:
            if vals[left] != vals[right]:
                return False
            left += 1
            right -= 1
        return True
```

## 日期

2017 年 5 月 21 日 
2018 年 11 月 24 日 —— 周六快乐

  [1]: https://leetcode.com/problems/palindrome-linked-list/#/description
