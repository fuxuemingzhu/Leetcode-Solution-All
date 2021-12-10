# 【LeetCode】809. Expressive Words 解题报告（Python）

标签（空格分隔）： LeetCode

作者： 		负雪明烛 
id：				fuxuemingzhu
个人博客：	http://fuxuemingzhu.me/

---

题目地址：https://leetcode.com/problems/expressive-words/description/

## 题目描述：

Sometimes people repeat letters to represent extra feeling, such as "hello" -> "heeellooo", "hi" -> "hiiii".  Here, we have groups, of adjacent letters that are all the same character, and adjacent characters to the group are different.  A group is extended if that group is length 3 or more, so "e" and "o" would be extended in the first example, and "i" would be extended in the second example.  As another example, the groups of "abbcccaaaa" would be "a", "bb", "ccc", and "aaaa"; and "ccc" and "aaaa" are the extended groups of that string.

For some given string S, a query word is stretchy if it can be made to be equal to S by extending some groups.  Formally, we are allowed to repeatedly choose a group (as defined above) of characters c, and add some number of the same character c to it so that the length of the group is 3 or more.  Note that we cannot extend a group of size one like "h" to a group of size two like "hh" - all extensions must leave the group extended - ie., at least 3 characters long.

Given a list of query words, return the number of words that are stretchy. 

Example:

    Input: 
    S = "heeellooo"
    words = ["hello", "hi", "helo"]
    Output: 1
    Explanation: 
    We can extend "e" and "o" in the word "hello" to get "heeellooo".
    We can't extend "helo" to get "heeellooo" because the group "ll" is not extended.

Notes:

1. 0 <= len(S) <= 100.
1. 0 <= len(words) <= 100.
1. 0 <= len(words[i]) <= 100.
1. S and all words in words consist only of lowercase letters

## 题目大意

给出了一个字符串，其中有些字母是为了表现“情绪”而重复出现了多次，给出了一个列表，看列表中有多少个可以是这个字符串的源字符串。前提：表现语气最少需要一个字母重复三次。

## 解题方法

出题人真会玩啊，这个题首先把源字符串做分割，把列表中的每个词也做分割，判断源字符串的分割能否被列表中单词的分割一一对应上。其实重点就是如何按照重复情况进行字符串分割。

另外，判断能否被表达的方式是，分割出来的元素个数是一致的，如果S的分割的字符长度小于3需要完全相等，否则需要大于word的长度。

```python
class Solution(object):
    def expressiveWords(self, S, words):
        """
        :type S: str
        :type words: List[str]
        :rtype: int
        """
        ans = 0
        set_S = set(S)
        S_list = []
        pre_s, pre_index = S[0], 0
        for i, s in enumerate(S):
            if pre_s != s:
                S_list.append(S[pre_index:i])
                pre_s, pre_index = s, i
            if i == len(S) - 1:
                S_list.append(S[pre_index:])
        for word in words:
            if set(word) != set_S:
                continue
            word_list = []
            pre_w, pre_index = word[0], 0
            for i, w in enumerate(word):
                if pre_w != w:
                    word_list.append(word[pre_index:i])
                    pre_w, pre_index = w, i
                if i == len(word) - 1:
                    word_list.append(word[pre_index:])
            if len(S_list) == len(word_list):
                if all(S_list[i] == word_list[i] if len(S_list[i]) < 3 else len(S_list[i]) >= len(word_list[i]) for i in range(len(S_list))):
                    ans += 1
        return ans
```

## 日期

2018 年 6 月 13 日 ———— 实验室椅子质量不行啊。。往后一仰，靠背断了。。


  [1]: https://blog.csdn.net/fuxuemingzhu/article/details/80661715