# 【LeetCode】880. Decoded String at Index 解题报告（Python）

标签（空格分隔）： LeetCode

作者： 		负雪明烛 
id：				fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---

题目地址：https://leetcode.com/problems/decoded-string-at-index/description/

## 题目描述：

An encoded string S is given.  To find and write the decoded string to a tape, the encoded string is read **one character at a time** and the following steps are taken:

If the character read is a letter, that letter is written onto the tape.
If the character read is a digit (say d), the entire current tape is repeatedly written d-1 more times in total.
Now for some encoded string S, and an index K, find and return the K-th letter (1 indexed) in the decoded string.

Example 1:

    Input: S = "leet2code3", K = 10
    Output: "o"
    Explanation: 
    The decoded string is "leetleetcodeleetleetcodeleetleetcode".
    The 10th letter in the string is "o".

Example 2:

    Input: S = "ha22", K = 5
    Output: "h"
    Explanation: 
    The decoded string is "hahahaha".  The 5th letter is "h".

Example 3:

    Input: S = "a2345678999999999999999", K = 1
    Output: "a"
    Explanation: 
    The decoded string is "a" repeated 8301530446056247680 times.  The 1st letter is "a".

Note:

1. 2 <= S.length <= 100
1. S will only contain lowercase letters and digits 2 through 9.
1. S starts with a letter.
1. 1 <= K <= 10^9
1. The decoded string is guaranteed to have less than 2^63 letters.

## 题目大意

从左到右是一个编码了的字符串，如果某个位置是字符，那么拼接到前面的字符串上去；如果某个位置是数字，那么将左边所有的字符串*这个数字的倍数，变成新的字符串。

## 解题方法

如果模拟题目中的操作进行解码，空间占用过大，一定会通不过。而且，题目只要求了求指定位置的字符，并没有要求所有的字符，所以全部解码没有必要。

参考了官方的解答。思路如下：

比如，对于一个解码了的字符串，``appleappleappleappleappleapple ``，并且要求的索引K=24的话，那么结果和K=4是一样的。因为单词``apple``的size=5，重复了6次。所以第K个索引和第K%size个索引是一样的。

所以我们使用反向的计算，保持追踪解码字符串的size，如果解码字符串等于一个``word``重复了``d``次的时候，我们可以把``K``变化为``K % (word.length)``.

算法：

首先，找出解码字符串的长度。然后，我们反向查找，保持追踪size，也就是对编码字符串``S[0], S[1], ..., S[i]``解码后的长度。

如果找到的是一个数字``S[i]``，那么意味着解码字符串``S[0], S[1], ..., S[i-1]``的长度应该是``size / Integer(S[i])``；否则应该是``size-1``.

代码如下：

```python3
class Solution(object):
    def decodeAtIndex(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        size = 0
        for c in S:
            if c.isdigit():
                size *= int(c)
            else:
                size += 1
        
        for c in reversed(S):
            K %= size
            if K == 0 and c.isalpha():
                return c
            if c.isdigit():
                size /= int(c)
            else:
                size -= 1
```

参考资料：https://leetcode.com/problems/decoded-string-at-index/solution/

## 日期

2018 年 8 月 23 日 ———— 疲惫说明在逆流而上