
- 作者：    负雪明烛
- id：      fuxuemingzhu
- 个人博客：[http://fuxuemingzhu.cn/](http://fuxuemingzhu.cn/)

---
@[TOC](目录)


题目地址：https://leetcode-cn.com/problems/add-bold-tag-in-string/

## 题目描述

Given a string s and a list of strings dict, you need to add a closed pair of bold tag `<b>` and `</b>` to wrap the substrings in `s` that exist in `dict`. If two such substrings overlap, you need to wrap them together by only one pair of closed bold tag. Also, if two substrings wrapped by bold tags are consecutive, you need to combine them.

Example 1:

    Input: 
    s = "abcxyz123"
    dict = ["abc","123"]
    Output:
    "<b>abc</b>xyz<b>123</b>"

Example 2:

    Input: 
    s = "aaabbcc"
    dict = ["aaa","aab","bc"]
    Output:
    "<b>aaabbc</b>c"

Note:

1. The given dict won't contain duplicates, and its length won't exceed 100.
1. All the strings in input have length in range [1, 1000].


## 题目大意

给一个字符串 `s` 和一个字符串列表 `dict` ，你需要将在字符串列表中出现过的 `s` 的子串添加加粗闭合标签 `<b>` 和 `</b>` 。如果两个子串有重叠部分，你需要把它们一起用一个闭合标签包围起来。同理，如果两个子字符串连续被加粗，那么你也需要把它们合起来用一个加粗标签包围。

## 解题方法

### 遍历

这个题和758. Bold Words in String题是一模一样的题目。

先使用一个数组isBold保存S中的每个字符是否应该加粗，判断的方式暴力解决即可，即查找每个子串是否在words中出现过。

是否增加标签`<b>`的方法是当前字符需要加粗，但是其前面的字符不用加粗，或者当前字符是第一个字符。
是否增加标签`</b>`的方法是当前字符需要加粗，但是其后面的字符不用加粗，或者当前字符是最后一个字符。

C++代码如下：

```cpp
class Solution {
public:
    string addBoldTag(string s, vector<string>& dict) {
        const int N = s.size();
        vector<bool> isBold(N, false);
        unordered_set<string> wordset(dict.begin(), dict.end());
        for (string& word : dict) {
            for (int i = 0; i < N; ++i) {
                string sub = s.substr(i, word.size());
                if (sub == word) {
                    for (int k = i; k < i + word.size(); ++k) {
                        isBold[k] = true;
                    }
                }
            }
        }
        string res;
        for (int i = 0; i < N; ++i) {
            if (isBold[i] && (i == 0 || !isBold[i - 1])) {
                res += "<b>";
            }
            res += s[i];
            if (isBold[i] && (i == N - 1 || !isBold[i + 1])) {
                res += "</b>";
            }
        }
        return res;
    }
};
```

## 日期

2019 年 9 月 18 日 —— 今日又是九一八


  [1]: https://blog.csdn.net/fuxuemingzhu/article/details/100977773
