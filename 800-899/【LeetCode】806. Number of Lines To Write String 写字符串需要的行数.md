
作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)

题目地址：https://leetcode.com/problems/number-of-lines-to-write-string/description/

## 题目描述

We are to write the letters of a given string ``S``, from left to right into lines. Each line has maximum width 100 units, and if writing a letter would cause the width of the line to exceed 100 units, it is written on the next line. We are given an array widths, an array where widths[0] is the width of 'a', widths[1] is the width of 'b', ..., and widths[25] is the width of 'z'.

Now answer two questions: how many lines have at least one character from S, and what is the width used by the last such line? Return your answer as an integer list of length 2.

 

Example :
    
    Input: 
    widths = [10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10]
    S = "abcdefghijklmnopqrstuvwxyz"
    
    Output: [3, 60]
    
    Explanation: 
    All letters have the same length of 10. To write all 26 letters,
    we need two full lines and one line with 60 units.
    
Example :
    
    Input: 
    widths = [4,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10]
    S = "bbbcccdddaaa"
    
    Output: [2, 4]
    
    Explanation: 
    All letters except 'a' have the same length of 10, and 
    "bbbcccdddaa" will cover 9 * 10 + 2 * 4 = 98 units.
    For the last 'a', it is written on the second line because
    there is only 2 units left in the first line.
    So the answer is 2 lines, plus 4 units in the second line.
 

Note:

1. The length of S will be in the range [1, 1000].
1. S will only contain lowercase letters.
1. widths is an array of length 26.
1. widths[i] will be in the range of [2, 10].

    
## 题目大意

有张纸，每行的长度为100.然后要在上面写字符串S，26个英文字符的每个字符的宽度右widths给出。如果一行写不下了，那么就往下一行写，看最后需要多少行，并且计算最后一行用了的长度。

## 解题方法

### 使用ASIIC码求长度

我们使用遍历S的方式去做，并用last统计这行写了多少宽度了，如果宽度大于100，那么就要lines+=1，last = width了，因为要换行。

代码：

```python
class Solution(object):
    def numberOfLines(self, widths, S):
        """
        :type widths: List[int]
        :type S: str
        :rtype: List[int]
        """
        lines = 1
        last = 0
        for s in S:
            width = widths[ord(s) - ord('a')]
            last += width
            if last > 100:
                lines += 1
                last = width
        return [lines, last]
```

### 使用字典保存长度

完全可以使用字典保存每个字符的长度，这样的话就能直接查找每个字符的长度了。

```python
class Solution(object):
    def numberOfLines(self, widths, S):
        """
        :type widths: List[int]
        :type S: str
        :rtype: List[int]
        """
        lines, row = 1, 0
        lendict = {c : widths[i] for i, c in enumerate("abcdefghijklmnopqrstuvwxyz")}
        N = len(S)
        for s in S:
            if row + lendict[s] > 100:
                row = lendict[s]
                lines += 1
            else:
                row += lendict[s]
        return lines, row
```


## 日期

2018 年 4 月 3 日 —— 北京这天气，昨天穿短袖，今天穿棉袄
2018 年 11 月 6 日 —— 腰酸背痛要废了
