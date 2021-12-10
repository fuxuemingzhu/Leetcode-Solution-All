
作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)

题目地址：https://leetcode.com/problems/most-common-word/description/

## 题目描述

Given a paragraph and a list of banned words, return the most frequent word that is not in the list of banned words.  It is guaranteed there is at least one word that isn't banned, and that the answer is unique.

Words in the list of banned words are given in lowercase, and free of punctuation.  Words in the paragraph are not case sensitive.  The answer is in lowercase.

Example:

    Input: 
    
    paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
    banned = ["hit"]
    
    Output: "ball"
    
    Explanation: 
    
    "hit" occurs 3 times, but it is a banned word.
    "ball" occurs twice (and no other word does), so it is the most frequent non-banned word in the paragraph. 
    Note that words in the paragraph are not case sensitive,
    that punctuation is ignored (even if adjacent to words, such as "ball,"), 
    and that "hit" isn't the answer even though it occurs more because it is banned.
 

Note:

1. `1 <= paragraph.length <= 1000.`
1. `1 <= banned.length <= 100.`
1. `1 <= banned[i].length <= 10.`
1. The answer is unique, and written in lowercase (even if its occurrences in paragraph may have uppercase symbols, and even if it is a proper noun.)
1. paragraph only consists of letters, spaces, or the punctuation symbols `!?',;.`
1. Different words in paragraph are always separated by a space.
1. There are no hyphens or hyphenated words.
1. Words only consist of letters, never apostrophes or other punctuation symbols.


## 题目大意

给出了一段文字，并给出了一个过滤词的列表。要把该段文字全部转化为小写，过滤掉标点符号和过滤词。在剩下的单词里，找出出现次数最多的词。

## 解题方法

### 正则+统计

字符串问题都不是问题。

因为要过滤掉标点，所以可以使用很多次的replace函数，但这样太蠢了。直接正则搞定，使用sub函数可以实现替换，即把出现过的标点符号替换成空格`" "`。并且把字符串转成小写。

例如对于case：

```
"a, a, a, a, b,b,b,c, c"
["a"]
```

经过正则把标点替换成空格之后的words的结果：

```
['a', '', 'a', '', 'a', '', 'a', '', 'b', 'b', 'b', 'c', '', 'c']
```

剩下的工作就比较简单了：找出不是空字符串并且不在过滤词表里的词，使用Counter统计词频。

most_common函数的参数设为1表示找出出现次数最多的词，返回的格式是`[["hit",3]]`。

Python代码如下：

```python
class Solution:
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        p = re.compile(r"[!?',;.]")
        sub_para = p.sub(' ', paragraph.lower())
        words = sub_para.split(' ')
        words = [word for word in words if word and word not in banned]
        count = collections.Counter(words)
        return count.most_common(1)[0][0]
```

另外一种正则方法是，只保留字符串。写法如下：

```python
class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        paragraph = re.findall(r"\w+", paragraph.lower())
        count = collections.Counter(x for x in paragraph if x not in banned)
        return count.most_common(1)[0][0]
```


## 日期

2018 年 5 月 27 日 —— 周末的天气很好～
2018 年 11 月 19 日 —— 周一又开始了
2020 年 3 月 26 日 —— 感谢本文评论给出的case
