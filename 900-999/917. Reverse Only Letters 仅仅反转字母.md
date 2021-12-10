
作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)

题目地址: https://leetcode.com/contest/weekly-contest-105/problems/reverse-only-letters/

## 题目描述

Given a string ``S``, return the "reversed" string where all characters that are not a letter stay in the same place, and all letters reverse their positions.


Example 1:

    Input: "ab-cd"
    Output: "dc-ba"

Example 2:

    Input: "a-bC-dEf-ghIj"
    Output: "j-Ih-gfE-dCba"

Example 3:

    Input: "Test1ng-Leet=code-Q!"
    Output: "Qedo1ct-eeLg=ntse-T!"
 

Note:

1. S.length <= 100
1. 33 <= S[i].ASCIIcode <= 122 
1. S doesn't contain \ or "

## 题目大意

对字符串进行逆序排序，要求只把字母的顺序翻转，而其他字符原地不动。

## 解题方法

### 栈

周赛第一题，做法很简单了，先把所有的字母保存下来，然后再次对字符串进行遍历，如果源字符串的某个位置是字母，那么把字母列表中最后一个元素换过来，否则就还是原来的字符。

时间复杂度是O(N)，空间复杂度是O(N)。

```python
class Solution(object):
    def reverseOnlyLetters(self, S):
        """
        :type S: str
        :rtype: str
        """
        letters = []
        N = len(S)
        for i, s in enumerate(S):
            if s.isalpha():
                letters.append(s)
        res = ""
        for i, s in enumerate(S):
            if s.isalpha():
                res += letters.pop()
            else:
                res += s
        return res
```

### 单指针

也可以不用把所有的字符保存下来，直接使用一个指针从后向前扫描，可以把空间复杂度降到O(1)。

时间复杂度是O(N)，空间复杂度是O(1)。

```python
class Solution(object):
    def reverseOnlyLetters(self, S):
        """
        :type S: str
        :rtype: str
        """
        N = len(S)
        l = N - 1
        res = ""
        for i, s in enumerate(S):
            if s.isalpha():
                while not S[l].isalpha():
                    l -= 1
                res += S[l]
                l -= 1
            else:
                res += s
        return res
```



### 双指针

双指针版本，使用两个指针分别前面和后面的两个字母位置。然后将两个字母翻转，其他的位置不用动。这个做法比较难点，里面的两个while循环都需要加上边界判断，里面的if还需要边界判断以及left和right的判断。

时间复杂度是O(N)，空间复杂度是O(1)。打败100%的提交。

```python
class Solution(object):
    def reverseOnlyLetters(self, S):
        """
        :type S: str
        :rtype: str
        """
        N = len(S)
        left, right = 0, N - 1
        slist = list(S)
        while left < right:
            while left < N and (not S[left].isalpha()):
                left += 1
            while right >= 0 and (not S[right].isalpha()):
                right -= 1
            if left < N and right >= 0 and left < right:
                slist[left], slist[right] = slist[right], slist[left]
            left, right = left + 1, right - 1
        return "".join(slist)
```

参考资料：


## 日期

2018 年 10 月 7 日 —— 假期最后一天！！
