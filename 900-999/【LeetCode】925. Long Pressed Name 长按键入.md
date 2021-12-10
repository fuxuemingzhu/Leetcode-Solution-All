
作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)


题目地址：https://leetcode.com/contest/weekly-contest-107/problems/long-pressed-name/


## 题目描述

Your friend is typing his name into a keyboard.  Sometimes, when typing a character c, the key might get long pressed, and the character will be typed 1 or more times.

You examine the typed characters of the keyboard.  Return True if it is possible that it was your friends name, with some characters (possibly none) being long pressed.

 

Example 1:

    Input: name = "alex", typed = "aaleex"
    Output: true
    Explanation: 'a' and 'e' in 'alex' were long pressed.

Example 2:

    Input: name = "saeed", typed = "ssaaedd"
    Output: false
    Explanation: 'e' must have been pressed twice, but it wasn't in the typed output.

Example 3:

    Input: name = "leelee", typed = "lleeelee"
    Output: true

Example 4:

    Input: name = "laiden", typed = "laiden"
    Output: true
    Explanation: It's not necessary to long press any character.
 

Note:

1. name.length <= 1000
1. typed.length <= 1000
1. The characters of name and typed are lowercase letters.

## 题目大意

打字输入名字的时候有可能手一滑把某些字符重复输入了，现在想知道输入的这个字符串是否可能由真正的名字打出来。

## 解题方法

周赛第一题，随时是个easy的题目，但是还是花了半个小时。

思想是，使用两个指针，分别指向名字和输入字符串，然后判断对应位置是否能够对应的上。具体做法是统计两个字符串中相同的字符串重复出现了多少次。我用一个变量指向name，每次向后移动，在每次开始的时候需要保存这个字符，然后我们需要找一下每个字符串后面有多少个相同的字符。最后需要判断，如果输入的这个字符的个数小于名字里面有的，那么就是输入错误了。当所有的判断都结束没有返回错误，那么就是成功了。

时间复杂度是O(N)，空间复杂度是O(1).

```python
class Solution(object):
    def isLongPressedName(self, name, typed):
        """
        :type name: str
        :type typed: str
        :rtype: bool
        """
        M = len(name)
        N = len(typed)
        i, j = 0, 0
        while i < M:
            c_i = name[i]
            count_i = 0
            count_j = 0
            while i < M and name[i] == c_i:
                i += 1
                count_i += 1
            while j < N and typed[j] == c_i:
                j += 1
                count_j += 1
            if count_j < count_i:
                return False
        return True
```

## 参考资料


## 日期

2018 年 10 月 21 日 —— 这个周赛有点难


  [1]: https://blog.csdn.net/fuxuemingzhu/article/details/79534213
