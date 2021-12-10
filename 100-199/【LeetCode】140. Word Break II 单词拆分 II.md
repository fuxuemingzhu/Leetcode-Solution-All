
作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)


题目地址：https://leetcode.com/problems/word-break-ii/


## 题目描述


Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, add spaces in s to construct a sentence where each word is a valid dictionary word. Return all such possible sentences.

Note:

The same word in the dictionary may be reused multiple times in the segmentation.
You may assume the dictionary does not contain duplicate words.
Example 1:

    Input:
    s = "catsanddog"
    wordDict = ["cat", "cats", "and", "sand", "dog"]
    Output:
    [
      "cats and dog",
      "cat sand dog"
    ]

Example 2:

    Input:
    s = "pineapplepenapple"
    wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]
    Output:
    [
      "pine apple pen apple",
      "pineapple pen apple",
      "pine applepen apple"
    ]
    Explanation: Note that you are allowed to reuse a dictionary word.

Example 3:

    Input:
    s = "catsandog"
    wordDict = ["cats", "dog", "sand", "and", "cat"]
    Output:
    []


## 题目大意

给了一个字典，问给定的字符串s能有多少种被字典构造出来的方式，返回每一种构造方式。

## 解题方法

### 递归求解

这个题就是[139. Word Break][1]的变形，现在要求所有的构造方式了。

一般这种题就需要使用递归，把所有的构造方式都求出来。这个题必须使用字典保存已经能切分的方式，否则，递归的时间复杂度太高。我们定义函数dfs，其含义是字符串s能被字典中的元素构成的所有构造方式字符串（中间由空格分割）。所以，我们只需要知道如果当前的字符串能分割，再拼接上后面的分割就行了。如果后面部分不能分割，应该返回的是空的vector，这样就不会产生新的结果字符串放入到res里。

Python代码如下：

```python
class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        res = []
        memo = dict()
        return self.dfs(s, res, wordDict, memo)
    
    def dfs(self, s, res, wordDict, memo):
        if s in memo: return memo[s]
        if not s:
            return [""]
        res = []
        for word in wordDict:
            if s[:len(word)] != word: continue
            for r in self.dfs(s[len(word):], res, wordDict, memo):
                res.append(word + ("" if not r else " " + r))
        memo[s] = res
        return res
```

C++代码如下：

```cpp
class Solution {
public:
    vector<string> wordBreak(string s, vector<string>& wordDict) {
        set<string> wordset(wordDict.begin(), wordDict.end());
        unordered_map<string, vector<string>> m;
        return dfs(wordset, s, m);
    }
private:
    vector<string> dfs(set<string>& wordset, string s, unordered_map<string, vector<string>>& m) {
        if (m.count(s)) return m[s];
        if (s.empty())  return {""};
        vector<string> res;
        for (string word : wordset) {
            if (s.substr(0, word.size()) != word) continue;
            vector<string> remain = dfs(wordset, s.substr(word.size()), m);
            for (string r : remain) {
                res.push_back(word + (r.empty() ? "" : " ") + r);
            }
        }
        return m[s] = res;
    }
};
```

也可以不用一个新的函数，直接在原始的函数上进行操作。这时候就需要一个全局的字典。代码如下：

```cpp
class Solution {
public:
    vector<string> wordBreak(string s, vector<string>& wordDict) {
        if (m.count(s)) return m[s];
        if (s.empty())  return {""};
        vector<string> res;
        for (string word : wordDict) {
            if (s.substr(0, word.size()) != word) continue;
            for (string r : wordBreak(s.substr(word.size()), wordDict)) {
                res.push_back(word + (r.empty() ? "" : " ") + r);
            }
        }
        return m[s] = res;
    }
private:
    unordered_map<string, vector<string>> m;
};
```

参考资料：http://www.cnblogs.com/grandyang/p/4576240.html


## 日期

2018 年 12 月 19 日 —— 感冒了，好难受


  [1]: https://blog.csdn.net/fuxuemingzhu/article/details/79368360
