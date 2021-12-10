

- 作者：    负雪明烛
- id：      fuxuemingzhu
- 个人博客：[http://fuxuemingzhu.cn/](http://fuxuemingzhu.cn/)

---
@[TOC](目录)

题目地址：https://leetcode-cn.com/problems/reverse-words-in-a-string-ii/

## 题目描述

Given an input string , reverse the string word by word. 

Example:

    Input:  ["t","h","e"," ","s","k","y"," ","i","s"," ","b","l","u","e"]
    Output: ["b","l","u","e"," ","i","s"," ","s","k","y"," ","t","h","e"]

Note: 

1. A word is defined as a sequence of non-space characters.
1. The input string does not contain leading or trailing spaces.
1. The words are always separated by a single space.

Follow up: Could you do it in-place without allocating extra space?

## 题目大意

给定一个字符串，逐个翻转字符串中的每个单词。

## 解题方法

### 每个单词单独翻转+总的翻转

没记错的话是剑指offer上的题目，做法是用到了一个公式`c b a = (aT bT cT)T`，如果知道这个公式应该很好办了。

为什么需要公式而不是直接找到首尾单词互换位置呢？很容易看出每个单词的长度是不同的，互换位置可能会覆盖其他的单词。

C++代码如下：

```cpp
class Solution {
public:
    void reverseWords(vector<char>& s) {
        if (s.empty()) return;
        int pre = 0;
        int cur = 0;
        while (cur <= s.size()) {
            if (cur == s.size() || s[cur] == ' ') {
                reverse(s, pre, cur - 1);
                pre = cur + 1;
            }
            cur ++;
        }
        reverse(s, 0, s.size() - 1);
    }
    // reverse [start, end]
    void reverse(vector<char>& s, int start, int end) {
        for (int i = 0; i <= (end - start) / 2; ++i) {
            swap(s[start + i], s[end - i]);
        }
    }
};
```

## 日期

2019 年 9 月 22 日 —— 熬夜废掉半条命


  [1]: https://assets.leetcode.com/uploads/2018/10/12/maze_1_example_1.png
  [2]: https://assets.leetcode.com/uploads/2018/10/13/maze_1_example_2.png
  [3]: https://blog.csdn.net/fuxuemingzhu/article/details/101056461
