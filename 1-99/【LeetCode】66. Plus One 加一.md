
- 作者： 负雪明烛
- id：	fuxuemingzhu
- 个人博客：	http://fuxuemingzhu.cn/
- 公众号：负雪明烛
- 本文关键词：Leetcode, 力扣，加法，两数之和，求加法，数组，Python, C++, Java

---
@[TOC](目录)

[LeetCode]

题目地址：[https://leetcode.com/problems/plus-one/][1]

Total Accepted: 99274 Total Submissions: 294302 Difficulty: Easy


# 题目描述

Given a **non-empty** array of digits representing a non-negative integer, plus one to the integer.

The digits are stored such that the most significant digit is at the head of the list, and each element in the array contain a single digit.

You may assume the integer does not contain any leading zero, except the number 0 itself.

Example 1:

	Input: [1,2,3]
	Output: [1,2,4]
	Explanation: The array represents the integer 123.

Example 2:

	Input: [4,3,2,1]
	Output: [4,3,2,2]
	Explanation: The array represents the integer 4321.

# 题目大意

给出了一个数组表示的十进制数字，数组的每个位置都是单个数字，现在要把这个十进制数字+1，求结果数组。

# 解题方法

「**求加法**」是个系列题目，相关题目见文末。

## 数九

就是把一个数组表示的整数+1，看起来非常简单的一个题目。但是据说是Google最喜欢的面试题。

想法是从最后一位开始看，如果这位是9的话转为0，不是的话就+1，再往前面看，直到不是9为止。

运算结束之后，如果最高位为0，说明这个数所有的位数都为9，那么需要创建新数组，把最高位置为一。

这个想法的确实是一个加法最基本的想法。说明我们需要从最常见的事物中找到准确表达的算法。

```java
public class Solution {
    public int[] plusOne(int[] digits) {
        for(int i=digits.length-1; i>=0; i--){
            if(digits[i]==9){
                digits[i]=0;
                continue;
            }else{
                digits[i]+=1;
                break;
            }
        }
        
        if(digits[0]==0){
          int[] answer=new int[digits.length + 1];
            answer[0]=1;
            return answer;
        }else{
            return digits;
        }
    }
}
```

AC:0ms

## 采用进位
### 十进制加法

我们先回顾一下用「竖式」计算十进制加法的过程：

![加法.001.jpeg](https://img-blog.csdnimg.cn/img_convert/a149529af80add8a261a4321784740c1.png)



**使用「竖式」计算十进制的加法的方式：**

1. 两个「**加数**」的右端对齐；
1. 从最右侧开始，依次计算对应的两位数字的和。如果和大于等于 10，则把和的个位数字计入结果，并向前面进位。
1. 依次向左计算对应位置两位数字的和，如果有进位需要加上进位。如果和大于等于 10，仍然把和的个位数字计入结果，并向前面进位。
1. 当两个「**加数**」的每个位置都计算完成，如果最后仍有进位，需要把进位数字保留到计算结果中。

### 本题解法


本题给出的数字是 `digits` 以列表形式给出每一位数字，让我们对 `digits` 加一。
​

其实就是模拟十进制加法的过程：**两个加数分别是 `digits` 和 $1$ 。**
​

直接按照上面的十进制加法的模拟思路进行计算就可以，可以套用「[2. 两数相加，详解「求加法」：循环与递归](https://leetcode-cn.com/problems/add-two-numbers/solution/fu-xue-ming-zhu-xiang-jie-qiu-jia-fa-xun-6bah/)」 的代码模板，把第二个加数置为 $1$ 即可。
​

### 在实现中需要注意的有：

1. 不可以把 `digits` 先转化成 int 型数字再求和，因为**可能溢出**；
1. 另一个「加数」是 `adder` ，初始化为 $1$ ，以后都是 $0$；
1. 两个「**加数**」的长度可能不同；
1. 在最后，如果进位 `carry` 不为 0，那么**最后需要计算进位**；



### 方法：循环


循环的思想比较朴素，就是倒序遍历 `digits` 的每个元素，与另一个加数 `adder` 和 进位 `carry`相加的过程。
​

#### 代码中的巧妙之处：

1. `while (p1 >= 0 || adder > 0 || carry > 0)`含义：
   1. `digits` 和 `adder` 只要有一个没遍历完，那么就继续遍历；
   1. 如果字符串 `digits` 和 `adder` 都遍历完了，但是最后留下的进位 `carry != 0`，那么需要把进位也保留到结果中。
2. 取当前位置的数字的时候，如果 `digits` 已经遍历完了（即 $p1 <= 0$），则认为 `digits` 的对应位置是 $0$ 。



​

Java 语言的代码如下：

```java
class Solution {
    public int[] plusOne(int[] digits) {
        int N = digits.length;
        List<Integer> resultList = new ArrayList<>();
        int p1 = N - 1;
        int carry = 0;
        int adder = 1;
        while (p1 >= 0 || adder > 0 || carry > 0) {
            int num = p1 >= 0 ? digits[p1] : 0;
            int sum = num + adder + carry;
            carry = sum >= 10 ? 1 : 0;
            sum = sum >= 10 ? sum - 10 : sum;
            resultList.add(sum);
            p1 --;
            adder = 0;
        }
        int[] res = new int[resultList.size()];
        for (int i = 0; i < resultList.size(); ++i) {
            res[i] = resultList.get(resultList.size() - i - 1);
        }
        return res;
    }
}
```

C++ 代码如下：

```cpp
class Solution {
public:
    vector<int> plusOne(vector<int>& digits) {
        const int N = digits.size();
        vector<int> res;
        int p1 = N - 1;
        int carry = 0;
        int adder = 1;
        while (p1 >= 0 || adder > 0 || carry > 0) {
            int num = p1 >= 0 ? digits[p1] : 0;
            int sum = num + adder + carry;
            carry = sum >= 10 ? 1 : 0;
            sum = sum >= 10 ? sum - 10 : sum;
            res.push_back(sum);
            p1 --;
            adder = 0;
        }
        reverse(res.begin(), res.end());
        return res;
    }
};
```

Python 代码如下：

```python
class Solution(object):
    def plusOne(self, digits):
        N = len(digits)
        res = []
        adder = 1
        carry = 0
        p1 = N - 1
        while p1 >= 0 or adder > 0 or carry > 0:
            num = digits[p1] if p1 >= 0 else 0
            sum = num + adder + carry
            carry = 1 if sum >= 10 else 0
            sum = sum - 10 if sum >= 10 else sum
            res.append(sum)
            p1 -= 1
            adder = 0
        return res[::-1]
```

**复杂度分析：**

- 时间复杂度：$O(max(N))$，$N$ 是 `digits`的长度；
- 空间复杂度：$O(1)$，只使用了常数的空间。

​

## 类似题目
看完本题解本题，你可以解决以下题目：

- [2. 两数相加](https://leetcode-cn.com/problems/add-two-numbers/)
- [445. 两数相加 II](https://leetcode-cn.com/problems/add-two-numbers-ii/)
- [67. 二进制求和](https://leetcode-cn.com/problems/add-binary/)
- [415. 字符串相加](https://leetcode-cn.com/problems/add-strings/)
- [989. 数组形式的整数加法](https://leetcode-cn.com/problems/add-to-array-form-of-integer/)

​

## 总结

1. 「**加法**」系列题目都不难，其实就是 **「列竖式」模拟法** 。
1. 需要注意的是 `while`循环结束条件，注意遍历两个「加数」不要越界，以及考虑进位。

​

# 日期

2016 年 05月 8日 
2018 年 11 月 21 日 —— 又是一个美好的开始
2021 年 11 月 3 日 —— 持续学习！

  [1]: https://leetcode.com/problems/plus-one/
