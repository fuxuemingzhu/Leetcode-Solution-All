
作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)

题目地址：[https://leetcode.com/problems/word-pattern/#/description][1]


## 题目描述

Given a pattern and a string str, find if str follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in str.

Examples:

    pattern = "abba", str = "dog cat cat dog" should return true.
    pattern = "abba", str = "dog cat cat fish" should return false.
    pattern = "aaaa", str = "dog cat cat dog" should return false.
    pattern = "abba", str = "dog dog dog dog" should return false.

Notes:

- You may assume pattern contains only lowercase letters, and str contains lowercase letters separated by a single space.

## 题目大意

看模式和空格分割的字符串模式能不能构成一一映射。

## 解题方法

这个题第一感觉就是使用HashMap，看到Tags也是HashMap我就放心了。想法基本就是把字符和单词对应起来，看单词和字符能不能对应上，这样就知道模式是否匹配了。做的时候出现了一个小问题，就是``pattern = "abba", str = "dog dog dog dog"``这种，要判断是不是已经放进了value，之前不知道怎么办，今天学到了HashMap有个containsValue()方法，可以判断是否已经放进了value。

```java
public class Solution {
    public boolean wordPattern(String pattern, String str) {
        HashMap<Character, String> map = new HashMap<Character, String>();
        String[] words = str.split(" ");
        if(words.length != pattern.length()){
            return false;
        }
        for(int i = 0; i < words.length; i++){
            String word = words[i];
            char temp = pattern.charAt(i);
            if(map.containsKey(temp)){
                if(!map.get(temp).equals(word)){
                    return false;
                }
            }else{
                if(map.containsValue(word)){
                    return false;
                }
                map.put(temp, word);
            }
        }
        return true;
    }
}
```

---

二刷，使用Python解法，这个题和[205. Isomorphic Strings](https://blog.csdn.net/fuxuemingzhu/article/details/72127108)一模一样，所以很快就写出来这个一一映射的代码：

```python
class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        strs = str.split()
        if len(pattern) != len(strs):
            return False
        d = dict()
        for i, p in enumerate(pattern):
            if p not in d:
                d[p] = strs[i]
            else:
                if d[p] != strs[i]:
                    return False
        d = dict()
        for i, p in enumerate(strs):
            if p not in d:
                d[p] = pattern[i]
            else:
                if d[p] != pattern[i]:
                    return False
        return True
```

## 日期

2017 年 5 月 19 日 
2018 年 11 月 24 日 —— 周六快乐

  [1]: https://leetcode.com/problems/word-pattern/#/description
