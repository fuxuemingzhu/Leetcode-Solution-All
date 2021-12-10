作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)

[LeetCode]

题目地址：[https://leetcode.com/problems/power-of-four/](https://leetcode.com/problems/power-of-four/)

Total Accepted: 9305 Total Submissions: 28083 Difficulty: Easy

## 题目描述

Given an integer (signed 32 bits), write a function to check whether it is a power of 4.

Example 1:

	Input: 16
	Output: true

Example 2:

	Input: 5
	Output: false

Follow up: Could you solve it without loops/recursion?

## 题目大意

判断一个数是不是4的幂。

## 解题方法


### 递归

如果能被4整除，就看除以4之后是否能继续整除。


```python
class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 0: return False
        if num == 1: return True
        if num % 4 == 0:
            return self.isPowerOfFour(num / 4)
        return False
```

AC:2ms

### 迭代

和递归同样的原理。

```python
class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 0: return False
        while num % 4 == 0:
            num /= 4
        return num == 1
```

效率凑活。

### 位运算

查了一下，发现还有更好的方法。就是判断二进制中1出现的位数是不是在奇数位。用0101 0101 ……来进行排除。16进制数为：0x55555555。

```python
class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        return num > 0 and (num & (num - 1)) == 0 and (num & 0x55555555) != 0
```

Java代码如下：

```java
public class Solution {
    public boolean isPowerOfFour(int num) {
        return num > 0 && (num & (num - 1)) ==0  && (num & 0x55555555) !=0;
    }
}
```

### 函数法

判断取以4为底的log之后，强转成int，再取上4的幂是不是原来的数字。

```python
class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        return num > 0 and (4 ** (int(math.log(num, 4)))) == num
```


## 日期

2016/5/1 17:36:06 
2018 年 11 月 22 日 —— 感恩节快乐~
