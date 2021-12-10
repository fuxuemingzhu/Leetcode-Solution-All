# 【LeetCode】385. Mini Parser 解题报告（Python）

标签： LeetCode

---

题目地址：https://leetcode.com/problems/mini-parser/description/

## 题目描述：

Given a nested list of integers represented as a string, implement a parser to deserialize it.

Each element is either an integer, or a list -- whose elements may also be integers or other lists.

Note: You may assume that the string is well-formed:

1. String is non-empty.
1. String does not contain white spaces.
1. String contains only digits 0-9, [, - ,, ].

    Example 1:
    
    Given s = "324",
    
    You should return a NestedInteger object which contains a single integer 324.
   
    Example 2:
    
    Given s = "[123,[456,[789]]]",
    
    Return a NestedInteger object containing a nested list with 2 elements:
    
    1. An integer containing value 123.
    2. A nested list containing two elements:
        i.  An integer containing value 456.
        ii. A nested list with one element:
             a. An integer containing value 789.



## 题目大意

给了一个字符串表示的列表，返回一个NestedInteger形式的列表，其每个元素都是NestedInteger形式的整数对象。

面向对象的编程。

## 解题方法

Python看到这个题笑了，直接eval就能把字符串转成一个数组，而且这个数组的每个元素已经转成了int。

直接写个递归就好了。哈哈哈

```python
# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger(object):
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """"[123,[456,[789]]]"
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class Solution(object):
    def deserialize(self, s):
        """
        :type s: str
        :rtype: NestedInteger
        """
        def getNumber(nums):
            if isinstance(nums, int):
                return NestedInteger(nums)
            lst = NestedInteger()
            for num in nums:
                lst.add(getNumber(num))
            return lst
        return getNumber(eval(s))

```

## 日期

2018 年 3 月 13 日 