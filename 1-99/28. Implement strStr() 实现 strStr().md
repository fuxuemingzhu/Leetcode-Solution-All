
作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)

题目地址：https://leetcode.com/problems/implement-strstr/description/


## 题目描述

Implement strStr().

Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Example 1:
    
    Input: haystack = "hello", needle = "ll"
    Output: 2
    
Example 2:
    
    Input: haystack = "aaaaa", needle = "bba"
    Output: -1

## 题目大意

实现在haystack中找出needle第一次出现的位置，如果不存在，那么就返回-1.

## 解题方法

### find函数

找出一个长串中小串的位置。这样太简单了。。

Python中，find()函数就是实现这个功能，如果找不到子串的话，返回-1.

另外，index()会在找不到的时候报错，这是两个函数的区别。

```python
class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        return haystack.find(needle)
```

### 遍历+切片

这个题这么考就没意思了，自己实现了一下find函数。这里有个需要注意的点，i的变动范围是[0,M-N]闭区间，

时间复杂度是O(M)，空间复杂度是O(1)。超过96%.

```python3
class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        M, N = len(haystack), len(needle)
        for i in range(M - N + 1):
            if haystack[i : i + N] == needle:
                return i
        return -1
```

C++写法：

要注意的是string的substr方法第一个参数是起始位置，第二个参数是切片长度。

```cpp
class Solution {
public:
    int strStr(string haystack, string needle) {
        int M = haystack.size();
        int N = needle.size();
        for (int i = 0; i < M - N + 1; i ++){
            if (haystack.substr(i, N) == needle){
                return i;
            }
        }
        return -1;
    }
};
```

## 日期

2018 年 2 月 4 日 
2018 年 11 月 3 日 —— 雾霾的周六
2018 年 11 月 26 日 —— 11月最后一周！
