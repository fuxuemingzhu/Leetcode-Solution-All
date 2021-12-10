
作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)

[LeetCode]

题目地址：[https://leetcode.com/problems/ugly-number/](https://leetcode.com/problems/ugly-number/)

Total Accepted: 22335 Total Submissions: 67449 Difficulty: Easy


## 题目描述


Write a program to check whether a given number is an ugly number.

Ugly numbers are positive numbers whose prime factors only include ``2, 3, 5``.

Example 1:

	Input: 6
	Output: true
	Explanation: 6 = 2 × 3

Example 2:

	Input: 8
	Output: true
	Explanation: 8 = 2 × 2 × 2

Example 3:

	Input: 14
	Output: false 
	Explanation: 14 is not ugly since it includes another prime factor 7.

Note:

1. 1 is typically treated as an ugly number.
1. Input is within the 32-bit signed integer range: [−231,  231 − 1].

## 题目大意

如果一个数的因子只有``2,3,5``，那么这个数是丑数。判断一个数是不是丑数。

## 解题方法

### 除去2,3,5因子

把这个数中的所有的2,3,5的因子全部除去，剩余的数为1，则说明全部为这几个因子构成。

python解法。

```python
class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 0: return False
        while num % 2 == 0:
            num /= 2
        while num % 3 == 0:
            num /= 3
        while num % 5 == 0:
            num /= 5
        return num == 1
```

Java解法：

```java
public static boolean isUgly(int num) {
	if (num == 1) {
		return true;
	}

	while (num >= 2 && num % 2 == 0) {
		num = num / 2;
	}
	while (num >= 3 && num % 3 == 0) {
		num = num / 3;
	}
	while (num >= 5 && num % 5 == 0) {
		num = num / 5;
	}
	return num == 1;
}
```

另外有精简的答案如下。

```java
public class Solution {
    public boolean isUgly(int num) {
        int[] divides ={2,3,5};
        for(int i = 0; i < divides.length && num > 0; i++){
            while(num % divides[i] == 0){
                num /= divides[i];
            }
        }
		return num == 1;
    }
}
```

## 日期

2015/10/16 21:20:23 
2018 年 11 月 21 日 —— 又是一个美好的开始
