

- 作者：    负雪明烛
- id：      fuxuemingzhu
- 个人博客：[http://fuxuemingzhu.cn/](http://fuxuemingzhu.cn/)

---
@[TOC](目录)


题目地址：https://leetcode-cn.com/problems/strobogrammatic-number/

## 题目描述

A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).

Write a function to determine if a number is strobogrammatic. The number is represented as a string.

Example 1:

    Input:  "69"
    Output: true

Example 2:

    Input:  "88"
    Output: true

Example 3:

    Input:  "962"
    Output: false

## 题目大意

中心对称数是指一个数字在旋转了 180 度之后看起来依旧相同的数字（或者上下颠倒地看）。
请写一个函数来判断该数字是否是中心对称数，其输入将会以一个字符串的形式来表达数字。


## 解题方法

### 字典

这个题和[1056. Confusing Number][1]是类似的，只不过这个题目使用的是字符串，因此需要更小心：字符串如果转整数越界！所以使用一个指针从最右边移动到最左边，把翻转后的字符拼接到一起，判断和原始字符串是否相等。

C++代码如下：

```cpp
class Solution {
public:
    bool isStrobogrammatic(string num) {
        if (num.empty()) return false;
        unordered_map<char, char> m{{'0', '0'}, {'1', '1'}, {'6', '9'}, {'8', '8'}, {'9', '6'}};
        string rotate;
        int pos = num.size() - 1;
        while (pos != -1) {
            char mod = num[pos];
            if (!m.count(mod))
                return false;
            rotate += m[mod];
            pos --;
        }
        return rotate == num;
    }
};
```

## 日期

2019 年 9 月 19 日 —— 举杯邀明月，对影成三人


  [1]: https://blog.csdn.net/fuxuemingzhu/article/details/100992424
