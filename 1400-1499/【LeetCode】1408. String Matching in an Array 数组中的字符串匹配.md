- 作者：    负雪明烛
- id：      fuxuemingzhu
- 个人博客：[http://fuxuemingzhu.cn/](http://fuxuemingzhu.cn/)

---
@[TOC](目录)


题目地址：https://leetcode-cn.com/problems/string-matching-in-an-array/

# 题目描述

给你一个字符串数组 `words` ，数组中的每个字符串都可以看作是一个单词。请你按 任意 顺序返回 `words` 中是其他单词的子字符串的所有单词。

如果你可以删除 `words[j]` 最左侧和/或最右侧的若干字符得到 `word[i]` ，那么字符串 `words[i]` 就是 `words[j]` 的一个子字符串。

 

示例 1：

    输入：words = ["mass","as","hero","superhero"]
    输出：["as","hero"]
    解释："as" 是 "mass" 的子字符串，"hero" 是 "superhero" 的子字符串。
    ["hero","as"] 也是有效的答案。

示例 2：

    输入：words = ["leetcode","et","code"]
    输出：["et","code"]
    解释："et" 和 "code" 都是 "leetcode" 的子字符串。

示例 3：

    输入：words = ["blue","green","bu"]
    输出：[]
     

提示：

1. `1 <= words.length <= 100`
1. `1 <= words[i].length <= 30`
1. `words[i]` 仅包含小写英文字母。
1. 题目数据 保证 每个 `words[i]` 都是独一无二的。


# 题目大意

看有哪些词被另外一个词所包含。

# 解题方法

## 暴力遍历

题目给出的规模很少，所以直接暴力两两遍历，直接判断其中一个是不是包含另外一个单词。

Python代码如下：

```python
class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        res = set()
        for word in words:
            for cur in words:
                if cur in word and cur != word:
                    res.add(cur)
        return list(res)
```


**欢迎关注[负雪明烛的刷题博客](https://blog.csdn.net/fuxuemingzhu)，leetcode刷题800多，每道都讲解了详细写法！**

# 日期

2020 年 4 月 12 日 —— dp问题还是不太会


  [1]: https://blog.csdn.net/fuxuemingzhu/article/details/79451733
