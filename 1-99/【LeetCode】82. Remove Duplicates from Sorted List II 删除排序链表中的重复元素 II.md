作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---

题目地址：https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/description/

## 题目描述

Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.

Example 1:

    Input: 1->2->3->3->4->4->5
    Output: 1->2->5

Example 2:

    Input: 1->1->1->2->3
    Output: 2->3

## 题目大意

在一个**有序**链表中，如果一个节点的值出现的不止一次，那么把这个节点删除掉。

## 解题方法

### 递归

注意审题啊，这个distinct的意思并不是去重，而是删除出现次数不止一次的。

去重的可以看这个题：[83. Remove Duplicates from Sorted List](https://blog.csdn.net/fuxuemingzhu/article/details/51290506)

使用递归解法，重点在于找出头结点。如果头结点和第二个节点相等，那么需要一直遍历到第一个和head不相等的节点作为新的头结点，再重复这个过程。

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
    ListNode* deleteDuplicates(ListNode* head) {
        if (!head || !head->next) {
            return head;
        }
        if (head->val != head->next->val) {
            head->next = deleteDuplicates(head->next);
        } else {
            ListNode* move = head->next;
            while (move && head->val == move->val) {
                move = move->next;
            }
            return deleteDuplicates(move);
        }
        return head;
    }
};
```

### 遍历

说实话，这个非递归的解法写了挺久的。设定了两个指针pre和cur，确保pre节点指向结果链表的尾部，而cur指向当前已经判断多了的链表中重复元素的末尾（若当前不重复，就是该节点），pre->next指向尚未判断的剩余链表的头部。判断是否有重复元素的方法是pre->next和cur是否相等。举例说明：

	1. 1(pre,pre->next=2)->2(cur)->3->3->4->4->5
	2. 1->2(pre,pre->next=4)->3->3(cur)->4->4->5
	3. 1->2(pre,pre->next=5)->3->3->4->4(cur)->5
	4. 1->2(pre,pre->next=None)->3->3->4->4->5(cur)
	5. 1->2->3->3->4->4->5(pre,pre->next=None)(cur=None)

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
    ListNode* deleteDuplicates(ListNode* head) {
        if (!head || !head->next) return head;
        ListNode* preHead = new ListNode(0);
        preHead->next = head;
        ListNode* pre = preHead;
        ListNode* cur = head;
        while (cur) {
            //跳过当前的重复节点，使得cur指向当前重复元素的最后一个位置
            while (cur->next && cur->val == cur->next->val) {
                cur = cur->next;
            }
            if (pre->next == cur) {
                //pre和cur之间没有重复节点，pre后移
                pre = pre->next; 
            } else {
                //pre->next指向cur的下一个位置（相当于跳过了当前的重复元素）
                //但是pre不移动，仍然指向之前的链表结尾
                pre->next = cur->next;
            }
            cur = cur->next;
        }
        return preHead->next;
    }
};
```


### 字典统计次数

如果忽略有序这个特征，可以统计每个节点出现的次数，判断出现次数是不是1。

第二次遍历的时候，查找下个节点的值出现的次数如果不是1次，那么就删除下个节点。修改这个节点的下个指针指向下下个节点，这是指向该节点位置的指针不要动，因为还要判断新的next值。

python代码如下：

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        root = ListNode(0)
        root.next = head
        val_list = []
        while head:
            val_list.append(head.val)
            head = head.next
        counter = collections.Counter(val_list)
        head = root
        while head and head.next:
            if counter[head.next.val] != 1:
                head.next = head.next.next
            else:
                head = head.next
        return root.next
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
    ListNode* deleteDuplicates(ListNode* head) {
        unordered_map<int, int> m;
        ListNode dummy(0);
        ListNode* dummy_move = &dummy;
        ListNode* move = head;
        while (move) {
            m[move->val]++;
            move = move->next;
        }
        move = head;
        while (move) {
            if (m[move->val] == 1) {
                dummy_move->next = move;
                dummy_move = dummy_move->next;
            }
            move = move->next;
        }
        dummy_move->next = nullptr;
        return dummy.next;
    }
};
```

参考资料：https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/discuss/28335/My-accepted-Java-code

## 日期

2018 年 6 月 23 日 ———— 美好的周末要从刷题开始


  [1]: https://upload.wikimedia.org/wikipedia/commons/0/0f/Insertion-sort-example-300px.gif
  [2]: https://blog.csdn.net/happyaaaaaaaaaaa/article/details/51619973
