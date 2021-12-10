
作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)

题目地址：[https://leetcode.com/problems/valid-palindrome-ii/description/][1]


## 题目描述

Given a non-empty string s, you may delete at most one character. Judge whether you can make it a palindrome.

Example 1:

    Input: "aba"
    Output: True
    
Example 2:
    
    Input: "abca"
    Output: True
    Explanation: You could delete the character 'c'.

Note:

- The string will only contain lowercase characters a-z. The maximum length of the string is 50000.

## 题目大意

最多删除一个字符后，判断剩余的字符串是否为回文串。

## 解题方法

### 双指针


### 思路来源
题目问我们最多删除一个字符的情况下是否可以构成**回文字符串**，第一反应是逐个删除各个字符看剩下的字符串是否为回文串，但是这个时间复杂度是 `O(N ^ 2)`，题目给出的字符串的长度最大为 50000 ，此做法会超时。

回文串的特点是左右对称。假如有两个指针从字符串的两端同时向中间走：如果遇到的元素相等，则该相等的元素是最终回文字符串的一部分；如果遇到的元素不等，则认为此时遇到了构建回文字符串的「障碍」，**应当进行处理**，处理方式见下文。

### 初版方案

当遇到不等的元素时，按照题目的意思，我们处理的方式是删除一个字符，判断 **删除一个字符后的剩余所有字符** 是否可以构成回文串。

我们观察一下题目给出的示例 2：

    输入: "abca"
    输出: True
    解释: 你可以删除c字符。

如果左右指针从两端同时向中间走，那么：

    第一步：
    a       b       c       a
    |                       |
    left                  right

    第二步：
    a       b       c       a
            |       |
            left  right

第一步，左右指针遇到的元素相等，继续向中间走；
第二步，左右指针遇到的元素不等，则必须进行处理：我们必须删除其中的一个字符，然后再判断 **剩余的所有字符** 是否是回文串。

    删除 b：
    a       c       a
    或者，  删除 c：
    a       b       a

即判断 `aca` 或者 `aba` 是否为回文字符串。

如果删除一个字符后，剩余的全部字符构成字符串 是回文字符串，那么就满足题意。

本方案的时间复杂度是：`O(N)`；由于我判断是否回文使用了 `[::-1]` 翻转形成了新字符串，所以空间复杂度是`O(N)`。如果不通过翻转的方式来判断，空间复杂度可以降到`O(1)`。

Python 代码如下。

```python
class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        isPalindrome = lambda s: s == s[::-1]
        strPart = lambda s, x: s[:x] + s[x + 1:]
        left = 0
        right = len(s) - 1
        while left < right:
            if s[left] != s[right]:
                return isPalindrome(strPart(s, left)) or isPalindrome(strPart(s, right))
            left += 1
            right -= 1
        return True

```

### 进阶方案

我们注意到「初版方案」中，在找到第一个不相等的元素后，删除了不相等的一个元素，判断**剩下的所有字符串**是不是回文字符串。这个做法和题目的意思完全一致。是否可以简化呢？

分析发现，在找到不相等的元素时，`left` 和 `right` 指针外边的元素已经判断过是回文的，因此不用再次判断。只用判断 `[left, right]` 区间中，删除 `left` 或者 `right` 指向的元素，剩余的区间 `(left, right]` 或者 `[left, right)` 是否为回文串。

若 `(left, right]` 或者 `[left, right)` 为回文串，则说明删除了一个字符可以构成回文串。

举上面的例子来说，当左右指针遇到了不等元素时，删除 `left` 或者 `right` 指向元素， 我们只用判断 `c` 或者 `b` 是否为回文串，因为这两者是回文串，所以总体的字符串 `s` 删除 `left` 或者 `right` 指向元素也可以构成回文串。

本方案的时间复杂度是：`O(N)`；由于我判断是否回文使用了 `[::-1]` 翻转形成了新字符串，所以空间复杂度是`O(N)`。如果不通过翻转的方式来判断，空间复杂度可以降到`O(1)`。

虽然时间复杂度和初版方案一样是`O(N)`，但这个方案所要检查的回文更少。

Python 代码如下。

```python
class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        isPalindrome = lambda x : x == x[::-1]
        left, right = 0, len(s) - 1
        while left <= right:
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                return isPalindrome(s[left + 1 : right + 1]) or isPalindrome(s[left: right])
        return True
```

## 日期

2018 年 2 月 4 日 
2018 年 11 月 24 日 —— 周日开始！一周就过去了～
2020 年 5 月 19 日 —— 希望工作效率更高

  [1]: https://leetcode.com/problems/valid-palindrome-ii/description/
