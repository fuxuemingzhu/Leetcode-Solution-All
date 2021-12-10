
作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)

题目地址：https://leetcode.com/problems/design-hashmap/description/

## 题目描述

Design a HashMap without using any built-in hash table libraries.

To be specific, your design should include these two functions:

- ``put(key, value)`` : Insert a (key, value) pair into the HashMap. If the value already exists in the HashMap, update the value.
- ``get(key)``: Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key.
- ``remove(key)`` : Remove the mapping for the value key if this map contains the mapping for the key.

Example:

    MyHashMap hashMap = new MyHashMap();
    hashMap.put(1, 1);          
    hashMap.put(2, 2);         
    hashMap.get(1);            // returns 1
    hashMap.get(3);            // returns -1 (not found)
    hashMap.put(2, 1);          // update the existing value
    hashMap.get(2);            // returns 1 
    hashMap.remove(2);          // remove the mapping for 2
    hashMap.get(2);            // returns -1 (not found) 

Note:

- All values will be in the range of [1, 1000000].
- The number of operations will be in the range of [1, 10000].
- Please do not use the built-in HashMap library.


## 题目大意

动手实现一个hashmap.不能用已经内置的函数。

## 解题方法

这个题和[705. Design HashSet][1]基本一样啊。705是要设计hashset，当时只要把某个位置设置成1，就表示这个元素存在了即可。这个题只需要把当时的设置成1改成设置成对应的value。

写这个题的时候就要考虑，不能把每个位置初始化成0，因为这样会和value值冲突。即加入value就是0，那么这个位置的0不知道怎么判断。所以应该初始化None，后面对这个位置是否存在元素的判断也是必须判断==None而不是not的方式进行判断。

代码如下：

```python
class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.buckets = 1000
        self.itemsPerBuckect = 1001
        self.hashmap = [[] for _ in range(self.buckets)]

    def hash(self, key):
        return key % self.buckets
    
    def pos(self, key):
        return key // self.buckets

    def put(self, key, value):
        """
        value will always be positive.
        :type key: int
        :type value: int
        :rtype: void
        """
        hashkey = self.hash(key)
        if not self.hashmap[hashkey]:
            self.hashmap[hashkey] = [None] * self.itemsPerBuckect
        self.hashmap[hashkey][self.pos(key)] = value

    def get(self, key):
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        :type key: int
        :rtype: int
        """
        hashkey = self.hash(key)
        if (not self.hashmap[hashkey]) or self.hashmap[hashkey][self.pos(key)] == None:
            return -1
        else:
            return self.hashmap[hashkey][self.pos(key)]

    def remove(self, key):
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        :type key: int
        :rtype: void
        """
        hashkey = self.hash(key)
        if self.hashmap[hashkey]:
            self.hashmap[hashkey][self.pos(key)] = None


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
```

上面的做法比较省内存，如果不用省内存的话，可以直接开出来这么大的数组即可。事实上，1000000大小的数组，内存不会超的。

另外一个技巧就是，把数组初始化为-1，这样既不会和原始的数据冲突，而且当查询的时候，可以直接返回这个数值，正好是题目的要求。

```python
class MyHashMap(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.bitmap = [[-1] * 1000 for _ in range(1001)]

    def put(self, key, value):
        """
        value will always be non-negative.
        :type key: int
        :type value: int
        :rtype: void
        """
        row, col = key / 1000, key % 1000
        self.bitmap[row][col] = value

    def get(self, key):
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        :type key: int
        :rtype: int
        """
        row, col = key / 1000, key % 1000
        return self.bitmap[row][col]

    def remove(self, key):
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        :type key: int
        :rtype: void
        """
        row, col = key / 1000, key % 1000
        self.bitmap[row][col] = -1


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
```

如果直接使用一维数组的话，那么也可以通过，其实更简单了。

```python
class MyHashMap(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.bitmap = [-1] * 1000001

    def put(self, key, value):
        """
        value will always be non-negative.
        :type key: int
        :type value: int
        :rtype: void
        """
        self.bitmap[key] = value

    def get(self, key):
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        :type key: int
        :rtype: int
        """
        return self.bitmap[key]

    def remove(self, key):
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        :type key: int
        :rtype: void
        """
        self.bitmap[key] = -1


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
```

## 日期

2018 年 7 月 12 日 —— 天阴阴地潮潮，已经连着两天这样了
2018 年 11 月 13 日 —— 时间有点快

  [1]: https://blog.csdn.net/fuxuemingzhu/article/details/81016992
