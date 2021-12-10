

- 作者：    负雪明烛
- id：      fuxuemingzhu
- 个人博客：[http://fuxuemingzhu.cn/](http://fuxuemingzhu.cn/)

---
@[TOC](目录)


题目地址：https://leetcode-cn.com/problems/valid-word-abbreviation/

## 题目描述

Given a non-empty string s and an abbreviation abbr, return whether the string matches with the given abbreviation.

A string such as "word" contains only the following valid abbreviations:

    ["word", "1ord", "w1rd", "wo1d", "wor1", "2rd", "w2d", "wo2", "1o1d", "1or1", "w1r1", "1o2", "2r1", "3d", "w3", "4"]

Notice that only the above abbreviations are valid abbreviations of the string "word". Any other string is not a valid abbreviation of "word".

Note:
- Assume s contains only lowercase letters and abbr contains only lowercase letters and digits.

Example 1:

    Given s = "internationalization", abbr = "i12iz4n":
    
    Return true.

Example 2:

    Given s = "apple", abbr = "a2e":
    
    Return false.


## 题目大意

给一个 非空 字符串 s 和一个单词缩写 abbr ，判断这个缩写是否可以是给定单词的缩写。

## 解题方法

### 双指针

一个指针指向abbr，一个指针指向word，根据abbr的数字情况移动word的指针，如果abbr指针指向的不是数字而是字符，那么判断是否和word字符相同。最后两个指针应该会同时移动到各自的结尾。

这个题有个小坑，就是有前导0的数字是非法的，需要判断一下。

C++代码如下：

```cpp
class Solution {
public:
    bool validWordAbbreviation(string word, string abbr) {
        int iword = 0;
        int iabbr = 0;
        while (iword < word.size() && iabbr < abbr.size()) {
            int count = 0;
            if (count == 0 && abbr[iabbr] == '0')
                return false;
            while (abbr[iabbr] >= '0' && abbr[iabbr] <= '9') {
                count = 10 * count + abbr[iabbr] - '0';
                iabbr ++;
            }
            iword += count;
            if ((iword >= word.size() && iabbr != abbr.size()) || 
                (iword != word.size() && iabbr >= abbr.size()))
                return false;
            if (iword == word.size() && iabbr == abbr.size())
                return true;
            if (word[iword] != abbr[iabbr])
                return false;
            iword ++;
            iabbr ++;
        }
        return iword == word.size() && iabbr == abbr.size();
    }
};
```

## 日期

2019 年 9 月 19 日 —— 举杯邀明月，对影成三人


  [1]: https://blog.csdn.net/fuxuemingzhu/article/details/100977773
