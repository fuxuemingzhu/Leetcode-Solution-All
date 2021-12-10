作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)

[LeetCode]

题目地址：[https://leetcode.com/problems/repeated-substring-pattern/][1]

 - Difficulty: Easy

## 题目描述

Given a non-empty string check if it can be constructed by taking a substring of it and appending multiple copies of the substring together. You may assume the given string consists of lowercase English letters only and its length will not exceed 10000.


Example 1:

	Input: "abab"
	Output: True
	Explanation: It's the substring "ab" twice.

Example 2:

	Input: "aba"
	Output: False

Example 3:

	Input: "abcabcabcabc"
	Output: True
	Explanation: It's the substring "abc" four times. (And the substring "abcabc" twice.)

## 题目大意

判断一个字符串能不能由比它更小的子串构成。

## 解题方法

### 遍历子串

思路是这样的：

- 重复的子串的长度肯定是总长度的因子。
- 遍历所有的因子，从length/2开始
- 如果i是length的因子，把从0到i这个substring重复length()/i倍
- 看看这个重复后的串是否与原来的串相等。

```java
public class Solution {
    public boolean repeatedSubstringPattern(String str) {
    	int l = str.length();
    	for(int i=l/2;i>=1;i--) {
    		if(l%i==0) {
    			int m = l/i;
    			String subS = str.substring(0,i);
    			StringBuilder sb = new StringBuilder();
    			for(int j=0;j<m;j++) {
    				sb.append(subS);
    			}
    			if(sb.toString().equals(str)) return true;
    		}
    	}
    	return false;
    }
    
}
```

AC: 48 ms

-------

二刷， python.

现在再刷这个题的时候因为用的Python，已经对字符串处理了然于胸了，所以很快就写出了下面的答案：

同样是遍历因子，然后把新的切片乘以倍数，看得到的字符串是否和源字符串相同。


```python
class Solution:
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        len_s = len(s)
        for i in range(1, len_s // 2 + 1):
            if len_s % i == 0:
                sub_s = s[:i]
                if sub_s * (len_s // i) == s:
                    return True
        return False
```


## 日期

2017 年 1 月 15 日 
2018 年 7 月 4 日 
2018 年 11 月 22 日 —— 感恩节快乐～

  [1]: https://leetcode.com/problems/repeated-substring-pattern/
