# 【LeetCode】299. Bulls and Cows 解题报告（Python）

作者： 		负雪明烛 
id：				fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---

题目地址：https://leetcode.com/problems/bulls-and-cows/description/

## 题目描述：

You are playing the following Bulls and Cows game with your friend: You write down a number and ask your friend to guess what the number is. Each time your friend makes a guess, you provide a hint that indicates how many digits in said guess match your secret number exactly in both digit and position (called "bulls") and how many digits match the secret number but locate in the wrong position (called "cows"). Your friend will use successive guesses and hints to eventually derive the secret number.

Write a function to return a hint according to the secret number and friend's guess, use ``A`` to indicate the bulls and ``B`` to indicate the cows. 

Please note that both secret number and friend's guess may contain duplicate digits.

Example 1:

    Input: secret = "1807", guess = "7810"
    
    Output: "1A3B"
    
    Explanation: 1 bull and 3 cows. The bull is 8, the cows are 0, 1 and 7.

Example 2:

    Input: secret = "1123", guess = "0111"
    
    Output: "1A1B"
    
    Explanation: The 1st 1 in friend's guess is a bull, the 2nd or 3rd 1 is a cow.

Note: You may assume that the secret number and your friend's guess only contain digits, and their lengths are always equal.

## 题目大意

玩一个叫做`` Bulls and Cows``的游戏，即给出了一个源字符串和一个猜的字符串，长度相等。如果对应位置猜对了，那么这个叫做一个bull；如果某个位置猜的字符没有猜对，但是这个猜的字符在其他位置出现了，叫做一个cow。统计多少个bull和cow。

这个题说了，可能会出现重复数字，所以必须猜的多个位置都可能和在源字符串中有对应，是这个意思。

## 解题方法

只要明白了题目，我想这个题还是很简单的。bulls比较好统计，直接判断对应位置是否相等。计算cows的时候，要在secret中查找有没有出现过，而且出现过的话就要把这个出现的位置去掉，以后就不能再用了。这个该怎么实现呢？如果是暴力的话，使用List进行保存、查找、删除，那么操作很费时。如果使用set保存secret，那么当secret中有多个相同的字符的时候，set就进行了去重，也不是可以的。所以，必须保存secret中每个字符出现的次数，因此用dict.

思路出来只有，实现很简单了，就不讲了。

每个操作的时间复杂度是O(N)，空间复杂度是O(1).字符串中仅包含数字，那么，字典中最多10个元素，可以认为是O(1)的空间。

代码如下：

```python
class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        bulls = 0
        cows = 0
        secret_dict = collections.defaultdict(int)
        for s, g in zip(secret, guess):
            if s == g:
                bulls += 1
            else:
                secret_dict[s] += 1
        for i, g in enumerate(guess):
            if secret[i] != guess[i] and secret_dict[g]:
                cows += 1
                secret_dict[g] -= 1
        return str(bulls) + "A" + str(cows) + "B"
```

参考资料：


## 日期

2018 年 9 月 26 日 —— 美好的一周又快要过去了。。
