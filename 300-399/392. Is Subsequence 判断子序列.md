# 【LeetCode】392. Is Subsequence 解题报告（Python）

标签： LeetCode

---

题目地址：https://leetcode.com/problems/is-subsequence/description/

## 题目描述：

Given a string s and a string t, check if s is subsequence of t.

You may assume that there is only lower case English letters in both s and t. t is potentially a very long (length ~= 500,000) string, and s is a short string (<=100).

A subsequence of a string is a new string which is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (ie, "ace" is a subsequence of "abcde" while "aec" is not).

    Example 1:
    s = "abc", t = "ahbgdc"
    
    Return true.
    
    Example 2:
    s = "axc", t = "ahbgdc"
    
    Return false.

Follow up:

If there are lots of incoming S, say S1, S2, ... , Sk where k >= 1B, and you want to check one by one to see if T has its subsequence. In this scenario, how would you change your code?



## 题目大意

有两个字符串s和t，其中s是短字符串，t是长字符串。判断s是不是t的子字符串。注意，这里应该是保留相对顺序的子字符串，也就是在s中出现的两个字符a,b应该在s中t中的相对次序相同。

## 解题方法

其实这个题就考了一个相对顺序。s比较短，而t很长，那么尽量就对t进行一次遍历最好。可以使用一个队列保留s的每个元素，这样对t进行遍历，如果遍历到的元素和队列的头元素相等，那么队列出头元素。这样最后返回队列是否为空即可。

```python
class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        queue = collections.deque(s)
        for c in t:
            if not queue: return True
            if c == queue[0]:
                queue.popleft()
        return not queue
```

如果不使用队列的话，可以使用两个指针，一个作为s的索引，一个作为t的索引。如果在t中找到了s的元素，把s的指针右移，否则把t的指针右移。

这个竟然比上面的更慢？？不懂为什么。

```python
class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        si, ti = 0, 0
        while si < len(s) and ti < len(t):
            if t[ti] == s[si]:
                si += 1
            ti += 1
        return si == len(s)
```

方法二：

二分查找，留给二刷。


## 日期

2018 年 3 月 15 日 --雾霾消散，春光明媚