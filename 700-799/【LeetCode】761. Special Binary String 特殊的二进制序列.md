作者： 		负雪明烛 
id：				fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---

题目地址: https://leetcode.com/problems/special-binary-string/description/

## 题目描述：

Special binary strings are binary strings with the following two properties:

- The number of 0's is equal to the number of 1's.
- Every prefix of the binary string has at least as many 1's as 0's.

Given a special string S, a move consists of choosing two consecutive, non-empty, special substrings of S, and swapping them. (Two strings are consecutive if the last character of the first string is exactly one index before the first character of the second string.)

At the end of any number of moves, what is the lexicographically largest resulting string possible?

Example 1:

    Input: S = "11011000"
    Output: "11100100"
    Explanation:
    The strings "10" [occuring at S[1]] and "1100" [at S[3]] are swapped.
    This is the lexicographically largest string possible after some number of swaps.

Note:

1. S has length at most 50.
1. S is guaranteed to be a special binary string as defined above.

## 题目大意

一个特殊的二进制字符串满足以下两个属性：

1. 字符串中0的个数等于1的个数
2. 这个字符串中任何前缀中1的个数不少于0的个数

给了一个满足要求的特殊字符串，每次移动可以选择两个两个连续的非空的特殊二进制子串进行交换。求在一系列移动之后，能得到的字母顺序的字符串最大结果。


## 解题方法

这道题的原型是括号匹配问题。求括号匹配的经典的方法是使用cnt记数的方法，如果是左括号，那么cnt+1，如果是右括号，那么cnt-1，如果cnt等于0了，说明这已经是个匹配了的括号了。注意，一个括号匹配问题中可能存在多个匹配的括号，这个题也是，比如``1010``就是满足题意的二进制字符串，相等于两个满足题意的二进制串组成。

如果要想在一系列移动之后，得到最大的字符串，那么可以看出要求1尽量在前面，同时0尽量在后面。我们使用list保存那些符合要求的字符串，最后排序即可。一个符合要求的字符串其开头必须是1，末尾必须是0。同时我们意识到，符合要求的字符串的内部也要进行排序。比如子串``1010``，要给他排序成``1100``这个样子，注意中间的字符串``01``并不符合题目要求，给他重新排成``10``样式，使用递归结构。使用i保存上一次判断完成的字符串的结尾，用j遍历字符串。每次判断结束一个符合要求的子串之后，要令 i = j + 1。

最坏情况下的时间复杂度是O(N!),最优情况下的时间复杂度是O(1)，空间复杂度是O(N)。

```python
class Solution(object):
    def makeLargestSpecial(self, S):
        """
        :type S: str
        :rtype: str
        """
        cnt = 0
        res = list()
        i= 0
        for j, v in enumerate(S):
            cnt += 1 if v == "1" else -1
            if cnt == 0:
                res.append("1" + self.makeLargestSpecial(S[i + 1:j]) + "0")
                i = j + 1
        return "".join(sorted(res, reverse=True))
```

参考资料：

http://www.cnblogs.com/grandyang/p/8606024.html
https://blog.csdn.net/u014688145/article/details/78996824
https://blog.csdn.net/BambooYH/article/details/80686074
http://www.cnblogs.com/zzuli2sjy/p/8260854.html

## 日期

2018 年 10 月 2 日 —— 小蓝单车莫名其妙收了我1块钱，明明每个月免费骑10次的啊！


  [1]: https://blog.csdn.net/fuxuemingzhu/article/details/82917037
