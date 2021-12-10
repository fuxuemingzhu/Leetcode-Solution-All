
作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)

题目地址：https://leetcode.com/problems/largest-palindrome-product/description/


## 题目描述

Find the largest palindrome made from the product of two n-digit numbers.

Since the result could be very large, you should return the largest palindrome mod 1337.

Example:
    
    Input: 2
    
    Output: 987
    
    Explanation: 99 x 91 = 9009, 9009 % 1337 = 987

Note:

- The range of n is [1,8].



## 题目大意

找出两个n位数字乘积能构成的最大回文数字。

## 解题方法

题目本身不是难题，但是普通方法肯定会超时。。这个题我没认真做，抄了一个别人的答案。我觉得这个题没什么意思。

```python
class Solution(object):
    def largestPalindrome(self, n):
        if n==1: return 9
        if n==2: return 987
        for a in xrange(2, 9*10**(n-1)):
            hi=(10**n)-a
            lo=int(str(hi)[::-1])
            if a**2-4*lo < 0: continue
            if (a**2-4*lo)**.5 == int((a**2-4*lo)**.5):
                return (lo+10**n*(10**n-a))%1337
```

二刷，下面的python代码依然会超时，尴尬。思路是找出n位数字的上界和下界，然后我们把目标在这区间内进行搜索，看这个区间内的每个数字给构成回文，然后判断这个数字能否被区间内的数字整除。

```py
class Solution(object):
    def largestPalindrome(self, n):
        """
        :type n: int
        :rtype: int
        """
        upper = 10 ** n - 1
        lower = upper / 10
        for i in xrange(upper, lower, -1):
            l = int(str(i) + str(i)[::-1])
            j = upper
            while j * j > l:
                if l % j == 0:
                    return l % 1337
                j -= 1
        return 9
```

C++代码效率比较高，能通过。

```cpp
class Solution {
public:
    int largestPalindrome(int n) {
        int upper = pow(10, n) - 1;
        int lower = upper / 10;
        for (int i = upper; i > lower; i--){
            string s = to_string(i);
            long p = stol(s + string(s.rbegin(), s.rend()));
            for (long j = upper; j * j > p; j--){
                if (p % j == 0){
                    return p % 1337;
                }
            }
        }
        return 9;
    }
};
```

## 日期

2018 年 2 月 28 日 
2018 年 11 月 30 日 —— 又到了周末
