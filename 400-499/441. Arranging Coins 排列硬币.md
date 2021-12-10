
作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)

题目地址：[https://leetcode.com/problems/arranging-coins/#/description][1]


## 题目描述


You have a total of n coins that you want to form in a staircase shape, where every k-th row must have exactly k coins.

Given n, find the total number of full staircase rows that can be formed.

n is a non-negative integer and fits within the range of a 32-bit signed integer.

Example 1:

	n = 5
	
	The coins can form the following rows:
	
	¤
	¤ ¤
	¤ ¤
	
	Because the 3rd row is incomplete, we return 2.

Example 2:

	n = 8
	
	The coins can form the following rows:
	
	¤
	¤ ¤
	¤ ¤ ¤
	¤ ¤
	
	Because the 4th row is incomplete, we return 3.

## 题目大意

给了n个硬币，要求第k层有k个硬币，问能摆出多少层，如果最后一层不满足的话，是不算的。

## 解题方法

### 模拟计算

如果模拟这个安排硬币的过程的话，可以这么做：

```python
class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        level = 0
        count = 0
        while count + level + 1 <= n:
            level += 1
            count += level
        return level
```

### 二分查找

上面做法的效率不高。因为前k层的硬币个数可以直接通过(k + 1) * k / 2求出来，所以很直接的想法就可以使用二分查找。

即目的是找到(k + 1) * k / 2<=sum的最大数字，套用二分查找的模板，很容易写出来。

```python
class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        left, right = 0, n + 1 #[left, right)
        while left < right:
            mid = left + (right - left) / 2
            if mid * (mid + 1) / 2 <= n:
                left = mid + 1
            else:
                right = mid
        return left - 1
```

### 数学公式

刷题的时候第一次遇到纯数学的问题，其实就是求解`sum = (x + 1) * x / 2`这个方程，很简单的就能得到`x = (-1 + sqrt(8 * n + 1)) / 2`，向下取整就能得到结果了。

下面的代码的括号也要重视一下。

```java
public class Solution {
    public int arrangeCoins(int n) {
        return (int)((-1 + Math.sqrt(1 + 8 * (long) n)) / 2);
    }
}
```

## 日期

2017 年 5 月 6 日 
2018 年 11 月 24 日 —— 周六快乐

  [1]: https://leetcode.com/problems/arranging-coins/#/description
