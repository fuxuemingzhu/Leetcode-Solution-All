
作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)

题目地址：[https://leetcode.com/problems/perfect-number/#/description][1]


## 题目描述

We define the Perfect Number is a positive integer that is equal to the sum of all its positive divisors except itself.

Now, given an integer n, write a function that returns true when it is a perfect number and false when it is not.

Example:

    Input: 28
    Output: True
    Explanation: 28 = 1 + 2 + 4 + 7 + 14

Note: The input number n will not exceed 100,000,000. (1e8)

## 题目大意

如果一个数字等于它的所有除了自己的因子之和，那么是个完美数字。判断一个数字是不是完美数字。

## 解题方法

这个题其实非常简单，循环一遍看看哪些是约数，然后加在一起就行了。注意i从2开始循环，这样不会把1和num自身加进去，最后sum++，把1这个数字加进去。

Java解法如下：

```java
public class Solution {
    public boolean checkPerfectNumber(int num) {
        if(num == 1) return false;
        int sum = 0;
        for(int i = 2; i < Math.sqrt(num);  i++){
            if(num % i == 0){
                sum += i + num / i;
            }
        }
        sum++;
        return sum == num;
    }
}
```

C++版本如下：

```cpp
class Solution {
public:
    bool checkPerfectNumber(int num) {
        if(num <= 1) return false;
        int sums = 1;
        for(int i = 2; i < (int) sqrt(num) + 1; ++i){
            if(num % i == 0){
                sums += i + num / i;
            }
        }
        return num == sums;
    }
};
```

Python版本如下：

```python
class Solution(object):
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 1: return False
        sums = 1
        for i in range(2, int(math.sqrt(num) + 1)):
            if num % i == 0:
                sums += i + num / i
        return num == sums
```

## 日期

2017 年 5 月 16 日 
2018 年 11 月 24 日 —— 周日开始！一周就过去了～

  [1]: https://leetcode.com/problems/perfect-number/#/description
