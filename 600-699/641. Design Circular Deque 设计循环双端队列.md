作者： 		负雪明烛 
id：				fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---

题目地址：https://leetcode.com/problems/design-circular-deque/description/

## 题目描述：

Design your implementation of the circular double-ended queue (deque).
Your implementation should support following operations:

- MyCircularDeque(k): Constructor, set the size of the deque to be k.
- insertFront(): Adds an item at the front of Deque. Return true if the operation is successful.
- insertLast(): Adds an item at the rear of Deque. Return true if the operation is successful.
- deleteFront(): Deletes an item from the front of Deque. Return true if the operation is successful.
- deleteLast(): Deletes an item from the rear of Deque. Return true if the operation is successful.
- getFront(): Gets the front item from the Deque. If the deque is empty, return -1.
- getRear(): Gets the last item from Deque. If the deque is empty, return -1.
- isEmpty(): Checks whether Deque is empty or not. 
- isFull(): Checks whether Deque is full or not.

Example:

    MyCircularDeque circularDeque = new MycircularDeque(3); // set the size to be 3
    circularDeque.insertLast(1);			// return true
    circularDeque.insertLast(2);			// return true
    circularDeque.insertFront(3);			// return true
    circularDeque.insertFront(4);			// return false, the queue is full
    circularDeque.getRear();  				// return 32
    circularDeque.isFull();				// return true
    circularDeque.deleteLast();			// return true
    circularDeque.insertFront(4);			// return true
    circularDeque.getFront();				// return 4
 
Note:

- All values will be in the range of [1, 1000].
- The number of operations will be in the range of [1, 1000].
- Please do not use the built-in Deque library.

## 题目大意

实现一个双向环形链表。

## 解题方法

### 使用列表

和[622. Design Circular Queue][1]很类似了，622题要求的是单向的环形链表，这个题要求是双向的。

做法同样是采用和622题目类似的“作弊”做法，用一个list实现类似的环形列表。因为是双向链表，所以可以从头尾插入元素，对应了list的insert和append方法。

特别注意的是，插入元素，无论是在头尾插入，要移动的指针都是rear。

我这个题的做法比622更加成熟一点，622是通过头部指针来实现的，这个题里面是直接操作的头部元素导致后面的元素跟着变化，头部指针没有用到。。

这么一说可以把头部指针删除了23333.

在这么一说发现rear一直指向的是list的结尾，所以也可以删除了23333.

没删除头部指针的代码如下：

```python
class MyCircularDeque(object):

    def __init__(self, k):
        """
        Initialize your data structure here. Set the size of the deque to be k.
        :type k: int
        """
        self.queue = []
        self.size = k
        self.front = 0
        self.rear = 0

    def insertFront(self, value):
        """
        Adds an item at the front of Deque. Return true if the operation is successful.
        :type value: int
        :rtype: bool
        """
        if not self.isFull():
            self.queue.insert(0, value)
            self.rear += 1
            return True
        else:
            return False
        

    def insertLast(self, value):
        """
        Adds an item at the rear of Deque. Return true if the operation is successful.
        :type value: int
        :rtype: bool
        """
        if not self.isFull():
            self.queue.append(value)
            self.rear += 1
            return True
        else:
            return False

    def deleteFront(self):
        """
        Deletes an item from the front of Deque. Return true if the operation is successful.
        :rtype: bool
        """
        if not self.isEmpty():
            self.queue.pop(0)
            self.rear -= 1
            return True
        else:
            return False

    def deleteLast(self):
        """
        Deletes an item from the rear of Deque. Return true if the operation is successful.
        :rtype: bool
        """
        if not self.isEmpty():
            self.queue.pop()
            self.rear -= 1
            return True
        else:
            return False

    def getFront(self):
        """
        Get the front item from the deque.
        :rtype: int
        """
        if self.isEmpty():
            return -1
        else:
            return self.queue[self.front]

    def getRear(self):
        """
        Get the last item from the deque.
        :rtype: int
        """
        if self.isEmpty():
            return -1
        else:
            return self.queue[self.rear -1]

    def isEmpty(self):
        """
        Checks whether the circular deque is empty or not.
        :rtype: bool
        """
        return self.front == self.rear

    def isFull(self):
        """
        Checks whether the circular deque is full or not.
        :rtype: bool
        """
        return self.rear - self.front == self.size


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()
```

