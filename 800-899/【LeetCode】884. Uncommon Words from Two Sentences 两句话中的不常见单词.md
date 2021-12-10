
作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)

题目地址：https://leetcode.com/problems/uncommon-words-from-two-sentences/description/

## 题目描述

We are given two sentences ``A`` and ``B``.  (A sentence is a string of space separated words.  Each word consists only of lowercase letters.)

A word is uncommon if it appears exactly once in one of the sentences, and does not appear in the other sentence.

Return a list of all uncommon words. 

You may return the list in any order.

 

Example 1:

    Input: A = "this apple is sweet", B = "this apple is sour"
    Output: ["sweet","sour"]

Example 2:

    Input: A = "apple apple", B = "banana"
    Output: ["banana"]
 
Note:

- 0 <= A.length <= 200
- 0 <= B.length <= 200
- A and B both contain only spaces and lowercase letters.


## 题目大意

如果一个词在一句话中只出现了一次，在另外一句话中没出现，那么这个词是不同的词。找出两句话中所有不同的词。

## 解题方法

### 字典统计

统计一下两句话单词的set，找出两个set的不同词，然后再判断这个词是否只出现了1次，如果只出现了1次，即为题目所求。

注意，要先找不同词，然后再判断是否出现1次。如这个测试用例：

    Input:
    "s z z z s"
    "s z ejt"
    Output:
    ["ejt","s","z"]
    Expected:
    ["ejt"]

不可以先去重组成set，然后再求。。也就是说，只要一个词在一句话中出现的次数超过了1次，那么一定会被排除掉。

另外注意，这其实是求下面这个图的A+B部分。在python3中的Counter.keys是个set，可以直接做交并补操作。

![此处输入图片的描述][1]

代码如下：

```python3
class Solution:
    def uncommonFromSentences(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: List[str]
        """
        count_A = collections.Counter(A.split(' '))
        count_B = collections.Counter(B.split(' '))
        words = list((count_A.keys() | count_B.keys()) - (count_A.keys() & count_B.keys()))
        ans = []
        for word in words:
            if count_A[word] == 1 or count_B[word] == 1:
                ans.append(word)
        return ans
```

## 日期

2018 年 8 月 16 日 —— 一个月不写题，竟然啥都不会了。。加油！
2018 年 11 月 8 日 —— 项目进展缓慢

  [1]: https://t.alipayobjects.com/images/rmsweb/T1GM0iXaNhXXXXXXXX.png
