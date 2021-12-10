
作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)

题目地址：[https://leetcode.com/problems/find-smallest-letter-greater-than-target/description/][1]


## 题目描述

Given a list of sorted characters letters containing only lowercase letters, and given a target letter target, find the smallest element in the list that is larger than the given target.

Letters also wrap around. For example, if the target is target = `'z'` and `letters = ['a', 'b']`, the answer is `'a'`.

Examples:

    Input:
    letters = ["c", "f", "j"]
    target = "a"
    Output: "c"
    
    Input:
    letters = ["c", "f", "j"]
    target = "c"
    Output: "f"
    
    Input:
    letters = ["c", "f", "j"]
    target = "d"
    Output: "f"
    
    Input:
    letters = ["c", "f", "j"]
    target = "g"
    Output: "j"
    
    Input:
    letters = ["c", "f", "j"]
    target = "j"
    Output: "c"
    
    Input:
    letters = ["c", "f", "j"]
    target = "k"
    Output: "c"
Note:

1. letters has a length in range [2, 10000].
1. letters consists of lowercase letters, and contains at least 2 unique letters.
1. target is a lowercase letter.

## 题目大意

给出了一个排序的字符数组，找出第一个比target大的字符。注意是数组是循环的。

## 解题方法

### 线性扫描

找到第一个比指定字符大的。如果没找到的话，列表是可以循环的。也就是说如果没找到就返回列表第一个字符。

```python
class Solution(object):
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        for letter in letters:
        ## 提交了之后发现不用使用ord，字符可以用'>''<'比较大小
            if ord(letter) > ord(target):
                return letter
        return letters[0]
```

### 二分查找

因为是有序的，所以直接二分即可。

```python
class Solution(object):
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        index = bisect.bisect_right(letters, target)
        return letters[index % len(letters)]
```

## 日期

2018 年 1 月 23 日 
2018 年 11 月 19 日 —— 周一又开始了


  [1]: https://leetcode.com/problems/find-smallest-letter-greater-than-target/description/
