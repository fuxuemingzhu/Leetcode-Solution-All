作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)

题目地址：[https://leetcode.com/problems/base-7/#/description][1]


## 题目描述


Given an integer, return its base 7 string representation.

Example 1:

	Input: 100
	Output: "202"

Example 2:

	Input: -7
	Output: "-10"

Note: The input will be in range of [-1e7, 1e7].

## 题目大意

把10进制数字转换成7进制字符串。

## 解题方法

### 内建库

进制转换在java里特别简单。首先用Integer类的toString()。

```java
public class Solution {
    public String convertToBase7(int num) {
        return Integer.toString(num,7);
    }
}
```

### BigInteger类

之前用过的BigInteger类。

```java
import java.math.BigInteger;
public class Solution {
    public String convertToBase7(int num) {
        return new BigInteger("" + num, 10).toString(7);
    }
}
```

### 逐位计算

用数学方法，判断正负之后，逐位求：
```java
public class Solution {
    public String convertToBase7(int num) {
        if(num == 0){
            return "0";
        }
        StringBuilder ans = new StringBuilder();
        boolean isNeg = num < 0;
        num = Math.abs(num);
        while(num != 0){
            ans.append("" + (num % 7));
            num /= 7;
        }
        if(isNeg){
            ans.append("-");
        }
        ans.reverse();
        return ans.toString();
    }
}
```

二刷的时候，Python。

```python
class Solution:
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0: return "0"
        res = []
        sign =  num >= 0
        num = abs(num)
        while num != 0:
            res.append(num % 7)
            num //= 7
        return ("" if sign else "-") + "".join(map(str, res[::-1]))
```

### 倍数相加

用倍数相加的方法：
```java
public class Solution {
    public String convertToBase7(int num) {
        if (num == 0) return "0";
        
        int sign = (num > 0 ? 1 : -1);
        long res = 0;   // 因为base7会比base10的数字要长， 防止越界，必须用long
        int digit = 1;  // 位数，从个位开始
        
        num *= sign;
        
        while (num > 0) {
            res += (num % 7) * digit;
            digit *= 10;
            num /= 7;
        }
        return String.valueOf(res * sign);
    }
}
```

## 日期

2017 年 4 月 16 日 
2018 年 11 月 17 日 —— 美妙的周末，美丽的天气

  [1]: https://leetcode.com/problems/base-7/#/description
