
作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)

题目地址：[https://leetcode.com/problems/guess-number-higher-or-lower/#/description][1]


## 题目描述

We are playing the Guess Game. The game is as follows:

I pick a number from 1 to n. You have to guess which number I picked.

Every time you guess wrong, I'll tell you whether the number is higher or lower.

You call a pre-defined API guess(int num) which returns 3 possible results (-1, 1, or 0):

    -1 : My number is lower
     1 : My number is higher
     0 : Congrats! You got it!

Example:

    n = 10, I pick 6.
    
    Return 6.

## 题目大意

从1～n中取了一个数字，现在给出了guess()函数，要**你**猜这个数字是多少。

## 解题方法

做这个题的重点是明白guess()函数，题目说了是``我``取了一个数字，``你``去猜这个数字，guess()是``我``的数字大了还是小了。。明白这个意思了么。

所以这个题是标准的二分查找。

```java
/* The guess API is defined in the parent class GuessGame.
   @param num, your guess
   @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
      int guess(int num); */

public class Solution extends GuessGame {
    public int guessNumber(int n) {
        int low = 1;
        int high = n;
        int mid = 0;
        while(low <= high){
            mid = low + (high - low) / 2;
            if(guess(mid) == -1){
                high = mid - 1;
            }else if(guess(mid) == 1){
                low = mid + 1;
            }else{
                return mid;
            }
        }
        return mid;
    }
}
```

python解法如下：

```python
# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        left, right = 1, n #[left, right]
        mid = left
        while left <= right:
            mid = (right + left) / 2
            res = guess(mid)
            if res == 0:
                return mid
            elif res == 1:
                left = mid + 1
            else:
                right = mid - 1
        return mid
```

## 日期

2017 年 5 月 10 日 
2018 年 11 月 23 日 —— 这就星期五了？？

  [1]: https://leetcode.com/problems/guess-number-higher-or-lower/#/description
