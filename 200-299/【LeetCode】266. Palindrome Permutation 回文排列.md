
- 作者：    负雪明烛
- id：      fuxuemingzhu
- 个人博客：[http://fuxuemingzhu.cn/](http://fuxuemingzhu.cn/)

---
@[TOC](目录)


题目地址：https://leetcode-cn.com/problems/palindrome-permutation/

## 题目描述

Given a string, determine if a permutation of the string could form a palindrome.

Example 1:

    Input: "code"
    Output: false

Example 2:

    Input: "aab"
    Output: true

Example 3:

    Input: "carerac"
    Output: true


## 题目大意

给定一个字符串，判断该字符串中是否可以通过重新排列组合，形成一个回文字符串。

## 解题方法

### 字典

回文串中，左右必须对称，因此出现次数为奇数的字符最多只有一个。

使用一个字典，保存每个字符出现的次数。如果出现次数为奇数个的字符<=1，那么可以构成回文串。

C++代码如下：

```cpp
class Solution {
public:
    bool canPermutePalindrome(string s) {
        unordered_map<char, int> m_;
        for (char c : s) {
            m_[c]++;
        }
        int odd_count = 0;
        for (auto& it : m_) {
            if (it.second & 1)
                odd_count++;
        }
        return odd_count <= 1;
    }
};
```


## 日期

2019 年 9 月 17 日 —— 听了hulu宣讲会，觉得hulu的压力不大
