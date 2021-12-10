
作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)


题目地址：https://leetcode.com/problems/string-without-aaa-or-bbb/


## 题目描述

Given two integers A and B, return any string S such that:

- S has length A + B and contains exactly A 'a' letters, and exactly B 'b' letters;
- The substring 'aaa' does not occur in S;
- The substring 'bbb' does not occur in S.
 

Example 1:

    Input: A = 1, B = 2
    Output: "abb"
    Explanation: "abb", "bab" and "bba" are all correct answers.

Example 2:

    Input: A = 4, B = 1
    Output: "aabaa"
     

Note:

1. 0 <= A <= 100
1. 0 <= B <= 100
1. It is guaranteed such an S exists for the given A and B.


## 题目大意

构造出来一个字符串，要求出现A个a和B个b，同时要求不能出现连续三个的a或者b.


## 解题方法

### 字符串构造

有不少人第一题就扑街了……我虽然一遍过了，但是也花了不少时间。

首先为了简化判断我做了一个设定就是A>B,如果不满足这个条件，就把A和B进行翻转，这里需要注意的是如果翻转A和B，那么需要把A和B对应的'a'和'b'也翻转。这步之后就能保证了A代表的字符是出现多的字符，B代表的是出现次数少的字符。

那么如何构造呢？我想了一个比较巧妙的方法：先构造出成对出现的'a','b'，然后把剩余的字符进行插空。

具体的说，我们保证了构造出的ab是'ab'，当A>B；ab是'ba'，当B>A.即出现次数多的字符在前面。然后我们统计一下剩余的字符还有多少个，很显然是A - B个。然后把剩余的A-B个a插入到ab中间，会构成了aabaab...abab的样子。如果还有剩余的ab对放到后面即可。

这个思路的好处在于，我们优先构造出ab对，在插空的时候不会产生连续aaa或者bbb，而且剩余的一定是abab的形式，因为题目已经保证了可以构造出来，所以不会出现A>>B导致不能构造。


```python
class Solution(object):
    def strWithout3a3b(self, A, B):
        """
        :type A: int
        :type B: int
        :rtype: str
        """
        _len = A + B
        # to make A > B
        a, b = ('a', 'b') if A > B else ('b', 'a')
        A, B = (A, B) if A > B else (B, A)
        ab = [a + b] * B
        A -= B
        res = []
        while A:
            res.append(a)
            if ab:
                res.append(ab.pop())
            A -= 1
        res += ab
        return "".join(res)
```


## 日期

2019 年 1 月 27 日 —— 这个周赛不太爽
