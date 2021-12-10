作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)


题目地址：https://leetcode.com/problems/find-common-characters/


## 题目描述

Given an array ``A`` of strings made only from lowercase letters, return a list of all characters that show up in all strings within the list (**including duplicates**).  For example, if a character occurs 3 times in all strings but not 4 times, you need to include that character three times in the final answer.

You may return the answer in any order.

 

Example 1:

    Input: ["bella","label","roller"]
    Output: ["e","l","l"]

Example 2:

    Input: ["cool","lock","cook"]
    Output: ["c","o"]

Note:

1. ``1 <= A.length <= 100``
1. ``1 <= A[i].length <= 100``
1. ``A[i][j]`` is a lowercase letter

## 题目大意

给出了一个字符串列表，每个字符串都只包含小写字符，如果某个字符在所有的字符串中均出现，那么就把这个字符放到结果列表中。注意，如果同样的字符出现了不止一次，那么需要放等量的数目到结果中。

## 解题方法

### 字典

毕竟周赛第一题，比较简单。只要明白题意之后，我们就知道了这个题可以用字典解决。

使用字典统计每个字符串中的每个字符的次数，然后对26个字符进行遍历，统计在所有字符串中这个字符出现的最少次数，把该最小次数个该字符放到结果列表中即可。

问：在统计完一个小写字符之后需要把每个字符串对应的字典中减去该最小次数吗？

答：不需要，因为我们接着就会遍历下一个字符，当前字符出现的次数不影响。

python代码如下：

```python
class Solution(object):
    def commonChars(self, A):
        """
        :type A: List[str]
        :rtype: List[str]
        """
        A_count = map(lambda x : collections.Counter(x), A)
        res = []
        for i in range(26):
            c = chr(ord('a') + i)
            min_count = min([a_count[c] for a_count in A_count])
            if min_count:
                res.extend([c] * min_count)
        return res
```

## 日期

2019 年 3 月 3 日 —— 3月开始，春天到了


  [1]: https://blog.csdn.net/fuxuemingzhu/article/details/85227593
