作者： 		负雪明烛 
id：				fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---

题目地址：https://leetcode.com/problems/peeking-iterator/description/

## 题目描述：

Given an Iterator class interface with methods: ``next()`` and ``hasNext()``, design and implement a PeekingIterator that support the ``peek()`` operation -- it essentially ``peek()`` at the element that will be returned by the next call to ``next()``.

Example:

    Assume that the iterator is initialized to the beginning of the list: [1,2,3].
    
    Call next() gets you 1, the first element in the list.
    Now you call peek() and it returns 2, the next element. Calling next() after that still return 2. 
    You call next() the final time and it returns 3, the last element. 
    Calling hasNext() after that should return false.

Follow up: How would you extend your design to be generic and work with all types, not just integer?

## 题目大意

已有一个迭代器，这个迭代器里面有``hasNext()``和``next()``函数，让我们对这个迭代器进行封装，添加一个能获取下一个元素是什么但不需要弹出的``peek()``函数。

## 解题方法

这个题可以说非常简单没难度了，peek()通过获取迭代器的next()然后保存当前值就好了。如果调用自身的next()的时候，需要判断一下当前的值是否存在，如果存在就优先弹出。hasNext()也是同样的道理。

需要注意的两点：第一，刚开始把保存下一个元素的变量定义为了self.next，这样和函数重名了是不可以的；第二，注意保存的是int，因此注意不能给self.n初始化任何一个整数值，使用None判断是否保存有元素，if的时候不能简单的if self.n这种操作，因为当n等于0的时候也会触发。

每个操作的时间复杂度是O(1)，空间复杂度是O(1).

代码如下：

```python
# Below is the interface for Iterator, which is already defined for you.
#
# class Iterator(object):
#     def __init__(self, nums):
#         """
#         Initializes an iterator object to the beginning of a list.
#         :type nums: List[int]
#         """
#
#     def hasNext(self):
#         """
#         Returns true if the iteration has more elements.
#         :rtype: bool
#         """
#
#     def next(self):
#         """
#         Returns the next element in the iteration.
#         :rtype: int
#         """

class PeekingIterator(object):
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self.iterator = iterator
        self.n = None

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        if self.n == None:
            self.n = self.iterator.next()
        return self.n
        

    def next(self):
        """
        :rtype: int
        """
        if self.n != None:
            tmp = self.n
            self.n = None
            return tmp
        else:
            return self.iterator.next()

    def hasNext(self):
        """
        :rtype: bool
        """
        if self.n != None:
            return True
        else:
            return self.iterator.hasNext()

# Your PeekingIterator object will be instantiated and called as such:
# iter = PeekingIterator(Iterator(nums))
# while iter.hasNext():
#     val = iter.peek()   # Get the next element but not advance the iterator.
#     iter.next()         # Should return the same value as [val].
```

参考资料：


## 日期

2018 年 9 月 26 日 —— 美好的一周又快要过去了。。


  [1]: https://blog.csdn.net/fuxuemingzhu/article/details/82809923
