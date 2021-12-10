
作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)

[LeetCode]

题目地址：[https://leetcode.com/problems/power-of-two/](https://leetcode.com/problems/power-of-two/)

Total Accepted: 71172 Total Submissions: 194399 Difficulty: Easy


## 题目描述

Given an integer, write a function to determine if it is a power of two.

Example 1:

	Input: 1
	Output: true 
	Explanation: 20 = 1

Example 2:

	Input: 16
	Output: true
	Explanation: 24 = 16

Example 3:

	Input: 218
	Output: false

## 题目大意

判断一个整数是不是2的幂。

## 解题方法

和刚才那个是否为3的倍数好像。嗯。刚才有个字符串的方法没讲。这里试了一下。

### 二进制

这个方法应该是通用的方法，转换为特定的进制的字符串，然后判断是否为1开头的字符。

The code above converts number into base base and returns the result as a String. For example, Integer.toString(5, 2) == "101" and Integer.toString(5, 3) == "12".

```java
boolean matches = myString.matches("123");

public class Solution {
    public boolean isPowerOfThree(int n) {
        return Integer.toString(n, 2).matches("^10*$");
    }
}
```
AC:20ms

如果用Python写的话，可以直接数一下二进制中1的个数是不是正好是1个.

```python
class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return n > 0 and bin(n).count("1") == 1
```

### 位运算

还记得那个 n&(n-1) 的方法来数一个数里边有多少个1吗？没错，只要只有一个1就好。

```java
public class Solution {
    public boolean isPowerOfTwo(int n) {
        if(n<=0) return false;
        return (n & (n-1)) == 0;
    }
}
```
AC:2ms

python解法如下：

```python
class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0: return False
        return n & (n - 1) == 0
```


### 判断是不是最大2的幂的因数

嗯。参考了3的幂的另一种解法，用满足条件的最大的int来看这个n能否整除。本来想手算2的最大的幂的int是多少呢，后来一想可以用位移运算。太聪明了。恩。

```java
public class Solution {
    public boolean isPowerOfTwo(int n) {
        if(n<=0) return false;
        return (1<<31) % n == 0;
    }
}
```
AC:2ms

### 判断因子是不是只有2

不停地循环。判断因子是不是只有2，最后的话结果应该是1.

```python
class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0: return False
        while n % 2 == 0:
            n /= 2
        return n == 1
```

## 日期

2016/5/1 17:10:28 
2018 年 11 月 19 日 —— 周一又开始了
