- 作者：    负雪明烛
- id：      fuxuemingzhu
- 个人博客：[http://fuxuemingzhu.cn/](http://fuxuemingzhu.cn/)

---
@[TOC](目录)

题目地址：https://leetcode.com/problems/letter-case-permutation/description/


## 题目描述

Given a string S, we can transform every letter individually to be lowercase or uppercase to create another string.  Return a list of all possible strings we could create.

    Examples:
    Input: S = "a1b2"
    Output: ["a1b2", "a1B2", "A1b2", "A1B2"]
    
    Input: S = "3z4"
    Output: ["3z4", "3Z4"]
    
    Input: S = "12345"
    Output: ["12345"]

Note:

1. S will be a string with length at most 12.
1. S will consist only of letters or digits.

## 题目大意

给了一个字符串S，返回把S中的每个字母分别变成大写和小写的情况下，所有的结果组合。如果不是字母的，需要保留在原地。

## 解题方法

### 回溯法

看到这个题，仍然想到了回溯法。这个题要求数字保留，字母分成大小写两种。使用回溯法就是分类成数字和字母，字母再分为大写和小写继续。

要注意的一点是不需要使用for循环了。做39. Combination Sum题目的时候使用for循环的目的是能在任意位置起始求和得到目标。本题不需要从任意位置开始。

Python代码如下：

```python
class Solution(object):
    def letterCasePermutation(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        res = []
        self.dfs(S, 0, res, '')
        return res
    
    def dfs(self, string, index, res, path):
        if index == len(string):
            res.append(path)
            return
        else:
            if string[index].isalpha():
                self.dfs(string, index + 1, res, path + string[index].upper())
                self.dfs(string, index + 1, res, path + string[index].lower())
            else:
                self.dfs(string, index + 1, res, path + string[index])
```

二刷，重写了一下这个回溯法，可以使用字符串切片，能少了一个index变量。

Python代码如下：

```python
class Solution(object):
    def letterCasePermutation(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        res = []
        self.dfs(S, res, "")
        return res
    
    def dfs(self, S, res, word):
        if not S:
            res.append(word)
            return
        if S[0].isalpha():
            self.dfs(S[1:], res, word + S[0].upper())
            self.dfs(S[1:], res, word + S[0].lower())
        else:
            self.dfs(S[1:], res, word + S[0])
```

C++代码如下，由于C++对字符串进行切片操作不方便，所以一般都使用了起始位置的方式实现变相切片。

```cpp
class Solution {
public:
    vector<string> letterCasePermutation(string S) {
        vector<string> res;
        helper(S, res, {}, 0);
        return res;
    }
    void helper(const string S, vector<string>& res, string path, int start) {
        if (start == S.size()) {
            res.push_back(path);
            return;
        }
        if (S[start] >= '0' && S[start] <= '9') {
            helper(S, res, path + S[start], start + 1);
        } else {
            helper(S, res, path + (char)toupper(S[start]), start + 1);
            helper(S, res, path + (char)tolower(S[start]), start + 1);
        }
    }
};
```

### 循环

递归很简单，但是循环时更高效的实现方式。这个实现同样只用一个res数组，然后遍历S，每次判断这个字符是不是字母，然后哦把这个字母分为大小写，然后再次放入到结果中，更新res就好。

时间复杂度是O(N^2)，空间复杂度是O(1)。打败96%的提交。

```python
class Solution(object):
    def letterCasePermutation(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        res = [""]
        for s in S:
            if s.isalpha():
                res = [word + j for word in res for j in [s.lower(), s.upper()]]
            else:
                res = [word + s for word in res]
        return res
```

## 日期

2018 年 2 月 24 日 
2018 年 11 月 10 日 —— 这么快就到双十一了？？
2019 年 9 月 24 日 —— 梦见回到了小学，小学已经芳草萋萋破败不堪
