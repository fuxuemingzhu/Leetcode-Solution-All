

- 作者：    负雪明烛
- id：      fuxuemingzhu
- 个人博客：[http://fuxuemingzhu.cn/](http://fuxuemingzhu.cn/)

---
@[TOC](目录)


题目地址：https://leetcode.com/problems/day-of-the-week/

## 题目描述

Given a date, return the corresponding day of the week for that date.

The input is given as three integers representing the day, month and year respectively.

Return the answer as one of the following values `{"Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"}`.

Example 1:

    Input: day = 31, month = 8, year = 2019
    Output: "Saturday"

Example 2:

    Input: day = 18, month = 7, year = 1999
    Output: "Sunday"

Example 3:

    Input: day = 15, month = 8, year = 1993
    Output: "Sunday"
 

Constraints:

- The given dates are valid dates between the years 1971 and 2100.

## 题目大意

判断给出的日期是星期几。

## 解题方法

### 计算与1971-1-1之间天数

已知1971-1-1是星期5，那么计算出给出的天数和1971-1-1之间的天数即可。要判断是否是闰年，总共**度过**了多少年，**度过了**多少月，**度过了**多少天。

C++代码如下：

```cpp
class Solution {
public:
    string dayOfTheWeek(int day, int month, int year) {
        int days = countDaysFrom1971(day, month, year);
        return weekName[(days+ 5) % 7];
    }
    bool isLeapYear(int year) {
        return (year % 4 == 0 && year % 100 != 0) || year % 400 == 0;
    }
    int countDaysFrom1971(int day, int month, int year) {
        int res = 0;
        bool leapYear = isLeapYear(year);
        year --;
        while (year >= 1971) {
            res += isLeapYear(year) ? 366 : 365;
            year--;
        }
        while (month > 1) {
            res += daysOfMonth[leapYear][month - 2];
            month--;
        }
        res += day - 1;
        return res;
    }
    int daysOfMonth[2][12] = {
        {31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31},
        {31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31}
    };
    string weekName[7] = {"Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"};
};
```

## 日期

2019 年 9 月 18 日 —— 今日又是九一八
