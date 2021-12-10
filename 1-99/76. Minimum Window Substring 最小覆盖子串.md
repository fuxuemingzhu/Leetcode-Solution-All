

作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)

题目地址: https://leetcode.com/problems/minimum-window-substring/description/

## 题目描述

Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).

Example:

    Input: S = "ADOBECODEBANC", T = "ABC"
    Output: "BANC"

Note:

- If there is no such window in S that covers all characters in T, return the empty string "".
- If there is such window, you are guaranteed that there will always be only one unique minimum window in S.

## 题目大意

在S中找出包含T的全部字符的最小子串。

## 解题方法
### 滑动窗口

统计字符出现的个数，而且时间复杂度要求 O(N)，明显使用**滑动窗口**解题。和[567. Permutation in String][1]有点相似，都是要求子字符串满足一定的次数要求。

**什么场景下使用滑动窗口？** 答：如果我们找到了一个满足要求的区间，并且当区间的右边界再向右扩张已没有意义，此时可以移动左边界到达不满足要求的位置。再移动右边界，持续如此，直到区间的右边界到达整体的结束点。

比如本题：当我们在 s 中找到了一个覆盖了 t 的所有字符的子字符串 `s[left, right]` 时，如果再向右移动 right ，扩大范围后的新的子字符串仍然覆盖了 t 的所有字符，但新子字符串一定不是最短了（题目要求最短的子字符串）。这就是我说的右边界向右扩张已没有意义，此时应该移动左边界直至使得区间不满足子字符串不满足覆盖 t 。

本题做法：

1. 定义 `left`, `right` 分别指向滑动窗口的左右边界，子字符串为 `s[left, right]` 双闭区间。

2. 使用 `right` 指针向右搜索，同时要记录在 `s[left, right]` 这个区间覆盖了多少个 `t` 中的元素。如果在 `s[left,right]` 内，覆盖了所有 t 的元素，说明这个区间是符合要求的一个区间。此时 `right `指针再向右移动已经没有意义。
3. 现在要移动 `left` 指针，直至 `s[left,right]` 子字符串不能覆盖 `t` 。

统计字符出现的次数可以直接使用字典，但如果对于每个 `s[left, right]` 区间都去统计一遍所有元素出现的次数，会导致方法复杂度会增加到 `O(N ^ 2)`，因此不能通过 OJ。必须快速地判定  `s[left,right]`  是否覆盖了 `t`。

题目说，在 `s[left, right]` **闭区间**内的元素出现个数应该把 `t` 中所有的元素都包含，所以我们定义 `scount` 字典变量保存`s[left, right]` **闭区间**中各个元素出现的次数；定义 `tcount` 字典变量保存 `t` 中的元素出现次数。  `cnt` 变量储存 `s[left, right]` 闭区间中已经覆盖了 `t` 中的多少个元素，如果 `cnt == t.size()` 说明该子数组覆盖了 `t`。

在移动 `left` 指针的时候要注意存储最短的子串，使用的 `minLen` 变量存储当前满足题目要求的最短子串长度。当某个子字符串区间满足要求时，根据`minLen`更新最终的最短子串结果 `res`。

这个题难点就在于维护 `cnt`，它的作用仅仅为了提高速度。

时间复杂度是`O(N)`，空间复杂度是`O(N)`。

这个题的 C++ 代码如下：

```cpp
class Solution {
public:
    string minWindow(string s, string t) {
        int M = s.size();
        int N = t.size();
        unordered_map<char, int> scount;
        unordered_map<char, int> tcount;
        // left and right means [left, right] of s
        // count means the same chars of s[left, right] with t
        int left = 0, right = 0, count = 0;
        int minLen = INT_MAX;
        string res;
        for (char c : t)
            ++tcount[c];
        while (right < M) {
            char c = s[right];
            scount[c] += 1;
            if (tcount.count(c) && scount[c] <= tcount[c]) {
                count += 1;
            }
            while (left <= right && count == N) {
                if (minLen > right - left + 1) {
                    minLen = right - left + 1;
                    res = s.substr(left, minLen);
                }
                char l = s[left];
                scount[l] -= 1;
                if (tcount.count(l) && scount[l] < tcount[l])
                    count -= 1;
                ++left;
            }
            ++right;
        }
        return res;
    }
};
```

参考资料：

https://leetcode.com/articles/minimum-window-substring/
http://www.cnblogs.com/grandyang/p/4340948.html

## 日期

2018 年 10 月 3 日 —— 玩游戏导致没睡好，脑子是浆糊。
2020 年 5 月 23 日 —— 这次编辑时对滑动窗口有了更深的理解

  [1]: https://blog.csdn.net/fuxuemingzhu/article/details/82876662