其实可以删除头指针，因为头指针一直指向0.

删除头部指针的代码如下：

```python
class MyCircularDeque(object):

    def __init__(self, k):
        """
        Initialize your data structure here. Set the size of the deque to be k.
        :type k: int
        """
        self.queue = []
        self.size = k
        self.rear = 0

    def insertFront(self, value):
        """
        Adds an item at the front of Deque. Return true if the operation is successful.
        :type value: int
        :rtype: bool
        """
        if not self.isFull():
            self.queue.insert(0, value)
            self.rear += 1
            return True
        else:
            return False
        

    def insertLast(self, value):
        """
        Adds an item at the rear of Deque. Return true if the operation is successful.
        :type value: int
        :rtype: bool
        """
        if not self.isFull():
            self.queue.append(value)
            self.rear += 1
            return True
        else:
            return False

    def deleteFront(self):
        """
        Deletes an item from the front of Deque. Return true if the operation is successful.
        :rtype: bool
        """
        if not self.isEmpty():
            self.queue.pop(0)
            self.rear -= 1
            return True
        else:
            return False

    def deleteLast(self):
        """
        Deletes an item from the rear of Deque. Return true if the operation is successful.
        :rtype: bool
        """
        if not self.isEmpty():
            self.queue.pop()
            self.rear -= 1
            return True
        else:
            return False

    def getFront(self):
        """
        Get the front item from the deque.
        :rtype: int
        """
        if self.isEmpty():
            return -1
        else:
            return self.queue[0]

    def getRear(self):
        """
        Get the last item from the deque.
        :rtype: int
        """
        if self.isEmpty():
            return -1
        else:
            return self.queue[self.rear -1]

    def isEmpty(self):
        """
        Checks whether the circular deque is empty or not.
        :rtype: bool
        """
        return 0 == self.rear

    def isFull(self):
        """
        Checks whether the circular deque is full or not.
        :rtype: bool
        """
        return self.rear == self.size


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()
```

rear 始终等于 len(self.queue)，所以完全可以删除。

删除front和rear指针的代码如下：

```python
class MyCircularDeque(object):

    def __init__(self, k):
        """
        Initialize your data structure here. Set the size of the deque to be k.
        :type k: int
        """
        self.queue = []
        self.size = k

    def insertFront(self, value):
        """
        Adds an item at the front of Deque. Return true if the operation is successful.
        :type value: int
        :rtype: bool
        """
        if not self.isFull():
            self.queue.insert(0, value)
            return True
        else:
            return False
        

    def insertLast(self, value):
        """
        Adds an item at the rear of Deque. Return true if the operation is successful.
        :type value: int
        :rtype: bool
        """
        if not self.isFull():
            self.queue.append(value)
            return True
        else:
            return False

    def deleteFront(self):
        """
        Deletes an item from the front of Deque. Return true if the operation is successful.
        :rtype: bool
        """
        if not self.isEmpty():
            self.queue.pop(0)
            return True
        else:
            return False

    def deleteLast(self):
        """
        Deletes an item from the rear of Deque. Return true if the operation is successful.
        :rtype: bool
        """
        if not self.isEmpty():
            self.queue.pop()
            return True
        else:
            return False

    def getFront(self):
        """
        Get the front item from the deque.
        :rtype: int
        """
        if self.isEmpty():
            return -1
        else:
            return self.queue[0]

    def getRear(self):
        """
        Get the last item from the deque.
        :rtype: int
        """
        if self.isEmpty():
            return -1
        else:
            return self.queue[-1]

    def isEmpty(self):
        """
        Checks whether the circular deque is empty or not.
        :rtype: bool
        """
        return 0 == len(self.queue)

    def isFull(self):
        """
        Checks whether the circular deque is full or not.
        :rtype: bool
        """
        return self.size == len(self.queue)


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()
```

