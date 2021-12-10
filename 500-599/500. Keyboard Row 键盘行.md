
作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)

题目地址：[https://leetcode.com/problems/keyboard-row/#/description][1]


## 题目描述

Given a List of words, return the words that can be typed using letters of alphabet on only one row's of American keyboard like the image below.
![此处输入图片的描述][2]

Example :

	Input: ["Hello", "Alaska", "Dad", "Peace"]
	Output: ["Alaska", "Dad"]

## 题目大意

判断那些字符串能使用键盘中的其中一行就能全部拼出来。

## 解题方法

### 暴力解

暴力解决了。分别把三行弄在三个数组里，对于每个单词每个字母都去循环，数在三行中的个数分别多少。如果这个单词能在一张中打出来完，那么说明由某一行的个数为1，其他行都为0.

注意字符串数组的写法。

```java
public class Solution {
    public String[] findWords(String[] words) {
        char []arr1 = new char[]{'q','w','e','r','t','y','u','i','o','p','Q','W','E','R','T','Y','U','I','O','P'};
        char []arr2 = new char[]{'a','s','d','f','g','h','j','k','l','A','S','D','F','G','H','J','K','L'};
        char []arr3 = new char[]{'z','x','c','v','b','n','m','Z','X','C','V','B','N','M'};
        List<String> ans = new ArrayList<String>();
        for(String word: words){
            int count1 = 0, count2 = 0, count3 = 0;
            for(int i =0; i < word.length(); i++){
                for(int j =0; j < arr1.length; j++){
                    if(word.charAt(i) == arr1[j]){
                        count1++;
                    }
                }
                for(int j =0; j < arr2.length; j++){
                    if(word.charAt(i) == arr2[j]){
                        count2++;
                    }
                }
                for(int j =0; j < arr3.length; j++){
                    if(word.charAt(i) == arr3[j]){
                        count3++;
                    }
                }
            }
            if((count1 != 0 && count2 == 0 && count3 == 0)
                ||(count1 == 0 && count2 != 0 && count3 == 0)
                ||(count1 == 0 && count2 == 0 && count3 != 0)){
                    ans.add(word);
            }
        }
        String []answer = new String[ans.size()];
        for(int i =0; i < ans.size(); i ++){
            answer[i] = ans.get(i);
        }
        return answer;
    }
}
```

### 字典 + set

二刷，Python。

使用字典来保存字符串在哪一行，然后遍历每个字符串，看它所有的字符在哪几行，用set对行数去重，如果set的结果是1，说明可以使用一行就求解出来。

```python
class Solution:
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        rowdict = {}
        for c in "qwertyuiopQWERTYUIOP":
            rowdict[c] = 1
        for c in "asdfghjklASDFGHJKL":
            rowdict[c] = 2
        for c in "zxcvbnmZXCVBNM":
            rowdict[c] = 3
        res = []
        for word in words:
            if len(set(rowdict[c] for c in word)) == 1:
                res.append(word)
        return res
```


## 日期

2017 年 4 月 2 日 
2018 年 11 月 6 日 —— 腰酸背痛要废了

  [1]: https://leetcode.com/problems/keyboard-row/#/description
  [2]: https://leetcode.com/static/images/problemset/keyboard.png
