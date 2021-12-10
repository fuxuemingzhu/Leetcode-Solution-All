
作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)

题目地址：https://leetcode.com/problems/goat-latin/description/

## 题目描述

A sentence ``S`` is given, composed of words separated by spaces. Each word consists of lowercase and uppercase letters only.

We would like to convert the sentence to "Goat Latin" (a made-up language similar to Pig Latin.)

The rules of Goat Latin are as follows:

- If a word begins with a vowel (a, e, i, o, or u), append ``"ma"`` to the end of the word.
For example, the word ``'apple'`` becomes ``'applema'``.
 
- If a word begins with a consonant (i.e. not a vowel), remove the first letter and append it to the end, then add ``"ma"``.
For example, the word ``"goat"`` becomes ``"oatgma"``.
 
- Add one letter ``'a'`` to the end of each word per its word index in the sentence, starting with 1.
For example, the first word gets ``"a"`` added to the end, the second word gets ``"aa"`` added to the end and so on.

Return the final sentence representing the conversion from ``S`` to Goat Latin. 

 

Example 1:

    Input: "I speak Goat Latin"
    Output: "Imaa peaksmaaa oatGmaaaa atinLmaaaaa"

Example 2:

    Input: "The quick brown fox jumped over the lazy dog"
    Output: "heTmaa uickqmaaa rownbmaaaa oxfmaaaaa umpedjmaaaaaa overmaaaaaaa hetmaaaaaaaa azylmaaaaaaaaa ogdmaaaaaaaaaa"
 

Notes:

1. S contains only uppercase, lowercase and spaces. Exactly one space between each word.
1. 1 <= S.length <= 150.


## 题目大意

要把英语翻译成Goat Latin语。翻译规则如下：

把英文句子按照空格分割成各个单词。

1. 如果单词以元音字母开头，后面接上``"ma"``；
2. 如果不以元音开头，把首字母移到最后，然后接上``"ma"``；
3. 每个单词后面接上在句子中出现的第几位置个``"a"``。

## 解题方法

python天生的适合处理字符串问题。这种纯粹的拼操作的，没有思考的题目，分分钟搞定啊～

太简单了，不讲了。

```python
class Solution:
    def toGoatLatin(self, S):
        """
        :type S: str
        :rtype: str
        """
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        words = S.split(' ')
        new_words = []
        for i, word in enumerate(words):
            if word[0] in vowels:
                word += 'ma'
            else:
                word = word[1:] + word[0] + 'ma'
            word += 'a' * (i + 1)
            new_words.append(word)
        return ' '.join(new_words)
```

## 日期

2018 年 5 月 27 日 —— 周末的天气很好～
2018 年 11 月 ９ 日 —— 睡眠可以
