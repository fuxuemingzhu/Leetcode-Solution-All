- 作者：    负雪明烛
- id：      fuxuemingzhu
- 个人博客：[http://fuxuemingzhu.cn/](http://fuxuemingzhu.cn/)

---
@[TOC](目录)


题目地址：https://leetcode-cn.com/problems/construct-k-palindrome-strings/

# 题目描述

给你一个字符串 `s` 和一个整数 `k` 。请你用 `s` 字符串中 所有字符 构造 `k` 个非空 回文串 。

如果你可以用 `s` 中所有字符构造 `k` 个回文字符串，那么请你返回 `True` ，否则返回 `False` 。

 
示例 1：

    输入：s = "annabelle", k = 2
    输出：true
    解释：可以用 s 中所有字符构造 2 个回文字符串。
    一些可行的构造方案包括："anna" + "elble"，"anbna" + "elle"，"anellena" + "b"

示例 2：

    输入：s = "leetcode", k = 3
    输出：false
    解释：无法用 s 中所有字符构造 3 个回文串。

示例 3：

    输入：s = "true", k = 4
    输出：true
    解释：唯一可行的方案是让 s 中每个字符单独构成一个字符串。

示例 4：

    输入：s = "yzyzyzyzyzyzyzy", k = 2
    输出：true
    解释：你只需要将所有的 z 放在一个字符串中，所有的 y 放在另一个字符串中。那么两个字符串都是回文串。

示例 5：

    输入：s = "cr", k = 7
    输出：false
    解释：我们没有足够的字符去构造 7 个回文串。
 

提示：

1. `1 <= s.length <= 10^5`
1. `s` 中所有字符都是小写英文字母。
1. `1 <= k <= 10^5`

# 题目大意

判断给出的字符串 s 能不能恰好构成 k 个回文串。

# 解题方法

## 统计奇数字符出现次数

其实很简单。我们只需要判断字符串中有多少个出现次数为奇数的字符就行了。

为什么？

一个回文字符串中只能有 0 个或者 1 个出现次数为 1 的字符，这个字符必须位于回文字符串的中间。

因此，要判断能不能有 k 个回文字符串，我们就看奇数字符出现的次数是否小于等于 k 个。

分配情况：
1. 如果奇数字符恰好有 k 个，那么拆分出来的每个回文字符串中各分配 1 个。
2. 如果奇数字符小于 k 个，那么剩下的回文串中不分配奇数字符，即只由偶数字符构成。


C++代码如下。

```cpp
class Solution {
public:
    bool canConstruct(string s, int k) {
        const int N = s.size();
        if (N < k) return false;
        if (N == k) return true;
        vector<int> count(26, 0);
        for (char c : s) {
            count[c - 'a'] ++;
        }
        int count_odd = 0;
        for (int i = 0; i < count.size(); ++i) {
            if (count[i] % 2 == 1) {
                count_odd ++;
            }
        }
        return count_odd <= k;
    }
};
```


 **欢迎关注[负雪明烛的刷题博客](https://blog.csdn.net/fuxuemingzhu)，leetcode刷题800多，每道都讲解了详细写法！**

# 日期

2020 年 4 月 5 日 —— 好久不打周赛了


  [1]: https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/04/04/sample_4_1728.png
  [2]: https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/04/04/sample_2_1728.png
  [3]: https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/04/04/sample_6_1728.png
