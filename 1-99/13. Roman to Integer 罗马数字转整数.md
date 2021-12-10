- 作者：    负雪明烛
- id：      fuxuemingzhu
- 个人博客：[http://fuxuemingzhu.cn/](http://fuxuemingzhu.cn/)
- 个人公众号：负雪明烛
- 本文关键词：roman，罗马，整数，题解，leetcode, 力扣，Python, C++, Java

---
@[TOC](目录)

题目地址：[https://leetcode.com/problems/roman-to-integer/](https://leetcode.com/problems/roman-to-integer/)


## 题目描述


Roman numerals are represented by seven different symbols: ``I``, ``V``, ``X``, ``L``, ``C``, ``D`` and ``M``.

	Symbol       Value
	I             1
	V             5
	X             10
	L             50
	C             100
	D             500
	M             1000

For example, two is written as II in Roman numeral, just two one's added together. Twelve is written as, XII, which is simply X + II. The number twenty seven is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

- I can be placed before V (5) and X (10) to make 4 and 9. 
- X can be placed before L (50) and C (100) to make 40 and 90. 
- C can be placed before D (500) and M (1000) to make 400 and 900.

Given a roman numeral, convert it to an integer. Input is guaranteed to be within the range from 1 to 3999.

Example 1:

	Input: "III"
	Output: 3

Example 2:

	Input: "IV"
	Output: 4

Example 3:

	Input: "IX"
	Output: 9

Example 4:

	Input: "LVIII"
	Output: 58
	Explanation: L = 50, V= 5, III = 3.

Example 5:

	Input: "MCMXCIV"
	Output: 1994
	Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.

## 题目大意

罗马数字是阿拉伯数字传入之前使用的一种数码。罗马数字采用七个罗马字母作数字、即Ⅰ（1）、X（10）、C（100）、M（1000）、V（5）、L（50）、D（500）。记数的方法：

1. 相同的数字连写，所表示的数等于这些数字相加得到的数，如 Ⅲ=3；
1. 小的数字在大的数字的右边，所表示的数等于这些数字相加得到的数，如 Ⅷ=8、Ⅻ=12；
1. 小的数字（限于 Ⅰ、X 和 C）在大的数字的左边，所表示的数等于大数减小数得到的数，如 Ⅳ=4、Ⅸ=9； 

现在输入一个罗马数字，求其对应的10进制数字是多少。

## 解题方法

### Java解法

这个解法是从前向后遍历的。

逐位计算，将这一位数字和前者比较，根据比较大小结论来判断计算方式，注意如果此为前者小，应该减去2倍前者，此结果计入总结果。

```java
/**
	 * 逐位计算，将这一位数字和前者比较，根据比较大小结论来判断计算方式，注意如果此为前者小，应该减去2倍前者，此结果计入总结果
 *
 * @param s
 * @return
 */
public static int romanToInt(String s) {
	int previous = toNumber(s.charAt(0));
	int answer = previous;
	for (int i = 1; i < s.length(); i++) {
		int now = toNumber(s.charAt(i));
		int tempAns = 0;
		if (previous >= now) {
			tempAns += now;
		} else {
			// please pay attention to this
			tempAns = now - 2 * previous;
		}
		previous = now;
		answer += tempAns;
	}
	return answer;
}

static int toNumber(char ch) {
	switch (ch) {
		case 'I':
			return 1;
		case 'V':
			return 5;
		case 'X':
			return 10;
		case 'L':
			return 50;
		case 'C':
			return 100;
		case 'D':
			return 500;
		case 'M':
			return 1000;
	}
	return 0;
}
```

### Python解法

这个解法是从后向前遍历的。这种解法更简单，因为如果判断得到的新数字比原来的小，就直接减去就好了，而不用像上面的解法一样减去2倍。

```python
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
        res = roman[s[-1]]
        N = len(s)
        for i in range(N - 2, -1, -1):
            if roman[s[i]] < roman[s[i + 1]]:
                res -= roman[s[i]]
            else:
                res += roman[s[i]]
        return res
```

## 日期

2015/9/4 14:26:40 
2018 年 11 月 11 日 —— 剁手节快乐
