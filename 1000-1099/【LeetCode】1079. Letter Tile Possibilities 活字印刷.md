
- 作者：    负雪明烛
- id：      fuxuemingzhu
- 个人博客：[http://fuxuemingzhu.cn/](http://fuxuemingzhu.cn/)

---
@[TOC](目录)

题目地址：https://leetcode.com/problems/letter-tile-possibilities/

## 题目描述

You have a set of tiles, where each tile has one letter `tiles[i]` printed on it.  Return the number of possible non-empty sequences of letters you can make.

Example 1:

    Input: "AAB"
    Output: 8
    Explanation: The possible sequences are "A", "B", "AA", "AB", "BA", "AAB", "ABA", "BAA".

Example 2:

    Input: "AAABBC"
    Output: 188

Note:

1. `1 <= tiles.length <= 7`
1. tiles consists of uppercase English letters.


## 题目大意

给出了一些活字印刷的模具，看能组合成多少种不同的单词。

## 解题方法

### 回溯

又是一个经典的回溯法。

让我们先看下AAB能构成的结果：

    A           // 剩余A、B
    AA AB       // 剩余B，剩余A
    AAB ABA     // 不剩
    
    B           // 剩余A、A
    BA          // 剩余A
    BAA         // 不剩

我们可以发现，先选择一个字母开始，然后从剩余的字母里选择1个、2个...直至用完所有字母，放到了第一个字母的后面。

因此是一个递归的方法，先统计每个字母出现的多少次，然后从中选择一个字母，再从剩下的字母中选择，直至所有字母都用完为止。

这里回溯的含义是，我们使用了个数组保存每个字母出现的次数，每次拼接上一个新的字母的时候，把结果res就加一，同时把对应的字母出现的次数减一；当把剩余的结果递归完成之后，需要把当前的字母的次数加上，以便后续的遍历，故称为回溯。

那为什么使用统计字母出现的次数，而不是直接在原来的单词上选择呢？好处是，这样同样的字母在同样的位置只会被选择一次。比如`AAB`的第一个A和第二个A都可以组成`AB`，如果在单词上选可能需要set进行去重，但是统计字母出现的次数的时候，在第一个位置选择A的时候只会选择一次。

C++代码如下：

```cpp
class Solution {
public:
    int numTilePossibilities(string tiles) {
        vector<int> count(26, 0);
        for (char c : tiles) {
            count[c - 'A'] ++;
        }
        int res = 0;
        backtrack(count, res);
        return res;
    }
    void backtrack(vector<int>& count, int& res) {
        for (int i = 0; i < 26; ++i) {
            if (count[i] == 0) continue;
            res ++;
            count[i] --;
            backtrack(count, res);
            count[i] ++;
        }
    }
};
```

## 日期

2019 年 9 月 25 日 —— 做梦都在秋招，这个秋天有毒


  [1]: https://ss0.bdstatic.com/70cFvHSh_Q1YnxGkpoWK1HF6hhy/it/u=3958884440,3883801982&fm=26&gp=0.jpg
