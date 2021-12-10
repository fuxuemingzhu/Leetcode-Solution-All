
作者： 		负雪明烛 
id：				fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)

题目地址：https://leetcode.com/problems/sort-array-by-parity/description/

## 题目描述：

Given an array A of non-negative integers, return an array consisting of all the even elements of A, followed by all the odd elements of A.

You may return any answer array that satisfies this condition.

 

Example 1:

    Input: [3,1,2,4]
    Output: [2,4,3,1]
    The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.
 

Note:

- 1 <= A.length <= 5000
- 0 <= A[i] <= 5000


## 题目大意

对数组A按照偶数和奇数重新排序，使得偶数在前，奇数在后。可以返回任何一种满足这个条件的数组即可。

## 解题方法

### 自定义sorted函数的cmp

看到排序就写个排序就行了，比较的key是对2取余数之后的值。这样偶数取余得0，排在前面，奇数取余得1，排在后面。

时间复杂度是O(nlogn)，空间复杂度是O(1)。

代码如下：

```python3
class Solution(object):
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        return sorted(A, key = lambda x : x % 2)
```

参考资料：


## 日期

2018 年 9 月 17 日 —— 早上很凉，夜里更凉
