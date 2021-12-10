
作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)

题目地址：[https://leetcode.com/problems/baseball-game/description/][1]


## 题目描述

Give a string s, count the number of non-empty (contiguous) substrings that have the same number of 0's and 1's, and all the 0's and all the 1's in these substrings are grouped consecutively.

Substrings that occur multiple times are counted the number of times they occur.

    Example 1:
    Input: "00110011"
    Output: 6
    Explanation: There are 6 substrings that have equal number of consecutive 1's and 0's: "0011", "01", "1100", "10", "0011", and "01".
    
    Notice that some of these substrings repeat and are counted the number of times they occur.
    
    Also, "00110011" is not a valid substring because all the 0's (and 1's) are not grouped together.
    Example 2:
    Input: "10101"
    Output: 4
    Explanation: There are 4 substrings: "10", "01", "10", "01" that have equal number of consecutive 1's and 0's.
Note:

1. s.length will be between 1 and 50,000.
1. s will only consist of "0" or "1" characters.

## 题目大意

一个字符串由01组成，现在需要寻找满足连续子字符串中01个数相等的子字符串的个数。如果在不同位置出现的子字符串，不要去重计数。

## 解题方法

### 方法一：暴力解法（TLE）

看了s的长度那么大，估计暴力解法会超时，果然就超时了。但是做法很简单，只需要从每个位置开始向后数，数到0的个数和1的个数相等时候停止就好了。每次不需要遍历到结尾，所以最坏时间复杂度是O(N^2)，最优时间复杂度是O(N)。但是没有通过。

```python
class Solution(object):
    def countBinarySubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        N = len(s)
        res = 0
        for i in range(N):
            c1, c0 = 0, 0
            if s[i] == "1":
                c1 = 1
            else:
                c0 = 1
            for j in range(i + 1, N):
                if s[j] == "1":
                    c1 += 1
                else:
                    c0 += 1
                if c0 == c1:
                    res += 1
                    break
        return res
```


### 方法二：连续子串计算

首先，数一下，连续的0,1的个数有多少，构成一个数组。比如，``“0110001111”``的连续0和1的个数是[1, 2, 3, 4].

然后，我们想求得0和1的个数相等的子串，所以需要进行一个交错，找出相邻的两个个数的最小值就好了。比如``“0001111”``, 结果是``min(3, 4) = 3``, 即，``("01", "0011", "000111")``。

有什么道理呢？因为我们求得字符串出现的数组，它的每个位置一定是0,1交错的子字符串长度。否则相邻的0或者1会拼成更长的长度。所以我们最后求交错的最小值，就是得到了相邻字符串的0和1相等的长度。

根据上面的思路，可以写出这个代码：

```python
class Solution(object):
    def countBinarySubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        N = len(s)
        curlen = 1
        res = []
        for i in range(1, N):
            if s[i] == s[i - 1]:
                curlen += 1
            else:
                res.append(curlen)
                curlen = 1
        res.append(curlen)
        return sum(min(x, y) for x, y in zip(res[:-1], res[1:]))
```

上面的代码可以写的更简洁：

```python
class Solution(object):
    def countBinarySubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = map(len, s.replace('01','0 1').replace('10','1 0').split())
        return sum(min(i, j) for i,j in zip(s, s[1:]))
```

## 日期

2018 年 1 月 27 日 
2018 年 11 月 10 日 —— 欢度光棍节

  [1]: https://leetcode.com/problems/count-binary-substrings/description/
