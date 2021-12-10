
作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---

@[TOC](目录)

题目地址：https://leetcode.com/problems/multiply-strings/description/

## 题目描述

Given two non-negative integers ``num1`` and ``num2`` represented as strings, return the product of num1 and num2, also represented as a string.

Example 1:

    Input: num1 = "2", num2 = "3"
    Output: "6"

Example 2:

    Input: num1 = "123", num2 = "456"
    Output: "56088"

Note:

1. The length of both num1 and num2 is < 110.
1. Both num1 and num2 contain only digits 0-9.
1. Both num1 and num2 do not contain any leading zero, except the number 0 itself.
1. You **must not use any built-in BigInteger library or convert the inputs to integer directly**.

## 题目大意

实现字符串表示的数字乘法。

## 解题方法

先抖个机灵：

```python
class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        return str(int(num1) * int(num2))
```

上面的能过，下面正经点。

此题是让我们模拟乘法，所以计算方法也就是模拟了小学数学的列竖式。从末尾数字开始计算乘积，注意进位，先得到num2中每个数字与num1的乘积，再通过10的多少次方的形式代表其位数。啊，描述起来太难了，可以想想竖式怎么列的。

另外，这个题用python这么做是不合理的，因为Python的int可以无限大的，所以没有真正实现了大数乘法。


```python
class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if num1 == '0' or num2 == '0':
            return '0'
        ans = 0
        for i, n1 in enumerate(num2[::-1]):
            pre = 0
            curr = 0
            for j, n2 in enumerate(num1[::-1]):
                multi = (ord(n1) - ord('0')) * (ord(n2) - ord('0'))
                first, second = multi // 10, multi % 10
                curr += (second + pre) * (10 ** j) 
                pre = first
            curr += pre * (10 ** len(num1))
            ans += curr * (10 ** i)
        return str(ans)
```

根据[JustDoIT](http://www.cnblogs.com/TenosDoIt/p/3735309.html)的做法，首先我们把每一位相乘，得到一个没有进位的临时结果，如图中中间的一行红色数字就是临时结果，然后把临时结果从低位起依次进位。对于一个m位整数乘以n位整数的结果，最多只有m+n位。

![在这里插入图片描述](https://images0.cnblogs.com/blog/517264/201405/181618228901716.png)

C++代码如下：

```cpp
class Solution {
public:
    string multiply(string num1, string num2) {
        const int M = num1.size();
        const int N = num2.size();
        const int k = M + N - 2;
        vector<int> res(M + N, 0);
        for (int i = 0; i < M; ++i) {
            for (int j = 0; j < N; ++j) {
                res[k - i - j] += (num1[i] - '0') * (num2[j] - '0');
            }
        }
        int carry = 0;
        for (int i = 0; i < res.size(); ++i) {
            res[i] += carry;
            carry = res[i] / 10;
            res[i] %= 10;
        }
        int start = res.size() - 1;
        while (start >= 0 && res[start] == 0)
            --start;
        if (start < 0) return "0";
        string ans;
        while (start >= 0) {
            ans += char(res[start] + '0');
            --start;
        }
        return ans;
    }
};
```

## 日期

2018 年 6 月 13 日 —— 腾讯赛圆满结束！两个月修得正果哈哈～～
2019 年 3 月 3 日 —— 3月开始，春天到了

  [1]: http://bookshadow.com/weblog/2017/09/17/leetcode-valid-parenthesis-string/
