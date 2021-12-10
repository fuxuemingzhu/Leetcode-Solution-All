
作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)

题目地址：[https://leetcode.com/problems/detect-capital/#/description][1]


## 题目描述

Given a word, you need to judge whether the usage of capitals in it is right or not.

We define the usage of capitals in a word to be right when one of the following cases holds:

1. All letters in this word are capitals, like "USA".
2. All letters in this word are not capitals, like "leetcode".
3. Only the first letter in this word is capital if it has more than one letter, like "Google".

Otherwise, we define that this word doesn't use capitals in a right way.

Example :

    Input: "USA"
    Output: True
    
    Input: "FlaG"
    Output: False

## 题目大意

判断一个字符串是否满足大写规则：全部大写，开头大写后面小写，全部小写。

## 解题方法

### 循环判断三个条件

往往简单的方法就最有效。这个题说了有三种情况，那我就判断三种情况，如果有一个情况满足就可以。在判断是否满足全大写的时候，如果有一个字母是小写，那么就判断为false，然后break；就好了。就这样判断了三次，最后如果有一个是true，即可返回是。

这样的一个缺点就是如果已经判断是全大写，还要判断其他的，当然可以写if语句判断，但是我感觉有点啰嗦，还不如直接三个情况都判断简单。

```java
public class Solution {
    public boolean detectCapitalUse(String word) {
        if(word == null || word.length() == 0){
            return false;
        }
        int len = word.length();
        boolean isUpper = true;//全大写
        boolean isLower = true;//全小写
        boolean isFirst = true;//首字母大写
        for(int i = 0; i < len; i++){
            if(word.charAt(i) >= 'a' && word.charAt(i) <= 'z'){
                isUpper = false;
                break;
            }
        }
        for(int i =0; i < len; i++){
            if(word.charAt(i) >= 'A' && word.charAt(i) <= 'Z'){
                isLower = false;
                break;
            }
        }
        if(word.charAt(0) >= 'a' && word.charAt(0) <= 'z'){
            isFirst = false;
        }
        for(int i = 1; i < len; i++){
            if(word.charAt(i) >= 'A' && word.charAt(i) <= 'Z'){
                isFirst = false;
                break;
            }
        }
        return isLower || isUpper || isFirst;
    }
}
```

### 大写字母个数和位置判断

看到了别人的更简洁的做法，统计大写字母的个数，有0个或者全是大写，或者只有一个大写并且在首位。

Java版本：

```java
public class Solution {
    public boolean detectCapitalUse(String word) {
        int cnt = 0;
        for(char c: word.toCharArray()) if('Z' - c >= 0) cnt++;
        return ((cnt==0 || cnt==word.length()) || (cnt==1 && 'Z' - word.charAt(0)>=0));
    }
}
```

python版本：

```python
class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        count = 0
        for i, w in enumerate(word):
            if w.isupper():
                count += 1
        return count == len(word) or count == 0 or (word[0].isupper() and count == 1)
```



### 根据首字符判断

如果首字符是大写，那么后面可以全部小写或者全部小写。
如果首字符是小写，那么后面只能全部小写。

python版本：

```python
class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        if word[0].isupper():
            return all(map(lambda w : w.isupper(), word[1:])) or all(map(lambda w : w.islower(), word[1:]))
        else:
            return all(map(lambda w : w.islower(), word[1:]))
```

## 日期

2017 年 4 月 3 日 
2018 年 11 月 10 日 —— 这么快就到双十一了？？

  [1]: https://leetcode.com/problems/detect-capital/#/description
