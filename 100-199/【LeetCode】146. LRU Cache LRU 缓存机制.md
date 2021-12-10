
作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)


题目地址：https://leetcode.com/problems/lru-cache/

## 题目描述

Design and implement a data structure for `Least Recently Used (LRU)` cache. It should support the following operations: `get` and `put`.

- `get(key)` - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
- `put(key, value)` - Set or insert the value if the key is not already present. When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.

The cache is initialized with a `positive` capacity.

Follow up:
Could you do both operations in `O(1)` time complexity?

Example:

    LRUCache cache = new LRUCache( 2 /* capacity */ );
    
    cache.put(1, 1);
    cache.put(2, 2);
    cache.get(1);       // returns 1
    cache.put(3, 3);    // evicts key 2
    cache.get(2);       // returns -1 (not found)
    cache.put(4, 4);    // evicts key 1
    cache.get(1);       // returns -1 (not found)
    cache.get(3);       // returns 3
    cache.get(4);       // returns 4

 
## 题目大意

实现一个LRU，LRU全称是Least Recently Used，即最近最久未使用的意思。

LRU算法的设计原则是：如果一个数据在最近一段时间没有被访问到，那么在将来它被访问的可能性也很小。也就是说，当限定的空间已存满数据时，应当把最久没有被访问到的数据淘汰。

题目中给出了LRU的负载大小，当数据被用到的时候变成了最新被使用的，当存放的数据达到了容量上线，需要把最近未被使用的弹出。

## 解题方法

### 字典+双向链表

如果看过Java的LinkedHashMap源码，大家都知道可以使用字典+双向链表来实现LRU。

其中双向链表的作用是用来维护使用的顺序的工具，把最近刚使用的放到链表最前面，一直未被使用的放到链表结尾，当达到容量的时候需要把链表结尾节点去除。

大家都知道链表的查找时间复杂度是O(N)，题目要求用O(1)的时间复杂度，那么就需要高效的查找方法。我们使用字典来达到这个目的！把链表的每个节点按照{key: node}的方式放入字典里，这样就能通过key快速查到链表节点，从而对该节点进行修改。

综上，我们要对链表实现两个函数：
1. 把一个节点从链表中删除（这就是为什么选择双向链表的原因，方便找到前后节点）
2. 把一个节点放入链表的头部（需要一个不保存数据的root节点，其prev和next分别指向链表尾部和头部）

这个题中，链表节点需要同时保存key和value。我们通过key在字典找到该节点，返回其val；当要删除一直没被使用过的链表尾部节点时，我们也要从字典中删除它，因此需要知道其key。

![此处输入图片的描述][1]

python代码如下：

```python
class ListNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = self
        self.next = self

class LRUCache:

    def __init__(self, capacity: int):
        self.dic = dict()
        self.capacity = capacity
        self.size = 0
        self.root = ListNode(0, 0)

    def get(self, key: int) -> int:
        if key in self.dic:
            node = self.dic[key]
            self.removeFromList(node)
            self.insertIntoHead(node)
            return node.value
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.dic:
            node = self.dic[key]
            self.removeFromList(node)
            self.insertIntoHead(node)
            node.value = value
        else:
            if self.size >= self.capacity:
                self.removeFromTail()
                self.size -= 1
            node = ListNode(key, value)
            self.insertIntoHead(node)
            self.dic[key] = node
            self.size += 1

    def removeFromList(self, node):
        if node == self.root: return
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node
        node.prev = node.next = None
    
    def insertIntoHead(self, node):
        head_node = self.root.next
        head_node.prev = node
        node.prev = self.root
        self.root.next = node
        node.next = head_node
    
    def removeFromTail(self):
        if self.size == 0: return
        tail_node = self.root.prev
        del self.dic[tail_node.key]
        self.removeFromList(tail_node)

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
```

参考资料：https://yikun.github.io/2015/04/03/%E5%A6%82%E4%BD%95%E8%AE%BE%E8%AE%A1%E5%AE%9E%E7%8E%B0%E4%B8%80%E4%B8%AALRU-Cache%EF%BC%9F/

## 日期

2019 年 9 月 13 日 —— 今天是中秋节，祝大家中秋快乐


  [1]: https://cloud.githubusercontent.com/assets/1736354/6984935/92033a96-da60-11e4-8754-66135bb0d233.png
