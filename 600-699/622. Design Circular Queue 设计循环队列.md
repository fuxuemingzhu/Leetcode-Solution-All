
作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)

题目地址：https://leetcode.com/problems/design-circular-queue/description/

## 题目描述

Design your implementation of the circular queue. The circular queue is a linear data structure in which the operations are performed based on FIFO (First In First Out) principle and the last position is connected back to the first position to make a circle. It is also called ‘Ring Buffer’.
One of the Benefits of the circular queue is that we can make use of the spaces in front of the queue. In a normal queue, once the queue becomes full, we can not insert the next element even if there is a space in front of the queue. But using the circular queue, we can use the space to store new values.
Your implementation should support following operations:

- MyCircularQueue(k): Constructor, set the size of the queue to be k.
- Front: Get the front item from the queue. If the queue is empty, return -1.
- Rear: Get the last item from the queue. If the queue is empty, return -1.
- enQueue(value): Insert an element into the circular queue. Return true if the operation is successful.
- deQueue(): Delete an element from the circular queue. Return true if the operation is successful.
- isEmpty(): Checks whether the circular queue is empty or not.
- isFull(): Checks whether the circular queue is full or not.

Example:

    MyCircularQueue circularQueue = new MycircularQueue(3); // set the size to be 3
    
    circularQueue.enQueue(1);  // return true
    
    circularQueue.enQueue(2);  // return true
    
    circularQueue.enQueue(3);  // return true
    
    circularQueue.enQueue(4);  // return false, the queue is full
    
    circularQueue.Rear();  // return 3
    
    circularQueue.isFull();  // return true
    
    circularQueue.deQueue();  // return true
    
    circularQueue.enQueue(4);  // return true
    
    circularQueue.Rear();  // return 4
     
 
Note:

- All values will be in the range of [1, 1000].
- The number of operations will be in the range of [1, 1000].
- Please do not use the built-in Queue library.


## 题目大意

实现一个环形链表。

## 解题方法

### 用直的代替弯的

环形的肯定不好设计，于是我就是直接弄了一个直的，不断的整体往后移，保持最大容纳k个元素。只需要维护好front和rear指针，就能模拟出来一个环状队列。

需要注意的几个点：

1. Front()和Rear()函数要判断是否为空；
2. 在得到元素的时候rear-1，而front不用。

代码如下：

```python
class MyCircularQueue(object):

    def __init__(self, k):
        """
        Initialize your data structure here. Set the size of the queue to be k.
        :type k: int
        """
        self.queue = []
        self.size = k
        self.front = 0
        self.rear = 0

    def enQueue(self, value):
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        :type value: int
        :rtype: bool
        """
        if self.rear - self.front < self.size:
            self.queue.append(value)
            self.rear += 1
            return True
        else:
            return False

    def deQueue(self):
        """
        Delete an element from the circular queue. Return true if the operation is successful.
        :rtype: bool
        """
        if self.rear - self.front > 0:
            self.front += 1
            return True
        else:
            return False

    def Front(self):
        """
        Get the front item from the queue.
        :rtype: int
        """
        if self.isEmpty():
            return -1
        else:
            return self.queue[self.front]

    def Rear(self):
        """
        Get the last item from the queue.
        :rtype: int
        """
        if self.isEmpty():
            return -1
        else:
            return self.queue[self.rear - 1]

    def isEmpty(self):
        """
        Checks whether the circular queue is empty or not.
        :rtype: bool
        """
        return self.front == self.rear

    def isFull(self):
        """
        Checks whether the circular queue is full or not.
        :rtype: bool
        """
        return self.rear - self.front == self.size


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
```

在经过做[641. Design Circular Deque][1]之后，我发现其实头尾指针都是不重要的，只要我们维护好这个list，使得这个list中保存的就是队列里面应该剩下来的元素即可。

所以删除头指针front的代码如下：

