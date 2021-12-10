
作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)


题目地址：https://leetcode.com/problems/distinct-subsequences-ii/description/


## 题目描述

Given a string ``S``, count the number of distinct, non-empty subsequences of ``S`` .

Since the result may be large, return the answer modulo ``10^9 + 7``.
 

Example 1:

    Input: "abc"
    Output: 7
    Explanation: The 7 distinct subsequences are "a", "b", "c", "ab", "ac", "bc", and "abc".

Example 2:

    Input: "aba"
    Output: 6
    Explanation: The 6 distinct subsequences are "a", "b", "ab", "ba", "aa" and "aba".

Example 3:

    Input: "aaa"
    Output: 3
    Explanation: The 3 distinct subsequences are "a", "aa" and "aaa".
 
Note:

1. S contains only lowercase letters.
1. 1 <= S.length <= 2000


## 题目大意

计算一个字符串中，有多少种不同的子序列。

## 解题方法

### 动态规划

周赛的第四题，不会做，还是因为我的动态规划太弱了。。

瞻仰一下寒神的做法吧，膜拜！[\[C++/Java/Python\] 4 lines O(N) Time, O(1) Space][1]。

使用一个endswith[26]数组，保存的是有多少个子序列以i结尾。则，当前总共有``N = sum(endswith)``个不同的子序列，当我们新增加一个字符c时，相当于在以前每个结尾的位置后面又增添了一个新的字符，所以现在有了N个以c结尾的不同的子序列了。

所以，我们遍历一遍s，更新的方式是``end[c] = sum(end) + 1``。加一是因为c本身也是一个子序列。

比如举个例子。

    Input: "aba"
    Current parsed: "ab"
    
    endswith 'a': ["a"]
    endswith 'b': ["ab","b"]
    
    "a" -> "aa"
    "ab" -> "aba"
    "b" -> "ba"
    "" -> "a"
    
    endswith 'a': ["aa","aba","ba","a"]
    endswith 'b': ["ab","b"]
    result: 6


时间复杂度是O(26N)，空间复杂度是O(1)。

```python
class Solution(object):
    def distinctSubseqII(self, S):
        """
        :type S: str
        :rtype: int
        """
        nums = [0] * 26
        for s in S:
            nums[ord(s) - ord("a")] = (sum(nums) + 1) % (10 ** 9 + 7)
        return sum(nums) % (10 ** 9 + 7)
```

## 日期

2018 年 11 月 11 日 —— 剁手节快乐

  [1]: https://leetcode.com/problems/distinct-subsequences-ii/discuss/192017/C++JavaPython-4-lines-O%28N%29-Time-O%281%29-Space
