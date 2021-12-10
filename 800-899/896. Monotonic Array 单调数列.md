
作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)

题目地址：https://leetcode.com/problems/monotonic-array/description/

## 题目描述

An array is monotonic if it is either monotone increasing or monotone decreasing.

An array ``A`` is monotone increasing if for all ``i <= j``, ``A[i] <= A[j]``.  An array ``A`` is monotone decreasing if for all ``i <= j``, ``A[i] >= A[j]``.

Return ``true`` if and only if the given array ``A`` is monotonic.

 

Example 1:

    Input: [1,2,2,3]
    Output: true

Example 2:

    Input: [6,5,4,4]
    Output: true

Example 3:

    Input: [1,3,2]
    Output: false

Example 4:

    Input: [1,2,4,5]
    Output: true

Example 5:

    Input: [1,1,1]
    Output: true
 

Note:

- 1 <= A.length <= 50000
- -100000 <= A[i] <= 100000


## 题目大意

判断一个数组是不是单调的。单调包括单调递增和单调递减。

## 解题方法

用python的话，最快的方式应该是使用all，只用看连续两个数字之间的差值和0之间的比较就行了。

代码如下：

```python
class Solution(object):
    def isMonotonic(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        return self.isIncrease(A) or self.isDecrease(A)
        
    def isIncrease(self, A):
        return all(A[i] - A[i+1] >= 0 for i in range(len(A) - 1))
        
    def isDecrease(self, A):
        return all(A[i] - A[i+1] <= 0 for i in range(len(A) - 1))
```

参考资料：


## 日期

2018 年 9 月 3 日 —— 新学期开学第一天！
2018 年 11 月 ９ 日 —— 睡眠可以2018 年 11 月 ９ 日 —— 睡眠可以
