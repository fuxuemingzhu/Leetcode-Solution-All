
作者： 		负雪明烛 
id：				fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---

题目地址: https://leetcode.com/problems/unique-substrings-in-wraparound-string/description/

## 题目描述：

Consider the string s to be the infinite wraparound string of "abcdefghijklmnopqrstuvwxyz", so s will look like this: ``"...zabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcd...."``.

Now we have another string p. Your job is to find out how many unique non-empty substrings of p are present in s. In particular, your input is the string p and you need to output the number of different non-empty substrings of p in the string s.

Note: p consists of only lowercase English letters and the size of p might be over 10000.

Example 1:

    Input: "a"
    Output: 1
    
    Explanation: Only the substring "a" of string "a" is in the string s.

Example 2:

    Input: "cac"
    Output: 2
    Explanation: There are two substrings "a", "c" of string "cac" in the string s.

Example 3:

    Input: "zab"
    Output: 6
    Explanation: There are six substrings "z", "a", "b", "za", "ab", "zab" of string "zab" in the string s.

## 题目大意

在一个无限循环的字母表s中，找出给定的字符串的所有子串在s中出现了多少次。

## 解题方法

这个做法和前几天的某个做法一致，从头开始遍历，在遍历的过程中，只用考虑当新添加这个字符的时候，能否和前面构成连续的，如果能构成连续的，那么结果中增加上以这个字符结尾的子串个数，即当前的长度。否则就是一个新串，长度是1.

其实这个思路就是dp，dp数组保存的是以当前字符结尾，能够成的所有子字符串个数。

> 比如abcd这个字符串，以d结尾的子字符串有abcd, bcd, cd,
> d，那么我们可以发现bcd或者cd这些以d结尾的字符串的子字符串都包含在abcd中，那么我们知道以某个字符结束的最大字符串包含其他以该字符结束的字符串的所有子字符串。

这个思路又有点类似于虫取法，一直更新和保存子区间的长度。

时间复杂度是O(N)，空间复杂度是O(26)。

```python
class Solution:
    def findSubstringInWraproundString(self, p):
        """
        :type p: str
        :rtype: int
        """
        count = collections.defaultdict(int)
        N = len(p)
        _len = 0
        for i in range(N):
            if i > 0 and (ord(p[i]) - ord(p[i - 1]) == 1 or (p[i] == 'a' and p[i - 1] == 'z')):
                _len += 1
            else:
                _len = 1
            count[p[i]] = max(count[p[i]], _len)
        return sum(count.values())
```

参考资料：

http://www.cnblogs.com/grandyang/p/6143071.html


## 日期

2018 年 10 月 16 日 —— 下雨天还是挺舒服的


  [1]: https://blog.csdn.net/fuxuemingzhu/article/details/51291406
