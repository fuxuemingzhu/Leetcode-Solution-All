

- 作者：    负雪明烛
- id：      fuxuemingzhu
- 个人博客：[http://fuxuemingzhu.cn/](http://fuxuemingzhu.cn/)

---
@[TOC](目录)

题目地址：https://leetcode-cn.com/problems/output-contest-matches/

## 题目描述

During the NBA playoffs, we always arrange the rather strong team to play with the rather weak team, like make the rank 1 team play with the rank nth team, which is a good strategy to make the contest more interesting. Now, you're given n teams, you need to output their final contest matches in the form of a string.

The n teams are given in the form of positive integers from 1 to n, which represents their initial rank. (Rank 1 is the strongest team and Rank n is the weakest team.) We'll use parentheses('(', ')') and commas(',') to represent the contest team pairing - parentheses('(' , ')') for pairing and commas(',') for partition. During the pairing process in each round, you always need to follow the strategy of making the rather strong one pair with the rather weak one.

Example 1:

    Input: 2
    Output: (1,2)
    Explanation: 
    Initially, we have the team 1 and the team 2, placed like: 1,2.
    Then we pair the team (1,2) together with '(', ')' and ',', which is the final answer.

Example 2:

    Input: 4
    Output: ((1,4),(2,3))
    Explanation: 
    In the first round, we pair the team 1 and 4, the team 2 and 3 together, as we need to make the strong team and weak team together.
    And we got (1,4),(2,3).
    In the second round, the winners of (1,4) and (2,3) need to play again to generate the final winner, so you need to add the paratheses outside them.
    And we got the final answer ((1,4),(2,3)).

Example 3:

    Input: 8
    Output: (((1,8),(4,5)),((2,7),(3,6)))
    Explanation: 
    First round: (1,8),(2,7),(3,6),(4,5)
    Second round: ((1,8),(4,5)),((2,7),(3,6))
    Third round: (((1,8),(4,5)),((2,7),(3,6)))
    Since the third round will generate the final winner, you need to output the answer (((1,8),(4,5)),((2,7),(3,6))).

Note:

- The n is in range [2, 212].
- We ensure that the input n can be converted into the form 2k, where k is a positive integer.

## 题目大意

在 NBA 季后赛中，我们总是安排较强的队伍对战较弱的队伍，例如用排名第 1 的队伍和第 n 的队伍对决，这是一个可以让比赛更加有趣的好策略。现在，给你 n 支队伍，你需要以字符串格式输出它们的 最终 比赛配对。

n 支队伍按从 1 到 n 的正整数格式给出，分别代表它们的初始排名（排名 1 最强，排名 n 最弱）。我们用括号（'(', ')'）和逗号（','）来表示匹配对——括号（'(', ')'）表示匹配，逗号（','）来用于分割。 在每一轮的匹配过程中，你都需要遵循将强队与弱队配对的原则。

## 解题方法

### 遍历

理解这个题的一个点是强队一定会战胜弱队。先安排最强和最弱，然后每次把剩余的最强和最弱安排到一起。

我们或许可以从第一轮里面得到灵感：

    First round: (1,8),(2,7),(3,6),(4,5)
    
每个括号里面的第一个元素是1,2,3,4是递增的，第二个元素是8,7,6,5是递减的。

使用一个vector<string>，里面存储的是各个队，然后每次把最后面的队伍弹出，放入最前面的队伍中，这样循环拼接即可。

再看第二轮：

    Second round: ((1,8),(4,5)),((2,7),(3,6))

(1,8)是第一轮的第一个，(4,5)是第一轮的最后一个，这两个构成了一个新的组，说明也是同样的最前和最后的组合。

这样会得到第三轮：

    Third round: (((1,8),(4,5)),((2,7),(3,6)))

把第二轮剩下的两组再拼到一起。

C++代码如下：

```cpp
class Solution {
public:
    string findContestMatch(int n) {
        vector<string> nums(n, "");
        for (int i = 1; i <= n; ++i) {
            nums[i - 1] = to_string(i);
        }
        while (n) {
            for (int i = 0; i < n / 2; ++i) {
                nums[i] = "(" + nums[i] + "," + nums.back() + ")";
                nums.pop_back();
            }
            n /= 2;
        }
        return nums[0];
    }
};
```

参考资料：https://leetcode-cn.com/problems/output-contest-matches/solution/shu-chu-bi-sai-pi-pei-dui-by-leetcode/

## 日期

2019 年 9 月 24 日 —— 梦见回到了小学，小学已经芳草萋萋破败不堪


  [1]: https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1569299800527&di=0791f14b34f5db98eb9acb10fbb908b1&imgtype=0&src=http://gss0.baidu.com/94o3dSag_xI4khGko9WTAnF6hhy/zhidao/pic/item/1ad5ad6eddc451da41652b3bb0fd5266d116324a.jpg
