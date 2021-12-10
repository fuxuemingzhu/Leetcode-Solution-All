- 作者：    负雪明烛
- id：      fuxuemingzhu
- 个人博客：[http://fuxuemingzhu.cn/](http://fuxuemingzhu.cn/)

---
@[TOC](目录)


题目地址：https://leetcode.com/problems/next-greater-node-in-linked-list/

## 题目描述

We are given a linked list with ``head`` as the first node.  Let's number the nodes in the list: ``node_1, node_2, node_3, ...`` etc.

Each node may have a next larger value: for ``node_i``, ``next_larger(node_i)`` is the ``node_j.val`` such that ``j > i``, ``node_j.val > node_i.val``, and ``j`` is the smallest possible choice.  If such a ``j`` does not exist, the next larger value is ``0``.

Return an array of integers ``answer``, where ``answer[i] = next_larger(node_{i+1})``.

Note that in the example **inputs** (not outputs) below, arrays such as ``[2,1,5]`` represent the serialization of a linked list with a head node value of 2, second node value of 1, and third node value of 5.

Example 1:
    
    Input: [2,1,5]
    Output: [5,5,0]

Example 2:

    Input: [2,7,4,3,5]
    Output: [7,0,5,5,0]

Example 3:

    Input: [1,7,5,1,9,2,5,1]
    Output: [7,9,9,9,0,5,0,0]
 
Note:

1. ``1 <= node.val <= 10^9`` for each node in the linked list.
1. The given list has length in the range ``[0, 10000]``.


## 题目大意

给出了一个单链表，现在要找到每个节点的后面第一个比它大的元素是多少。如果后面不存在比它大的，那么放0.

## 解题方法

### 单调递减栈

这个题和之前的[503. Next Greater Element II][1]做法一样的，都是使用一个`单调递减栈`保存每个数字的下标。

首先，把链表遍历一遍，转化成数组问题。

然后遍历数组，需要维护单调递减栈，每个元素的位置都要往栈里面放，放之前先把栈里面小于该元素的全部弹出。

如果遇到了一个数字n比栈顶元素stack[-1]为下标的数字更大时，需要一直退栈，而且每次退栈的时候都要把该栈顶元素stack[-1]对应res位置的结果设置为n。退栈到栈顶元素大于等于目前元素为止。

方法讲完了，下面解释下为什么能这么做。

由于栈中的保存的每个位置对应的元素是单调递减的，那么说明栈中的数字都没有遇到比它更大的数字。所以当我们遇到一个更大的数字的时候，那么把栈中的比当前元素小都依次退出来，此时此刻的元素是退栈的元素的next greater number。

如果遍历完成了一次Nums，栈中还有元素，即有些元素没有找到next greater number，按照题目要求，这些元素对应的位置应该设定成0，所以我们可以在res初始化的时候就设定默认值为0.

举例说明，注意栈中保存的是下标：

	Input: [2,7,4,3,5]
	Output: [7,0,5,5,0]

| 输入 | 栈 | 结果 |
|--|--|--|
| 2 | [0] | [0,0,0,0,0]|
| 7 | [`1`] | [7,0,0,0,0]|
| 4 | [1,2] | [7,0,0,0,0]|
| 3 | [1,2,3] | [7,0,0,0,0]|
| 5 | [1,5] | [7,0,5,5,0]|

Python代码如下：

```python
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def nextLargerNodes(self, head):
        """
        :type head: ListNode
        :rtype: List[int]
        """
        nums = []
        while head:
            nums.append(head.val)
            head = head.next
        stack = []
        res = [0] * len(nums)
        for i, n in enumerate(nums):
            while stack and nums[stack[-1]] < n:
                res[stack.pop()] = n
            stack.append(i)
        return res
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
    vector<int> nextLargerNodes(ListNode* head) {
        vector<int> nums;
        while (head) {
            nums.push_back(head->val);
            head = head->next;
        }
        vector<int> res(nums.size(), 0);
        stack<int> s;
        for (int i = 0; i < nums.size(); ++i) {
            while (!s.empty() && nums[s.top()] < nums[i]) {
                res[s.top()] = nums[i];
                s.pop();
            }
            s.push(i);
        }
        return res;
    }
};
```

## 日期

2019 年 4 月 5 日 —— 清明节休息一下～
2019 年 9 月 27 日 —— 昨天面快手，竟然是纯刷题


  [1]: https://blog.csdn.net/fuxuemingzhu/article/details/79463006
