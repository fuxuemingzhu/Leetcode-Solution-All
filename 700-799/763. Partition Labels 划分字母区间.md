
作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)

题目地址：https://leetcode.com/problems/partition-labels/description/

## 题目描述

A string S of lowercase letters is given. We want to partition this string into as many parts as possible so that each letter appears in at most one part, and return a list of integers representing the size of these parts.

Example 1:

    Input: S = "ababcbacadefegdehijhklij"
    Output: [9,7,8]
    Explanation:
    The partition is "ababcbaca", "defegde", "hijhklij".
    This is a partition so that each letter appears in at most one part.
    A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits S into less parts.

Note:

1. S will have length in range [1, 500].
1. S will consist of lowercase letters ('a' to 'z') only.


## 解题方法

方法一：

题意是要对一个字符串进行尽可能多的划分，并保证每个划分中的元素不在其他划分中出现。

想法比较具有技巧性。如果一段序列中每个元素的在S中最右边的序号都在某个范围内，那么就可以划分成一个段。

因此，使用字典保存每个元素出现的最靠右的位置。然后对字符串S进行遍历，找出最靠右的序号的最大值j。如果i和j重合了，说明已经到了这个划分的末尾了，然后进行划分。并开始计算下一个划分。


```python
class Solution(object):
    def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        lindex = {c: i for i, c in enumerate(S)}
        j = anchor = 0
        ans = []
        for i, c in enumerate(S):
            j = max(j, lindex[c])
            if i == j:
                ans.append(j - anchor + 1)
                anchor = j + 1
        return ans
```

C++版本如下：

```cpp
class Solution {
public:
    vector<int> partitionLabels(string S) {
        map<char, int> d;
        for (int i = 0; i < S.size(); i++) d[S[i]] = i;
        int start = 0, end = 0;
        vector<int> res;
        for (int i = 0; i < S.size(); i++) {
            end = max(end, d[S[i]]);
            if (i == end) {
                res.push_back(end - start + 1);
                start = end + 1;
            }
        }
        return res;
    }
};
```

## 日期

2018 年 2 月 5 日 
2018 年 12 月 2 日 —— 又到了周日
