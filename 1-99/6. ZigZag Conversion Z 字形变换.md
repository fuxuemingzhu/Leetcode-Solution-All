
作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/
公众号：负雪明烛
本文关键词：字形变换，ZigZag，题解，Leetcode, 力扣，Python, C++, Java

---

@[TOC](目录)


题目地址：https://leetcode.com/problems/zigzag-conversion/description/

## 题目描述

The string ``"PAYPALISHIRING"`` is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

    P   A   H   N
    A P L S I I G
    Y   I   R

And then read line by line: ``"PAHNAPLSIIGYIR"``

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);
Example 1:

    Input: s = "PAYPALISHIRING", numRows = 3
    Output: "PAHNAPLSIIGYIR"

Example 2:
    
    Input: s = "PAYPALISHIRING", numRows = 4
    Output: "PINALSIGYAHRPI"

Explanation:

    P     I    N
    A   L S  I G
    Y A   H R
    P     I

## 题目大意

把一个字符串按照锯齿型的方式去排列，然后按照``行``进行拼接到一起。输出这样得到的结果。

## 解题方法

### 公式


明眼人一看就知道，这个肯定是有公式的。我自己推导的公式和[JustDoIT][1]的一样：

1. 第一行和最后一行下标间隔都是 `interval = n*2-2 = 8`;
2. 中间行的间隔是周期性的,第 `i` 行的间隔是: `interval–2*i` ,  `2*i`,  `interval–2*i` , `2*i`, `interval–2*i`, `2*i`, …

 Python 代码如下：

```python3
class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1: return s
        ans = ""
        interval = 2 * (numRows - 1)
        for i in range(0, len(s), interval):
            ans += s[i]
        for row in range(1, numRows - 1):
            inter = 2 * row
            i = row
            while i < len(s):
                ans += s[i]
                inter = interval - inter
                i += inter
        print(ans)
        for i in range(numRows - 1, len(s), interval):
            ans += s[i]
        return ans
```

## 日期

2018 年 6 月 27 日 ———— 阳光明媚，心情大好，抓紧科研啊


  [1]: https://www.cnblogs.com/TenosDoIt/p/3738693.html
