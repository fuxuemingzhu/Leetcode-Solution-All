
- 作者：    负雪明烛
- id：      fuxuemingzhu
- 个人博客：[http://fuxuemingzhu.cn/](http://fuxuemingzhu.cn/)

---
@[TOC](目录)


题目地址：https://leetcode-cn.com/problems/split-concatenated-strings/

## 题目描述

Given a list of strings, you could concatenate these strings together into a loop, where for each string you could choose to reverse it or not. Among all the possible loops, you need to find the lexicographically biggest string after cutting the loop, which will make the looped string into a regular one.

Specifically, to find the lexicographically biggest string, you need to experience two phases:

Concatenate all the strings into a loop, where you can reverse some strings or not and connect them in the same order as given.
Cut and make one breakpoint in any place of the loop, which will make the looped string into a regular one starting from the character at the cutpoint.
And your job is to find the lexicographically biggest one among all the possible regular strings.

Example:

    Input: "abc", "xyz"
    Output: "zyxcba"
    Explanation: You can get the looped string "-abcxyz-", "-abczyx-", "-cbaxyz-", "-cbazyx-", 
    where '-' represents the looped status. 
    The answer string came from the fourth looped one, 
    where you could cut from the middle character 'a' and get "zyxcba".

Note:

1. The input strings will only contain lowercase letters.
1. The total length of all the strings will not over 1,000.

## 题目大意

给定一个字符串列表，你可以将这些字符串连接成一个循环字符串，对于每个字符串，你可以选择是否翻转它。在所有可能的循环字符串中，你需要分割循环字符串（这将使循环字符串变成一个常规的字符串），然后找到字典序最大的字符串。

## 解题方法

### 遍历

这个题比较绕，最重要的是理解题目：每个字符串可以翻转，不同字符串可以构成一个环，可以分割其中的一个字符串，但是字符串之间的相对顺序是不能改变的。因此，如果确定某个字符串放在最前面并分割，那么其余的字符串顺序是固定的！

因此，我们可以推断出，想要让所有的字符串环的结果最大，我们可以轮流把每个字符串当做起始字符串并进行分割，必须让当前分割后的字符串和其他字符串拼接成环是最大的。此时，由于其他字符串没有被分割而且顺序是固定的，因此他们能够成的最大值就是各自最大值之和。当前字符串有两种状态：翻转和不翻转，我们分别进行判断。

故方法为：先把每个字符串都进行是否翻转的判断，使成为单个字符串最大值。遍历每个字符串，遍历翻转不翻转两种状态，遍历该字符串分割位置，拼接其余所有字符串。求出最大值。

C++代码如下：

```cpp
class Solution {
public:
    string splitLoopedString(vector<string>& strs) {
        const int N = strs.size();
        vector<string> reversed;
        for (string& str : strs) {
            string rever = str;
            reverse(rever.begin(), rever.end());
            reversed.push_back(rever > str ? rever : str);
        }
        string res;
        for (int pos = 0; pos < N; ++pos) {
            string& str = reversed[pos];
            string rever = str;
            reverse(rever.begin(), rever.end());
            for (string cur : {str, rever}) {
                for (int i = 0; i < cur.size(); ++i) {
                    string curres;
                    curres += cur.substr(i);
                    for (int j = pos + 1; j < N; ++j) {
                        curres += reversed[j];
                    }
                    for (int j = 0; j < pos; ++j) {
                        curres += reversed[j];
                    }
                    curres += cur.substr(0, i);
                    res = res > curres ? res : curres;
                }
                
            }
            
        }
        return res;
    }
};
```

## 日期

2019 年 9 月 19 日 —— 举杯邀明月，对影成三人


  [1]: https://blog.csdn.net/fuxuemingzhu/article/details/100977773
