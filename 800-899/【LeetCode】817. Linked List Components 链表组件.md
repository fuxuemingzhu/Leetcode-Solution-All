
作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)

题目地址：https://leetcode.com/problems/linked-list-components/description/

## 题目描述

We are given ``head``, the head node of a linked list containing unique integer values.

We are also given the list ``G``, a subset of the values in the linked list.

Return the number of connected components in ``G``, where two values are connected if they appear consecutively in the linked list.

Example 1:
    
    Input: 
    head: 0->1->2->3
    G = [0, 1, 3]
    Output: 2
    Explanation: 
    0 and 1 are connected, so [0, 1] and [3] are the two connected components.
    
Example 2:
    
    Input: 
    head: 0->1->2->3->4
    G = [0, 3, 1, 4]
    Output: 2
    Explanation: 
    0 and 1 are connected, 3 and 4 are connected, so [0, 1] and [3, 4] are the two connected components.

Note:

1. If N is the length of the linked list given by head, 1 <= N <= 10000.
1. The value of each node in the linked list will be in the range [0, N - 1].
1. 1 <= G.length <= 10000.
1. G is a subset of all values in the linked list.

## 题目大意

给出了一个不包含重复数字的链表，和由该链表部分节点元素构成的数组。要统计出这个数组能构成链表中的多少段联通分量。

## 解题方法

这个题乍一看，感觉很高大上，其实就是[【LeetCode】830. Positions of Large Groups 解题报告（Python）][1]的翻版嘛。

从左到右遍历链表依次，每遇到一个节点，就看看这个节点的数值在不在G中，并且这个节点的下一个节点是不是空（末尾），下一个节点值在不在G中。

如果当前的节点值在G中，而下一个节点是空或者节点值不在G中，那么就是一个新的分段呗。

这个题第一次提交的时候超时，超时原因应该在判断一个元素在不在列表中这步比较慢。使用set之后就能提交通过了。。


```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def numComponents(self, head, G):
        """
        :type head: ListNode
        :type G: List[int]
        :rtype: int
        """
        groups = 0
        subset = set(G)
        while head:
            if head.val in subset and (not head.next or head.next.val not in subset):
                groups += 1
            head = head.next
        return groups
```

二刷的时候使用判断是否连续，使用的一个变量，手动维护一个变量稍嫌麻烦。

注意set的写法，可以传入开始和结束两个指针。

C++版本的代码如下：

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
    int numComponents(ListNode* head, vector<int>& G) {
        set<int> s(G.begin(), G.end());
        ListNode* p = head;
        int res = 0;
        bool isCon = false;
        while (p) {
            if (s.count(p->val)) {
                if (!isCon) {
                    res ++;
                    isCon = true;
                }
            } else {
                isCon = false;
            }
            p = p->next;
        }
        return res;
    }
};
```

## 日期

2018 年 5 月 28 日 —— 太阳真的像日光灯～
2018 年 12 月 14 日 —— 12月过半，2019就要开始

  [1]: https://blog.csdn.net/fuxuemingzhu/article/details/80472242
