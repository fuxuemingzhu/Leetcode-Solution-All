作者： 		负雪明烛 
id：				fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---

@[TOC](目录)

题目地址: https://leetcode.com/problems/sort-array-by-parity-ii

## 题目描述

Given an array A of non-negative integers, half of the integers in A are odd, and half of the integers are even.

Sort the array so that whenever A[i] is odd, i is odd; and whenever A[i] is even, i is even.

You may return any answer array that satisfies this condition.

 

Example 1:

	Input: [4,2,5,7]
	Output: [4,5,2,7]
	Explanation: [4,7,2,5], [2,5,4,7], [2,7,4,5] would also have been accepted.
	 

Note:

1. 2 <= A.length <= 20000
1. A.length % 2 == 0
1. 0 <= A[i] <= 1000


## 题目大意

把一个数组重新排序，使得偶数位置全是偶数，奇数位置全是奇数。

## 解题方法

### 使用奇偶数组

直接使用两个数组分别存放奇数和偶数，然后结果就是在这两个里面来回的选取就好了。这种做法比较简单，打比赛比较适用。

时间复杂度是O(N)，空间复杂度是O(N)。

```python
class Solution(object):
    def sortArrayByParityII(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        odd = [x for x in A if x % 2 == 1]
        even = [x for x in A if x % 2 == 0]
        res = []
        iseven = True
        while odd or even:
            if iseven:
                res.append(even.pop())
            else:
                res.append(odd.pop())
            iseven = not iseven
        return res
```

### 排序

先对A进行排序，使得偶数都在前面，奇数都在后面，然后每次从前从后各取一个数，然后放到结果里就好了。

```python3
class Solution:
    def sortArrayByParityII(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        A.sort(key = lambda x : x % 2)
        N = len(A)
        res = []
        for i in range(N // 2):
            res.append(A[i])
            res.append(A[N - 1 - i])
        return res
```

时间复杂度是O(NlogN)，空间复杂度是O(1)。

### 奇偶数位置变量

先把结果数组创建好，然后使用奇偶数两个变量保存位置，然后判断A中的每个数字是奇数还是偶数，对应放到奇偶位置就行了。

时间复杂度是O(N)，空间复杂度是O(1)。

```python3
class Solution:
    def sortArrayByParityII(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        N = len(A)
        res = [0] * N
        even, odd = 0, 1
        for a in A:
            if a % 2 == 1:
                res[odd] = a
                odd += 2
            else:
                res[even] = a
                even += 2
        return res
```

时间复杂度是O(N)，空间复杂度是O(N)。

参考资料：


## 日期

2018 年 10 月 14 日 —— 周赛做出来3个题，开心
2018 年 11 月 5 日 —— 打了羽毛球，有点累
