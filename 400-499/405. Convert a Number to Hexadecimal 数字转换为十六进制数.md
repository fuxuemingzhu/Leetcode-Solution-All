作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)


题目地址：[https://leetcode.com/problems/convert-a-number-to-hexadecimal/][1]


## 题目描述

Given an integer, write an algorithm to convert it to hexadecimal. For negative integer, two’s complement method is used.

Note:

- All letters in hexadecimal (a-f) must be in lowercase.
- The hexadecimal string must not contain extra leading 0s. If the number is zero, it is represented by a single zero character '0'; otherwise, the first character in the hexadecimal string will not be the zero character.
- The given number is guaranteed to fit within the range of a 32-bit signed integer.
- You must not use any method provided by the library which converts/formats the number to hex directly.

Example 1:

	Input:
	26
	
	Output:
	"1a"

Example 2:
	
	Input:
	-1
	
	Output:
	"ffffffff"

## 题目大意

把一个数字转成16进制，如果这个数字是负数，那么返回它的补码形式。

    
## 解题方法

### Java解法

只管想法就是把数字/16，然后从数组中取字符组成字符串。但这个只对正数有用，负数没法用。

对负数的处理不好办。刚开始想用Integer.MAX_VALUE减去负数得到整数，再转成16进制，但是，尝试了之后，正数的最大值得符号位是0，因此这个思路不同。

然后就是想到位运算。>>>的作用是无符号右移。每次右移4位就是相当于除以16，然后再把这个结果对16求余，即可。无论正负都可。因为这就是正确的每四位数划分求对应16进制数的方式。

这里有个技巧，就是hexs[(16 + num % 16) % 16]，这样做的目的就是使正负数都能统一计算16进制，不会导致数组溢出。


```java
public class Solution {
	public String toHex(int num) {
		char[] hexs = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f'};
		StringBuilder answer = new StringBuilder();
		if (num == 0) {
			return "0";
		}
		while (num != 0) {
			answer.insert(0, hexs[(16 + num % 16) % 16]);
			num = num >>> 4;
		}

		return answer.toString();

	}
}
```

AC: 8 ms

### Python解法

二刷的时候使用的是Python解法，这个解法对负数的处理方式是加上2的31次方，这样也就变成了题目要求的补码形式。

```python
class Solution(object):
    def toHex(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0:
            return "0"
        res = ""
        if num < 0:
            num += 1 << 32
        while num != 0:
            last = num % 16
            if last < 10:
                res = str(last) + res
            else:
                res = chr(last - 10 + ord('a')) + res
            num /= 16
        return res
```

## 日期

2017 年 1 月 14 日 
2018 年 11 月 20 日 —— 真是一个好天气

  [1]: https://leetcode.com/problems/convert-a-number-to-hexadecimal/
