- 作者：    负雪明烛
- id：      fuxuemingzhu
- 个人博客：[http://fuxuemingzhu.cn/](http://fuxuemingzhu.cn/)

---
@[TOC](目录)


题目地址：https://leetcode.com/problems/day-of-the-year/

## 题目描述

Given a year `Y` and a month `M`, return how many days there are in that month.


Example 1:

    Input: Y = 1992, M = 7
    Output: 31

Example 2:

    Input: Y = 2000, M = 2
    Output: 29

Example 3:

    Input: Y = 1900, M = 2
    Output: 28

Note:

1. `1583 <= Y <= 2100`
1. `1 <= M <= 12`


## 题目大意

判断给出的某年某月有多少天。

## 解题方法

### 判断是否是闰年

这个题和[1185. Day of the Week][1]类似。

这个题中计算出当年是不是闰年，然后从数组中读取当月的天数。

C++代码如下：

```cpp
class Solution {
public:
    int numberOfDays(int Y, int M) {
        return daysOfMonth[isLeapYear(Y)][M - 1];
    }
    bool isLeapYear(int year) {
        return (year % 4 == 0 && year % 100 != 0) || year % 400 == 0;
    }
    int daysOfMonth[2][12] = {
        {31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31},
        {31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31}
    };
};
```

## 日期

2019 年 9 月 18 日 —— 今日又是九一八


  [1]: https://blog.csdn.net/fuxuemingzhu/article/details/100977773
