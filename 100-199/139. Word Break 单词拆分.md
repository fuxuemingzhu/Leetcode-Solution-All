
作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)

题目地址：https://leetcode.com/problems/unique-binary-search-trees/description/


## 题目描述


Given a non-empty string s and a dictionary ``wordDict`` containing a list of non-empty words, determine if s can be segmented into a space-separated sequence of one or more dictionary words.

Note:

- The same word in the dictionary may be reused multiple times in the segmentation.
- You may assume the dictionary does not contain duplicate words.

Example 1:

	Input: s = "leetcode", wordDict = ["leet", "code"]
	Output: true
	Explanation: Return true because "leetcode" can be segmented as "leet code".

Example 2:

	Input: s = "applepenapple", wordDict = ["apple", "pen"]
	Output: true
	Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
	             Note that you are allowed to reuse a dictionary word.

Example 3:

	Input: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
	Output: false

## 题目大意
判断一个字符串能不能由给定的字典中的字符串拼接得到。

## 解题方法

正好又学习巩固了一下DP。感觉DP套路太多了，每道题都不一样，至少LC上是这样的，很难说总结出什么规律。

按照CodeGanker的路子来：

1. 确定可以保存的信息
2. 递推式(以及如何在递推中使用保存的信息)
3. 确定起始条件

放到这个题说

S能拆成功的话，说明

s[0:k]能拆成功，然后 s[k:i]是一个在字典中的单词。

后者是一步check: s[k:i] in wordDict;
前者是需要记录的信息dp[k]表示可拆

然后从头撸一遍就行了

有的时候，一个题自己不明白，看了别人的答案还是不懂，但是看了运行的结果就行。

    "leetcode"
    [u'leet', u'code']
    [True, False, False, False, False, False, False, False, False]
    [True, False, False, False, True, False, False, False, False]
    [True, False, False, False, True, False, False, False, True]
    "leetcode"
    [u'le', u'et', u'code']
    [True, False, False, False, False, False, False, False, False]
    [True, False, True, False, False, False, False, False, False]
    [True, False, True, False, True, False, False, False, False]
    [True, False, True, False, True, False, False, False, True]
    "leetcode"
    [u'l', u'ee', u't', u'co', u'd', u'e']
    [True, False, False, False, False, False, False, False, False]
    [True, True, False, False, False, False, False, False, False]
    [True, True, True, False, False, False, False, False, False]
    [True, True, True, True, False, False, False, False, False]
    [True, True, True, True, False, False, False, False, False]
    [True, True, True, True, True, False, False, False, False]
    [True, True, True, True, True, False, True, False, False]
    [True, True, True, True, True, False, True, True, False]
    [True, True, True, True, True, False, True, True, True]

做DP的题目一定要明白定义的dp[i]到底是什么，这个题里面的dp[i]代表的是[0,i)符不符合word break。需要遍历的范围就是从0~N+1. dp[0]是空字符串，就是true.

其实这个题和[416. Partition Equal Subset Sum](https://blog.csdn.net/fuxuemingzhu/article/details/79787425#_71)很像的，都是两重循环，第一重循环判断每个位置的状态，内层循环判断这个状态能不能有前面的某个状态+一个符合题目要求的条件得到。

Python代码：

```python
class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        print(s)
        print(wordDict)
        dp = [False] * (len(s) + 1)
        dp[0] = True
        print(dp)
        for i in xrange(1, len(s) + 1):
            for k in xrange(i):
                if dp[k] and s[k:i] in wordDict:
                    dp[i] = True
                    print(dp)
        return dp.pop()
```

这个题的C++代码如下：

```cpp
class Solution {
public:
    bool wordBreak(string s, vector<string>& wordDict) {
        const int N = s.size();
        unordered_set<string> wordSet(wordDict.begin(), wordDict.end());
        // dp[i] means s[0:i) is wordBreak or not.
        vector<bool> dp(N + 1, false);
        dp[0] = true;
        // i in range [0, N)
        for (int i = 0; i <= N; ++i) {
            for (int j = 0; j < i; ++j) {
                if (dp[j] && wordSet.count(s.substr(j, i - j))) {
                    dp[i] = true;
                    break;
                }
            }
        }
        return dp.back();
    }
};
```

## 日期

2018 年 2 月 25 日 
2018 年 12 月 18 日 —— 改革开放40周年
2019 年 1 月 10 日 —— 加油
