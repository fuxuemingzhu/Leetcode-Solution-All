
- 作者：    负雪明烛
- id：      fuxuemingzhu
- 个人博客：[http://fuxuemingzhu.cn/](http://fuxuemingzhu.cn/)

---
@[TOC](目录)


题目地址：https://leetcode-cn.com/contest/weekly-contest-185/problems/reformat-the-string/

# 题目描述


给你一个混合了数字和字母的字符串 s，其中的字母均为小写英文字母。

请你将该字符串重新格式化，使得任意两个相邻字符的类型都不同。也就是说，字母后面应该跟着数字，而数字后面应该跟着字母。

请你返回 重新格式化后 的字符串；如果无法按要求重新格式化，则返回一个 空字符串 。

 

示例 1：

    输入：s = "a0b1c2"
    输出："0a1b2c"
    解释："0a1b2c" 中任意两个相邻字符的类型都不同。 "a0b1c2", "0a1b2c", "0c2a1b" 也是满足题目要求的答案。

示例 2：

    输入：s = "leetcode"
    输出：""
    解释："leetcode" 中只有字母，所以无法满足重新格式化的条件。

示例 3：

    输入：s = "1229857369"
    输出：""
    解释："1229857369" 中只有数字，所以无法满足重新格式化的条件。

示例 4：

    输入：s = "covid2019"
    输出："c2o0v1i9d"

示例 5：

    输入：s = "ab123"
    输出："1a2b3"
 

提示：

1. `1 <= s.length <= 500`
1. s 仅由小写英文字母和/或数字组成。


# 题目大意

把一个字符串重新整理成 字符和 数字 轮流交替的形式。

# 解题方法

## 栈

让字符和 数字 轮流交替拼接到字符串里。

需要注意的是如果最后剩下来有字符怎么办。

1. 如果剩下的字符大于2个，不能完成拼接
2. 如果剩下字符只有1个，拼到字符串的开头或者结尾，注意保证交替。

我用的是个栈的思想。由于题目没有说明排列顺序的问题，其实可以用任何方法，只要保证字符和数字不连续就行。

Python代码如下：

```python
class Solution:
    def reformat(self, s: str) -> str:
        strs = [c for c in s if not c.isdigit()]
        digits = [c for c in s if c.isdigit()]
        res = ""
        while strs and digits:
            res += strs.pop() + digits.pop()
        if len(strs) > 1 or len(digits) > 1:
            return ""
        elif len(strs) == 1:
            res += strs.pop()
        elif len(digits) == 1:
            res = digits.pop() + res
        return res
```


**欢迎关注[负雪明烛的刷题博客](https://blog.csdn.net/fuxuemingzhu)，leetcode刷题800多，每道都讲解了详细写法！**

# 日期

2020 年 4 月 19 日 —— 近期比赛太多


  [1]: https://blog.csdn.net/fuxuemingzhu/article/details/79451733
