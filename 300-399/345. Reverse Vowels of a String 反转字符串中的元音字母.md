作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)

[LeetCode]

题目地址：[https://leetcode.com/problems/reverse-vowels-of-a-string/](https://leetcode.com/problems/reverse-vowels-of-a-string/)

Total Accepted: 7758 Total Submissions: 22132 Difficulty: Easy


## 题目描述

Write a function that takes a string as input and reverse only the vowels of a string.

Example 1:

	Input: "hello"
	Output: "holle"

Example 2:

	Input: "leetcode"
	Output: "leotcede"

Note:

- The vowels does not include the letter "y".

## 题目大意

把一个字符串中所有的元音字母倒序，其他位置不变。

## 解题方法

### 使用栈

理解题意很重要啊！

这个题的意思是把收尾向中间走的时候遇到的所有元音字符换位置。也就是说 "abecui"-->"ibucea";

把某个东西进行翻转，很容易想到栈。所以把元音字符进栈，再次遍历的时候遇到元音字符就出栈即可。

```python
class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vstack = []
        for c in s:
            if c in "aeiouAEIOU":
                vstack.append(c)
        res = []
        for c in s:
            if c in "aeiouAEIOU":
                res.append(vstack.pop())
            else:
                res.append(c)
        return "".join(res)
```

### 双指针

也就是用双指针的方法。一个从头查找，一个从尾查找。同时判断是否为元音字符，如果两个指针都是落在了元音字符上的时候，交换。别忘了交换位置之后前往下一个地点。

python代码如下：

```python
class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        N = len(s)
        res = list(s)
        left, right = 0, N - 1
        while left < right:
            while right >= 0 and res[right] not in "aeiouAEIOU":
                right -= 1
            while left < right and res[left] not in "aeiouAEIOU":
                left += 1
            if left < right:
                res[left], res[right] = res[right], res[left]
            left += 1
            right -= 1
        return "".join(res)
```

Java代码如下：

```java
public class Solution {
    public String reverseVowels(String s) {
        ArrayList<Character> list=new ArrayList();
        list.add('a');
        list.add('e');
        list.add('i');
        list.add('o');
        list.add('u');
        list.add('A');
        list.add('E');
        list.add('I');
        list.add('O');
        list.add('U');
        
        char[] array=s.toCharArray();
        
        int head=0;
        int tail=array.length-1;
        
        while(head<tail){
            if(!list.contains(array[head])){
                head++;
                continue;
            }
            if(!list.contains(array[tail])){
                tail--;
                continue;
            }
            char temp=array[head];
            array[head]=array[tail];
            array[tail]=temp;
            
            head++;
            tail--;
        }
        
        return new String(array);
    }
}
```
AC:11ms

C++代码如下：

```cpp
class Solution {
public:
    string reverseVowels(string s) {
        const int N = s.size();
        int left = 0, right = N - 1;
        while (left < right) {
            while (left < N && !isVowel(s[left])) left ++;
            while (right >= 0 && !isVowel(s[right])) right --;
            if (left < right)
                swap(s[left], s[right]);
            left ++;
            right --;
        }
        return s;
    }
private:
    bool isVowel(char x) {
        string t = "aeiouAEIOU";
        return t.find(x) != string::npos;
    }
};
```

## 日期

2016/5/1 20:52:19 
2018 年 11 月 21 日 —— 又是一个美好的开始
2018 年 12 月 4 日 —— 周二啦！
