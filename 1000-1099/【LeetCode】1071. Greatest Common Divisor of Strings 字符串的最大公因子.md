
作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)


题目地址：https://leetcode.com/problems/greatest-common-divisor-of-strings/

## 题目描述

For strings ``S`` and ``T``, we say ``"T divides S"`` if and only if ``S = T + ... + T``  (T concatenated with itself 1 or more times)

Return the largest string ``X`` such that ``X`` divides ``str1`` and ``X`` divides ``str2``.

 

Example 1:

    Input: str1 = "ABCABC", str2 = "ABC"
    Output: "ABC"

Example 2:

    Input: str1 = "ABABAB", str2 = "ABAB"
    Output: "AB"

Example 3:

    Input: str1 = "LEET", str2 = "CODE"
    Output: ""
     

Note:

1. 1 <= str1.length <= 1000
1. 1 <= str2.length <= 1000
1. str1[i] and str2[i] are English uppercase letters.


## 题目大意

求两个字符串的最长公共重复子串。重复子串是指原字符串可以有其子串重复若干次得到。

## 解题方法

### 暴力遍历

最长公共重复子串重复若干次之后能分别得到str1和str2，那么最明显地，该子串的长度一定是str1和str2长度的公因数。看了一下字符串的长度最多只有1000，所以我们完全可以对长度进行遍历，判断每个公因数是不是构成最长公共重复子串。因为要找最长的，所以找到最长之后，直接返回即可。

时间复杂度O(N^2)。外部循环找到公因数，时间复杂度O(N)；内部要创建新的字符串和原先的字符串进行比较，时间复杂度也是O(N)。

Python代码如下：

```python
class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        l1, l2 = len(str1), len(str2)
        shorter = min(l1, l2)
        res = ""
        for i in range(shorter, 0, -1):
            if l1 % i or l2 % i:
                continue
            t1, t2 = l1 // i, l2 // i
            gcd = str1[:i]
            rebuild1 = gcd * t1
            rebuild2 = gcd * t2
            if rebuild1 == str1 and rebuild2 == str2:
                res = gcd
                break
        return res
```

C++代码如下：


```cpp
class Solution {
public:
    string gcdOfStrings(string str1, string str2) {
        int l1 = str1.size();
        int l2 = str2.size();
        int shorter = min(l1, l2);
        string res;
        for (int i = shorter; i >= 1; --i) {
            if ((l1 % i == 0) && (l2 % i == 0)) {
                int t1 = l1 / i;
                int t2 = l2 / i;
                string gcd = str1.substr(0, i);
                string rebuild1 = genRepeatStr(t1, gcd);
                string rebuild2 = genRepeatStr(t2, gcd);
                if ((rebuild1 == str1) && (rebuild2 == str2)) {
                    res = gcd;
                    break;
                }
            }
        }
        return res;
    }
    string genRepeatStr(int times, string substr) {
        string res;
        while (times--) {
            res += substr;
        }
        return res;
    }
};
```

## 日期

2019 年 6 月 8 日 —— 刷题尽量不要停
