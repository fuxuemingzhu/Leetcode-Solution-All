作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---

@[TOC](目录)

题目地址：[https://leetcode.com/problems/valid-perfect-square/description/][1]


## 题目描述

Given a positive integer num, write a function which returns True if num is a perfect square else False.

Note: Do not use any built-in library function such as sqrt.

    Example 1:
    
    Input: 16
    Returns: True
    Example 2:
    
    Input: 14
    Returns: False

## 题目大意

判断一个数字是不是完全平方数。

## 解题方法

### 方法一：完全平方式性质

这个题其实不难，困扰我的是时间复杂度，下面这个方法是利用了完全平方数的一个性质：

	a square number is 1+3+5+7+... Time Complexity O(sqrt(N))

这个性质就是说一个完全平方数是从1开始的若干连续奇数的和。

代码如下。

```java
public class Solution {
    public boolean isPerfectSquare(int num) {
        for(int i = 1; num > 0; i += 2){
            num -= i;
        }
        return num == 0;
    }
}
```

python版本：

```python
class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        i = 1
        while num > 0:
            num -= i
            i += 2
        return num == 0
```

### 方法二：暴力求解

第一想法，直接看比这个数小的数的平方能否有等于这个数的，注意比较的范围是num/2+1，宁愿多比较一个数也不能让结果错误。

```java
public class Solution {
    public boolean isPerfectSquare(int num) {
        for(int i = 1; i <= num / 2 + 1; i++){
            if(i * i == num){
                return true;
            }
        }
        return false;
    }
}
```

### 方法三：二分查找

注意的是left调整到mid+1,right调整到mid-1,这样交叉着才能保证left<= right的判断条件有效。

```java
public class Solution {
    public boolean isPerfectSquare(int num) {
        long left = 0;
        long right = num;
        long mul = 0;
        while(left <= right){
            long mid = (right + left) / 2;
            mul = mid * mid;
            if(mul < num){
                left = mid + 1;
            }else if(mul > num){
                right = mid - 1;
            }else{
                return true;
            }
        }
        return false;
    }
}
```
python版本如下，注意我使用的其实这个模板，左闭右开的区间：

```python
class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        l, r = 0, num + 1
        # [l, r)
        while l < r:
            mid = l + (r - l) / 2
            if mid * mid == num:
                return True
            if mid * mid < num:
                l = mid + 1
            else:
                r = mid
        return False
```


### 方法四：牛顿法

牛顿法详见：[https://en.wikipedia.org/wiki/Newton%27s_method][2].

这个问题其实就是求``f(x)=num - x ^ 2``的零点。

那么，``Xn+1 = Xn - f(Xn)/f'(Xn)``.

又``f'(x) = -2x``. 

得``Xn+1 = Xn +(num - Xn ^ 2)/2Xn = (num + Xn ^ 2) / 2Xn = (num / Xn + Xn) / 2``.

即``t = (num / t + t) / 2``.

```java
public class Solution {
    public boolean isPerfectSquare(int num) {
        long t = num / 2 + 1;
        while(t * t > num){
            t = (num / t + t) / 2;
        }
        return t * t == num;
    }
}
```

python版本：

```python
class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        x = num
        while x * x > num:
            x = (x + num / x) / 2
        return x * x == num
```


## 日期

2017 年 5 月 4 日 
2018 年 10 月 27 日 —— 10月份最后的周末！
2018 年 11 月 22 日 —— 感恩节快乐～

  [1]: https://leetcode.com/problems/valid-perfect-square/description/
  [2]: https://en.wikipedia.org/wiki/Newton%27s_method
