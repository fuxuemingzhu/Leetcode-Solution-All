
作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)

题目地址：[https://leetcode.com/problems/length-of-last-word/description/][1]


## 题目描述

Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word in the string.

If the last word does not exist, return 0.

Note: A word is defined as a character sequence consists of non-space characters only.

Examle:

input:

    "Hello World"
    "Hello World "
    "Hello W orld"
    "Hello Wo   rld"

output:

    5
    5
    4
    3

## 题目大意

计算一个字符串中，最后一个不为空的单词的长度。

## 解题方法

### 库函数

使用库函数，方法比较简单，一行代码。

```python
class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        return len(s.strip().split(' ')[-1])
                
```

### 双指针

使用两个指针，一个指向最后一个字符串的结尾，一个指向最后一个字符串的开头。

Python代码如下：

```python
class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        N = len(s)
        left, right = 0, N - 1
        while right >= 0 and s[right] == " ":
            right -= 1
        left = right
        while left >= 0 and s[left] != " ":
            left -= 1
        return right - left
```

C++代码如下：

```cpp
class Solution {
public:
    int lengthOfLastWord(string s) {
        int N = s.size();
        int left = 0, right = N - 1;
        while (right >= 0 && s[right] == ' ') right--;
        left = right;
        while (left >= 0 && s[left] != ' ') left--;
        return right - left;
    }
};
```

### 单指针

使用一个指针也可以完成上面的操作。代码比较简单，不解释了。

Python版本如下：

```python
class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        N = len(s)
        count = 0
        for i in range(N - 1, -1, -1):
            if s[i] == " ":
                if count == 0:
                    continue
                else:
                    break
            else:
                count += 1
        return count
```

C++版本如下：

```cpp
class Solution {
public:
    int lengthOfLastWord(string s) {
        int N = s.size();
        int count = 0;
        for (int i = N - 1; i >= 0; --i) {
            if (s[i] == ' ') {
                if (count != 0) {
                    break;
                }
            } else {
                count++;
            }
        }
        return count;
    }
};
```

## 日期

2017 年 8 月 24 日 
2018 年 11 月 24 日 —— 周日开始！一周就过去了～

  [1]: https://leetcode.com/problems/length-of-last-word/description/
