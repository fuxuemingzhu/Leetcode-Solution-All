# 【LeetCode】792. Number of Matching Subsequences 解题报告（Python）

作者： 		负雪明烛 
id：				fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---

题目地址：https://leetcode.com/problems/number-of-matching-subsequences/description/

## 题目描述：

Given string S and a dictionary of words ``word``s, find the number of ``words[i]`` that is a subsequence of S.

Example :

    Input: 
    S = "abcde"
    words = ["a", "bb", "acd", "ace"]
    Output: 3
    Explanation: There are three words in words that are a subsequence of S: "a", "acd", "ace".

Note:

1. All words in words and S will only consists of lowercase letters.
1. The length of S will be in the range of [1, 50000].
1. The length of words will be in the range of [1, 5000].
1. The length of words[i] will be in the range of [1, 50].

## 题目大意

找出words里面有多少个S的子序列。注意，子序列可以不连续。

## 解题方法

最开始想的肯定是DP了，但是这种思路想歪了，因为不同words之间好像没有什么转移方程。。

现在又学到了一个新的判断是不是子序列的方法，使用字典保存s中字母所有索引，然后遍历word寻找索引。

对于word的每个位置的字符，同时用个prev变量保存遍历S时已经到达哪个位置了，然后从字典中寻找这个字符是否存在prev 后面出现过。很巧妙。

时间复杂度是O(S) + O(W*L*log(S))，空间复杂度是O(S).

代码如下：

```python
class Solution(object):
    def numMatchingSubseq(self, S, words):
        """
        :type S: str
        :type words: List[str]
        :rtype: int
        """
        m = dict()
        def isMatch(word, d):
            if word in m:
                return m[word]
            prev = -1
            for w in word:
                i = bisect.bisect_left(d[w], prev + 1)
                if i == len(d[w]):
                    return 0
                prev = d[w][i]
            m[word] = 1
            return 1
        
        d = collections.defaultdict(list)
        for i, s in enumerate(S):
            d[s].append(i)
        ans = [isMatch(word, d) for word in words]
        return sum(ans)
```

参考资料：

https://www.youtube.com/watch?v=l8_vcmjQA4g

## 日期

2018 年 9 月 25 日 —— 美好的一周又开始了，划重点，今天是周二
