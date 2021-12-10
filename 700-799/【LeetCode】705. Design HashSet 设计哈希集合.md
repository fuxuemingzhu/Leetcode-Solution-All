
作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)

题目地址：https://leetcode.com/problems/design-hashset/description/

## 题目描述

Design a HashSet without using any built-in hash table libraries.

To be specific, your design should include these two functions:

- ``add(value)``: Insert a value into the HashSet. 
- ``contains(value)`` : Return whether the value exists in the HashSet or not.
- ``remove(value)``: Remove a value in the HashSet. If the value does not exist in the HashSet, do nothing.

Example:

    MyHashSet hashSet = new MyHashSet();
    hashSet.add(1);         
    hashSet.add(2);         
    hashSet.contains(1);    // returns true
    hashSet.contains(3);    // returns false (not found)
    hashSet.add(2);          
    hashSet.contains(2);    // returns true
    hashSet.remove(2);          
    hashSet.contains(2);    // returns false (already removed)

Note:

- All values will be in the range of [1, 1000000].
- The number of operations will be in the range of [1, 10000].
- Please do not use the built-in HashSet library.

## 题目大意

动手实现一个hashset.不能用已经内置的函数。

## 解题方法

### 位图法

那么直接想到能不能真正模拟hashset呢？通过计算hash，或者一个元素一个坑的方法进行模拟？

参考了一下别人的代码，比我想的要机智一点。这个思路的方法是第一个维度只做hash，第二个维度保存具体元素。这个思想类似于HashMap中的bucket+链表桶。

我觉得这个方法最大的优点就是省内存，因为这种设计当需要的时候，才会产生第二个维度的数据。

代码如下：

```python
class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.buckets = 1000
        self.itemsPerBucket = 1001
        self.table = [[] for _ in range(self.buckets)]

    def hash(self, key):
        return key % self.buckets
    
    def pos(self, key):
        return key // self.buckets
    
    def add(self, key):
        """
        :type key: int
        :rtype: void
        """
        hashkey = self.hash(key)
        if not self.table[hashkey]:
            self.table[hashkey] = [0] * self.itemsPerBucket
        self.table[hashkey][self.pos(key)] = 1
        
    def remove(self, key):
        """
        :type key: int
        :rtype: void
        """
        hashkey = self.hash(key)
        if self.table[hashkey]:
            self.table[hashkey][self.pos(key)] = 0

    def contains(self, key):
        """
        Returns true if this set did not already contain the specified element
        :type key: int
        :rtype: bool
        """
        hashkey = self.hash(key)
        return (self.table[hashkey] != []) and (self.table[hashkey][self.pos(key)] == 1)

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
```

### 数组法

直接开辟这么大的一个数组，然后全部设置成False，哪里有数字哪里就是True。空间没有超。

```python
class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.set = [False] * 1000001

    def add(self, key):
        """
        :type key: int
        :rtype: void
        """
        self.set[key] = True

    def remove(self, key):
        """
        :type key: int
        :rtype: void
        """
        self.set[key] = False

    def contains(self, key):
        """
        Returns true if this set contains the specified element
        :type key: int
        :rtype: bool
        """
        return self.set[key]


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
```

## 日期

2018 年 7 月 12 日 —— 天阴阴地潮潮，已经连着两天这样了
2018 年 11 月 17 日 —— 美妙的周末，美丽的天气
