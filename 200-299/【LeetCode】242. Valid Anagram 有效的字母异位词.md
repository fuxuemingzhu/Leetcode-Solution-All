作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)

[LeetCode]

题目地址：[https://leetcode.com/problems/valid-anagram/](https://leetcode.com/problems/valid-anagram/)

Total Accepted: 78186 Total Submissions: 187211 Difficulty: Easy


## 题目描述

Given two strings s and t , write a function to determine if t is an anagram of s.

Example 1:

	Input: s = "anagram", t = "nagaram"
	Output: true

Example 2:

	Input: s = "rat", t = "car"
	Output: false

Note:

- You may assume the string contains only lowercase alphabets.

Follow up:
What if the inputs contain unicode characters? How would you adapt your solution to such case?

## 题目大意

### 字典统计词频

这个题刚开始我想的是通过s字符串的每个字符能否在t中找到的方式。这个显然是错的。没有考虑到多次出现的问题。即两字符串长度相等，而且每个字符出现的次数相同，那么就是变位词。

题目中说了只有小写，那就是只有26个字母。统计一下出现的频率就好了。两个字符串中如果出现的词的频率都一样则说明是变位词。

算法如下：

```java
public class Solution {
    public boolean isAnagram(String s, String t) {
        if(s.length()!=t.length()){
            return false;
        }
       int[] sTimes=new int[26];
       int[] tTimes=new int[26];
       for(int i=0;i<s.length();i++){
           sTimes[s.charAt(i)-'a']+=1;
           tTimes[t.charAt(i)-'a']+=1;
       }
       for(int i=0;i<sTimes.length;i++){
           if(sTimes[i]!=tTimes[i]){
               return false;
           }
       }
       return true;
    }
}
```
AC:12ms

在上面看到了用到了两个数组进行保存。这样空间复杂度比较大，可以用一个进行保存。

对于s, 将其作为字符数组进行遍历，在遍历的过程中，对每个出现的字符计数加一。

对于t， 同样将其遍历，对每个出现的字符计数减一。

如果s和t是anagram ， 那么最后的charcount数组中所有字符的计数都应该是0， 否则就不是anagram。

简化之后的代码：
```java
public class Solution {
    public boolean isAnagram(String s, String t) {
        if(s.length()!=t.length()){
            return false;
        }
       int[] times=new int[26];
       for(int i=0;i<s.length();i++){
           times[s.charAt(i)-'a']+=1;
           times[t.charAt(i)-'a']-=1;
       }
       for(int i=0;i<times.length;i++){
           if(times[i]!=0){
               return false;
           }
       }
       return true;
    }
}
```
AC:10ms

使用python做法，也是统计词频，代码如下：

```python
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        scount = collections.Counter(s)
        tcount = collections.Counter(t)
        return scount == tcount
```

### 排序

判断两个数字排序之后的结果是否一样即可。

```python
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        slist = list(s)
        tlist = list(t)
        return sorted(slist) == sorted(tlist)
```


## 日期

2016/4/30 13:08:21 
2018 年 11 月 13 日 —— 时间有点快
