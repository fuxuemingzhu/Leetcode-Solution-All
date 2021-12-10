
- 作者：    负雪明烛
- id：      fuxuemingzhu
- 个人博客：[http://fuxuemingzhu.cn/](http://fuxuemingzhu.cn/)

---
@[TOC](目录)


题目地址：https://leetcode-cn.com/problems/paint-house/

## 题目描述

There is a special keyboard with all keys in a single row.

Given a string keyboard of length 26 indicating the layout of the keyboard (indexed from 0 to 25), initially your finger is at index 0. To type a character, you have to move your finger to the index of the desired character. The time taken to move your finger from index `i` to index `j` is `|i - j|`.

You want to type a string word. Write a function to calculate how much time it takes to type it with one finger.


Example 1:

    Input: keyboard = "abcdefghijklmnopqrstuvwxyz", word = "cba"
    Output: 4
    Explanation: The index moves from 0 to 2 to write 'c' then to 1 to write 'b' then to 0 again to write 'a'.
    Total time = 2 + 1 + 1 = 4. 

Example 2:

    Input: keyboard = "pqrstuvwxyzabcdefghijklmno", word = "leetcode"
    Output: 73


Constraints:

1. `keyboard.length == 26`
1. keyboard contains each English lowercase letter exactly once in some order.
1. `1 <= word.length <= 10^4`
1. `word[i]` is an English lowercase letter.

## 题目大意

我们定制了一款特殊的力扣键盘，所有的键都排列在一行上。

我们可以按从左到右的顺序，用一个长度为 26 的字符串`keyboard`（索引从 0 开始，到 25 结束）来表示该键盘的键位布局。

现在需要测试这个键盘是否能够有效工作，那么我们就需要个机械手来测试这个键盘。

最初的时候，机械手位于左边起第一个键（也就是索引为 0 的键）的上方。当机械手移动到某一字符所在的键位时，就会在终端上输出该字符。

机械手从索引`i`移动到索引`j`所需要的时间是 `|i - j|`。

当前测试需要你使用机械手输出指定的单词 word，请你编写一个函数来计算机械手输出该单词所需的时间。


## 解题方法

### 字典

字典保存每个字符在keyboard中出现的位置，然后遍历单词，累加每个字符出现的位置与上次机械手的位置差。

C++代码如下：

```cpp
class Solution {
public:
    int calculateTime(string keyboard, string word) {
        unordered_map<char, int> keys;
        for (int i = 0; i < keyboard.size(); ++i) {
            keys[keyboard[i]] = i;
        }
        int res = 0;
        int pos = 0;
        for (char c : word) {
            int cur = keys[c];
            res += cur > pos ? cur - pos : pos - cur;
            pos = cur;
        }
        return res;
    }
};
```

## 日期

2019 年 9 月 18 日 —— 今日又是九一八
