

- 作者：    负雪明烛
- id：      fuxuemingzhu
- 个人博客：[http://fuxuemingzhu.cn/](http://fuxuemingzhu.cn/)

---
@[TOC](目录)


题目地址：https://leetcode-cn.com/problems/remove-vowels-from-a-string/

## 题目描述

Given a string `S`, remove the vowels `'a', 'e', 'i', 'o', and 'u'` from it, and return the new string.

Example 1:

    Input: "leetcodeisacommunityforcoders"
    Output: "ltcdscmmntyfrcdrs"

Example 2:

    Input: "aeiou"
    Output: ""

Note:

1. S consists of lowercase English letters only.
1. `1 <= S.length <= 1000`


## 题目大意

给你一个字符串 S，请你删去其中的所有元音字母（ 'a'，'e'，'i'，'o'，'u'），并返回这个新字符串。

## 解题方法

### 判断字符是否是aeiou

判断是否是元音字符，决定是否加入结果中。

C++代码如下：

```cpp
class Solution {
public:
    string removeVowels(string S) {
        string res;
        for (char c : S) {
            if (c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u')
                continue;
            res += c;
        }
        return res;
    }
};
```

## 日期

2019 年 9 月 18 日 —— 今日又是九一八
