作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/
公众号：负雪明烛
本文关键词：Leetcode, 力扣，字符串相加，两数相加，两数之和，求加法，代码模板，Python, C++, Java

---
@[TOC](目录)

题目地址：[https://leetcode-cn.com/problems/add-strings][1]



# 题目描述

给定两个字符串形式的非负整数 `num1` 和 `num2` ，计算它们的和并同样以字符串形式返回。

你不能使用任何內建的用于处理大整数的库（比如 `BigInteger` ）， 也不能直接将输入的字符串转换为整数形式。

 

示例 1：

	输入：num1 = "11", num2 = "123"
	输出："134"

示例 2：

	输入：num1 = "456", num2 = "77"
	输出："533"

示例 3：

	输入：num1 = "0", num2 = "0"
	输出："0"
 
提示：

1. `1 <= num1.length, num2.length <= 10^4`
2. `num1` 和 `num2` 都只包含数字 `0-9`
3. `num1` 和 `num2` 都不包含任何前导零

# 题目大意

不使用大整数的情况下，计算两个字符串表示的数字的和。

# 解题方法

## 前言
**加法**是我们上小学的时候开始学习的第一种数学运算。

在算法题中，「求加法」问题大多考察「**列竖式**」求和。

题目中，「两数之和」通常与其他形式表示的数字结合起来：

- **两个字符串形式的数字相加（第 415 题）**
- **两个链表形式的数字相加（第 2 、445、369 题）**
- **数组形式的数字相加（第 66 、989题）**
- **两个二进制形式的数字相加（第 67 题）**

做法都是非常类似的，本质是在考察各种数据表示形式：**字符串，链表，数组，二进制**。

我们只要掌握了用「列竖式」求「两数之和」的方法，这类题目全都可以秒杀。

## 十进制加法

我们先回顾一下十进制加法的计算过程：

![加法.001.jpeg](https://img-blog.csdnimg.cn/img_convert/fcdcfb61c1c6d9d7825660b163cc8445.png)


**使用「竖式」计算十进制的加法的方式：**

1. 两个「**加数**」的右端对齐；
1. 从最右侧开始，从右向左依次计算对应的两位数字的和，如果有进位需要加上进位。如果和大于等于 10，则把和的个位数字计入结果，并向前面进位；
1. 重复步骤 2；
1. 当两个「**加数**」的每个位置都计算完成，如果最后仍有进位，需要把进位数字保留到计算结果中。

### 在实现中需要注意的有：

1. 不可以把字符串表示的「加数」先转化成 `int` 型数字再求和，因为**可能溢出**；
2. 两个「**加数**」的字符串长度可能不同；
3. 在最后，如果进位 carry 不为 0，那么**最后需要计算进位**。
4. 注意 结果数字 是否为低位结果在前，根据题目要求判断最后**是否要反转结果**。

## 详细代码
题目要我们求两个字符串形式表示的数字相加，按照「列竖式」的方法进行求解即可。


### 代码说明


1. `while (p1 >= 0 || p2 >= 0 || carry != 0)`含义： 
   1. 字符串 `num1` 和 `num2` 只要有一个没遍历完，那么就继续遍历；
   1. 如果字符串 `num1` 和 `num2` 都遍历完了，但是最后留下的进位 `carry != 0`，那么需要把进位也保留到结果中。
2. 取 `digit` 的时候，如果字符串 `num1` 和 `num2` 中有一个已经遍历完了（即 $p1 < 0$ 或者 $p2< 0$），则认为 `num1` 和 `num2` 的对应位置是 $0$。



### 代码


**该代码可以作为「求加法」的模板。**


Java 语言代码如下：

```java
class Solution {
    public String addStrings(String num1, String num2) {
        StringBuilder res = new StringBuilder(); // 返回结果
        int p1 = num1.length() - 1; // 标记遍历到 num1 的位置
        int p2 = num2.length() - 1; // 标记遍历到 num2 的位置
        int carry = 0; // 进位
        while (p1 >= 0 || p2 >= 0 || carry != 0) { // num1 没遍历完，或 num2 没遍历完，或进位不为 0
            int digit1 = p1 >= 0 ? num1.charAt(p1) - '0' : 0; // 当前 num1 的取值
            int digit2 = p2 >= 0 ? num2.charAt(p2) - '0' : 0; // 当前 num2 的取值
            int add = digit1 + digit2 + carry; // 当前位置相加的结果
            carry = add >= 10 ? 1 : 0; // 是否有进位
            add = add >= 10 ? add - 10 : add; // 去除进位后留下的数字
            res.append(add); // 把去除进位后留下的数字拼接到结果中
            p1 --; // 遍历到 num1 的位置向左移动
            p2 --; // 遍历到 num2 的位置向左移动
        }
        return res.reverse().toString(); // 把结果反转并返回
    }
}
```

C++ 代码如下：

```cpp
class Solution {
public:
    string addStrings(string num1, string num2) {
        const int M = num1.size();
        const int N = num2.size();
        string res;
        int p1 = M - 1;
        int p2 = N - 1;
        int carry = 0;
        while (p1 >= 0 || p2 >= 0 || carry > 0) {
            int cur1 = p1 >= 0 ? num1[p1] - '0' : 0;
            int cur2 = p2 >= 0 ? num2[p2] - '0' : 0;
            int sum = cur1 + cur2 + carry;
            carry = sum >= 10 ? 1 : 0;
            sum = sum >= 10 ? sum - 10 : sum;
            res += to_string(sum);
            p1 --;
            p2 --;
        }
        reverse(res.begin(), res.end());
        return res;
    }
};
```

Python 代码如下：

```python
class Solution(object):
    def addStrings(self, num1, num2):
        p1 = len(num1) - 1
        p2 = len(num2) - 1
        res = ""
        carry = 0
        while p1 >= 0 or p2 >= 0 or carry > 0:
            digit1 = int(num1[p1]) if p1 >= 0 else 0
            digit2 = int(num2[p2]) if p2 >= 0 else 0
            sum = digit1 + digit2 + carry
            carry = 1 if sum >= 10 else 0
            sum = sum - 10 if sum >= 10 else sum
            res += str(sum)
            p1 -= 1
            p2 -= 1
        return res[::-1]
```
### 复杂度分析


- 时间复杂度：$O(max(M, N))$，$M$ 和 $N$ 分别是字符串 `num1` 和 `num2` 的长度；
- 空间复杂度：$O(1)$，只使用了常数的空间。


# 类似题目
看完本文，你可以解决以下题目：

- [415. 字符串相加](https://leetcode-cn.com/problems/add-strings/)
- [2. 两数相加](https://leetcode-cn.com/problems/add-two-numbers/)
- [445. 两数相加 II](https://leetcode-cn.com/problems/add-two-numbers-ii/)
- [369. 给单链表加一](https://leetcode-cn.com/problems/plus-one-linked-list/)
- [66. 加一](https://leetcode-cn.com/problems/plus-one/)
- [989. 数组形式的整数加法](https://leetcode-cn.com/problems/add-to-array-form-of-integer/)
- [67. 二进制求和](https://leetcode-cn.com/problems/add-binary/)
# 总结

1. 「**求加法**」系列题目都不难，其实就是 **「列竖式」** 计算。
1. 需要注意的是：
   1. while循环结束条件；
   1. 遍历两个「加数」不要越界；
   1. 进位。
   1. 最后的结果需要翻转



# 日期

2017 年 1 月 12 日 
2018 年 11 月 19 日 —— 周一又开始了
2021 年 11 月 1 日 —— 把求加法的题目一次性更新完

  [1]: https://leetcode-cn.com/problems/add-strings
