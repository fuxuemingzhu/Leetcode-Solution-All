作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)

题目地址：https://leetcode.com/problems/peak-index-in-a-mountain-array/description/

## 题目描述

Let's call an array A a mountain if the following properties hold:

1. ``A.length >= 3``
1. There exists some ``0 < i < A.length - 1`` such that ``A[0] < A[1] < ... A[i-1] < A[i] > A[i+1] > ... > A[A.length - 1]``

Given an array that is definitely a mountain, return any i such that ``A[0] < A[1] < ... A[i-1] < A[i] > A[i+1] > ... > A[A.length - 1]``.

Example 1:

    Input: [0,1,0]
    Output: 1

Example 2:

    Input: [0,2,1,0]
    Output: 1

Note:

1. 3 <= A.length <= 10000
1. 0 <= A[i] <= 10^6
1. A is a mountain, as defined above.

## 题目大意

找出一个数组中的山峰的索引。山峰的意思是指在一个长度大于3的数组中，某个数值比相邻的两个数值都大。

## 解题方法

### 二分查找

这个一看就是二叉搜索啊，曾经的面试题，印象很深刻。

这个比普通二叉搜索的改进地方就是不再判断left, mid, right三者之间的关系。而是对于中间的mid，去判断mid和其相邻的两个元素的关系。根据是否符合山峰的上坡和下坡，去移动指针。

```python
class Solution(object):
    def peakIndexInMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        left, right = 0, len(A) - 1
        while left < right:
            mid = (left + right) / 2
            if A[mid - 1] < A[mid] and A[mid] < A[mid + 1]:
                left = mid
            elif A[mid - 1] > A[mid] and A[mid] > A[mid + 1]:
                right = mid
            else:
                break
        return mid
```

二刷的时候，写了一个打败100%的写法，也就是我们使用了更少的判断。

```python3
class Solution:
    def peakIndexInMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        N = len(A)
        left, right = 0, N
        while left < right:
            mid = left + (right - left) // 2
            if A[mid - 1] < A[mid] and A[mid] > A[mid + 1]:
                return mid
            if A[mid] < A[mid + 1]:
                left = mid + 1
            else:
                right = mid
        return -1
```

### 查找最大值位置

这个做法是在题目保证了给出的数组是满足条件的，那么只要找出最大值的位置那么一定就满足了条件。

```python3
class Solution:
    def peakIndexInMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        return A.index(max(A))
```

### 寻找第一个下降的位置

题目给出的是满足条件的数组，所以找出第一个下降的位置就是题目所求啊。

```python3
class Solution:
    def peakIndexInMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        for i in range(len(A) - 1):
            if A[i + 1] < A[i]:
                return i
        return -1
```


## 日期

2018 年 6 月 17 日 —— 端午节也在刷题2333
2018 年 11 月 5 日 —— 打了羽毛球，有点累
