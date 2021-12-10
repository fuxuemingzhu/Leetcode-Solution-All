作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)

[LeetCode]

题目地址：[https://leetcode.com/problems/excel-sheet-column-title/](https://leetcode.com/problems/excel-sheet-column-title/)

Total Accepted: 59514 Total Submissions: 274188 Difficulty: Easy


## 题目描述

Given a positive integer, return its corresponding column title as appear in an Excel sheet.

For example:

    1 -> A
    2 -> B
    3 -> C
    ...
    26 -> Z
    27 -> AA
    28 -> AB 
    ...

Example 1:

	Input: 1
	Output: "A"

Example 2:

	Input: 28
	Output: "AB"

Example 3:

	Input: 701
	Output: "ZY"

## 题目大意

### 迭代

和之前的罗马数很像嘛！

转换数字然后往右移位。主要问题是26这个数字和0效果上是一样的，除以26都是剩余0，我做了单独讨论。第二，中间用到了字符强转和重新构造字符串。这些都比较耗时。

Java解法如下：

```java
public class Solution {
    public String convertToTitle(int n) {
        String answer="";
        while( n > 0){
            int temp= n % 26;
            if(temp==0){
                answer="Z" + answer;
                n=n/26-1;
            }else{
                answer=new String(Character.toChars('A'+temp-1)) + answer;
                n/=26;
            }
        }
        return answer;
    }
}
```
AC:0ms

Python解法如下：

```python
class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n == 1: return 'A'
        res = ""
        while n:
            if n % 26 == 0:
                res = "Z" + res
                n -= 26
            else:
                res = chr(ord('A') - 1 + n % 26) + res
                n -= n % 26
            n /= 26
        return res
```

C++代码如下，主要思路是一样的，但是不能直接使用char + string， 但是string + char是可以的。因为string作为一个类，重载了operator+(char)方法，但是char是原始数据类型，他没有重载operator+(string)方法。

所以最后需要reverse。

```cpp
class Solution {
public:
    string convertToTitle(int n) {
        string res;
        while (n != 0) {
            if (n % 26 == 0) {
                res += "Z";
                n -= 26;
            } else {
                res += (n % 26) - 1 + 'A';
                n -= n % 26;
            }
            n /= 26;
        }
        reverse(res.begin(), res.end());
        return res;
    }
};
```


### 递归

感觉自己方法不够好，看到了九章算术这个方法，我认为很好。n-1的效果是算法上每个循环都是从0--25，这样使程序对齐，简化了运算。

```java
public class Solution {
    public String convertToTitle(int n) {
        if (n == 0) {
            return "";
        }
        return convertToTitle((n - 1) / 26) + (char)((n - 1) % 26 + 'A');
    }
}
```
AC:0ms

## 日期

2016/4/30 16:20:51 
2018 年 11 月 28 日 —— 听说楼下有传染病。。
