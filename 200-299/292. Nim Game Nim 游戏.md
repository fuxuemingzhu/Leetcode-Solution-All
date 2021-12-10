
作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)

题目地址：[https://leetcode.com/problems/nim-game/](https://leetcode.com/problems/nim-game/)

Total Accepted: 66290 Total Submissions: 125590 Difficulty: Easy


## 题目描述

You are playing the following Nim Game with your friend: There is a heap of stones on the table, each time one of you take turns to remove 1 to 3 stones. The one who removes the last stone will be the winner. You will take the first turn to remove the stones.

Both of you are very clever and have optimal strategies for the game. Write a function to determine whether you can win the game given the number of stones in the heap.

Example:

	Input: 4
	Output: false 
	Explanation: If there are 4 stones in the heap, then you will never win the game;
	             No matter 1, 2, or 3 stones you remove, the last stone will always be 
	             removed by your friend.

## 题目大意

你和另一个人在玩一个游戏，每次可以取1~3个石头，而且每次都必须取。现在要你先取，并且能取到最后的那个石头的人能赢。问你是不是有机会赢？

## 解题方法

题目的意思是只要拿最后一个石子的人赢。

因为每次最多拿三个，所以只要我拿走子之后，最后剩余四个的话，我就输了。

所以，所有子的个数不能被四整除我就赢了，否则我会输。输的原因是对手每次都拿4-n，n为当次我拿到子的个数。

Java代码：

```java
public class Solution {
    public boolean canWinNim(int n) {
        return n % 4!= 0;
    }
}
```

---

二刷，python.

转眼两年办过去了，再次做了这个题。python代码如下：

```python
class Solution(object):
    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return n % 4 != 0
```


## 日期

2016/4/29 21:39:23 
2018 年 11 月 ９ 日 —— 睡眠可以
