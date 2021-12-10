
- 作者：    负雪明烛
- id：      fuxuemingzhu
- 个人博客：[http://fuxuemingzhu.cn/](http://fuxuemingzhu.cn/)

---
@[TOC](目录)

题目地址：https://leetcode-cn.com/problems/shortest-word-distance-iii/

## 题目描述

Given a list of words and two words `word1` and `word2`, return the shortest distance between these two words in the list.

`word1` and `word2` may be the same and they represent two individual words in the list.

Example:

    Assume that words = ["practice", "makes", "perfect", "coding", "makes"].

    Input: word1 = “makes”, word2 = “coding”
    Output: 1
    Input: word1 = "makes", word2 = "makes"
    Output: 3

Note:

- You may assume word1 and word2 are both in the list.


## 题目大意

给定一个单词列表和两个单词 word1 和 word2，返回列表中这两个单词之间的最短距离。

word1 和 word2 是有可能相同的，并且它们将分别表示为列表中两个独立的单词。

## 解题方法

### 字典+暴力检索

字典保存每个单词的下标，然后分类讨论：

1. 如果两个单词不同，那么直接暴力检索这两个的所有坐标的差值绝对值，找最小的。
2. 如果两个单词相同，那么相当于从一个有序数组中找到相邻数字的最小差值，需要一次遍历。

C++代码如下：

```cpp
class Solution {
public:
    int shortestWordDistance(vector<string>& words, string word1, string word2) {
        unordered_map<string, vector<int>> m;
        for (int i = 0; i < words.size(); ++i) {
            m[words[i]].push_back(i);
        }
        int res = INT_MAX;
        if (word1 != word2) {
            for (int i : m[word1]) {
                for (int j : m[word2]) {
                    res = min(res, abs(i - j));
                }
            }
        } else {
            for (int i = 1; i < m[word1].size(); ++i) {
                res = min(res, m[word1][i] - m[word1][i - 1]);
            }
        }
        return res;
    }
};
```

## 日期

2019 年 9 月 24 日 —— 梦见回到了小学，小学已经芳草萋萋破败不堪


  [1]: https://ss0.bdstatic.com/70cFvHSh_Q1YnxGkpoWK1HF6hhy/it/u=3958884440,3883801982&fm=26&gp=0.jpg
