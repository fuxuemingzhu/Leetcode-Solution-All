

- 作者：    负雪明烛
- id：      fuxuemingzhu
- 个人博客：[http://fuxuemingzhu.cn/](http://fuxuemingzhu.cn/)

---
@[TOC](目录)


题目地址：https://leetcode-cn.com/problems/flip-game/

## 题目描述

You are playing the following Flip Game with your friend: Given a string that contains only these two characters: `+` and `-`, you and your friend take turns to flip two consecutive `"++"` into `"--"`. The game ends when a person can no longer make a move and therefore the other person will be the winner.

Write a function to compute all possible states of the string after one valid move.

Example:

    Input: s = "++++"
    Output: 
    [
      "--++",
      "+--+",
      "++--"
    ]

Note: If there is no valid move, return an empty list [].


## 题目大意

把给定字符串中的`++`换成`--`，返回所有可能的结果。

## 解题方法

### 遍历

题目表述不清，其实只要把所有`++`换成`--`即可，那就很简单了，直接遍历一次就行了。

C++代码如下：

```cpp
class Solution {
public:
    vector<string> generatePossibleNextMoves(string s) {
        vector<string> res;
        if (s.empty() || s.size() == 1) return res;
        for (int i = 1; i < s.size(); ++i) {
            if (s[i] == '+' && s[i - 1] == '+') {
                string move = s;
                move[i] = move[i - 1] = '-';
                res.push_back(move);
            }
        }
        return res;
    }
};
```

## 日期

2019 年 9 月 19 日 —— 举杯邀明月，对影成三人


  [1]: https://blog.csdn.net/fuxuemingzhu/article/details/100977773
