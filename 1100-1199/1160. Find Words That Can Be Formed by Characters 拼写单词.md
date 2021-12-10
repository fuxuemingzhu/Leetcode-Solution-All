

- 作者：    负雪明烛
- id：      fuxuemingzhu
- 个人博客：[http://fuxuemingzhu.cn/](http://fuxuemingzhu.cn/)

---
@[TOC](目录)


题目地址：https://leetcode-cn.com/problems/index-pairs-of-a-string/submissions/

## 题目描述

You are given an array of strings words and a string chars.

A string is good if it can be formed by characters from chars (each character can only be used once).

Return the sum of lengths of all good strings in words.

 

Example 1:

    Input: words = ["cat","bt","hat","tree"], chars = "atach"
    Output: 6
    Explanation: 
    The strings that can be formed are "cat" and "hat" so the answer is 3 + 3 = 6.

Example 2:

    Input: words = ["hello","world","leetcode"], chars = "welldonehoneyr"
    Output: 10
    Explanation: 
    The strings that can be formed are "hello" and "world" so the answer is 5 + 5 = 10.
 

Note:

1. `1 <= words.length <= 1000`
1. `1 <= words[i].length, chars.length <= 100`
1. All strings contain lowercase English letters only.


## 题目大意

给你一份『词汇表』（字符串数组） words 和一张『字母表』（字符串） chars。

假如你可以用 chars 中的『字母』（字符）拼写出 words 中的某个『单词』（字符串），那么我们就认为你掌握了这个单词。

注意：每次拼写时，chars 中的每个字母都只能用一次。

返回词汇表 words 中你掌握的所有单词的 长度之和。

## 解题方法

### 字典统计

这个题说字母表的每个字符只能使用一次，可以想到我们统计每个字符出现的次数，然后也判断每个单词中的字符次数进行判断就好了。

1. 使用字典统计给出的字母表中每个字符出现的次数；
2. 使用字典统计词汇表中每个单词中的每个字符出现的次数；
3. 如果该单词中的每个字符出现的次数都小于字母表中对应字符出现的次数，那么说明可以使用字母表构成该单词。

C++代码如下：

```cpp
class Solution {
public:
    int countCharacters(vector<string>& words, string chars) {
        unordered_map<char, int> chars_count;
        for (char c : chars) {
            chars_count[c] ++;
        }
        int res = 0;
        for (string& word : words) {
            unordered_map<char, int> word_count;
            for (char c: word) {
                word_count[c] ++;
            }
            bool can_form = true;
            for (auto& wc_iter : word_count) {
                if (chars_count[wc_iter.first] < wc_iter.second) {
                    can_form = false;
                    break;
                }
            }
            if (can_form) {
                res += word.size();
            }
        }
        return res;
    }
};
```

## 日期

2020 年 3 月 17 日 —— 很久没有做新题了


  [1]: https://blog.csdn.net/fuxuemingzhu/article/details/100977773
