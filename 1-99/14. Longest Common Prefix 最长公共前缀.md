
- 作者：    负雪明烛
- id：      fuxuemingzhu
- 个人博客：[http://fuxuemingzhu.cn/](http://fuxuemingzhu.cn/)
- 个人公众号：负雪明烛
- 本文关键词：prefix, 公共前缀，题解，leetcode, 力扣，Python, C++, Java

---
@[TOC](目录)

题目地址：[https://leetcode.com/problems/longest-common-prefix/description/][1]


## 题目描述

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

	Input: ["flower","flow","flight"]
	Output: "fl"

Example 2:

	Input: ["dog","racecar","car"]
	Output: ""
	Explanation: There is no common prefix among the input strings.

Note:

- All given inputs are in lowercase letters a-z.

## 题目大意

找所有字符串的最长公共前缀。

## 解题方法

### 遍历前缀子串

遍历数组的第一个字符串的所有可能前缀字符串，看其他字符串的前缀是否全部一样。

用到的一个技巧是使用了all函数，判断所有的是否都满足条件。而是注意字符串切片，因为xrange是从0开始数的，而字符串切片的第二个数字是结束位置（不包含），这样必须让切片的位置加一才行。就是代码第13行。


```python
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if strs == None or len(strs) == 0:
            return ""
        def is_common(prefix, strs):
            return all(str.startswith(prefix) for str in strs)
        answer = ''
        for i in xrange(len(strs[0])):
            pre = strs[0][:i + 1]
            print pre
            if is_common(pre, strs):
                answer = pre
            else:
                break
        return answer
```

### 使用set

用set能获得去重的前缀有多少，如果只有一个的话，说明大家的前缀是相等的。

```python
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs: return ""
        pre = ""
        _len = min(len(s) for s in strs)
        for i in range(1, _len + 1):
            if len(set(s[:i] for s in strs)) == 1:
                pre = strs[0][:i]
        return pre
```

### 遍历最短字符串

又学到了一个新的找最短字符串的方法，就是min函数可以用key=len。

然后我们遍历这个最短字符串的每一位，如果所有的字符串中有个字符串的前缀不是这个字符的话，那么就返回当前的切片。如果遍历结束仍然没有提前返回的话，就返回这个最短的子串。

```python
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs: return ""
        pre = min(strs, key = len)
        for i, c in enumerate(pre):
            for word in strs:
                if word[i] != c:
                    return pre[:i]
        return pre
```

C++版本如下：

```cpp
class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        if (strs.size() == 0) return "";
        string pre = strs[0];
        for (auto word : strs){
            if (word.size() < pre.size()){
                pre = word;
            }
        }
        for (int i = 0; i < pre.size(); ++i){
            for (auto word : strs){
                if (word.at(i) != pre.at(i)){
                    return pre.substr(0, i);
                }
            }
        }
        return pre;
    }
};
```

### 排序

因为我们排序之后，相同的前缀字符串会尽量在一起，所以，我们只要判断第一个字符串和最后一个字符串的最长公共前缀就好了。

```python
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs: return ""
        strs.sort()
        size = min(len(strs[0]), len(strs[-1]))
        i = 0
        while i < size and strs[0][i] == strs[-1][i]:
            i += 1
        return strs[0][:i]
```

C++代码如下：

```cpp
class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        if (strs.empty()) return "";
        sort(strs.begin(), strs.end());
        int size = min(strs[0].size(), strs.back().size());
        int i = 0;
        while (i < size && strs[0].at(i) == strs.back().at(i)){
            ++i;
        }
        return strs[0].substr(0, i);
    }
};
```


## 日期

2017 年 8 月 25 日 
2018 年 11 月 24 日 —— 周日开始！一周就过去了～

  [1]: https://leetcode.com/problems/longest-common-prefix/description/
