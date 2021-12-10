作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)


题目地址：https://leetcode.com/problems/max-points-on-a-line/description/


## 题目描述

You have an array of ``logs``.  Each log is a space delimited string of words.

For each log, the first word in each log is an alphanumeric identifier.  Then, either:

- Each word after the identifier will consist only of lowercase letters, or;
- Each word after the identifier will consist only of digits.

We will call these two varieties of logs letter-logs and digit-logs.  It is guaranteed that each log has at least one word after its identifier.

Reorder the logs so that all of the letter-logs come before any digit-log.  The letter-logs are ordered lexicographically ignoring identifier, with the identifier used in case of ties.  The digit-logs should be put in their original order.

Return the final order of the logs.

 

Example 1:

    Input: ["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo"]
    Output: ["g1 act car","a8 act zoo","ab1 off key dog","a1 9 2 3 1","zo4 4 7"]
 

Note:

1. ``0 <= logs.length <= 100``
1. ``3 <= logs[i].length <= 100``
1. ``logs[i]`` is guaranteed to have an identifier, and a word after the identifier.

## 题目大意

Log的格式是第一个单词是Log的索引，后面的都是Log的内容。有两种Log，一种内容是纯数字的，一种内容是纯英文字符的。现在要求，把所有的英文Log放到数字Log前面。而且如果是纯英文的字符Log，需要按照内容对Log进行排序，当内容相同的时候按照索引排序；如果是数字Log，保持原来的顺序。


## 解题方法

### 分割和排序

周赛第一题，看起来题目很长，但是只要是字符串处理题，对于python都很简单。首先需要进行分割成索引和内容，然后对内容的第一个单词进行判断，如果是英文字符串，那么把内容和索引构成tuple放到letters的列表里；如果是数字字符串，那么直接把当前的这个log放到nums列表里。

然后我们需要对letters进行排序，因为tuple里首先是内容，然后是索引，所以会先对内容进行排序，然后再对索引进行排序。

把letters排序的结果重置成正常的状态和nums拼接在一起，返回即可。

时间复杂度是O(NlogN)，空间复杂度是O(N)。

```python
class Solution(object):
    def reorderLogFiles(self, logs):
        """
        :type logs: List[str]
        :rtype: List[str]
        """
        letters = []
        nums = []
        for log in logs:
            logsplit = log.split(" ")
            if logsplit[1].isalpha():
                letters.append((" ".join(logsplit[1:]), logsplit[0]))
            else:
                nums.append(log)
        letters.sort()
        return [letter[1] + " " + letter[0] for letter in letters] + nums
```


## 日期

2018 年 11 月 11 日 —— 剁手节快乐


  [1]: https://assets.leetcode.com/uploads/2018/10/12/island.png
  [2]: https://charlesliuyx.github.io/2018/10/11/%E3%80%90%E7%9B%B4%E8%A7%82%E7%AE%97%E6%B3%95%E3%80%91Egg%20Puzzle%20%E9%B8%A1%E8%9B%8B%E9%9A%BE%E9%A2%98/
