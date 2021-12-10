
- 作者：    负雪明烛
- id：      fuxuemingzhu
- 个人博客：[http://fuxuemingzhu.cn/](http://fuxuemingzhu.cn/)

---
@[TOC](目录)


题目地址：https://leetcode-cn.com/problems/bold-words-in-string/

## 题目描述

Given a set of keywords words and a string `S`, make all appearances of all keywords in `S` bold. Any letters between `<b>` and `</b>` tags become bold.

The returned string should use the least number of tags possible, and of course the tags should form a valid combination.

For example, given that `words = ["ab", "bc"]` and `S = "aabcd"`, we should return `"a<b>abc</b>d"`. Note that returning `"a<b>a<b>b</b>c</b>d"` would use more tags, so it is incorrect.

Note:

1. `words` has length in range `[0, 50]`.
1. `words[i]` has length in range `[1, 10]`.
1. `S` has length in range `[0, 500]`.
1. All characters in `words[i]` and `S` are lowercase letters.

## 题目大意

给定一个关键词集合 words 和一个字符串 S，将所有 S 中出现的关键词加粗。所有在标签 `<b>` 和 `</b>` 中的字母都会加粗。
返回的字符串需要使用尽可能少的标签，当然标签应形成有效的组合。
例如，给定 `words = ["ab", "bc"]` 和 `S = "aabcd"`，需要返回 `"a<b>abc</b>d"`。注意返回 `"a<b>a<b>b</b>c</b>d"` 会使用更多的标签，因此是错误的。

## 解题方法

### 遍历

先使用一个数组isBold保存S中的每个字符是否应该加粗，判断的方式是，遍历words中的每个字符串，找出S中有哪些位置和它匹配。

是否增加标签`<b>`的方法是当前字符需要加粗，但是其前面的字符不用加粗，或者当前字符是第一个字符。
是否增加标签`</b>`的方法是当前字符需要加粗，但是其后面的字符不用加粗，或者当前字符是最后一个字符。


C++代码如下：

```cpp
class Solution {
public:
    string boldWords(vector<string>& words, string S) {
        const int N = S.size();
        vector<bool> isBold(N, false);
        for (string& word : words) {
            for (int i = 0; i < N; ++i) {
                string sub = S.substr(i, word.size());
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
            res += S[i];
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
