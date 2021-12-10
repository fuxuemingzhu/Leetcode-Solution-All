作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)

题目地址：[https://leetcode.com/problems/reverse-string/](https://leetcode.com/problems/reverse-string/)

Total Accepted: 11014 Total Submissions: 18864 Difficulty: Easy


## 题目描述


Write a function that takes a string as input and returns the string reversed.

Example 1:

	Input: "hello"
	Output: "olleh"

Example 2:

	Input: "A man, a plan, a canal: Panama"
	Output: "amanaP :lanac a ,nalp a ,nam A"


## 题目大意

### 新构建字符串

字符串按位翻转：

```java
public class Solution {
    public String reverseString(String s) {
        StringBuffer answer=new StringBuffer("");
        int tail=s.length()-1;
        for(int i=tail;i>=0;i--){
            answer.append(s.charAt(i));
        }
        return answer.toString();
        
    }
}
```
AC:6ms

python支持切片进行翻转，所以代码只有一行。

```python
class Solution:
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        return s[::-1]
```


### 原地翻转

转换为字符串数组后，in-place翻转。下面的这个java解法返回值是个新的字符串，但是作为结果应该不计算空间复杂度之内。

java代码：

```java
public class Solution {
    public String reverseString(String s) {
        char[] chars=s.toCharArray();
        for(int i=0;i<chars.length/2;i++){
            char temp=chars[i];
            chars[i]=chars[chars.length-1-i];
            chars[chars.length-1-i]=temp;
        }
        return new String(chars);
        
    }
}
```
AC:3ms

## 日期

2016/4/29 21:27:57 
2018 年 11 月 6 日 —— 腰酸背痛要废了
