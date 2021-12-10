# 【LeetCode】760. Find Anagram Mappings 解题报告

标签（空格分隔）： LeetCode

---

题目地址：[https://leetcode.com/problems/find-anagram-mappings/description/][1]


## 题目描述：

Given two lists Aand B, and B is an anagram of A. B is an anagram of A means B is made by randomizing the order of the elements in A.

We want to find an index mapping P, from A to B. A mapping P[i] = j means the ith element in A appears in B at index j.

These lists A and B may contain duplicates. If there are multiple answers, output any of them.

For example, given

A = [12, 28, 46, 32, 50]
B = [50, 12, 32, 46, 28]
We should return
[1, 4, 3, 2, 0]
as P[0] = 1 because the 0th element of A appears at B[1], and P[1] = 4 because the 1st element of A appears at B[4], and so on.
Note:

A, B have equal lengths in range [1, 100].
A[i], B[i] are integers in range [0, 10^5].

## Ways

就是找到A中每个元素在B中的位置即可，如果出现了重复的元素，可以返回任意一种次序即可。

方法一：
```python
class Solution:
    def anagramMappings(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        answer = []
        for a in A:
            for i,b in enumerate(B):
                if a == b:
                    answer.append(i)
                    break
        return answer
```

方法二：
```python
class Solution:
    def anagramMappings(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        return [B.index(a) for a in A]
```

方法三：
```python
class Solution:
    def anagramMappings(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        d ={}
        for i,b in enumerate(B):
            d[b] = i
        return [d[a] for a in A]
```

## Date

2018 年 1 月 13 日 


  [1]: https://leetcode.com/problems/find-anagram-mappings/description/