```python
class MyCircularQueue(object):

    def __init__(self, k):
        """
        Initialize your data structure here. Set the size of the queue to be k.
        :type k: int
        """
        self.queue = []
        self.size = k
        self.rear = 0

    def enQueue(self, value):
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        :type value: int
        :rtype: bool
        """
        if not self.isFull():
            self.queue.append(value)
            self.rear += 1
            return True
        else:
            return False

    def deQueue(self):
        """
        Delete an element from the circular queue. Return true if the operation is successful.
        :rtype: bool
        """
        if not self.isEmpty():
            self.queue.pop(0)
            self.rear -= 1
            return True
        else:
            return False

    def Front(self):
        """
        Get the front item from the queue.
        :rtype: int
        """
        if self.isEmpty():
            return -1
        else:
            return self.queue[0]

    def Rear(self):
        """
        Get the last item from the queue.
        :rtype: int
        """
        if self.isEmpty():
            return -1
        else:
            return self.queue[self.rear - 1]

    def isEmpty(self):
        """
        Checks whether the circular queue is empty or not.
        :rtype: bool
        """
        return 0 == self.rear

    def isFull(self):
        """
        Checks whether the circular queue is full or not.
        :rtype: bool
        """
        return self.rear == self.size


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
```

同理，只要维护的list中保存的元素和队列应该有的元素相同的，那么末尾指针rear一直指向了list的结尾，所以，可以把rear也删除。

删除front和rear的代码如下：

```python
class MyCircularQueue(object):

    def __init__(self, k):
        """
        Initialize your data structure here. Set the size of the queue to be k.
        :type k: int
        """
        self.queue = []
        self.size = k

    def enQueue(self, value):
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        :type value: int
        :rtype: bool
        """
        if not self.isFull():
            self.queue.append(value)
            return True
        else:
            return False

    def deQueue(self):
        """
        Delete an element from the circular queue. Return true if the operation is successful.
        :rtype: bool
        """
        if not self.isEmpty():
            self.queue.pop(0)
            return True
        else:
            return False

    def Front(self):
        """
        Get the front item from the queue.
        :rtype: int
        """
        if self.isEmpty():
            return -1
        else:
            return self.queue[0]

    def Rear(self):
        """
        Get the last item from the queue.
        :rtype: int
        """
        if self.isEmpty():
            return -1
        else:
            return self.queue[-1]

    def isEmpty(self):
        """
        Checks whether the circular queue is empty or not.
        :rtype: bool
        """
        return 0 == len(self.queue)

    def isFull(self):
        """
        Checks whether the circular queue is full or not.
        :rtype: bool
        """
        return len(self.queue) == self.size


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
```

### 数组循环利用

环形队列的物理结构就是一个固定长度的数组，然后前后指针到达尾部之后，移到最前。使用了first指针指向队列的首部，使用了last指针指向了队列的尾部的后一个元素。

C++代码如下：

```cpp
class MyCircularQueue {
public:
    /** Initialize your data structure here. Set the size of the queue to be k. */
    MyCircularQueue(int k) {
        q = vector<int>(k + 1, 0);
        K = k;
        first = 0;
        last = 0;
        count = 0;
    }
    
    /** Insert an element into the circular queue. Return true if the operation is successful. */
    bool enQueue(int value) {
        if (!isFull()) {
            q[last] = value;
            last = (last + 1 + K) % K;
            count ++;
            return true;
        } else {
            return false;
        }
    }
    
    /** Delete an element from the circular queue. Return true if the operation is successful. */
    bool deQueue() {
        if (!isEmpty()) {
            int val = q[first];
            first = (first + 1 + K) % K;
            count --;
            return true;
        } else {
            return false;
        }
    }
    
    /** Get the front item from the queue. */
    int Front() {
        if (isEmpty())
            return -1;
        return q[first];
    }
    
    /** Get the last item from the queue. */
    int Rear() {
        if (isEmpty())
            return -1;
        return q[(last - 1 + K) % K];
    }
    
    /** Checks whether the circular queue is empty or not. */
    bool isEmpty() {
        return count == 0;
    }
    
    /** Checks whether the circular queue is full or not. */
    bool isFull() {
        return count == K;
    }
private:
    vector<int> q;
    int first;
    int last;
    int K;
    int count;
};

/**
 * Your MyCircularQueue object will be instantiated and called as such:
 * MyCircularQueue* obj = new MyCircularQueue(k);
 * bool param_1 = obj->enQueue(value);
 * bool param_2 = obj->deQueue();
 * int param_3 = obj->Front();
 * int param_4 = obj->Rear();
 * bool param_5 = obj->isEmpty();
 * bool param_6 = obj->isFull();
 */
```

## 日期

2018 年 7 月 13 日 —— 早起困一上午，中午必须好好休息才行啊
2018 年 12 月 12 日 —— 双十二

  [1]: https://blog.csdn.net/fuxuemingzhu/article/details/81027989
