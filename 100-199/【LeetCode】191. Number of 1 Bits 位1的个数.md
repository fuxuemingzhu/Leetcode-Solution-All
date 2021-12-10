作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)

[LeetCode]

题目地址：[https://leetcode.com/problems/number-of-1-bits/](https://leetcode.com/problems/number-of-1-bits/)

Total Accepted: 88721 Total Submissions: 236174 Difficulty: Easy

## 题目描述


Write a function that takes an unsigned integer and returns the number of ``'1'`` bits it has (also known as the Hamming weight).

Example 1:

	Input: 11
	Output: 3
	Explanation: Integer 11 has binary representation 00000000000000000000000000001011 

Example 2:

	Input: 128
	Output: 1
	Explanation: Integer 128 has binary representation 00000000000000000000000010000000

## 题目大意

统计一个数字的二进制中有多少个1.

## 解题方法

### 右移32次

其实就是不断地右移。判断最后一位总共出现了多少次1.

刚开始没有AC的原因是java是没有无符号整数的，也就是说int的最高位是1的话会认为是负数，所以普通右移并且判断n==0会超时，判断n>0的话直接不运行。

还好java提供了不保持符号位的>>>。
	
	>>是符号位保持不变的右移。
	
用左移的方法好像不用考虑这么多。

本来是想用n%2==1来判断是否最后一位是1的，效率太差，用n&1的方式可以加快最后一位计算时的速率。

```java
public class Solution {
    // you need to treat n as an unsigned value
    public int hammingWeight(int n) {
        int answer=0;
        while(n!=0){
            answer+=n&1;
            n>>>=1;
        }
        return answer;   
    }
}
```

AC:2ms

### 计算末尾的1的个数

LeetCode给出的另一种巧妙解法。

当n&(n-1)!=0时说明n中至少包含一个1.

通过不停的n=n&(n-1)的方法可以将最后的一个1消掉。


![](https://leetcode.com/media/original_images/191_Number_Of_Bits.png)

```java
public int hammingWeight(int n) {
    int sum = 0;
    while (n != 0) {
        sum++;
        n &= (n - 1);
    }
    return sum;
}
```

python代码如下：

```python
class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = 0
        while n:
            res += 1
            n &= n - 1
        return res
```


### 转成二进制统计1的个数

代码如下。

```python
class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        return bin(n).count("1")
```

### 使用mask

和原本的数字移动的方式没有太大区别，只不过用了个变量来看每位是不是1.

```python
class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        mask = 1 << 32
        res = 0
        while mask:
            if n & mask:
                res += 1
            mask >>= 1
        return res
```

## 日期

2016/5/1 14:31:33 
2018 年 11 月 20 日 —— 真是一个好天气
