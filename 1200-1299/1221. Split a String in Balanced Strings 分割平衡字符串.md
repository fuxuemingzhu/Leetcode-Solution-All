- 作者：    负雪明烛
- id：      fuxuemingzhu
- 个人博客：[http://fuxuemingzhu.cn/](http://fuxuemingzhu.cn/)

---
@[TOC](目录)

题目地址：https://leetcode.com/problems/split-a-string-in-balanced-strings/

## 题目描述

Balanced strings are those who have equal quantity of `'L'` and `'R'` characters.

Given a balanced string `s` split it in the maximum amount of balanced strings.

Return the maximum amount of splitted balanced strings.

Example 1:

    Input: s = "RLRRLLRLRL"
    Output: 4
    Explanation: s can be split into "RL", "RRLL", "RL", "RL", each substring contains same number of 'L' and 'R'.

Example 2:

    Input: s = "RLLLLRRRLR"
    Output: 3
    Explanation: s can be split into "RL", "LLLRRR", "LR", each substring contains same number of 'L' and 'R'.

Example 3:
    
    Input: s = "LLLLRRRR"
    Output: 1
    Explanation: s can be split into "LLLLRRRR".
     

Constraints:

1. `1 <= s.length <= 1000`
1. `s[i] = 'L' or 'R'`

## 题目大意

计算一个字符串中有多少个合法的括号匹配。

## 解题方法

### 统计

括号匹配可以使用一个变量cnt进行统计，如果遇到左括号，cnt++；如果遇到右括号，cnt--；如果cnt==0说明是一个合法的括号匹配。

C++代码如下：

```cpp
class Solution {
public:
    int balancedStringSplit(string s) {
        int cnt = 0;
        int res = 0;
        for (char c : s) {
            if (c == 'R') {
                cnt ++;
            } else {
                cnt --;
            }
            if (cnt == 0)
                res ++;
        }
        return res;
    }
};
```


## 日期

2019 年 10 月 13 日 —— 国庆调休，这周末只有这一天假
