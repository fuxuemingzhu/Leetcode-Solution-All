
- 作者：    负雪明烛
- id：      fuxuemingzhu
- 个人博客：[http://fuxuemingzhu.cn/](http://fuxuemingzhu.cn/)

---
@[TOC](目录)


题目地址：https://leetcode-cn.com/problems/index-pairs-of-a-string/

## 题目描述

Given a text string and words (a list of strings), return all index pairs `[i, j]` so that the substring `text[i]...text[j]` is in the list of words.

Example 1:

    Input: text = "thestoryofleetcodeandme", words = ["story","fleet","leetcode"]
    Output: [[3,7],[9,13],[10,17]]

Example 2:

    Input: text = "ababa", words = ["aba","ab"]
    Output: [[0,1],[0,2],[2,3],[2,4]]
    Explanation: 
    Notice that matches can overlap, see "aba" is found in [0,2] and [2,4].

Note:

1. All strings contains only lowercase English letters.
1. It's guaranteed that all strings in words are different.
1. `1 <= text.length <= 100`
1. `1 <= words.length <= 20`
1. `1 <= words[i].length <= 50`
Return the pairs [i,j] in sorted order (i.e. sort them by their first coordinate in case of ties sort them by their second coordinate).

## 题目大意

给出 字符串 `text` 和 字符串列表 `words`, 返回所有的索引对 `[i, j]` 使得在索引对范围内的子字符串 `text[i]...text[j]`（包括 i 和 j）属于字符串列表 words。


## 解题方法

### 遍历

暴力遍历所有的字符串子串，看其是否在words中。为了加速查找效率，使用的set。

C++代码如下：

```cpp
class Solution {
public:
    vector<vector<int>> indexPairs(string text, vector<string>& words) {
        unordered_set<string> wordset(words.begin(), words.end());
        const int N = text.size();
        vector<vector<int>> res;
        for (int i = 0; i < N; ++i) {
            for (int j = i; j < N; ++j) {
                string cur = text.substr(i, j - i + 1);
                if (wordset.count(cur)) {
                    res.push_back({i, j});
                }
            }
        }
        return res;
    }
};
```

## 日期

2019 年 9 月 18 日 —— 今日又是九一八


  [1]: https://blog.csdn.net/fuxuemingzhu/article/details/100977773
