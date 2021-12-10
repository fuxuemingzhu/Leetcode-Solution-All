
作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)

[LeetCode]

题目地址：[https://leetcode.com/problems/ransom-note/][1]

 - Difficulty: Easy

## 题目描述


Given an arbitrary ransom note string and another string containing letters from all the magazines, write a function that will return true if the ransom note can be constructed from the magazines ; otherwise, it will return false.

Each letter in the magazine string can only be used once in your ransom note.

Note:

You may assume that both strings contain only lowercase letters.

	canConstruct("a", "b") -> false
	canConstruct("aa", "ab") -> false
	canConstruct("aa", "aab") -> true

## 题目大意

判断ransom能否由magazines的字符构成。

## 解题方法

### Java解法

理解题意很关键，这个是说从magazine中取出几个元素排列组合能够摆成ransomNote。

参考Find the Difference的题目，做个有26个位置的数组，保存字符出现的次数，最后统计一下即可。

其中一个字符串的元素使位置元素++，另外个字符串使字符串--；

```java
public class Solution {
    public boolean canConstruct(String ransomNote, String magazine) {
        if(ransomNote.length() > magazine.length())
            return false;
        int []chars= new int[26];
        for(int i=0; i< magazine.length(); i++){
            chars[magazine.charAt(i)- 'a']++;
        }
        for(int i=0; i< ransomNote.length(); i++){
            chars[ransomNote.charAt(i)- 'a']--;
            if(chars[ransomNote.charAt(i)- 'a'] < 0){
                return false;
            }
        }
        return true;
    }
}
```
AC：18 ms

### Python解法

直接Counter，然后判断前者的每个字符出现次数都小于后者即可。

```python
class Solution:
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        rcount = collections.Counter(ransomNote)
        mcount = collections.Counter(magazine)
        for r, c in rcount.items():
            if c > mcount[r]:
                return False
        return True
```

## 日期

2017 年 1 月 7 日 
2018 年 11 月 14 日 —— 很严重的雾霾

  [1]: https://leetcode.com/problems/ransom-note/
