
作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)

题目地址：[https://leetcode.com/problems/reverse-words-in-a-string-iii/#/description][1]


## 题目描述

Given a string, you need to reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.

Example：

    Input: "Let's take LeetCode contest"
    Output: "s'teL ekat edoCteeL tsetnoc"

Note:

In the string, each word is separated by single space and there will not be any extra space in the string.

## 题目大意

把字符串中的每个单词进行翻转，翻转后仍然按照原来的单词顺序进行拼接。

## 解题方法

### Java解法

很简单的题，直接分割开每个单词，然后把单词翻转再拼接就好了。我的第一种做法：

```java
public class Solution {
    public String reverseWords(String s) {
        String[] words = s.split(" ");
        StringBuilder ans = new StringBuilder();
        boolean isFirst = true;
        for(String word : words){
            StringBuilder temp = new StringBuilder(word);
            word = temp.reverse().toString();
            if(isFirst){
                ans.append(word);
                isFirst = false;
            }else{
                ans.append(" " + word);
            }
            
        }
        return ans.toString();
    }
}
```

看着时间有点长 14 ms，于是没用StringBuilder，方法如下

```java
public class Solution {
    public String reverseWords(String s) {
        String[] words = s.split(" ");
        StringBuilder ans = new StringBuilder();
        boolean isFirst = true;
        for(String word : words){
            word= reverse(word);
            if(isFirst){
                ans.append(word);
                isFirst = false;
            }else{
                ans.append(" " + word);
            }
            
        }
        return ans.toString();
    }
    public String reverse(String s){
        char[] chars = s.toCharArray();
        for(int i = 0; i < chars.length / 2; i++){
            char temp = chars[i];
            chars[i] = chars[chars.length - 1 - i];
            chars[chars.length - 1 - i] = temp;
        }
        return new String(chars);
    }
}
```
时间变为 13 ms，还想继续压缩时间。全部用数组实现：

```java
public class Solution {
    public String reverseWords(String s) {
        String[] words = s.split(" ");
		char[] ans = new char[s.length()];
		boolean isFirst = true;
		int i = 0;
		for (String word : words) {
			char[] chars = word.toCharArray();
			for (int j = 0; j < chars.length / 2; j++) {
				char temp = chars[j];
				chars[j] = chars[chars.length - 1 - j];
				chars[chars.length - 1 - j] = temp;
			}
			System.arraycopy(chars, 0, ans, i, chars.length);
			i += chars.length;
			if (i != ans.length) {
				ans[i] = ' ';
			}
			i++;
		}
		return new String(ans);
    }
}
```
这个时间却变成了16ms，已经无语。嗯。就这样吧。

### Python解法

使用Python可以直接使用split函数之后，进行[::-1]即做了翻转操作，然后再用" ".join()拼接在一起就行了。


```python
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        return " ".join(map(lambda x : x[::-1], s.split(" ")))
```

## 日期

2017 年 4 月 12 日 
2018 年 11 月 6 日 —— 腰酸背痛要废了

  [1]: https://leetcode.com/problems/reverse-words-in-a-string-iii/#/description
