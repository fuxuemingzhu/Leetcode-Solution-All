

- 作者：    负雪明烛
- id：      fuxuemingzhu
- 个人博客：[http://fuxuemingzhu.cn/](http://fuxuemingzhu.cn/)

---
@[TOC](目录)


题目地址：https://leetcode-cn.com/problems/before-and-after-puzzle/

## 题目描述

Given a list of phrases, generate a list of Before and After puzzles.

A phrase is a string that consists of lowercase English letters and spaces only. No space appears in the start or the end of a phrase. There are no consecutive spaces in a phrase.

Before and After puzzles are phrases that are formed by merging two phrases where the last word of the first phrase is the same as the first word of the second phrase.

Return the Before and After puzzles that can be formed by every two phrases `phrases[i]` and `phrases[j]` where `i != j`. Note that the order of matching two phrases matters, we want to consider both orders.

You should return a list of distinct strings sorted lexicographically.

 

Example 1:

    Input: phrases = ["writing code","code rocks"]
    Output: ["writing code rocks"]

Example 2:

    Input: phrases = ["mission statement",
                      "a quick bite to eat",
                      "a chip off the old block",
                      "chocolate bar",
                      "mission impossible",
                      "a man on a mission",
                      "block party",
                      "eat my words",
                      "bar of soap"]
    Output: ["a chip off the old block party",
             "a man on a mission impossible",
             "a man on a mission statement",
             "a quick bite to eat my words",
             "chocolate bar of soap"]

Example 3:

    Input: phrases = ["a","b","a"]
    Output: ["a"]

Constraints:

1. `1 <= phrases.length <= 100`
1. `1 <= phrases[i].length <= 100`


## 题目大意

给你一个「短语」列表 phrases，请你帮忙按规则生成拼接后的「新短语」列表。
「短语」（phrase）是仅由小写英文字母和空格组成的字符串。「短语」的开头和结尾都不会出现空格，「短语」中的空格不会连续出现。
「前后拼接」（Before and After puzzles）是合并两个「短语」形成「新短语」的方法。我们规定拼接时，第一个短语的最后一个单词 和 第二个短语的第一个单词 必须相同。
返回每两个「短语」 phrases[i] 和 phrases[j]（i != j）进行「前后拼接」得到的「新短语」。

## 解题方法

### 保存首尾字符串

假如两个不同短语的首尾单词是相等的，就可以拼接到一起。因此重点在找到每个短语的首尾单词是什么。由于C++的string不支持split，使用了遍历的方法，找到第一个空格和最后一个空格出现的位置，从而分割出首单词head和尾单词tail，放入一个字典中。字典的格式是`{字符串的索引：{首单词，尾单词}}`。

之后我们对每个短语都进行遍历查找其余的短语的`头单词`是否等于当前短语的`尾单词`，若相等则可以进行拼接。注意拼接的时候，重叠的首尾单词只需要保留其中一个。

最后，题目要我们返回排序了的拼接后的新短语，在C++中可以直接使用set进行排序。

C++代码如下：

```cpp
class Solution {
public:
    vector<string> beforeAndAfterPuzzles(vector<string>& phrases) {
        const int N = phrases.size();
        unordered_map<int, pair<string, string>> m;
        for (int i = 0; i < N; ++i) {
            string& phrase = phrases[i];
            int first = -1;
            int last = -1;
            for (int j = 0; j < phrase.size(); ++j) {
                if (phrase[j] == ' ') {
                    if (first == -1) {
                        first = j;
                    } 
                    last = j;
                }
            }
            string head = phrase.substr(0, first);
            string tail = phrase.substr(last + 1);
            m[i] = make_pair(head, tail);
        }
        set<string> s;
        for (int i = 0; i < N; ++i) {
            string& cur = phrases[i];
            for (auto& other : m) {
                if (other.first == i)
                    continue;
                if (other.second.first == m[i].second) {
                    s.insert(cur + phrases[other.first].substr(m[i].second.size()));
                }
            }
        }
        return vector<string>(s.begin(), s.end());
    }
};
```

## 日期

2019 年 9 月 20 日 —— 是选择中国互联网式加班？还是外企式养生？


  [1]: https://assets.leetcode.com/uploads/2018/10/12/maze_1_example_1.png
  [2]: https://assets.leetcode.com/uploads/2018/10/13/maze_1_example_2.png
