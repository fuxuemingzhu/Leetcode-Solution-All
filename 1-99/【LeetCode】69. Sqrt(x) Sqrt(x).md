
作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)

题目地址：https://leetcode.com/problems/sqrtx/description/


## 题目描述

Implement int sqrt(int x).

Compute and return the square root of x.

x is guaranteed to be a non-negative integer.


Example 1:
    
    Input: 4
    Output: 2

Example 2:
    
    Input: 8
    Output: 2
    Explanation: The square root of 8 is 2.82842..., and since we want to return an integer, the decimal part will be truncated.

## 题目大意

求x的算术平方根向下取整。

## 解题方法

### 方法一：库函数

求算数平方根。可以直接用库。

```python
import math
class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        return int(math.sqrt(x))
```

### 方法二：牛顿法

牛顿法详见：https://en.wikipedia.org/wiki/Newton%27s_method

这个问题其实就是求``f(x)=num - x ^ 2``的零点。

那么，``Xn+1 = Xn - f(Xn)/f'(Xn)``.

又``f'(x) = -2x``. 

得``Xn+1 = Xn +(num - Xn ^ 2)/2Xn = (num + Xn ^ 2) / 2Xn = (num / Xn + Xn) / 2``.

即``t = (num / t + t) / 2``.


```python
class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        num = x
        while num * num > x:
            num = (num + x / num) / 2
        return num
```

### 方法三：二分查找

这个题是二分查找的经典题目了，直接套用二分查找的模板即可。这里贡献一个二分查找的模板，模板中查找的区间是[l, r)，即左闭右开。

```python
def binary_searche(l, r):
    while l < r:
        m = l + (r - l) // 2
        if f(m):    # 判断找了没有，optional
            return m
        if g(m):
            r = m   # new range [l, m)
        else:
            l = m + 1 # new range [m+1, r)
    return l    # or not found
```

这个题的二分查找版本的代码如下：

```python
class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        left, right = 0, x + 1
        # [left, right)
        while left < right:
            mid = left + (right - left) // 2
            if mid ** 2 == x:
                return mid
            if mid ** 2 < x:
                left = mid + 1
            else:
                right = mid
        return left - 1
```

二刷的时候用了二分查找，但是写法和上面略有区别。

```python
class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        left, right = 0, x + 1 #[left, right)
        while left < right:
            mid = (left + right) // 2
            if mid ** 2 == x:
                return mid
            elif (mid - 1) ** 2 < x and mid ** 2 >= x:
                return mid - 1
            elif mid ** 2 < x:
                left = mid + 1
            else:
                right = mid
        return left
```

如果是C++就比较痛苦了，因为要考虑到数字是不是越界了，所以我用了long long.

```cpp
class Solution {
public:
    int mySqrt(long long x) {
        if (x == 0) return 0;
        long long left = 0, right = x + 1; //[left, right)
        while (left < right) {
            long long mid = left + (right - left) / 2;
            if (mid == x / mid) {
                return mid;
            } else if (mid < x / mid) {
                left = mid + 1;
            } else {
                right = mid;
            }
        }
        return left - 1;
    }
};
```

如果只使用int的话，需要考虑right = x + 1这一步可能会超边界，所以仍然使用[left,right)区间，那么当x<=1的时候，返回的应该是x。

```cpp
class Solution {
public:
    int mySqrt(int x) {
        if (x <= 1) return x;
        int left = 0, right = x; //[left, right)
        while (left < right) {
            int mid = left + (right - left) / 2;
            if (mid == x / mid) {
                return mid;
            } else if (mid < x / mid) {
                left = mid + 1;
            } else {
                right = mid;
            }
        }
        return left - 1;
    }
};
```

## 日期

2018 年 2 月 4 日 
2018 年 10 月 26 日 ——项目验收结束了！
2018 年 11 月 27 日 —— 最近的雾霾太可怕

  [1]: https://leetcode.com/problems/valid-perfect-square/description/
