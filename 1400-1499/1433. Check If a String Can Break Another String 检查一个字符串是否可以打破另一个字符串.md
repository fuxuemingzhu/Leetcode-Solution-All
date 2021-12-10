- 作者：    负雪明烛
- id：      fuxuemingzhu
- 个人博客：[http://fuxuemingzhu.cn/](http://fuxuemingzhu.cn/)

---
@[TOC](目录)


题目地址：https://leetcode-cn.com/problems/check-if-a-string-can-break-another-string/

# 题目描述

给你两个字符串 `s1` 和 `s2` ，它们长度相等，请你检查是否存在一个 `s1` 的排列可以打破 `s2` 的一个排列，或者是否存在一个 `s2` 的排列可以打破 `s1` 的一个排列。

字符串 `x` 可以打破字符串 `y` （两者长度都为 `n` ）需满足对于所有 `i`（在 `0` 到 `n - 1` 之间）都有 `x[i] >= y[i]`（字典序意义下的顺序）。

示例 1：

    输入：s1 = "abc", s2 = "xya"
    输出：true
    解释："ayx" 是 s2="xya" 的一个排列，"abc" 是字符串 s1="abc" 的一个排列，且 "ayx" 可以打破 "abc" 。

示例 2：

    输入：s1 = "abe", s2 = "acd"
    输出：false 
    解释：s1="abe" 的所有排列包括："abe"，"aeb"，"bae"，"bea"，"eab" 和 "eba" ，s2="acd" 的所有排列包括："acd"，"adc"，"cad"，"cda"，"dac" 和 "dca"。然而没有任何 s1 的排列可以打破 s2 的排列。也没有 s2 的排列能打破 s1 的排列。

示例 3：

    输入：s1 = "leetcodee", s2 = "interview"
    输出：true

提示：

1. `s1.length == n`
1. `s2.length == n`
1. `1 <= n <= 10^5`
1. 所有字符串都只包含小写英文字母。

# 题目大意

对两个字符串分别进行重新排序，是否可以让某个字符串的每个字符 都大于等于 另外一个字符串对应位置的字符。

# 解题方法

## 排序

这个题不用想复杂，只用分别对两个字符串进行排序，然后依次比较两个字符串各个位置的字符。

为什么这样可行？

比如 bac 和 xyz 两个字符串，先对 bac 排序得到 abc。

假如把最小的 x 放到了最前面，如果 x 仍然小于 a，那么把 x 放在其他位置会仍然小于 abc 的对应字符。因此必须把第二个字符最小的字符也放在最前。

所以只用对两个字符串排序，然后按位置比较就行了。

Python 代码如下：

```python
class Solution:
    def checkIfCanBreak(self, s1: str, s2: str) -> bool:
        s1 = sorted(s1)
        s2 = sorted(s2)
        return all(s1[i] >= s2[i] for i in range(len(s1))) or all(s1[i] <= s2[i] for i in range(len(s1)))
```

**欢迎关注[负雪明烛的刷题博客](https://blog.csdn.net/fuxuemingzhu)，leetcode刷题800多，每道都讲解了详细写法！**

# 日期

2020 年 5 月 2 日 —— 双周赛最后一题不会，是时候多练练hard题了


  [1]: https://blog.csdn.net/fuxuemingzhu/article/details/79451733