### 双向链表

上面的解法直接使用了内置数据结构list，在头部插入的效率比较慢，时间复杂度是O(N)！所以我使用了双向链表模拟deque.

维护双向链表的方式和STL的list一样。对啊，可以直接用List。。方法就不仔细讲了。

```cpp
struct Node {
    Node* prev;
    Node* next;
    int val;
    Node(int v) : val(v) {};
};
struct List {
    Node* dummy;
    int size;
    List() : size(0) {
        dummy = new Node(0);
        dummy->next = dummy;
        dummy->prev = dummy;
    };
};
class MyCircularDeque {
public:
    /** Initialize your data structure here. Set the size of the deque to be k. */
    MyCircularDeque(int k) {
        maxSize = k;
    }
    
    /** Adds an item at the front of Deque. Return true if the operation is successful. */
    bool insertFront(int value) {
        if (list.size == maxSize)
            return false;
        Node* cur = new Node(value);
        Node* prev = list.dummy->prev;
        list.dummy->prev = cur;
        cur->prev = prev;
        prev->next = cur;
        cur->next = list.dummy;
        ++list.size;
        return true;
    }
    
    /** Adds an item at the rear of Deque. Return true if the operation is successful. */
    bool insertLast(int value) {
        if (list.size == maxSize)
            return false;
        Node* cur = new Node(value);
        Node* next = list.dummy->next;
        list.dummy->next = cur;
        cur->next = next;
        next->prev = cur;
        cur->prev = list.dummy;
        ++list.size;
        return true;
    }
    
    /** Deletes an item from the front of Deque. Return true if the operation is successful. */
    bool deleteFront() {
        if (list.size == 0) return false;
        Node* prev = list.dummy->prev;
        Node* pprev = prev->prev;
        list.dummy->prev = pprev;
        pprev->next = list.dummy;
        --list.size;
        return true;
    }
    
    /** Deletes an item from the rear of Deque. Return true if the operation is successful. */
    bool deleteLast() {
        if (list.size == 0) return false;
        Node* next = list.dummy->next;
        Node* nnext = next->next;
        list.dummy->next = nnext;
        nnext->prev = list.dummy;
        --list.size;
        return true;
    }
    
    /** Get the front item from the deque. */
    int getFront() {
        if (list.size == 0) return -1;
        return list.dummy->prev->val;
    }
    
    /** Get the last item from the deque. */
    int getRear() {
        if (list.size == 0) return -1;
        return list.dummy->next->val;
    }
    
    /** Checks whether the circular deque is empty or not. */
    bool isEmpty() {
        return list.size == 0;
    }
    
    /** Checks whether the circular deque is full or not. */
    bool isFull() {
        return list.size == maxSize;
    }
private:
    List list;
    int maxSize;
};

/**
 * Your MyCircularDeque object will be instantiated and called as such:
 * MyCircularDeque obj = new MyCircularDeque(k);
 * bool param_1 = obj.insertFront(value);
 * bool param_2 = obj.insertLast(value);
 * bool param_3 = obj.deleteFront();
 * bool param_4 = obj.deleteLast();
 * int param_5 = obj.getFront();
 * int param_6 = obj.getRear();
 * bool param_7 = obj.isEmpty();
 * bool param_8 = obj.isFull();
 */
```

## 日期

2018 年 7 月 13 日 —— 早起困一上午，中午必须好好休息才行啊
2019 年 2 月 26 日 —— 二月就要完了

  [1]: https://blog.csdn.net/fuxuemingzhu/article/details/81027583
