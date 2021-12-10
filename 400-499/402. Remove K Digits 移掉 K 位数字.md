# 【LeetCode】402. Remove K Digits 解题报告（Python）

标签（空格分隔）： LeetCode

作者： 		负雪明烛 
id：				fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---

题目地址：https://leetcode.com/problems/remove-k-digits/description/

## 题目描述：

Given a non-negative integer num represented as a string, remove k digits from the number so that the new number is the smallest possible.

Note:

- The length of num is less than 10002 and will be ≥ k.
- The given num does not contain any leading zero.

Example 1:

    Input: num = "1432219", k = 3
    Output: "1219"
    Explanation: Remove the three digits 4, 3, and 2 to form the new number 1219 which is the smallest.

Example 2:

    Input: num = "10200", k = 1
    Output: "200"
    Explanation: Remove the leading 1 and the number is 200. Note that the output must not contain leading zeroes.

Example 3:

    Input: num = "10", k = 2
    Output: "0"
    Explanation: Remove all the digits from the number and it is left with nothing which is 0.



## 题目大意

从一个数字字符串中删除k个数字，使得剩下来的数字字符串是最小的。

## 解题方法

看了Topics知道这个是用栈来解决的题目。看了别人的解答才明白怎么回事。

使用一个栈作为辅助，遍历数字字符串，当当前的字符比栈最后的字符小的时候，说明要把栈的最后的这个字符删除掉。为什么呢？你想，把栈最后的字符删除掉，然后用现在的字符进行替换，是不是数字比以前的那种情况更小了？所以同样的道理，做一个while循环！这个很重要，可是我没有想到。在每一个数字处理的时候，都要做一个循环，使得栈里面最后的数字比当前数字大的都弹出去。

最后，如果K还没用完，那要删除哪里的字符呢？毋庸置疑肯定是最后的字符，因为前面的字符都是小字符。

很有意思的一个题目！

代码如下：

```python
class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        if len(num) == k:
            return '0'
        stack = []
        for n in num:
            while stack and k and int(stack[-1]) > int(n):
                stack.pop()
                k -= 1
            stack.append(n)
        while k:
            stack.pop()
            k -= 1
        if not stack:
            return '0'
        return str(int("".join(stack)))
```

## 日期

2018 年 7 月 13 日 ———— 早起困一上午，中午必须好好休息才行啊


  [1]: https://blog.csdn.net/fuxuemingzhu/article/details/81027989