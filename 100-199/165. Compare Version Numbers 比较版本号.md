# 【LeetCode】165. Compare Version Numbers 解题报告（Python）

标签（空格分隔）： LeetCode

作者： 		负雪明烛 
id：				fuxuemingzhu
个人博客：	http://fuxuemingzhu.me/

---

题目地址：https://leetcode.com/problems/compare-version-numbers/description/

## 题目描述：

Compare two version numbers version1 and version2.
If ``version1 > version2`` return ``1``; if ``version1 < version2`` return ``-1``;otherwise return ``0``.

You may assume that the version strings are non-empty and contain only digits and the . character.
The . character does not represent a decimal point and is used to separate number sequences.
For instance, 2.5 is not "two and a half" or "half way to version three", it is the fifth second-level revision of the second first-level revision.

Example 1:

    Input: version1 = "0.1", version2 = "1.1"
    Output: -1

Example 2:

    Input: version1 = "1.0.1", version2 = "1"
    Output: 1

Example 3:

    Input: version1 = "7.5.2.4", version2 = "7.5.3"
    Output: -1

## 题目大意

比较两个版本号的大小。

## 解题方法

版本是用.进行分割的，那么我们也只能通过用.进行分割来判定版本号的大小。把版本号进行分割，需要找出一个较长的版本号的长度，把较短的版本的后面用0进行补齐。恩，然后进行比较。

```python
class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        v1_split = version1.split('.')
        v2_split = version2.split('.')
        v1_len, v2_len = len(v1_split), len(v2_split)
        maxLen = max(v1_len, v2_len)
        for i in range(maxLen):
            temp1, temp2 = 0, 0
            if i < v1_len:
                temp1 = int(v1_split[i])
            if i < v2_len:
                temp2 = int(v2_split[i])
            if temp1 < temp2:
                return -1
            elif temp1 > temp2:
                return 1
        return 0
```

## 日期

2018 年 6 月 26 日 ———— 早睡早起