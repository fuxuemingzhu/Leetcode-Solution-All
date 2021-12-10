
作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)

题目地址：[https://leetcode.com/problems/self-dividing-numbers/description/][1]


## 题目描述

A self-dividing number is a number that is divisible by every digit it contains.

For example, 128 is a self-dividing number because 128 % 1 == 0, 128 % 2 == 0, and 128 % 8 == 0.

Also, a self-dividing number is not allowed to contain the digit zero.

Given a lower and upper number bound, output a list of every possible self dividing number, including the bounds if possible.

Example 1:

    Input: 
    left = 1, right = 22
    Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]

Note:

    The boundaries of each input argument are 1 <= left <= right <= 10000.

## 题目大意

如果一个数字能被它自己的各位数字整除，那么这个数字是一个自除数字，求在[left, right]双闭区间内的所有自除数字。

## 解题方法

### 循环

用了两个函数，一个用来判断是否是dividing number，另一个用来循环和遍历。

要注意的一点是要判断0是否在num中，否则有除0错误。

dividing number 判断的有点麻烦，就是遍历每位数字。


```python
class Solution:
    def isDividingNumber(self, num):
        if '0' in str(num):
            return False
        return 0 == sum(num % int(i) for i in str(num))
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        answer = []
        for num in range(left, right+1):
            print(num)
            if self.isDividingNumber(num):
                answer.append(num)
        return answer
```

### filter函数

参考了https://leetcode.com/problems/self-dividing-numbers/discuss/109445。
有更简单的两个函数：
all()判断是不是所有的元素都满足，
filter过滤掉不满足条件的元素。

```python
class Solution(object):
    def selfDividingNumbers(self, left, right):
        is_self_dividing = lambda num: '0' not in str(num) and all([num % int(digit) == 0 for digit in str(num)])
        return filter(is_self_dividing, range(left, right + 1))
```
As pointed out by @ManuelP, [num % int(digit) == 0 for digit in str(num)] creates an entire list which is not necessary. By leaving out the [ and ], we can make use of generators which are lazy and allows for short-circuit evaluation, i.e. all will terminate as soon as one of the digits fail the check.

The answer below improves the run time from 128 ms to 95 ms:

```python
class Solution(object):
    def selfDividingNumbers(self, left, right):
        is_self_dividing = lambda num: '0' not in str(num) and all(num % int(digit) == 0 for digit in str(num))
        return filter(is_self_dividing, range(left, right + 1))
```

### 数字迭代

转成字符串的方法耗时，其实可以直接使用数字求余的方法节省了大量的时间。

时间复杂度是O(N)，空间复杂度是O(1)。打败98%.

```python
class Solution:
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        res = []
        for num in range(left, right + 1):
            if self.isDividing(num):
                res.append(num)
        return res
        
    def isDividing(self, num):
        temp = num
        while temp:
            div = temp % 10
            if not div or num % div != 0:
                return False
            temp //= 10
        return True
```

## 日期

2018 年 1 月 13 日 
2018 年 11 月 5 日 —— 打了羽毛球，有点累

  [1]: https://leetcode.com/problems/self-dividing-numbers/description/
