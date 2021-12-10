
- 作者：    负雪明烛
- id：      fuxuemingzhu
- 公众号：负雪明烛
- 本文关键词：LeetCode，力扣，算法，算法题，二进制相加，字符串相加，整数加法，刷题群，Python, C++, Java

---
@[TOC](目录)

题目地址：[https://leetcode.com/problems/add-binary/description/][1]


# 题目描述


Given two binary strings, return their sum (also a binary string).

The input strings are both non-empty and contains only characters 1 or 0.

Example 1:

	Input: a = "11", b = "1"
	Output: "100"

Example 2:

	Input: a = "1010", b = "1011"
	Output: "10101"

# 题目大意

使用字符串表示的二进制数，求他们的和，结果应该也是个字符串。

# 解题方法
大家好，我是 [@负雪明烛](https://leetcode-cn.com/u/fuxuemingzhu/)。写了 1000 多篇题解，欢迎关注。
​

「**求加法**」是个系列题目，类似的题目见文末。

## 解题方法：模拟法

### 十进制加法

我们先回顾一下十进制加法的计算过程，红点表示进位：

![加法.001.jpeg](https://img-blog.csdnimg.cn/img_convert/59673af57b2b7ec310a9642267ac3525.png)


**使用「竖式」计算十进制的加法的方式：**

1. 两个「**加数**」的右端对齐；
1. 从最右侧开始，依次计算对应的两位数字的和。如果和大于等于 10，则把和的个位数字计入结果，并向前面进位。
1. 依次向左计算对应位置两位数字的和，如果有进位需要加上进位。如果和大于等于 10，仍然把和的个位数字计入结果，并向前面进位。
1. 当两个「**加数**」的每个位置都计算完成，如果最后仍有进位，需要把进位数字保留到计算结果中。



### 二进制加法

二进制加法的计算也可以采用类似的方法，与十进制不同的是，**二进制的进位规则是「逢二进一」**，即当求和结果 $>= 2$ 时，需要向前进位。

- 红点表示进位。


![加法.002.jpeg](https://img-blog.csdnimg.cn/img_convert/5384240618fa9fb46c3870123aa8799e.png)



## 代码

### 在代码中需要注意的有：

1. 本题给出的二进制数字是字符串形式，不可以转化成 int 型，因为**可能溢出**；
1. 两个「**加数**」的字符串长度可能不同；
1. 在最后，如果进位 `carry` 不为 0，那么**最后需要计算进位**；
1. 向结果字符串 `res` 拼接的顺序是向后拼接，**返回时需要把** `res` **反转** 。



### 代码中的巧妙之处：

1. `while (i >= 0 || j >= 0 || carry != 0)`含义：
   - 字符串 `a` 和 `b` 只要有一个没遍历完，那么就继续遍历；
   - 如果字符串 `a` 和 `b` 都遍历完了，但是最后留下的进位 `carry != 0`，那么需要把进位也保留到结果中。
2. 取 `digit` 的时候，如果字符串 `a` 和 `b` 中有一个已经遍历完了（即 $i <= 0$ 或者 $j <= 0$），则认为 `a` 和 `b` 的对应位置是 $0$ 。



Java 语言的代码如下，有详细的注释：

```java
class Solution {
    public String addBinary(String a, String b) {
        StringBuilder res = new StringBuilder(); // 返回结果
        int i = a.length() - 1; // 标记遍历到 a 的位置
        int j = b.length() - 1; // 标记遍历到 b 的位置
        int carry = 0; // 进位
        while (i >= 0 || j >= 0 || carry != 0) { // a 没遍历完，或 b 没遍历完，或进位不为 0
            int digitA = i >= 0 ? a.charAt(i) - '0' : 0; // 当前 a 的取值
            int digitB = j >= 0 ? b.charAt(j) - '0' : 0; // 当前 b 的取值
            int sum = digitA + digitB + carry; // 当前位置相加的结果
            carry = sum >= 2 ? 1 : 0; // 是否有进位
            sum = sum >= 2 ? sum - 2 : sum; // 去除进位后留下的数字
            res.append(sum); // 把去除进位后留下的数字拼接到结果中
            i --;  // 遍历到 a 的位置向左移动
            j --;  // 遍历到 b 的位置向左移动
        }
        return res.reverse().toString(); // 把结果反转并返回
    }
}
```

C++ 代码如下：

```cpp
class Solution {
public:
    string addBinary(string a, string b) {
        string res;
        int carry = 0;
        int i = a.size() - 1;
        int j = b.size() - 1;
        while (i >= 0 || j >= 0 || carry != 0) {
            int digitA = i >= 0 ? a[i] - '0' : 0;
            int digitB = j >= 0 ? b[j] - '0' : 0;
            int sum = digitA + digitB + carry;
            carry = sum >= 2 ? 1 : 0;
            sum = sum >= 2 ? sum - 2 : sum;
            res += to_string(sum);
            i --;
            j --;
        }
        reverse(res.begin(), res.end());
        return res;
    }
};
```

Python 代码如下：

```python
class Solution(object):
    def addBinary(self, a, b):
        res = ""
        carry = 0
        i = len(a) - 1
        j = len(b) - 1
        while i >= 0 or j >= 0 or carry != 0:
            digitA = int(a[i]) if i >= 0 else 0
            digitB = int(b[j]) if j >= 0 else 0
            sum = digitA + digitB + carry
            carry = 1 if sum >= 2 else 0
            sum = sum - 2 if sum >= 2 else sum
            res += str(sum)
            i -= 1
            j -= 1
        return res[::-1]
```

**复杂度分析：**

- 时间复杂度：$O(max(M, N))$，$M$ 和 $N$ 分别是字符串 `a` 和 `b` 的长度；
- 空间复杂度：$O(1)$，只使用了常数的空间。



# 类似题目

看完本题解，你可以解决以下题目：

- [2. 两数相加](https://leetcode-cn.com/problems/add-two-numbers/)
- [445. 两数相加 II](https://leetcode-cn.com/problems/add-two-numbers-ii/)
- [67. 二进制求和](https://leetcode-cn.com/problems/add-binary/)
- [415. 字符串相加](https://leetcode-cn.com/problems/add-strings/)
- [66. 加一](https://leetcode-cn.com/problems/plus-one/)
- [989. 数组形式的整数加法](https://leetcode-cn.com/problems/add-to-array-form-of-integer/)



# 总结

1. 「**加法**」系列题目都不难，其实就是 **「列竖式」模拟法**。
1. 需要注意的是 `while`循环结束条件，注意遍历两个「**加数**」不要越界，以及进位。



----

我是 [@负雪明烛](https://leetcode-cn.com/u/fuxuemingzhu/) ，刷算法题 1000 多道，写了 1000 多篇算法题解，收获阅读量 300 万。
**关注我**，你将不会错过我的精彩动画题解、面试题分享、组队刷题活动，进入主页 [@负雪明烛](https://leetcode-cn.com/u/fuxuemingzhu/) 右侧有刷题组织，从此刷题不再孤单。

- 如果你不知道该怎么刷题，可以看 [LeetCode 应该怎么刷？](https://mp.weixin.qq.com/s/viDYrSlF5INEhVWiJhM2EQ)
- 如果你觉得题目太多，想在短时间内快速提高，可以看 [LeetCode 最经典的 100 道题](https://mp.weixin.qq.com/s/e51CEkEP6Wz850JYbgz8dw)。​

# 日期

2017 年 8 月 17 日 
2018 年 11 月 24 日 —— 周六快乐
2021 年 11 月 3 日 —— 把 Leetcode 上所有的加法题目都更新完了

  [1]: https://leetcode.com/problems/add-binary/description/
