作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)



题目地址： [https://leetcode.com/problems/hamming-distance/][1]

 - Total Accepted: 12155
 - Total Submissions: 16696
 - Difficulty: Easy

## 题目描述

The Hamming distance between two integers is the number of positions at which the corresponding bits are different.

Given two integers ``x`` and ``y``, calculate the Hamming distance.

Note: ``0 ≤ x, y < 2^31``.

Example:

	Input: x = 1, y = 4
	
	Output: 2
	
	Explanation: 
	
	    1   (0 0 0 1) 
	    4   (0 1 0 0)
	           ↑   ↑
	
	
	The above arrows point to positions where the corresponding bits are different.

## 题目大意

计算两个数字的汉明间距。汉明间距是指两个数字的二进制数字不同的位数。

## 解题方法

### Java解法

位运算，明显的是两者不一样时结果为一，那么就是使用异或。为了统计1的个数废了一点劲。

#### 方法一：异或 + 字符串分割

```java
public class Solution {
    public int hammingDistance(int x, int y) {
        return Integer.toBinaryString(x ^ y).split("0").length - 1;
    }
}
```

AC:18 ms

#### 方法二：异或 + 字符串遍历

上述方法效率不是很高，所以我试了试用统计1出现的次数的方法。

```java
public class Solution {
    public int hammingDistance(int x, int y) {
        int answer = 0;
		String charString = Integer.toBinaryString(x ^ y);
		for (int i = 0; i < charString.length(); i++) {
			if (charString.charAt(i) == '1') {
				answer++;
			}
		}
		return answer;
    }
}
```
AC:12 ms

#### 方法三：异或 + 位统计

看了top答案发现我对java的库函数还是不够了解。这个方法太酷了！
```java
public class Solution {
    public int hammingDistance(int x, int y) {
        return Integer.bitCount(x ^ y);
    }
}
```

方法四：

### 二刷 python解法

#### 方法一：异或 + 字符串count

python 封装的比较好用。

```python
class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        return bin(x ^ y).count('1')
```

#### 方法二：循环异或

每次得到x和y的最低位，然后异或，再把两个同时移位。

```python3
class Solution:
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        res = 0
        while x or y:
            if (x & 1) ^ (y & 1):
                res += 1
            x >>= 1
            y >>= 1
        return res
```

#### 方法三：异或 + 单次遍历

显然不需要每次移位之后再异或，这样操作很慢的。可以先异或好之后，再遍历求1的个数。

```python3
class Solution:
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        xor = x ^ y
        res = 0
        while xor:
            res += xor & 1
            xor >>= 1
        return res
```


## 日期

2017 年 1 月 2 日 

2018 年 3 月 9 日

2018 年 11 月 2 日 —— 浑浑噩噩的一天

  [1]: https://leetcode.com/problems/hamming-distance/
