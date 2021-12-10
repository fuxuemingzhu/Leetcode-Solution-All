

- 作者：    负雪明烛
- id：      fuxuemingzhu
- 个人博客：[http://fuxuemingzhu.cn/](http://fuxuemingzhu.cn/)

---
@[TOC](目录)


题目地址：https://leetcode-cn.com/problems/shortest-word-distance/

## 题目描述

Given a list of words and two words word1 and word2, return the shortest distance between these two words in the list.

Example:

    Assume that words = ["practice", "makes", "perfect", "coding", "makes"].
    
    Input: word1 = “coding”, word2 = “practice”
    Output: 3
    Input: word1 = "makes", word2 = "coding"
    Output: 1

Note:
- You may assume that word1 does not equal to word2, and word1 and word2 are both in the list.

## 题目大意

给定一个单词列表和两个单词 word1 和 word2，返回列表中这两个单词之间的最短距离。

## 解题方法

### 字典

字典保存每个单词出现位置，然后对于word1和word2的位置两两交叉求最小值即可。

C++代码如下：

```cpp
class Solution {
public:
    int shortestDistance(vector<string>& words, string word1, string word2) {
        unordered_map<string, vector<int>> position;
        for (int i = 0; i < words.size(); ++i) {
            position[words[i]].push_back(i);
        }
        int res = INT_MAX;
        for (int i : position[word1]) {
            for (int j : position[word2]) {
                res = min(res, i < j ? j - i : i - j);
            }
        }
        return res;
    }
};
```

## 日期

2019 年 9 月 18 日 —— 今日又是九一八
