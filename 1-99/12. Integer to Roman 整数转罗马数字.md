
- 作者：    负雪明烛
- id：      fuxuemingzhu
- 个人博客：[http://fuxuemingzhu.cn/](http://fuxuemingzhu.cn/)
- 个人公众号：负雪明烛
- 本文关键词：roman, 罗马数字，题解，leetcode, 力扣，Python, C++, Java
---
@[TOC](目录)

## 题目描述


Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

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

Given an integer, convert it to a roman numeral. Input is guaranteed to be within the range from 1 to 3999.

Example 1:
	
	Input: 3
	Output: "III"

Example 2:
	
	Input: 4
	Output: "IV"

Example 3:
	
	Input: 9
	Output: "IX"

Example 4:

	Input: 58
	Output: "LVIII"
	Explanation: L = 50, V = 5, III = 3.

Example 5:

	Input: 1994
	Output: "MCMXCIV"
	Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.

## 题目大意

把一个整数转成罗马数字。

## 解题方法

考虑到这个题给出的数字的范围是1~3999，所以不用太复杂的考虑。

最简单的方法就是建立起一个对应关系，每个整数对应的数字是多少，然后把要查询的数字进行拆解，得到一系列数字的和，同时把一系列字符拼接成一个更长的字符串。

C++代码如下：

```cpp
class Solution {
public:
    string intToRoman(int num) {
        string res = "";
        vector<int> val{1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1};
        vector<string> str{"M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"};
        for (int i = 0; i < val.size(); ++i) {
            while (num >= val[i]) {
                res += str[i];
                num -= val[i];
            }
        }
        return res;
    }
};
```

Java代码如下：

```java
package com.fuxuemingzhu.integertoroman;
/**
 * Given an integer, convert it to a roman numeral.
 * <p/>
 * Input is guaranteed to be within the range from 1 to 3999.
 * <p/>
 * Created by fuxuemingzhu on 2015/9/4.
 */
public class Solution {

	static int value[] = {1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1};
	static String symbol[] = {"M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"};
	/**
	 * 先存储好特定的数字，将输入的数字除以最大的特定数字，得到有几个最高为的数字，剩下的依次从次大数往下推。
	 *
	 * @return answer
	 */
	public static String intToRoman(int num) {
		String ret = "";
		int taps;
		for (int i = 0; i < value.length; i++) {
			taps = num / value[i];
			if (taps >= 1) {
				for (int j = 0; j < taps; j++) {
					ret += symbol[i];
				}
			}
			num -= taps * value[i];
		}
		return ret;
	}
}
```



参考资料：

[http://blog.csdn.net/ljiabin/article/details/39968583](http://blog.csdn.net/ljiabin/article/details/39968583)
[http://blog.csdn.net/havenoidea/article/details/11848921](http://blog.csdn.net/havenoidea/article/details/11848921)
http://www.cnblogs.com/grandyang/p/4123374.html

## 日期

2015/9/4 16:40:35 
2019 年 1 月 25 日 —— 这学期最后一个工作日
