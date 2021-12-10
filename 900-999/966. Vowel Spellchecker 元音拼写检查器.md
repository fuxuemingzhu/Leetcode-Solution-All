

作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)


题目地址：https://leetcode.com/problems/vowel-spellchecker/description/


## 题目描述

Given a wordlist, we want to implement a spellchecker that converts a query word into a correct word.

For a given query word, the spell checker handles two categories of spelling mistakes:

- Capitalization: If the query matches a word in the wordlist (case-insensitive), then the query word is returned with the same case as the case in the wordlist.
    - Example: wordlist = ["yellow"], query = "YellOw": correct = "yellow"
    - Example: wordlist = ["Yellow"], query = "yellow": correct = "Yellow"
    - Example: wordlist = ["yellow"], query = "yellow": correct = "yellow"

- Vowel Errors: If after replacing the vowels ('a', 'e', 'i', 'o', 'u') of the query word with any vowel individually, it matches a word in the wordlist (case-insensitive), then the query word is returned with the same case as the match in the wordlist.
    - Example: wordlist = ["YellOw"], query = "yollow": correct = "YellOw"
    - Example: wordlist = ["YellOw"], query = "yeellow": correct = "" (no match)
    - Example: wordlist = ["YellOw"], query = "yllw": correct = "" (no match)

In addition, the spell checker operates under the following precedence rules:

- When the query exactly matches a word in the wordlist (case-sensitive), you should return the same word back.
- When the query matches a word up to capitlization, you should return the first such match in the wordlist.
- When the query matches a word up to vowel errors, you should return the first such match in the wordlist.
- If the query has no matches in the wordlist, you should return the empty string.


Given some queries, return a list of words answer, where answer[i] is the correct word for query = queries[i].

 

Example 1:

    Input: wordlist = ["KiTe","kite","hare","Hare"], queries = ["kite","Kite","KiTe","Hare","HARE","Hear","hear","keti","keet","keto"]
    Output: ["kite","KiTe","KiTe","Hare","hare","","","KiTe","","KiTe"]
     

Note:

- 1 <= wordlist.length <= 5000
- 1 <= queries.length <= 5000
- 1 <= wordlist[i].length <= 7
- 1 <= queries[i].length <= 7
- All strings in wordlist and queries consist only of english letters.

## 题目大意

现在给了一个单词字典，给出了一堆要查询的词，要返回查询结果。查询的功能如下：

1. 如果字典里有现在的单词，就直接返回；
2. 如果不满足1，那么判断能不能更改要查询单词的某些大小写使得结果在字典中，如果字典里多个满足条件的，就返回第一个；
3. 如果不满足2，那么判断能不能替换要查询单词的元音字符成其他的字符使得结果在字典中，如果字典里多个满足条件的，就返回第一个；
4. 如果不满足4，返回查询的结果是空字符串。


## 解题方法

### 字典

这个题还是挺烦的，并不是一个考察搜索的题目，可以直接使用字典去解决。

首先，判断有没有相同的单词，这个很好办，直接使用set;
其次，要判断改变某些大小写，这里注意的是可以把要查询的字符串中的任意字符转换成大小写，如果抽象一点的话就是，忽略字符串所有字符的大小写之后匹配即可。因为要返回第一个出现的，所以，我们把要字典字符串反过来构成字典，这样就保存了忽略大小写之后的字符串第一个出现的位置。
最后，要把元音字符进行忽略，可以任意转换。这个思路很邪，直接把元音字符转成同样的字符，这样只要把元音统一替换之后的结果相等即可。同样反向构成字典。

python代码如下：

```python
class Solution(object):
    def spellchecker(self, wordlist, queries):
        """
        :type wordlist: List[str]
        :type queries: List[str]
        :rtype: List[str]
        """
        wordset = set(wordlist)
        capdict = {word.lower() : word for word in wordlist[::-1]}
        vodict = {re.sub(r'[aeiou]', '#', word.lower()) : word for word in wordlist[::-1]}
        res = []
        for q in queries:
            if q in wordset:
                res.append(q)
            elif q.lower() in capdict:
                res.append(capdict[q.lower()])
            elif re.sub(r'[aeiou]', '#', q.lower()) in vodict:
                res.append(vodict[re.sub(r'[aeiou]', '#', q.lower())])
            else:
                res.append("")
        return res
```


## 日期

2018 年 12 月 30 日 —— 周赛差强人意


  [1]: https://assets.leetcode.com/uploads/2018/12/28/unival_bst_1.png
  [2]: https://assets.leetcode.com/uploads/2018/12/28/unival_bst_2.png
  [3]: https://blog.csdn.net/fuxuemingzhu/article/details/82620422
