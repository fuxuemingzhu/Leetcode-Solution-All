
作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)

题目地址：[https://leetcode.com/problems/isomorphic-strings/#/description][1]


## 题目描述

Given two strings s and t, determine if they are isomorphic.

Two strings are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character but a character may map to itself.

    For example,
    
    Given "egg", "add", return true.
    
    Given "foo", "bar", return false.
    
    Given "paper", "title", return true.

Note:

- You may assume both s and t have the same length.

## 题目大意

看s到t的映射关系是不是一一映射的，s中不同的字符是不能映射到t的同一个字符的。

## 解题方法

### 字典保存位置

这个题可以看出来使用hashmap，但是，注意的一点是不要用位置++的方式，这样的话只统计了这个字符出现的次数，没有统计对应的位置，导致出错。比如``aba``和``baa``就会导致结果错误。因此，用到的是字符出现的位置+1的方式，保证能在hash位置处保存字符出现的位置。

```java
public class Solution {
    public boolean isIsomorphic(String s, String t) {
        int[] m1 = new int[256];
        int[] m2 = new int[256];
        int len = s.length();
        for(int i = 0; i < len; i++){
            if(m1[s.charAt(i)] != m2[t.charAt(i)]){
                return false;
            }
            m1[s.charAt(i)] = i + 1;
            m2[t.charAt(i)] = i + 1;
        }
        return true;
    }
}
```

### 字典保存映射

因为是一一映射关系，所以s到t和t到s的映射都要进行判断。最简单的方法就是使用两次判断，这样的话，我们可以分别看映射关系是不是一致的。

```python
class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        m = dict()
        for i, c in enumerate(s):
            if c in m:
                if t[i] != m[c]:
                    return False
            else:
                m[c] = t[i]
        m = dict()
        for i, c in enumerate(t):
            if c in m:
                if s[i] != m[c]:
                    return False
            else:
                m[c] = s[i]
        return True
```

既然想到了两次判断，那么我们应该也能想到，使用两个字典分别保存s到t的判断和t到s的判断。代码如下：

```python
class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        m = dict()
        n = dict()
        for i, c in enumerate(s):
            if c in m and m[c] != t[i]:
                return False
            if t[i] in n and c != n[t[i]]:
                return False
            m[c] = t[i]
            n[t[i]] = c
        return True
```

## 日期

2017 年 5 月 15 日 
2018 年 11 月 24 日 —— 周六快乐

  [1]: https://leetcode.com/problems/isomorphic-strings/#/description
