- 作者：    负雪明烛
- id：      fuxuemingzhu
- 个人博客：[http://fuxuemingzhu.cn/](http://fuxuemingzhu.cn/)

---
@[TOC](目录)


题目地址：https://leetcode-cn.com/problems/sentence-similarity/

## 题目描述

Given two sentences `words1`, `words2` (each represented as an array of strings), and a list of similar word pairs pairs, determine if two sentences are similar.

For example, "great acting skills" and "fine drama talent" are similar, if the similar word pairs are pairs = [["great", "fine"], ["acting","drama"], ["skills","talent"]].

Note that the similarity relation is not transitive. For example, if "great" and "fine" are similar, and "fine" and "good" are similar, "great" and "good" are not necessarily similar.

However, similarity is symmetric. For example, "great" and "fine" being similar is the same as "fine" and "great" being similar.

Also, a word is always similar with itself. For example, the sentences words1 = ["great"], words2 = ["great"], pairs = [] are similar, even though there are no specified similar word pairs.

Finally, sentences can only be similar if they have the same number of words. So a sentence like words1 = ["great"] can never be similar to words2 = ["doubleplus","good"].

Note:

1. The length of words1 and words2 will not exceed 1000.
1. The length of pairs will not exceed 2000.
1. The length of each `pairs[i]` will be 2.
1. The length of each `words[i]` and `pairs[i][j]` will be in the range `[1, 20]`.


## 题目大意

给定两个句子 words1, words2 （每个用字符串数组表示），和一个相似单词对的列表 pairs ，判断是否两个句子是相似的。

## 解题方法

### 只修改区间起终点

这个题有一个坑的地方没说清楚：一个词可能会和多个词相似。

因此使用map<string, set<string>>的方式，保存{每个词 : 与之相似的词}所有映射关系。

注意相似是双向的，因此对于一个Pair，需要正反插入两次。

判断是否相似的时候，需要对两个列表的对应元素进行遍历，判断是否相等或者在其相似set中出现。

C++代码如下：

```cpp
class Solution {
public:
    bool areSentencesSimilar(vector<string>& words1, vector<string>& words2, vector<vector<string>>& pairs) {
        if (words1.size() != words2.size()) return false;
        const int N = words1.size();
        unordered_map<string, unordered_set<string>> similar;
        for (auto& pair : pairs) {
            similar[pair[0]].insert(pair[1]);
            similar[pair[1]].insert(pair[0]);
        }
        for (int i = 0; i < N; ++i) {
            if (words1[i] != words2[i] && !similar[words1[i]].count(words2[i])) {
                return false;
            }
        }
        return true;
    }
};
```

## 日期

2019 年 9 月 18 日 —— 今日又是九一八


  [1]: https://blog.csdn.net/fuxuemingzhu/article/details/100977773
