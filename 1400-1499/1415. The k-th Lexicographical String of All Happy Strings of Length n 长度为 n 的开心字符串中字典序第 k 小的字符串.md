
- 作者：    负雪明烛
- id：      fuxuemingzhu
- 个人博客：[http://fuxuemingzhu.cn/](http://fuxuemingzhu.cn/)

---
@[TOC](目录)


题目地址：https://leetcode-cn.com/contest/biweekly-contest-24/problems/the-k-th-lexicographical-string-of-all-happy-strings-of-length-n/

# 题目描述

一个 「开心字符串」定义为：

- 仅包含小写字母 ['a', 'b', 'c'].
- 对所有在 1 到 s.length - 1 之间的 i ，满足 s[i] != s[i + 1] （字符串的下标从 1 开始）。

比方说，字符串 "abc"，"ac"，"b" 和 "abcbabcbcb" 都是开心字符串，但是 "aa"，"baa" 和 "ababbc" 都不是开心字符串。

给你两个整数 n 和 k ，你需要将长度为 n 的所有开心字符串按字典序排序。

请你返回排序后的第 k 个开心字符串，如果长度为 n 的开心字符串少于 k 个，那么请你返回 空字符串 。

 
示例 1：

    输入：n = 1, k = 3
    输出："c"
    解释：列表 ["a", "b", "c"] 包含了所有长度为 1 的开心字符串。按照字典序排序后第三个字符串为 "c" 。

示例 2：

    输入：n = 1, k = 4
    输出：""
    解释：长度为 1 的开心字符串只有 3 个。

示例 3：

    输入：n = 3, k = 9
    输出："cab"
    解释：长度为 3 的开心字符串总共有 12 个 ["aba", "abc", "aca", "acb", "bab", "bac", "bca", "bcb", "cab", "cac", "cba", "cbc"] 。第 9 个字符串为 "cab"

示例 4：

    输入：n = 2, k = 7
    输出：""

示例 5：

    输入：n = 10, k = 100
    输出："abacbabacb"
 

提示：

1. `1 <= n <= 10`
1. `1 <= k <= 100`
 

# 题目大意

开心字符串就是由`['a', 'b', 'c']`构成的，不存在连续字符的字符串。问长度为 n 的，第 k 个字符串是多少。

# 解题方法

## 回溯法

看到题目给出 n 的范围是10以内，我们就知道可以用 回溯法 暴力求。

我们直接可以按照顺序求出长度为 n 的所有开心字符串，然后找出第 k 个。

DFS的时候，向字符串的最后再新增字符，可以拼接上 `['a', 'b', 'c']`，但不能存在连续字符，因此要和已经搜索的路径的最后一个字符进行比较。

由于我们按照按照`['a', 'b', 'c']`的顺序添加到字符串的最后的，所以得到的所有字符串就是有序的，不用排序。

注意当 k 大于所有开心字符串的长度的时候，需要返回空字符串。

Python代码如下：

```python
class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        happies = []
        self.genHappies(n, "", happies)
        if k > len(happies):
            return ""
        return happies[k - 1]

    def genHappies(self, n, path, happies):
        if len(path) == n:
            happies.append(path)
            return
        for x in ['a', 'b', 'c']:
            if not path or path[-1] != x:
                self.genHappies(n, path + x, happies)
```


**欢迎关注[负雪明烛的刷题博客](https://blog.csdn.net/fuxuemingzhu)，leetcode刷题800多，每道都讲解了详细写法！**

# 日期

2020 年 4 月 18 日 —— 个人赛蒙了


  [1]: https://blog.csdn.net/fuxuemingzhu/article/details/79451733
