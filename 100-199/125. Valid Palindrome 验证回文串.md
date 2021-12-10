
作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)

题目地址：https://leetcode.com/problems/valid-palindrome/description/


## 题目描述


Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Note: For the purpose of this problem, we define empty string as valid palindrome.

Example 1:

	Input: "A man, a plan, a canal: Panama"
	Output: true

Example 2:

	Input: "race a car"
	Output: false


## 解题方法

### 列表生成式

python 处理起来很简单。isalnum()能判断字符是不是字母数字的，用列表表达式就能产生有效字符串，然后就可以看是不是回文。

```python
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        isValid = lambda x : x == x[::-1]
        string = ''.join([x for x in s.lower() if x.isalnum()])
        return isValid(string)
```

### 正则表达式

二刷的时候使用的正则表达式。然后写了一个判断是不是回文的循环，速度很快。

```python
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.lower()
        s = re.sub("\W", "", s)
        N = len(s)
        left, right = 0, N - 1
        while left <= right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True
```

### 双指针

使用双指针只需要一次遍历即可，如果遇到不是字母或者数字的字符，直接继续向中间走；

如果左右指针都是字母或者数字的话，那么进行判断是否相等，因为需要忽略掉大小写，所以需要统一处理大小写字母的情况。因为小写字母比其对应的大写字母的ASCII码大32，所以如果遇到了大写字母，我们需要先加上32，然后再减去'a'，就知道其相对于'a'的位置了，这个值肯定是小于32的，所以对32取余没啥影响。
如果遇到小写字母，虽然加上了32，但是最后对32取余了，多加的32也就没了，所以还是能得到其相对于'a'的正确位置。


```cpp
class Solution {
public:
    bool isPalindrome(string s) {
        int left = 0, right = s.size();
        while (left <= right) {
            if (!isalnum(s[left])) ++left;
            else if (!isalnum(s[right])) --right;
            else if ((s[left] + 32 - 'a') % 32 != (s[right] + 32 - 'a') % 32) return false;
            else {
                ++left;
                --right;
            }
        }
        return true;
    }
};
```

## 日期

2018 年 2 月 4 日 
2018 年 11 月 27 日 —— 最近的雾霾太可怕
