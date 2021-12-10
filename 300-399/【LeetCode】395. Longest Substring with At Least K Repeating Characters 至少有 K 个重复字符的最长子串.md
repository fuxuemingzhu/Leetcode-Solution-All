作者： 		负雪明烛 
id：				fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---

题目地址: https://leetcode.com/problems/longest-substring-with-at-least-k-repeating-characters/description/

## 题目描述：

Find the length of the longest substring ``T`` of a given string (consists of lowercase letters only) such that every character in T appears no less than k times.

Example 1:

    Input:
    s = "aaabb", k = 3
    
    Output:
    3
    
    The longest substring is "aaa", as 'a' is repeated 3 times.

Example 2:

    Input:
    s = "ababbc", k = 2
    
    Output:
    5
    
    The longest substring is "ababb", as 'a' is repeated 2 times and 'b' is repeated 3 times.

## 题目大意

找出一个字符串T的最长连续子字符串，要求这个子字符串中每个字符出现的次数都最少为K，求出这个子字符串的最长长度。


## 解题方法

为什么第一个感觉总是错的……这次我的第一感觉是使用双指针，但是没有想好怎么移动后面的哪个指针，所以放弃。

看到大神的做法，还是比我思路更活跃，思路是这样的：

1. 如果字符串s的长度少于k，那么一定不存在满足题意的子字符串，返回0；
2. 如果一个字符在s中出现的次数少于k次，那么所有的包含这个字符的子字符串都不能满足题意。所以，应该去不包含这个字符的子字符串继续寻找。这就是分而治之的思路，返回不同子串的长度最大值。
3. 如果s中的每个字符出现的次数都大于k次，那么s就是我们要求的字符串。

虽然代码比较简短，但这个题的思路还是挺新颖的，

递归的时间复杂度不会计算，最坏为O(n^2)吧，空间复杂度O(1)。n为字符串长度。

代码如下：

```python
class Solution(object):
    def longestSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        if len(s) < k:
            return 0
        for c in set(s):
            if s.count(c) < k:
                return max(self.longestSubstring(t, k) for t in s.split(c))
        return len(s)
```

参考资料：

https://leetcode.com/problems/longest-substring-with-at-least-k-repeating-characters/discuss/87768/4-lines-Python

## 日期

2018 年 9 月 27 日 —— 国庆9天长假就要开始了！
