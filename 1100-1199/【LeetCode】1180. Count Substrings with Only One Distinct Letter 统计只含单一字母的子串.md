
- 作者：    负雪明烛
- id：      fuxuemingzhu
- 个人博客：[http://fuxuemingzhu.cn/](http://fuxuemingzhu.cn/)

---
@[TOC](目录)


题目地址：https://leetcode-cn.com/problems/count-substrings-with-only-one-distinct-letter/

## 题目描述

Given a string `S`, return the number of substrings that have only one distinct letter.


Example 1:

    Input: S = "aaaba"
    Output: 8
    Explanation: The substrings with one distinct letter are "aaa", "aa", "a", "b".
    "aaa" occurs 1 time.
    "aa" occurs 2 times.
    "a" occurs 4 times.
    "b" occurs 1 time.
    So the answer is 1 + 2 + 4 + 1 = 8.

Example 2:

    Input: S = "aaaaaaaaaa"
    Output: 55

Constraints:

1. `1 <= S.length <= 1000`
1. `S[i]` consists of only lowercase English letters.


## 题目大意

给你一个字符串 S，返回只含 **单一字母** 的子串个数。

## 解题方法

### 组合数

从一段长度为n的单一字母字符串中，分别选择出长度为1,2,3,...,n的子串，共有`n * (n + 1) / 2`个结果。

因此，遍历字符串，分别统计出单一字母字符串的长度，累加所有结果即可。


C++代码如下：

```cpp
class Solution {
public:
    int countLetters(string S) {
        if (S.empty()) return 0;
        int count = 1;
        int res = 0;
        char cur = S[0];
        cout << endl;
        for (int i = 1; i <= S.size(); ++i) {
            if (i == S.size() || S[i] != cur) {
                res += count * (count + 1) / 2;
                cur = S[i];
                count = 1;
            } else {
                count ++;
            }
            
        }
        return res;
    }
};
```

## 日期

2019 年 9 月 18 日 —— 今日又是九一八
