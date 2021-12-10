作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)

[LeetCode]

题目地址：[https://leetcode.com/problems/power-of-three/](https://leetcode.com/problems/power-of-three/)

Total Accepted: 38705 Total Submissions: 105634 Difficulty: Easy


## 题目描述

Given an integer, write a function to determine if it is a power of three.

Example 1:

	Input: 27
	Output: true

Example 2:

	Input: 0
	Output: false

Example 3:

	Input: 9
	Output: true

Example 4:

	Input: 45
	Output: false

Follow up:

- Could you do it without using any loop / recursion?

## 题目大意

判断一个数是不是3的幂。

## 解题方法

### 循环

这是最简单的方法了，就是一直除以3，直到最后看看剩下的是不是1.

```python
class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 0: return False
        while n % 3 == 0:
            n /= 3
        return n == 1
```

### 递归

递归解法速度反而更快。

```python
class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0: return False
        if n == 1: return True
        if n % 3 == 0:
            return self.isPowerOfThree(n / 3)
        return False
```

### 取对数

取对数。看一个数以3为底的对数是否为整数。好吧还是挺聪明的。

```java
public class Solution {
    public boolean isPowerOfThree(int n) {
        return (Math.log10(n)/Math.log10(3)) % 1 == 0;
        
    }
}
```
AC:20ms

### 判断是不是最大3的倍数的因子

还有一种方法是说，先找出最大的3的幂的int，再看n能否整除这个数。效率应该比这个高，没有试。可以参考：

```java
public boolean isPowerOfThree(int n) {
     return n>0 && Math.pow(3, (int)(Math.log(0x7fffffff)/Math.log(3)))%n==0;
}
```

## 日期

2016/5/1 16:47:54 
2018 年 11 月 20 日 —— 真是一个好天气
