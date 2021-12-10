
- 作者：    负雪明烛
- id：      fuxuemingzhu
- 个人博客：[http://fuxuemingzhu.cn/](http://fuxuemingzhu.cn/)

---

@[TOC](目录)


题目地址：https://leetcode.com/problems/day-of-the-year/

## 题目描述

Given a string date representing a Gregorian calendar date formatted as `YYYY-MM-DD`, return the day number of the year.

Example 1:

    Input: date = "2019-01-09"
    Output: 9
    Explanation: Given date is the 9th day of the year in 2019.

Example 2:

    Input: date = "2019-02-10"
    Output: 41

Example 3:

    Input: date = "2003-03-01"
    Output: 60

Example 4:
    
    Input: date = "2004-03-01"
    Output: 61
 
Constraints:

1. `date.length == 10`
1. `date[4] == date[7] == '-'`, and all other `date[i]`'s are digits
1. date represents a calendar date between Jan 1st, 1900 and Dec 31, 2019.

## 题目大意

判断给出的日期是当月的第多少天。

## 解题方法

### 计算1月1号之间天数

这个题和[1185. Day of the Week][1]类似。这个题中计算出当年是不是闰年，然后计算和1月1号之间的天数就行了，需要累加每个月，特别注意二月份。

C++代码如下：

```cpp
class Solution {
public:
    int dayOfYear(string date) {
        int year = stoi(date.substr(0, 4));
        int month = stoi(date.substr(5, 2));
        int day = stoi(date.substr(8));
        return countDays(day, month, year);
    }
    bool isLeapYear(int year) {
        return (year % 4 == 0 && year % 100 != 0) || year % 400 == 0;
    }
    int countDays(int day, int month, int year) {
        int res = 0;
        while (month > 1) {
            res += daysOfMonth[isLeapYear(year)][month - 2];
            month--;
        }
        res += day;
        return res;
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
