
作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)

题目地址：https://leetcode.com/problems/find-and-replace-pattern/description/

## 题目描述

You have a list of ``words`` and a ``pattern``, and you want to know which words in ``words`` matches the pattern.

A word matches the pattern if there exists a permutation of letters ``p`` so that after replacing every letter ``x`` in the pattern with ``p(x)``, we get the desired word.

(Recall that a permutation of letters is a bijection from letters to letters: every letter maps to another letter, and no two letters map to the same letter.)

Return a list of the words in ``words`` that match the given pattern. 

You may return the answer in any order.

 

Example 1:

    Input: words = ["abc","deq","mee","aqq","dkd","ccc"], pattern = "abb"
    Output: ["mee","aqq"]
    Explanation: "mee" matches the pattern because there is a permutation {a -> m, b -> e, ...}. 
    "ccc" does not match the pattern because {a -> c, b -> c, ...} is not a permutation,
    since a and b map to the same letter.
 

Note:

1. 1 <= words.length <= 50
1. 1 <= pattern.length = words[i].length <= 20

## 题目大意

我觉得应该把题目中的permutation理解为“映射”更为合适。

这样的话，题目意思就是找出words中所有满足映射关系的单词。映射关系由pattern给出，即要求words中的单词和pattern中的每个字符的对应关系应该完全一致。

## 解题方法

### 字典+set

既然考到映射，那么应该是使用HashMap来搞定，直接把映射一一的放入map中，如果出现过这个映射的话，就看新的对应关系和原来的映射是否相同。

代码中使用了set，这个set很重要，因为这个保证了不会出现ccc对应abb这种。

注意题目中给出了一个细节，就是words里面的每个word都和pattern长度相同，省去了判断长度的过程。

代码如下：

```python
class Solution(object):
    def findAndReplacePattern(self, words, pattern):
        """
        :type words: List[str]
        :type pattern: str
        :rtype: List[str]
        """
        ans = []
        set_p = set(pattern)
        for word in words:
            if len(set(word)) != len(set_p):
                continue
            fx = dict()
            equal = True
            for i, w in enumerate(word):
                if w in fx:
                    if fx[w] != pattern[i]:
                        equal = False
                        break
                fx[w] = pattern[i]
            if equal:
                ans.append(word)
        return ans
```

### 单字典

如果使用单字典，需要判断word向pattern的映射和pattern向word的映射。这个代码就没有什么好说的了。

Python代码如下：

```python
class Solution(object):
    def findAndReplacePattern(self, words, pattern):
        """
        :type words: List[str]
        :type pattern: str
        :rtype: List[str]
        """
        res = []
        for word in words:
            if len(word) != len(pattern): continue
            d = dict()
            isMatch = True
            for i, c in enumerate(pattern):
                if c in d:
                    if d[c] != word[i]:
                        isMatch = False
                        break
                d[c] = word[i]
            d = dict()
            for i, c in enumerate(word):
                if c in d:
                    if d[c] != pattern[i]:
                        isMatch = False
                        break
                d[c] = pattern[i]
            if isMatch:
                res.append(word)
        return res
```

C++代码如下：

```cpp
class Solution {
public:
    vector<string> findAndReplacePattern(vector<string>& words, string pattern) {
        vector<string> res;
        for (string& word : words) {
            bool isMatch = true;
            map<char, char> d;
            for (int i = 0; i < word.size(); i++) {
                if (d.count(word[i])) {
                    if (d[word[i]] != pattern[i]) {
                        isMatch = false;
                        break;
                    }
                }
                d[word[i]] = pattern[i];
            }
            d.clear();
            for (int i = 0; i < word.size(); i++) {
                if (d.count(pattern[i])) {
                    if (d[pattern[i]] != word[i]) {
                        isMatch = false;
                        break;
                    }
                }
                d[pattern[i]] = word[i];
            }
            if (isMatch) res.push_back(word);
        }
        return res;
    }
};
```


## 日期

2018 年 8 月 24 日 —— Keep fighting!
2018 年 11 月 5 日 —— 打了羽毛球，有点累
2018 年 12 月 2 日 —— 又到了周日
