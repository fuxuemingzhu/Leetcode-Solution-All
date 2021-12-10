
作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)

题目地址：[https://leetcode.com/problems/jewels-and-stones/description/][1]


## 题目描述：

You're given strings J representing the types of stones that are jewels, and S representing the stones you have.  Each character in S is a type of stone you have.  You want to know how many of the stones you have are also jewels.

The letters in J are guaranteed distinct, and all characters in J and S are letters. Letters are case sensitive, so "a" is considered a different type of stone from "A".

Example 1:

	Input: J = "aA", S = "aAAbbbb"
	Output: 3

Example 2:

	Input: J = "z", S = "ZZ"
	Output: 0

Note:

1. S and J will consist of letters and have length at most 50.
1. The characters in J are distinct.

## 题目大意

J里面的每个字符是个宝石，保证不重复。S中的每个字符是一个石头，有可能出现重复。统计有多少个石头恰好也是宝石。

## 解题方法

### 数组count

因为J里的元素是独一无二的，所以只要数一数S中出现了多少个j就行了。不需要用set().

时间复杂度是O(MN)，空间复杂度是O(1)。M是J长度，N是S长度。


```python
class Solution(object):
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        return sum(S.count(j) for j in J)
```

### 字典Counter

先用Counter保存每个字母出现的次数，然后由于J里面的字符是不重复的，所以直接遍历，然后统计其中的每个字符在S中出现的次数就行了。

时间复杂度是O(MN)，空间复杂度是O(N)。M是J长度，N是S长度。

```python
class Solution:
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        sCount = collections.Counter(S)
        res = 0
        for j in J:
            res += sCount[j]
        return res
```

## 日期

2018 年 1 月 28 日 
2018 年 11 月 2 日 —— 浑浑噩噩的一天

  [1]: https://leetcode.com/problems/jewels-and-stones/description/
