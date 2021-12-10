- 作者：    负雪明烛
- id：      fuxuemingzhu
- 个人博客：[http://fuxuemingzhu.cn/](http://fuxuemingzhu.cn/)

---
@[TOC](目录)

题目地址：https://leetcode-cn.com/problems/generalized-abbreviation/

## 题目描述

Write a function to generate the generalized abbreviations of a word. 

Note: The order of the output does not matter.

Example:

    Input: "word"
    Output:
    ["word", "1ord", "w1rd", "wo1d", "wor1", "2rd", "w2d", "wo2", "1o1d", "1or1", "w1r1", "1o2", "2r1", "3d", "w3", "4"]


## 题目大意

生成一个字符串的所有缩写。

## 解题方法

### DFS

该题是让我们生成缩写，本质是个搜索题。

使用index表示当前遍历到哪个字符了，使用nums表示在遍历到当前字符时前面已经省略掉了多少个字符。

对于每个位置，我们有两个选择：

1. 这个位置如果不使用，则累加现在已有的省略掉的数字num
1. 这个位置如果使用，则拼接前面已经累加的数字num，拼接当前字符，省略掉的字符从0开始

所以这个问题本身还是简单的，需要注意的是num为0的时候不应该进行拼接。
另外，这个题为什么没有像全排列/子集一样，进行for循环呢？这是由于在构造字符缩写的时候起点、顺序都不能变的，这个不是抽取或者排列的问题。

C++代码如下：

```cpp
class Solution {
public:
    vector<string> generateAbbreviations(string word) {
        vector<string> res;
        dfs(res, word, 0, 0, "");
        return res;
    }
    void dfs(vector<string>& res, string& word, int index, int num, string cur) {
        if (index == word.size()) {
            if (num != 0)
                cur = cur + to_string(num);
            res.push_back(cur);
            return;
        }
        // 不用word[index]
        dfs(res, word, index + 1, num + 1, cur);
        // 用word[index]
        dfs(res, word, index + 1, 0, cur + (num == 0 ? "" : to_string(num)) + word[index]);
    }
};
```

## 日期

2019 年 9 月 27 日 —— 昨天面快手，竟然是纯刷题


  [1]: https://assets.leetcode.com/uploads/2019/05/03/capture.JPG
  [2]: https://blog.csdn.net/fuxuemingzhu/article/details/79616156
