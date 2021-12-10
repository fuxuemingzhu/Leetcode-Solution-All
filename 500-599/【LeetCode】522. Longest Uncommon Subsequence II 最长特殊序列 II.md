# 【LeetCode】522. Longest Uncommon Subsequence II 解题报告（Python）

标签（空格分隔）： LeetCode

作者： 		负雪明烛 
id：				fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---

题目地址：https://leetcode.com/problems/longest-uncommon-subsequence-ii/description/

## 题目描述：

Given a list of strings, you need to find the longest uncommon subsequence among them. The longest uncommon subsequence is defined as the longest subsequence of one of these strings and this subsequence should not be any subsequence of the other strings.

A subsequence is a sequence that can be derived from one sequence by deleting some characters without changing the order of the remaining elements. Trivially, any string is a subsequence of itself and an empty string is a subsequence of any string.

The input will be a list of strings, and the output needs to be the length of the longest uncommon subsequence. If the longest uncommon subsequence doesn't exist, return -1.

Example 1:

    Input: "aba", "cdc", "eae"
    Output: 3

Note:

1. All the given strings' lengths will not exceed 10.
1. The length of the given list will be in the range of [2, 50].


## 题目大意

找出最长非公共子序列。公共子序列的定义是一个字符串可由另一个字符串删除某些字符得到。如果在一组字符串中，某一个字符串不是任何另外的字符串的公共子序列，那么这就是它是全组的非公共子序列。找出最长的长度。


## 解题方法

做题多了，没想到暴力解法就能过了。

写出公共子序列的判断函数。主要是两个位置pos和i,如果能找到子字符串中的某个位置，那么就把全字符串的位置后移。

寻找最长非公共子序列的时候直接两重for循环即可，不要想太复杂。


代码如下：

```python
class Solution(object):
    def findLUSlength(self, strs):
        """
        :type strs: List[str]
        :rtype: int
        """
        longest = -1
        _len = len(strs)
        for i in range(_len):
            issub = False
            for j in range(_len):
                if i == j:
                    continue
                if self.checkSubString(strs[i], strs[j]):
                    issub = True
                    break
            if not issub:
                longest = max(longest, len(strs[i]))
        return longest
        
    def checkSubString(self, substr, string):
        if len(substr) > len(string): return False
        if substr == string: return True
        if not substr: return True
        pos = 0
        for i in range(len(string)):
            if pos == len(substr):
                break
            if substr[pos] == string[i]:
                pos += 1
        return pos == len(substr)
```

参考资料：

1. http://www.cnblogs.com/grandyang/p/6680548.html
1. https://blog.csdn.net/zsensei/article/details/75227927

## 日期

2018 年 8 月 27 日 ———— 就要开学了！


  [1]: https://s3-lc-upload.s3.amazonaws.com/uploads/2018/08/22/fivetrees.png
  [2]: https://blog.csdn.net/fuxuemingzhu/article/details/81748335
  [3]: http://ww2.sinaimg.cn/bmiddle/006x6MW7jw1fawdiy39nqj305i05iaa2.jpg