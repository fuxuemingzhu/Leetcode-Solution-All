作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)


题目地址：https://leetcode.com/contest/weekly-contest-114/problems/verifying-an-alien-dictionary/


## 题目描述

In an alien language, surprisingly they also use english lowercase letters, but possibly in a different ``order``. The ``order`` of the alphabet is some permutation of lowercase letters.

Given a sequence of ``words`` written in the alien language, and the ``order`` of the alphabet, return ``true`` if and only if the given ``words`` are sorted lexicographicaly in this alien language.

 

Example 1:

    Input: words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"
    Output: true
    Explanation: As 'h' comes before 'l' in this language, then the sequence is sorted.

Example 2:

    Input: words = ["word","world","row"], order = "worldabcefghijkmnpqstuvxyz"
    Output: false
    Explanation: As 'd' comes after 'l' in this language, then words[0] > words[1], hence the sequence is unsorted.

Example 3:

    Input: words = ["apple","app"], order = "abcdefghijklmnopqrstuvwxyz"
    Output: false
    Explanation: The first three characters "app" match, and the second string is shorter (in size.) According to lexicographical rules "apple" > "app", because 'l' > '∅', where '∅' is defined as the blank character which is less than any other character (More info).
 

Note:

1. 1 <= words.length <= 100
1. 1 <= words[i].length <= 20
1. order.length == 26
1. All characters in words[i] and order are english lowercase letters.



## 题目大意

题目给出的所有字符都是小写字符，给了一个新的字母表顺序，问，给出的words数组，是不是有序的。

## 解题方法

直接依次进行判断即可。拿出两个相邻的字符串pre和after，然后判断他们的相同位置的每个字符的顺序，如果pre的某个位置小于after，说明这两个字符串是有序的，那么继续判断；如果Pre的某个位置大于after，说明不有序，直接返回False。这两部判断完成之后没结束，我们还要继续判断Example 3的情况，所以，需要判断pre的长度是不是大于after，并且after等于pre的前部分。

在遍历完所有的字符串之后都没有返回False，说明是有序的，那么返回True.

```python
class Solution(object):
    def isAlienSorted(self, words, order):
        """
        :type words: List[str]
        :type order: str
        :rtype: bool
        """
        N = len(words)
        d = {c : i for i, c in enumerate(order)}
        for i in range(N - 1):
            pre, after = words[i], words[i + 1]
            if pre == after: continue
            _len = min(len(pre), len(after))
            for j in range(_len):
                if d[pre[j]] < d[after[j]]:
                    break
                elif d[pre[j]] > d[after[j]]:
                    return False
            if len(pre) > len(after) and pre[:_len] == after:
                return False
        return True
```



## 日期

2018 年 12 月 9 日 —— 周赛懵逼了



  [1]: https://leetcode.com/static/images/courses/range_sum_query_2d.png
  [2]: https://leetcode.com/static/images/courses/sum_od.png
  [3]: https://leetcode.com/static/images/courses/sum_ob.png
  [4]: https://leetcode.com/static/images/courses/sum_oc.png
  [5]: https://leetcode.com/static/images/courses/sum_oa.png
  [6]: https://blog.csdn.net/fuxuemingzhu/article/details/79253036
