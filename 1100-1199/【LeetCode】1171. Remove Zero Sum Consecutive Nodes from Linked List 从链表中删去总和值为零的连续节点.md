

- 作者：    负雪明烛
- id：      fuxuemingzhu
- 个人博客：[http://fuxuemingzhu.cn/](http://fuxuemingzhu.cn/)

---
@[TOC](目录)

题目地址：https://leetcode.com/problems/remove-zero-sum-consecutive-nodes-from-linked-list/

## 题目描述

Given the head of a linked list, we repeatedly delete consecutive sequences of nodes that sum to 0 until there are no such sequences.

After doing so, return the head of the final linked list.  You may return any such answer.

(Note that in the examples below, all sequences are serializations of ListNode objects.)

Example 1:

    Input: head = [1,2,-3,3,1]
    Output: [3,1]
    Note: The answer [1,2,1] would also be accepted.

Example 2:

    Input: head = [1,2,3,-3,4]
    Output: [1,2,4]

Example 3:

    Input: head = [1,2,3,-3,-2]
    Output: [1]
 

Constraints:

1. The given linked list will contain between `1` and `1000` nodes.
1. Each node in the linked list has `-1000 <= node.val <= 1000`.


## 题目大意

删除一个链表中和为0的连续节点。


## 解题方法

### preSum + 字典

如果是一个数组，我们删除其连续和为0的子数组怎么办？应该能想到preSum的方式，即累计preSum保存到字典中，如果preSum出现过，那么说明有一部分的和为0.

如果改成单链表，也可以使用同样的方式。使用字典保存preSum，如果遇到了已经出现过的preSum，那么需要根据上个preSum出现的位置，删除这段区间内的所有节点。

对于链表而言，删除其中的一段是很简单的，可以直接修改指针就行。但是只修改指针并没有修改字典，对于字典来说，我们也要删除被删除的哪些节点对应的preSum，为此，我们必须再次遍历被删除的这一段链表，计算preSum，并且从字典中删除。

由于头结点可能被删除，所以添加了一个dummy节点，把修改的链表放入dummy的后面。

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
    ListNode* removeZeroSumSublists(ListNode* head) {
        unordered_map<int, ListNode*> m;
        ListNode* dummy = new ListNode(-10000);
        dummy->next = head;
        int preSum = 0;
        m[0] = dummy;
        ListNode* cur = head;
        while (cur) {
            preSum += cur->val;
            if (m.count(preSum)) {
                ListNode* pre = m[preSum];
                ListNode* cur = pre->next;
                int p = preSum + cur->val;
                while (p != preSum) {
                    m.erase(p);
                    cur = cur->next;
                    p += cur->val;
                }
                pre->next = cur->next;
            } else {
                m[preSum] = cur;
            }
            cur = cur->next;
        }
        return dummy->next;
    }
};
```

参考资料：https://leetcode.com/problems/remove-zero-sum-consecutive-nodes-from-linked-list/discuss/366319/JavaC%2B%2BPython-Greedily-Skip-with-HashMap

## 日期

2019 年 9 月 27 日 —— 昨天面快手，竟然是纯刷题


  [1]: https://assets.leetcode.com/uploads/2019/07/01/screen-shot-2019-07-01-at-53836-pm.png
