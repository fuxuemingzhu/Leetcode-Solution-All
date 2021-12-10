作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---

@[TOC](目录)

题目地址：https://leetcode.com/problems/linked-list-random-node/description/

## 题目描述

Given a singly linked list, return a random node's value from the linked list. Each node must have the ``same probability`` of being chosen.

Follow up:
What if the linked list is extremely large and its length is unknown to you? Could you solve this efficiently without using extra space?

    Example:
    
    // Init a singly linked list [1,2,3].
    ListNode head = new ListNode(1);
    head.next = new ListNode(2);
    head.next.next = new ListNode(3);
    Solution solution = new Solution(head);
    
    // getRandom() should return either 1, 2, or 3 randomly. Each element should have equal probability of returning.
    solution.getRandom();

## 题目大意

随机从链表中抽出一个节点的数字。

## 解题方法

### 数组保存再随机选择

我使用一个数组保存了，然后从中间随机找的index。

代码：

```python
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):

    def __init__(self, head):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        :type head: ListNode
        """
        self.stack = []
        while head:
            self.stack.append(head.val)
            head = head.next
        

    def getRandom(self):
        """
        Returns a random node's value.
        :rtype: int
        """
        _len = len(self.stack)
        return self.stack[random.randint(0, _len - 1)]


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()
```

### 蓄水池抽样

这个做法和[398. Random Pick Index](https://blog.csdn.net/fuxuemingzhu/article/details/79540576)完全一致，即在一个流中随机选择一个数字。

蓄水池采样算法（Reservoir Sampling）是说在一个流中，随机选择k个数字，保证每个数字被选择的概率相等。

算法的过程：

假设数据序列的规模为 n，需要采样的数量的为 k。

首先构建一个可容纳 k 个元素的数组，将序列的前 k 个元素放入数组中。

然后从第 k+1 个元素开始，以 k/n 的概率来决定该元素是否被替换到数组中（数组中的元素被替换的概率是相同的）。 当遍历完所有元素之后，数组中剩下的元素即为所需采取的样本。

这个题中k = 1。

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
    /** @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node. */
    Solution(ListNode* head) : h_(head) {
    }
    
    /** Returns a random node's value. */
    int getRandom() {
        ListNode* head = h_;
        int cnt = 0, res = 0;
        while (head) {
            ++cnt;
            if (rand() % cnt == 0)
                res = head->val;
            head = head->next;
        }
        return res;
    }
private:
    ListNode* h_;
};

/**
 * Your Solution object will be instantiated and called as such:
 * Solution obj = new Solution(head);
 * int param_1 = obj.getRandom();
 */
```

## 日期

2018 年 3 月 8 日 
2019 年 2 月 26 日 —— 二月就要完了
