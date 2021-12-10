
作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)

题目地址：[https://leetcode.com/problems/sum-of-square-numbers/discuss/][1]


## 题目描述

Given a non-negative integer c, your task is to decide whether there're two integers a and b such that ``a2 + b2 = c``.

Example 1:

    Input: 5
    Output: True
    Explanation: 1 * 1 + 2 * 2 = 5

Example 2:

    Input: 3
    Output: False

## 题目大意

判断一个数字能不能有两个数的平方和构成。

## 解题方法

### 双指针

两个指针向中间靠拢，比较好理解。

```python
class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        left = 0
        right = int(c ** 0.5)
        while left <= right:
            cur = left ** 2 + right ** 2
            if cur < c:
                left += 1
            elif cur > c:
                right -= 1
            else:
                return True
        return False
                      
```

### 列表生成式

xrange是个生成式，range返回的是列表。判断去除一个平方数之后剩余的数是不是平方数。

```python
class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        def is_square(N):
            return int(N ** 0.5) ** 2 == N
        
        return any(is_square(c - a ** 2) for a in xrange(int(c ** 0.5) + 1))                
```

### 循环

使用循环进行判断，看是不是有一个a存在，使得c - a ^ 2是个完全平方数。

判断一个数是不是完全平方数，方法很多，我用的是最简单的，先取根号，然后再平方看是否相等的方式。

Python解法如下：

```python
class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        if c == 0: return True
        for a in range(1, int(math.sqrt(c) + 1)):
            b = c - a * a
            if int(math.sqrt(b)) ** 2 == b:
                return True
        return False
```

C++ 解法如下：

```cpp
class Solution {
public:
    bool judgeSquareSum(int c) {
        if (c == 0) return true;
        for (int a = 1; a < (int) sqrt(c) + 1; ++a){
            double b = sqrt(c - a * a);
            if (b == (int) b){
                return true;
            }
        }
        return false;
    }
};
```

## 日期

2017 年 8 月 24 日 
2018 年 11 月 24 日 —— 周日开始！一周就过去了～

  [1]: https://leetcode.com/problems/sum-of-square-numbers/discuss/
