
- 作者：    负雪明烛
- id：      fuxuemingzhu
- 个人博客：[http://fuxuemingzhu.cn/](http://fuxuemingzhu.cn/)

---
@[TOC](目录)


题目地址：https://leetcode-cn.com/problems/shortest-word-distance-ii/

## 题目描述

Design a class which receives a list of words in the constructor, and implements a method that takes two words *word1* and *word2* and return the shortest distance between these two words in the list. Your method will be called repeatedly many times with different parameters.

Example:

    Assume that words = ["practice", "makes", "perfect", "coding", "makes"].
    
    Input: word1 = “coding”, word2 = “practice”
    Output: 3
    Input: word1 = "makes", word2 = "coding"
    Output: 1

Note:
You may assume that word1 does not equal to word2, and word1 and word2 are both in the list.

## 题目大意

请设计一个类，使该类的构造函数能够接收一个单词列表。然后再实现一个方法，该方法能够分别接收两个单词 word1 和 word2，并返回列表中这两个单词之间的最短距离。您的方法将被以不同的参数调用 多次。

## 解题方法

### 字典保存出现位置

这个题让我们求两个字符串出现的最短距离，其实很好办，先分别找到这两个单词出现的位置，然后两两比较，找出最短距离即可。因为给出的words里面会有重复，所以应该使用`unordered_map<string, vector<int>> positions;`保存所有出现的位置。


C++代码如下：

```cpp
class WordDistance {
public:
    WordDistance(vector<string>& words) {
        for (int i = 0; i < words.size(); ++i) {
            positions[words[i]].push_back(i);
        }
    }
    
    int shortest(string word1, string word2) {
        vector<int> pos1 = positions[word1];
        vector<int> pos2 = positions[word2];
        int res = INT_MAX;
        for (int p1 : pos1) {
            for (int p2 : pos2) {
                res = min(res, abs(p1 - p2));
            }
        }
        return res;
    }
private:
    unordered_map<string, vector<int>> positions;
};

/**
 * Your WordDistance object will be instantiated and called as such:
 * WordDistance* obj = new WordDistance(words);
 * int param_1 = obj->shortest(word1,word2);
 */
```

## 日期

2019 年 9 月 22 日 —— 熬夜废掉半条命


  [1]: https://assets.leetcode.com/uploads/2018/10/12/candy_crush_example_2.png
  [2]: https://blog.csdn.net/fuxuemingzhu/article/details/101068011
