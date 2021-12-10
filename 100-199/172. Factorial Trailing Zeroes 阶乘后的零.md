
作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)

## 题目描述

Given an integer n, return the number of trailing zeroes in n!.

Example 1:

	Input: 3
	Output: 0
	Explanation: 3! = 6, no trailing zero.

Example 2:

	Input: 5
	Output: 1
	Explanation: 5! = 120, one trailing zero.

Note: Your solution should be in logarithmic time complexity.


## 题目大意

### 递归

分析一下，就是看n!有多少个5组成。
计算包含的2和5组成的pair的个数就可以了。  
因为5的个数比2少，所以2和5组成的pair的个数由5的个数决定。  
观察15! = 有3个5(来自其中的5, 10, 15)， 所以计算n/5就可以。  
但是25! = 有6个5(有5个5来自其中的5, 10, 15, 20, 25， 另外还有1个5来自25=(5*5)的另外一个5），  
所以除了计算n/5， 还要计算n/5/5, n/5/5/5, n/5/5/5/5, ..., n/5/5/5,,,/5直到商为0。  

最后的结果就是 

	return n/5 + n/25 + n/125 + n/625 + n/3125+...;

代码如下：

```python
class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = 0
        i = 5
        while n >= i:
            res += n / i
            i *= 5
        return res
```

### 循环

这个题一看就不能暴力求解。

算法中这个count += n / i;的意思是直接看有多少个5.
比如n=26;那么，26/5=5;26/25=1;所以结果是5+1=6个。

另外注意，一定用long。

```java
public class Solution {
    public int trailingZeroes(int n) {
        if(n<=0)    return 0;
        int count = 0;
    	for (long i = 5; n / i >= 1; i *= 5) {
    		count += n / i;
    	}
	    return count;
    }
}
```
AC:1ms

python解法如下：

```python
class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = 0
        i = 5
        while n >= i:
            res += n / i
            i *= 5
        return res
```


## 日期

2016 年 5 月 8日 
2018 年 11 月 24 日 —— 周六快乐

  [1]: https://leetcode.com/problems/factorial-trailing-zeroes/
