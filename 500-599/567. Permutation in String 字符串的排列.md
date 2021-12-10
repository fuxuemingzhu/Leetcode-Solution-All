作者： 		负雪明烛 
id：				fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---

题目地址：https://leetcode.com/problems/permutation-in-string/description/

## 题目描述：

Given two strings ``s1`` and ``s2``, write a function to return true if s2 contains the permutation of s1. In other words, one of the first string's permutations is the substring of the second string.

Example 1:

    Input:s1 = "ab" s2 = "eidbaooo"
    Output:True
    Explanation: s2 contains one permutation of s1 ("ba").

Example 2:

    Input:s1= "ab" s2 = "eidboaoo"
    Output: False

Note:

1. The input strings only contain lower case letters.
1. The length of both given strings is in range [1, 10,000].

## 题目大意

判断s1的某个全排列是不是在s2中（连续子字符串）。

## 解题方法

肯定不可能手动全排列的，时间复杂度太高。

思想是，使用和s1等长的滑动窗口判断s2在这个窗口内的字符出现个数和s1的字符出现个数是否相等。

使用的是一个字典，统计次数就行，比较简单。第一遍的时候是每次切片都去使用Counter，这样的话超时了。所以改用了每次增加窗口最右边的元素，删除最左边的元素，如果左边的元素次数已经为0了，需要手动删除这个元素，否则影响字典相等的判断。

时间复杂度为O(N)，空间复杂度O(1)。N为s2长度，假设判断两个字典是否相等的时间复杂度是O(1).

代码如下：

```python
class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if len(s2) < len(s1): return False
        c = collections.Counter(s1)
        n = len(s1)
        l, r = 0, n - 1
        s = collections.Counter(s2[l : r])
        while r < len(s2):
            s[s2[r]] += 1
            if s == c:
                return True
            s[s2[l]] -= 1
            if s[s2[l]] == 0:
                del s[s2[l]]
            l += 1
            r += 1
        return False
```

参考资料：

https://www.youtube.com/watch?v=wpq03MmEHIM

## 日期

2018 年 9 月 27 日 —— 国庆9天长假就要开始了！
