
作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)

题目地址：[https://leetcode.com/problems/reverse-string-ii/#/description][1]


## 题目描述


Given a string and an integer k, you need to reverse the first k characters for every 2k characters counting from the start of the string. If there are less than k characters left, reverse all of them. If there are less than 2k but greater than or equal to k characters, then reverse the first k characters and left the other as original.

Example:

	Input: s = "abcdefg", k = 2
	Output: "bacdfeg"

Restrictions:

- The string consists of lower English letters only.
- Length of the given string and k will in the range [1, 10000]

## 题目大意

每2k个字符的前k个字符进行翻转，然后后面k个数字正常，进行拼接到一起。

## 解题方法

### Java解法

也是很简单的题，但是我竟然耽误了很久。主要问题出现在了reverse函数上。我犯了错误。因为这个i不是从0开始的，那么，end-1-i的时候一定要再加上start才可以，负责不是end的下一个字符。只要细心还是可以做对的，实在不行就得用debug了。

```java
public class Solution {
    public String reverseStr(String s, int k) {
		char[] ans = s.toCharArray();
		int len = s.length();
		for (int i = 0; i < len; i += 2 * k) {
			if (len - i < k) {
				reverse(ans, i, len);
			} else {
				reverse(ans, i, i + k);
			}
		}
		return new String(ans);
    }
    public void reverse(char[] chars, int start, int end){
		for (int i = start; i < (start + end) / 2; i++) {
			char temp = chars[i];
			chars[i] = chars[end - 1 - i + start];
			chars[end - 1 - i + start] = temp;
		}
    }
}
```

### Python解法

Python的切片就是做这个的！而且切片很友好，如果切到外边的话也无所谓，因为Python会把切到外边的自动过滤掉。

```python
class Solution:
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        N = len(s)
        res = ""
        pos = 0
        while pos < N:
            nx = s[pos : pos + k]
            res = res + nx[::-1] + s[pos + k : pos + 2 * k]
            pos += 2 * k
        return res
```

## 日期

2017 年 4 月 12 日 
2018 年 11 月 17 日 —— 美妙的周末，美丽的天气

  [1]: https://leetcode.com/problems/reverse-string-ii/#/description
