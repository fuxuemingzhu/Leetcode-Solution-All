作者： **负雪明烛**
id：	**fuxuemingzhu**
个人公众号：**负雪明烛**
个人博客：	[http://fuxuemingzhu.cn/](http://fuxuemingzhu.cn/)

---
@[TOC](目录)


题目地址：https://leetcode-cn.com/problems/copy-list-with-random-pointer/

## 题目描述


给你一个长度为 `n` 的链表，每个节点包含一个额外增加的随机指针 `random` ，该指针可以指向链表中的任何节点或空节点。

构造这个链表的 深拷贝。 深拷贝应该正好由 `n` 个 全新 节点组成，其中每个新节点的值都设为其对应的原节点的值。新节点的 `next` 指针和 `random` 指针也都应指向复制链表中的新节点，并使原链表和复制链表中的这些指针能够表示相同的链表状态。复制链表中的指针都不应指向原链表中的节点 。

例如，如果原链表中有 `X` 和 `Y` 两个节点，其中 `X.random --> Y` 。那么在复制链表中对应的两个节点 `x` 和 `y` ，同样有 `x.random --> y` 。

返回复制链表的头节点。

用一个由 `n` 个节点组成的链表来表示输入/输出中的链表。每个节点用一个 `[val, random_index]` 表示：

- `val`：一个表示 `Node.val` 的整数。
- `random_index`：随机指针指向的节点索引（范围从 `0` 到 `n-1`）；如果不指向任何节点，则为  `null` 。

你的代码 **只** 接受原链表的头节点 `head` 作为传入参数。

 

示例 1：

![在这里插入图片描述](https://img-blog.csdnimg.cn/img_convert/b56618bcee565c8a6697b3d2bf2a6cca.png)

	
	
	输入：head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
	输出：[[7,null],[13,0],[11,4],[10,2],[1,0]]

示例 2：

![在这里插入图片描述](https://img-blog.csdnimg.cn/img_convert/33ab474db8732a4109ca16bc9ff75dae.png)

	
	输入：head = [[1,1],[2,1]]
	输出：[[1,1],[2,1]]

示例 3：

![在这里插入图片描述](https://img-blog.csdnimg.cn/img_convert/6d89896ff7aa904e4b7b9b79ce51b0e6.png)
	
	
	输入：head = [[3,null],[3,0],[3,null]]
	输出：[[3,null],[3,0],[3,null]]

示例 4：
	
	输入：head = []
	输出：[]
	解释：给定的链表为空（空指针），因此返回 null。
	 

提示：

- `0 <= n <= 1000`
- `-10000 <= Node.val <= 10000`
- Node.random 为空（null）或指向链表中的节点。


## 题目大意

复制一个复杂链表，这个复杂链表是指出了值和next指针外，还有一个random指针可能指向任何位置的链表节点或空。

## 解题方法

这个题是剑指Offer的“面试题26：复杂链表的复制”原题。书上的做法是在原先的每个节点之后进行复制了一个节点，从而构成了一个二倍长度的单链表，然后再修改random指针。这样做的好处是没有使用额外空间，但是缺点是做法比较麻烦。


一个更简洁的做法是使用 HashMap，在这个 HashMap 里，记录了 老链表的每个节点 和 新链表的每个节点的 对应关系。

第一步，先构造了一个纯next的链表；
第二部，对链表再次循环，修改每个节点的 random 的指针了。


Python 代码如下：

```python
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random
"""
class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        nodeDict = dict()
        dummy = Node(0, None, None)
        nodeDict[head] = dummy
        newHead, pointer = dummy, head
        while pointer:
            node = Node(pointer.val, pointer.next, None)
            nodeDict[pointer] = node
            newHead.next = node
            newHead, pointer = newHead.next, pointer.next
        pointer = head
        while pointer:
            if pointer.random:
                nodeDict[pointer].random = nodeDict[pointer.random]
            pointer = pointer.next
        return dummy.next
```

C++ 代码如下：

```cpp
/*
// Definition for a Node.
class Node {
public:
    int val;
    Node* next;
    Node* random;
    
    Node(int _val) {
        val = _val;
        next = NULL;
        random = NULL;
    }
};
*/

class Solution {
public:
    Node* copyRandomList(Node* head) {
        if (!head) return nullptr;
        unordered_map<Node*, Node*> copyMap;
        Node* newHead = new Node(head->val);
        Node* moveOld = head;
        Node* moveNew = newHead;
        while (moveOld) {
            copyMap[moveOld] = moveNew;
            moveNew->next = moveOld->next ? new Node(moveOld->next->val) : nullptr;
            moveNew = moveNew->next;
            moveOld = moveOld->next;
        }
        moveOld = head;
        moveNew = newHead;
        while (moveOld) {
            moveNew->random = copyMap[moveOld->random];
            moveNew = moveNew->next;
            moveOld = moveOld->next;
        }
        return newHead;
    }
};
```

## 日期

2018 年 6 月 23 日 —— 美好的周末要从刷题开始
2021 年 7 月 22 日 —— 最近天气一直是阴天下雨，希望天气好点
