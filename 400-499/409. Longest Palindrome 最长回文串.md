
作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)

[LeetCode]

题目地址：[https://leetcode.com/problems/longest-palindrome/][1]

 - Difficulty: Easy

## 题目描述

Given a string which consists of lowercase or uppercase letters, find the length of the longest palindromes that can be built with those letters.

This is case sensitive, for example "Aa" is not considered a palindrome here.

Note:

Assume the length of given string will not exceed 1,010.

Example:

    Input:
    "abccccdd"
    
    Output:
    7
    
    Explanation:
    One longest palindrome that can be built is "dccaccd", whose length is 7.

## 题目大意

判断一个字符串能够成的最长的回文字符串长度是多少。

## 解题方法

### 方法一：字典统计次数

题目的意思是找出字符串能够成的最长的回文字符串的长度。

思路是需要找出规律：
1. 先加上所有能够成偶数次的字符串次数：
	-  如果一个字符出现了偶数次，那么一定可以是最终回文字符串的一部分，加上该字符出现的次数；
	-  如果一个字符出现了奇数v次，那么可以加上v-1次（只使用偶数次这个字符）；
2. 如果有出现过奇数次的字符，那么最后结果+1，代表把该奇数字符放在中间。

Python解法：

```python
class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = collections.Counter(s)
        res = 0
        prime = 0
        for k, v in count.items():
            if v % 2 == 1:
                res += v - 1
                prime = 1
            else:
                res += v
        return res + prime
```

C++代码如下：

```cpp
class Solution {
public:
    int longestPalindrome(string s) {
        unordered_map<char, int> count;
        for (char c : s)
            ++count[c];
        int res = 0;
        bool hasOne = false;
        for (auto d : count) {
            if (d.second % 2 == 0)
                res += d.second;
            else {
                res += d.second - 1;
                hasOne = true;
            }
        }
        if (hasOne)
            ++res;
        return res;
    }
};
```

### 方法二：HashSet

看了高票的答案，可以HashSet的方法，统计一个字符是否出现了偶数次，一增一减相抵消，这样的个数*2，如果HashSet中还有元素再加上1即可。

Java代码如下：

```java
public class Solution {
    public int longestPalindrome(String s) {
        HashSet<Character> hashset=new HashSet<Character>();
        int count=0;
        for(int i =0; i< s.length(); i++){
            if(hashset.contains(s.charAt(i))){
                hashset.remove(s.charAt(i));
                count++;
            }else{
                hashset.add(s.charAt(i));
            }
        }
        if(!hashset.isEmpty()) return count*2 +1;
        return count*2;
    }
}
```
AC: 23 ms

虽然只遍历了一遍，但是用到了HashSet,因此效率没我的高。

### 方法三：次数除以2再乘以2

用两个int[26]，分别保存大小写字符，统计字符出现的对数，最后判断这些字符对数相加是否等于原字符的长度，如果不等说明有奇数的出现，在/2的时候被舍去了。方法思想挺巧妙的。

Java代码如下：

```java
public int longestPalindrome(String s) {
    int[] lowercase = new int[26];
    int[] uppercase = new int[26];
    int res = 0;
    for (int i = 0; i < s.length(); i++){
        char temp = s.charAt(i);
        if (temp >= 97) lowercase[temp-'a']++;
        else uppercase[temp-'A']++;
    }
    for (int i = 0; i < 26; i++){
        res+=(lowercase[i]/2)*2;
        res+=(uppercase[i]/2)*2;
    }
    return res == s.length() ? res : res+1;
        
}
```

## 日期

2017 年 1 月 8 日 
2018 年 11 月 16 日 —— 又到周五了！
2019 年 2 月 18 日 —— 继续学习～
2020 年 3 月 19 日 —— 恰巧每年都做一遍这个题

  [1]: https://leetcode.com/problems/longest-palindrome/
