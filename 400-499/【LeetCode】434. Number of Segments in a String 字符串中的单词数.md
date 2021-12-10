

作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)

题目地址：[https://leetcode.com/problems/number-of-segments-in-a-string/#/description][1]


## 题目描述


Count the number of segments in a string, where a segment is defined to be a contiguous sequence of non-space characters.

Please note that the string does not contain any non-printable characters.

Example:

	Input: "Hello, my name is John"
	Output: 5

## 题目大意

字符串中有多少个不包含空字符的子字符串。

## 解题方法

### 统计

这个题方法应该自己使用过的，不过是倒着来。回想自己以前在每个单词后面输入一个空格，但是行尾不要空格的时候怎么做的？不就是判断第一个单词的前面不打空格，在之后的所有单词的前面打了一个空格。这个题的思路是不是倒着来？

判断某个单词的开始的字符前面是不是空格，如果是字符串的第一个字符也会把技术加１，这样就能统计出所有用空格分割的字符串段的个数。

```java
public class Solution {
    public int countSegments(String s) {
        int count = 0;
        for(int i = 0; i < s.length(); i++){
            if(s.charAt(i) != ' ' && (i == 0 || s.charAt(i - 1) == ' ')){
                count++;
            }
        }
        return count;
    }
}
```

### 正则表达式

正则``\s``表示匹配空格，``+``表示匹配一次或者任意多次。所以有以下代码。

```java
public int countSegments(String s) {
    String trimmed = s.trim();
    if (trimmed.length() == 0) return 0;
    else return trimmed.split("\\s+").length;
}
```

python版本：

```python
class Solution(object):
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = re.sub("\s+", " ", s)
        s = s.strip()
        if not s: return 0
        return len(s.split(" "))
```

另外，如果``\S``就是匹配所有的非空字符，所以我们只要知道有多少个匹配就好了。

```python
class Solution(object):
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """
        return len(re.findall("\S+", s))
```

### 字符串分割

python的split()函数，默认的参数就是按照连续空格进行分割。注意，千万不要写参数为``" "``。

```python
class Solution(object):
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """
        return len(s.split())
```

## 日期

2017 年 5 月 ５ 日 
2018 年 11 月 24 日 —— 周六快乐

  [1]: https://leetcode.com/problems/number-of-segments-in-a-string/#/description
