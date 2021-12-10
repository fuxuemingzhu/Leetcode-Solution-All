- 作者：    负雪明烛
- id：      fuxuemingzhu
- 个人博客：[http://fuxuemingzhu.cn/](http://fuxuemingzhu.cn/)

---
@[TOC](目录)


题目地址：https://leetcode-cn.com/problems/html-entity-parser/

# 题目描述

「HTML 实体解析器」 是一种特殊的解析器，它将 HTML 代码作为输入，并用字符本身替换掉所有这些特殊的字符实体。

HTML 里这些特殊字符和它们对应的字符实体包括：

- 双引号：字符实体为 `&quot`; ，对应的字符是 " 。
- 单引号：字符实体为 `&apos`; ，对应的字符是 ' 。
- 与符号：字符实体为 `&amp`; ，对应对的字符是 & 。
- 大于号：字符实体为 `&gt`; ，对应的字符是 > 。
- 小于号：字符实体为 `&lt`; ，对应的字符是 < 。
- 斜线号：字符实体为 `&frasl`; ，对应的字符是 / 。

给你输入字符串 text ，请你实现一个 HTML 实体解析器，返回解析器解析后的结果。

示例 1：

    输入：text = "&amp; is an HTML entity but &ambassador; is not."
    输出："& is an HTML entity but &ambassador; is not."
    解释：解析器把字符实体 &amp; 用 & 替换

示例 2：

    输入：text = "and I quote: &quot;...&quot;"
    输出："and I quote: \"...\""

示例 3：

    输入：text = "Stay home! Practice on Leetcode :)"
    输出："Stay home! Practice on Leetcode :)"

示例 4：
    
    输入：text = "x &gt; y &amp;&amp; x &lt; y is always false"
    输出："x > y && x < y is always false"

示例 5：

    输入：text = "leetcode.com&frasl;problemset&frasl;all"
    输出："leetcode.com/problemset/all"
 

提示：

1. `1 <= text.length <= 10^5`
1. 字符串可能包含 256 个ASCII 字符中的任意字符。

# 题目大意

把给出的文本中的字符进行替换。

# 解题方法

## 替换

直接按照题目要求进行替换。

Python代码如下：

```python
class Solution:
    def entityParser(self, text: str) -> str:
        d = {"&quot;": '"',
            "&apos;": "'",
            "&amp;": "&",
            "&gt;": ">",
            "&lt;": "<",
            "&frasl;": "/"}
        for k, v in d.items():
            text = text.replace(k, v)
        return text
```


**欢迎关注[负雪明烛的刷题博客](https://blog.csdn.net/fuxuemingzhu)，leetcode刷题800多，每道都讲解了详细写法！**

# 日期

2020 年 4 月 12 日 —— dp问题还是不太会


  [1]: https://blog.csdn.net/fuxuemingzhu/article/details/79451733
