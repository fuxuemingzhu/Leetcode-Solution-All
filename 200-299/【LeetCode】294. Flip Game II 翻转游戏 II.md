- 作者：    负雪明烛
- id：      fuxuemingzhu
- 个人博客：[http://fuxuemingzhu.cn/](http://fuxuemingzhu.cn/)

---
@[TOC](目录)


题目地址：https://leetcode-cn.com/problems/flip-game-ii/

## 题目描述

You are playing the following Flip Game with your friend: Given a string that contains only these two characters: `+` and `-`, you and your friend take turns to flip two consecutive `"++"` into `"--"`. The game ends when a person can no longer make a move and therefore the other person will be the winner.

Write a function to determine if the **starting player** can guarantee a win.

Example:

    Input: s = "++++"
    Output: true 
    Explanation: The starting player can guarantee a win by flipping the middle "++" to become "+--+".
    Follow up:
    Derive your algorithm's runtime complexity.



## 题目大意

你和朋友玩一个叫做「翻转游戏」的游戏，游戏规则：给定一个只有 + 和 - 的字符串。你和朋友轮流将 连续 的两个 "++" 反转成 "--"。 当一方无法进行有效的翻转时便意味着游戏结束，则另一方获胜。
请你写出一个函数来判定起始玩家是否存在必胜的方案。

## 解题方法

### 记忆化搜索

类似的两个人轮流用同样的规则做游戏的题目，一般都可以用递归解决。

这个题使用递归的方法也很简单，第一个人在翻转`++`的时候，把翻转后的字符串递归传给下一个人。如果下一个人不能获胜，那么自己就获胜了。道理很简单。

如果不使用map保存已经判断过是否能获胜的字符串，总耗时540ms。但如果使用了map保存已经判定过的，可以获胜的字符串，那么时间缩短为52ms。这体现了记忆化搜索避免了重复的搜索，带来的高效。

C++代码如下：

```cpp
class Solution {
public:
    bool canWin(string s) {
        const int N = s.size();
        if (N <= 1) return false;
        if (win_.count(s) && win_[s]) return true;
        for (int i = 0; i < N - 1; ++i) {
            if (s[i] == '+' && s[i + 1] == '+') {
                string flip = s.substr(0, i) + "--" + s.substr(i + 2);
                if (!canWin(flip)) {
                    win_[s] = true;
                    return true;
                }
            }
        }
        return false;
    }
private:
    unordered_map<string, bool> win_;
};
```

## 日期

2019 年 9 月 21 日 —— 莫生气，我若气病谁如意


  [1]: https://assets.leetcode.com/uploads/2018/10/12/candy_crush_example_2.png
  [2]: https://blog.csdn.net/fuxuemingzhu/article/details/101068011
