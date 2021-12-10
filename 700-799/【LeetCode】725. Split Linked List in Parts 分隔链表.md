作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---

@[TOC](目录)

题目地址：https://leetcode.com/problems/split-linked-list-in-parts/description/

## 题目描述

Given a (``singly``) linked list with head node ``root``, write a function to split the linked list into k consecutive linked list "parts".

The length of each part should be as equal as possible: no two parts should have a size differing by more than 1. This may lead to some parts being null.

The parts should be in order of occurrence in the input list, and parts occurring earlier should always have a size greater than or equal parts occurring later.

Return a List of ListNode's representing the linked list parts that are formed.

Examples 1->2->3->4, k = 5 // 5 equal parts [ [1], [2], [3], [4], null ]

Example 1:

    Input: 
    root = [1, 2, 3], k = 5
    Output: [[1],[2],[3],[],[]]
    Explanation:
    The input and each element of the output are ListNodes, not arrays.
    For example, the input root has root.val = 1, root.next.val = 2, \root.next.next.val = 3, and root.next.next.next = null.
    The first element output[0] has output[0].val = 1, output[0].next = null.
    The last element output[4] is null, but it's string representation as a ListNode is [].

Example 2:

    Input: 
    root = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], k = 3
    Output: [[1, 2, 3, 4], [5, 6, 7], [8, 9, 10]]
    Explanation:
    The input has been split into consecutive parts with size difference at most 1, and earlier parts are a larger size than the later parts.

Note:

1. The length of root will be in the range [0, 1000].
1. Each value of a node in the input will be an integer in the range [0, 999].
1. k will be an integer in the range [1, 50].

## 题目大意

把链表进行相等的切割成k份，当然可能存在不能正好切割的情况。如果有空余就在结尾补空列表，如果多余就在起始位置的链表多加上元素。

1.如果链表的长度比k小就用null来补充。  就如给的例1一样，链表长度为3但是k的值为5，所以将链表分为5段时，节点不够，所以后面的都用null来表示。
 
2.如果链表不能平均分的时候，各段相差的节点数不能超过1，并且前面分段的要比后面的长。  就如给的例2一样，链表长度为10，分为3段，此时不能平均分配，各段相差的不能超过1并且前面分段的要比后面的长，所以就分为三段：[1,2,3,4]、[5,6,7]、[8,9,10]。

3.最后将每段组成一个链表，然后全部装进数组中返回。

## 解题方法

这个题还真有意思。是个好题。


我们先对给定的链表求长度，然后除以k，会得到一个商和余数，商的数值代表平均分为k段之后每段有多少个节点，余数的数值代表前多少段需要多加一个节点，商和余数总共有以下几个情况：

（1）商为0，余数为0。

此时说明链表长度就是0，也不需要做什么处理，直接返回一个空数组就行。

（2）商为0，余数不为0。

说明此时的链表长度是小于k的，就如例1一样，商为0，余数为3。说明平均分为5段之后，平均每段有0个节点，然后前3段需要多加一个节点，那么正好就是：[1]、[2]、[3]、[]、[]。

（3）商不为0，余数为0。

说明此时正好能够将链表平均分为k段，每段的长度就是商的数值了。

（4）商不为0，余数不为0。

此时说明能将链表分为k段，但是还有多余的节点。而题中规定了各个分段的长度相差不能大于1，那么我们就只能让这多出的节点再次分给每段，而且每段只能分一个。并且题中还规定了前面的长度要比后面的常，所以我们就应该按照段的顺序再给分配一个了。需要注意这里的节点顺序不能乱。

我们肯定要循环k次，以生成题目要求的k个子列表。在求解每一段的时候，先遍历num个节点，如果有rem,就在每一段上加上一个节点。

python代码如下：

```python
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def splitListToParts(self, root, k):
        """
        :type root: ListNode
        :type k: int
        :rtype: List[ListNode]
        """
        nodes = []
        counts = 0
        each = root
        while each:
            counts += 1
            each = each.next
        num = counts / k
        rem = counts % k
        for i in range(k):
            head = ListNode(0)
            each = head
            for j in range(num):
                node = ListNode(root.val)
                each.next = node
                each = each.next
                root = root.next
            if rem and root:
                rmnode = ListNode(root.val)
                each.next = rmnode
                if root:
                    root = root.next
                rem -= 1
            nodes.append(head.next)
        return nodes
```

二刷的时候意识到，这个题一点都不难。主要是每段多少个节点的判断，这个可以很简单的计算出来：首先要平分，直接相除即可得到；然后整除有剩余数字的话，那么会分到前几个位置。剩下的工作就是把链表切开，每段是对应的长度即可。所以封装了一个求长度的函数，一个把链表切出长度是k并返回下一个节点的函数，这个函数记得把链表切断。

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
    vector<ListNode*> splitListToParts(ListNode* root, int k) {
        int len = getLength(root);
        int c = len / k; // each part num
        int r = len % k; // remain
        vector<ListNode*> res(k);
        int pos = 0;
        while (root) {
            int curlen = r > 0 ? c + 1 : c;
            --r;
            res[pos] = root;
            ++pos;
            root = cut(root, curlen);
        }
        return res;
    }
    int getLength(ListNode* root) {
        int res = 0;
        while (root) {
            ++res;
            root = root->next;
        }
        return res;
    }
    // cut root, len = k, return k + 1
    ListNode* cut(ListNode* root, int k) {
        int count = 0;
        ListNode* prev = nullptr;
        while (count < k) {
            prev = root;
            root = root->next;
            ++count;
        }
        prev->next = nullptr;
        return root;
    }
};
```

参考文献：http://blog.csdn.net/Leafage_M/article/details/78586549

## 日期

2018 年 3 月 13 日 
2019 年 2 月 26 日 —— 二月就要完了
