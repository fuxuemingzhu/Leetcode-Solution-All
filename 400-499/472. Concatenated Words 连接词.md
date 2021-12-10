

作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)


题目地址：https://leetcode.com/problems/concatenated-words/


## 题目描述


Given a list of words (**without duplicates**), please write a program that returns all concatenated words in the given list of words.
A concatenated word is defined as a string that is comprised entirely of at least two shorter words in the given array.

Example:

    Input: ["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]
    
    Output: ["catsdogcats","dogcatsdog","ratcatdogcat"]

    Explanation: "catsdogcats" can be concatenated by "cats", "dog" and "cats"; 
     "dogcatsdog" can be concatenated by "dog", "cats" and "dog"; 
    "ratcatdogcat" can be concatenated by "rat", "cat", "dog" and "cat".

Note:

1. The number of elements of the given array will not exceed 10,000
1. The length sum of elements in the given array will not exceed 600,000.
1. All the input string will only include lower case letters.
1. The returned elements order does not matter.



## 题目大意

如果有个字符串能够由其他的至少两个字符串拼接构成，那么这个字符串符合要求。问总的有哪些字符串符合要求。

## 解题方法

### 动态规划

这个题的解题方法就是[139. Word Break][1]，如果不把139搞懂的话，这个题是做不出来的。

方法就是对每个字符串进行一次DP，判断这个字符串是不是能用其他的字符串拼接而成。为了加快判断的速度，使用的是字典保存的字符串。


代码如下：

```cpp
class Solution {
public:
    vector<string> findAllConcatenatedWordsInADict(vector<string>& words) {
        if (words.size() <= 2) return {};
        unordered_set<string> wordset(words.begin(), words.end());
        vector<string> res;
        for (string word : words) {
            wordset.erase(word);
            const int N = word.size();
            if (N == 0) continue;
            vector<bool> dp(N + 1, false);
            dp[0] = true;
            for (int i = 0; i <= N; ++i) {
                for (int j = 0; j < i; ++j) {
                    if (dp[j] && wordset.count(word.substr(j, i - j))) {
                        dp[i] = true;
                        break;
                    }
                }
            }
            if (dp.back())
                res.push_back(word);
            wordset.insert(word);
        }
        return res;
    }
};
```

参考资料：http://www.cnblogs.com/grandyang/p/6254527.html


## 日期

2018 年 12 月 18 日 —— 改革开放40周年


  [1]: https://blog.csdn.net/fuxuemingzhu/article/details/79368360
