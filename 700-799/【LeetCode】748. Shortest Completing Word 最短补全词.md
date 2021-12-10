
作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)

题目地址：https://leetcode.com/problems/shortest-completing-word/description/

## 题目描述

Find the minimum length word from a given dictionary words, which has all the letters from the string ``licensePlate``. Such a word is said to complete the given string ``licensePlate``

Here, for letters we ignore case. For example, "P" on the ``licensePlate`` still matches "p" on the word.

It is guaranteed an answer exists. If there are multiple answers, return the one that occurs first in the array.

The license plate might have the same letter occurring multiple times. For example, given a licensePlate of "PP", the word "pair" does not complete the ``licensePlate``, but the word "supper" does.

    Example 1:
    Input: licensePlate = "1s3 PSt", words = ["step", "steps", "stripe", "stepple"]
    Output: "steps"
    Explanation: The smallest length word that contains the letters "S", "P", "S", and "T".
    Note that the answer is not "step", because the letter "s" must occur in the word twice.
    Also note that we ignored case for the purposes of comparing whether a letter exists in the word.
    Example 2:
    Input: licensePlate = "1s3 456", words = ["looks", "pest", "stew", "show"]
    Output: "pest"
    Explanation: There are 3 smallest length words that contains the letters "s".
    We return the one that occurred first.
    
Note:
1. licensePlate will be a string with length in range [1, 7].
1. licensePlate will contain digits, spaces, or letters (uppercase or lowercase).
1. words will have a length in the range [10, 1000].
1. Every words[i] will consist of lowercase letters, and have length in range [1, 15].

## 题目大意

又是一个题目特别长，其实很简单的题，差点就放弃了。。

找出最短的符合licensePlate原则的字符串，如果有多个，那么返回第一个。

licensePlate原则其实特别简单，就是去除掉licensePlate里面的空格和数字，只保留英文字符，并转化为小写。然后再找words中包含这些字符的最短的字符串。

## 解题方法

这个题目中licensePlate规则看起来很复杂，其实只保留英文小写字母，然后找匹配就好了。看到一个比较好的方法，是通过Counter来做的，学到了可以使用``substract``方法来做减法。这样可以方便的找出words中包含的licensePlate的word。

代码：

```python
import re
from collections import Counter
class Solution(object):
    def shortestCompletingWord(self, licensePlate, words):
        """
        :type licensePlate: str
        :type words: List[str]
        :rtype: str
        """
        regex = re.compile('[^a-zA-Z]')
        license = regex.sub('',licensePlate)
        counter1 = Counter(license.lower())
        res = ''
        for word in words:
            if self.count(counter1, word):
                if res == '' or len(word) < len(res):
                    res = word
        return res
        
    def count(self, counter1, word):
        counter2 = Counter(word)
        counter2.subtract(counter1)
        return all([c >= 0 for c in counter2.values()])
```


---

二刷，python.

和上面的方法基本一样，可是更容易理解了。

```python
class Solution(object):
    def shortestCompletingWord(self, licensePlate, words):
        """
        :type licensePlate: str
        :type words: List[str]
        :rtype: str
        """
        subs = "1234567890"
        licensePlate = licensePlate.replace(" ", "").lower()
        for sub in subs:
            licensePlate = licensePlate.replace(sub, "")
        res = ""
        plateCount = collections.Counter(licensePlate)
        for word in words:
            match = True
            wordCount = collections.Counter(word)
            for w, c in plateCount.items():
                if c > wordCount[w]:
                    match = False
            if (not res or len(res) > len(word)) and match:
                res = word
        return res
```

## 日期

2018 年 3 月 3 日 
2018 年 11 月 10 日 —— 这么快就到双十一了？？

  [1]: http://blog.csdn.net/fuxuemingzhu/article/details/79359540
