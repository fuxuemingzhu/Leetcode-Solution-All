
- 作者：    负雪明烛
- id：      fuxuemingzhu
- 个人博客：[http://fuxuemingzhu.cn/](http://fuxuemingzhu.cn/)

---
@[TOC](目录)


题目地址：https://leetcode-cn.com/problems/valid-word-square/

## 题目描述

Given a sequence of words, check whether it forms a valid word square.

A sequence of words forms a valid word square if the kth row and column read the exact same string, where `0 ≤ k < max(numRows, numColumns)`.

Note:

1. The number of words given is at least 1 and does not exceed 500.
1. Word length will be at least 1 and does not exceed 500.
1. Each word contains only lowercase English alphabet a-z.

Example 1:

    Input:
    [
      "abcd",
      "bnrt",
      "crmy",
      "dtye"
    ]
    
    Output:
    true
    
    Explanation:
    The first row and first column both read "abcd".
    The second row and second column both read "bnrt".
    The third row and third column both read "crmy".
    The fourth row and fourth column both read "dtye".
    
    Therefore, it is a valid word square.

Example 2:

    Input:
    [
      "abcd",
      "bnrt",
      "crm",
      "dt"
    ]
    
    Output:
    true
    
    Explanation:
    The first row and first column both read "abcd".
    The second row and second column both read "bnrt".
    The third row and third column both read "crm".
    The fourth row and fourth column both read "dt".
    
    Therefore, it is a valid word square.

Example 3:

    Input:
    [
      "ball",
      "area",
      "read",
      "lady"
    ]
    
    Output:
    false
    
    Explanation:
    The third row reads "read" while the third column reads "lead".
    
    Therefore, it is NOT a valid word square.


## 题目大意

给你一个单词序列，判断其是否形成了一个有效的单词方块。

有效的单词方块是指此由单词序列组成的文字方块的 第 k 行 和 第 k 列 (0 ≤ k < max(行数, 列数)) 所显示的字符串完全相同。

## 解题方法

### 拼接出每一列的字符串

一种简单的做法，就是按照题目说的，拼接出每一列的字符串，然后判断是否和对应的行相等。

需要注意的是每行每列的字符串长度并不是固定的，在拼接每一列的字符串的时候要进行判断是否需要拼，防止字符串取字符时越界。


C++代码如下：

```cpp
class Solution {
public:
    bool validWordSquare(vector<string>& words) {
        int maxCol = 0;
        for (string& word : words) {
            if (maxCol < word.size())
                maxCol = word.size();
        }
        int total = maxCol > words.size() ? maxCol : words.size();
        for (int col = 0; col < total; ++col) {
            string curcol;
            for (int row = 0; row < words.size(); ++row) {
                if (words[row].size() > col) {
                    curcol += words[row][col];
                }
            }
            if (curcol != words[col]) {
                return false;
            }
                
        }
        return true;
    }
};
```

## 日期

2019 年 9 月 19 日 —— 举杯邀明月，对影成三人


  [1]: https://blog.csdn.net/fuxuemingzhu/article/details/100977773
