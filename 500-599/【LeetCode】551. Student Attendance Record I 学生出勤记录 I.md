
作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)

题目地址：[https://leetcode.com/problems/student-attendance-record-i/#/description][1]


## 题目描述

You are given a string representing an attendance record for a student. The record only contains the following three characters:

'A' : Absent.
'L' : Late.
'P' : Present.
A student could be rewarded if his attendance record doesn't contain **more than one 'A' (absent) or more than two continuous 'L' (late).**

You need to return whether the student could be rewarded according to his attendance record.

Example 1:

    Input: "PPALLP"
    Output: True

Example 2:

    Input: "PPALLL"
    Output: False

## 题目大意

如果A的次数不超过1次，连续L的次数不超过2次，那一定是优秀的同学，绝对是优秀的同学。

![在这里插入图片描述](https://www.jiuwa.net/tuku/20171226/jxnYtc8e.jpg)

判断一个学生是不是优秀的同学。

## 解题方法

### 正则表达式

一直错的原因是没看清题，题目说的是不超过一个A或者两个**连续的**L，直接求解有点麻烦，可以用正则表达式。
.*匹配的是任意字符重复0次或者任意次，一行代码搞定。

```java
public class Solution {
    public boolean checkRecord(String s) {
        return !s.matches(".*A.*A.*") && !s.matches(".*LLL.*");
    }
}
```

python写法如下，注意的是需要把正则表达式写在第一个参数，字符串s作为第二个参数。

```python
class Solution:
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        return not re.match(".*A.*A.*", s) and not re.match(".*LLL.*", s)
```

### 统计

直接数A的个数不能超过1，连续的L的个数不能多于2即可。代码还很简单高效的，超过了98%的提交。

```python
class Solution:
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        N = len(s)
        s = s + "P"
        countA = 0
        countL = 0
        for i in range(N):
            if s[i] == "A":
                countA += 1
            if countA > 1:
                return False
            if s[i] == "L":
                countL += 1
                if countL >= 3:
                    return False
            else:
                countL = 0
        return True
```

## 日期

2017 年 4 月 21 日 
2018 年 11 月 17 日 —— 美妙的周末，美丽的天气

  [1]: https://leetcode.com/problems/student-attendance-record-i/#/description
