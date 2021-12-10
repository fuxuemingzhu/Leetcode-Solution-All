
作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)

题目地址：[https://leetcode.com/problems/string-compression/description/][1]


## 题目描述

Given an array of characters, compress it in-place.

The length after compression must always be smaller than or equal to the original array.

Every element of the array should be a character (not int) of length 1.

After you are done modifying the input array in-place, return the new length of the array.


Follow up:
Could you solve it using only O(1) extra space?


Example 1:

    Input:
    ["a","a","b","b","c","c","c"]

    Output:
    Return 6, and the first 6 characters of the input array should be: ["a","2","b","2","c","3"]

    Explanation:
    "aa" is replaced by "a2". "bb" is replaced by "b2". "ccc" is replaced by "c3".

Example 2:

    Input:
    ["a"]
    
    Output:
    Return 1, and the first 1 characters of the input array should be: ["a"]
    
    Explanation:
    Nothing is replaced.

Example 3:

    Input:
    ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
    
    Output:
    Return 4, and the first 4 characters of the input array should be: ["a","b","1","2"].
    
    Explanation:
    Since the character "a" does not repeat, it is not compressed. "bbbbbbbbbbbb" is replaced by "b12".
    Notice each digit has it's own entry in the array.
Note:
1. All characters have an ASCII value in [35, 126].
1. 1 <= len(chars) <= 1000.

## 题目大意

统计每个字符出现的次数，然后放到原地，需要按照顺序放。完成了字符串的压缩。

## 解题方法

### 使用额外空间

自己的方法比较简单粗暴，用了额外的空间来保存了所有的数字出现的次数，最后再放回到chars上。

```python
class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        marks = ""
        length = -1
        cur = chars[0]
        for i, value in enumerate(chars):
            length += 1
            if value != cur:
                count = str(length) if length != 1 else ''
                marks += cur + count
                cur = value
                length = 0
            if i == len(chars) - 1:
                length += 1
                count = str(length) if length != 1 else ''
                marks += cur + count
                cur = value
                length = 0
        print marks
        for i, mark in enumerate(marks):
            chars[i] = mark
        return len(marks)
```

### 不使用额外空间

保存一个pos位置，告诉我们当前需要放在哪个地方。然后我们统计连续的字符出现了多少次，如果大于1次才往后拼接上去。

```python
class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        pre = chars[0]
        count = 0
        pos = 0
        for ch in chars:
            if pre == ch:
                count += 1
            else:
                chars[pos] = pre
                pos += 1
                if count > 1:
                    count = str(count)
                    for i in range(len(count)):
                        chars[pos] = count[i]
                        pos += 1
                count = 1
                pre = ch
        chars[pos] = pre
        pos += 1
        if count > 1:
            count = str(count)
            for i in range(len(count)):
                chars[pos] = count[i]
                pos += 1
        return pos
```

## 日期

2018 年 1 月 27 日 
2018 年 11 月 24 日 —— 周六快乐

  [1]: https://leetcode.com/problems/string-compression/description/
