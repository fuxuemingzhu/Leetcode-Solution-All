
作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)

题目地址：[https://leetcode.com/problems/find-all-anagrams-in-a-string/description/][1]


## 题目描述

Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.

Strings consists of lowercase English letters only and the length of both strings s and p will not be larger than 20,100.

The order of output does not matter.

Example 1:
    
    Input:
    s: "cbaebabacd" p: "abc"
    
    Output:
    [0, 6]
    
    Explanation:
    The substring with start index = 0 is "cba", which is an anagram of "abc".
    The substring with start index = 6 is "bac", which is an anagram of "abc".

Example 2:
    
    Input:
    s: "abab" p: "ab"
    
    Output:
    [0, 1, 2]
    
    Explanation:
    The substring with start index = 0 is "ab", which is an anagram of "ab".
    The substring with start index = 1 is "ba", which is an anagram of "ab".
    The substring with start index = 2 is "ab", which is an anagram of "ab".
    
## 题目大意

在s中有多少个位置，从这个位置开始和p等长度的子字符串中，所包含的字符和p是一样的。


## 解题方法

### 滑动窗口

这个题考的是时间复杂度。如果判断两个切片是否是排列组合的话，时间复杂度略高，会超时。

能AC的做法是用了一个滑动窗口，每次进入窗口的字符的个数+1，超出滑动窗口的字符个数-1.

这样就一遍就搞定了，而且不用每个切片都算是不是一个排列组合。

Counter大法好，判断两个字符串是否是排列组合直接统计词频然后==判断即可。

注意如果一个词出现的次数是0，那么需要从Counter中移除，因为Counter({'a': 0, 'b': 1}) w不等于Counter({'b': 1})。

```python
from collections import Counter
class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        answer = []
        m, n = len(s), len(p)
        if m < n:
            return answer
        pCounter = Counter(p)
        sCounter = Counter(s[:n-1])
        index = 0
        for index in xrange(n - 1, m):
                sCounter[s[index]] += 1
                if sCounter == pCounter:
                    answer.append(index - n + 1)
                sCounter[s[index - n + 1]] -= 1
                if sCounter[s[index - n + 1]] == 0:
                    del sCounter[s[index - n + 1]]
        return answer
            
```

### 双指针

二刷的时候也是滑动窗口，但是使用的是双指针的解法，看上去好像没有上面这个方法更简单。

```python
class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        count = collections.Counter()
        M, N = len(s), len(p)
        left, right = 0, 0
        pcount = collections.Counter(p)
        res = []
        while right < M:
            count[s[right]] += 1
            if right - left + 1 == N:
                if count == pcount:
                    res.append(left)
                count[s[left]] -= 1
                if count[s[left]] == 0:
                    del count[s[left]]
                left += 1
            right += 1
        return res
```

## 日期

2018 年 1 月 27 日 
2018 年 11 月 24 日 —— 周六快乐

  [1]: https://leetcode.com/problems/find-all-anagrams-in-a-string/description/
