
作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)

题目地址：https://leetcode.com/problems/repeated-string-match/description/

## 题目描述

Given two strings A and B, find the minimum number of times A has to be repeated such that B is a substring of it. If no such solution, return -1.

For example, with A = "abcd" and B = "cdabcdab".

Return 3, because by repeating A three times (“abcdabcdabcd”), B is a substring of it; and B is not a substring of A repeated two times ("abcdabcd").

Note:

The length of A and B will be between 1 and 10000.

## 题目大意

判断当A重复一定次数之后，B能否成为其子串。

## 解题方法

自己想了很久没想出怎么做，可是看到别人的解法后，立马就懂了：当A重复一定次数后，长度比B长了，那么就可以停止了！因为如果这种情况下B都不是A的子串，那么循环再多也没用。。因为对于B来说，A所有可能的重复都已经出现了。

python的除会向下取整，所以多加几次，比如+3。（+2会错误）

```python
class Solution(object):
    def repeatedStringMatch(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: int
        """
        na, nb = len(A), len(B)
        times = nb / na + 3
        for i in range(1, times):
            if B in A * i:
                return i
        return -1
```

C++版本如下：

```cpp
class Solution {
public:
    int repeatedStringMatch(string A, string B) {
        int NA = A.size(), NB = B.size();
        int times = NB / NA + 3;
        string t = A;
        for (int i = 1; i < times; i++) {
            if (t.find(B) != string::npos) return i;
            t += A;
        }
        return -1;
    }
};
```

参考资料：

[\[LeetCode\] Repeated String Match 重复字符串匹配](http://www.cnblogs.com/grandyang/p/7631434.html)


## 日期

2018 年 3 月 15 日 --雾霾消散，春光明媚
2018 年 11 月 24 日 —— 周日开始！一周就过去了～
