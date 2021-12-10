# 【LeetCode】380. Insert Delete GetRandom O(1) 解题报告（Python）

作者： 		负雪明烛 
id：				fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---

题目地址：https://leetcode.com/problems/insert-delete-getrandom-o1/description/

## 题目描述：

Design a data structure that supports all following operations in average ``O(1)`` time.

1. insert(val): Inserts an item val to the set if not already present.
1. remove(val): Removes an item val from the set if present.
1. getRandom: Returns a random element from current set of elements. Each element must have the same probability of being returned.

Example:

    // Init an empty set.
    RandomizedSet randomSet = new RandomizedSet();
    
    // Inserts 1 to the set. Returns true as 1 was inserted successfully.
    randomSet.insert(1);
    
    // Returns false as 2 does not exist in the set.
    randomSet.remove(2);
    
    // Inserts 2 to the set, returns true. Set now contains [1,2].
    randomSet.insert(2);
    
    // getRandom should return either 1 or 2 randomly.
    randomSet.getRandom();
    
    // Removes 1 from the set, returns true. Set now contains [2].
    randomSet.remove(1);
    
    // 2 was already in the set, so return false.
    randomSet.insert(2);
    
    // Since 2 is the only number in the set, getRandom always return 2.
    randomSet.getRandom();


## 题目大意

设计一个数据结构，有三个方法：插入、删除、随机选取一个数值。要求平均的时间复杂度是O(1).

## 解题方法

插入删除的时间复杂度要求O(1)的话，很容易想起来是set。所以我就用set来实现了。但是随机选取的时候，由于set不能使用索引，所以我先把它转成了list，然后使用随机数来进行索引。不知道python中set转list的时间复杂度是多少，估计最坏情况应该是O(n)，这一步没有满足题目的要求，但是也过了。

这个题目没有说清楚如果数据结构为空的时候使用getRandom()应该怎么返回，我觉得是个bug。当然测试用例避开了这一点。

代码如下：

```python3
class RandomizedSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.set = set()
        self.size = 0

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if val not in self.set:
            self.set.add(val)
            self.size += 1
            return True
        return False

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.set:
            self.set.remove(val)
            self.size -= 1
            return True
        return False

    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        ind = random.randint(0, self.size - 1)
        return list(self.set)[ind]

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
```

参考了一下，发现可以使用字典保存每个元素出现的位置，那么和list结合之后，每次移除一个元素的方式是把list结尾元素对要被移除元素出现的位置进行原地替换，这样就能把时间复杂度降下来。

如果list删除某个位置的元素，那么时间复杂度是O(N)，但是如果用最后的元素对该位置进行替换，并且移除最后的元素，时间复杂度能降到O(1)。

特别注意骚操作都在remove里面的，注意位置替换，以及别忘记把list和dict中要移除的元素删除。

```python
class RandomizedSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.nums, self.pos = list(), dict()
        
    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if val not in self.pos:
            self.nums.append(val)
            self.pos[val] = len(self.nums) - 1
            return True
        return False

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.pos:
            idx, last = self.pos[val], self.nums[-1]
            self.nums[idx] = last
            self.pos[last] = idx
            self.nums.pop()
            self.pos.pop(val, 0)
            return True
        return False

    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        idx = random.randint(0, len(self.nums) - 1)
        return self.nums[idx]

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
```

参考资料：

https://leetcode.com/problems/insert-delete-getrandom-o1/discuss/85397/Simple-solution-in-Python

## 日期

2018 年 9 月 17 日 —— 早上很凉，夜里更凉