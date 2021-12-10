
作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)

题目地址：https://leetcode.com/problems/reverse-bits/description/


## 题目描述


Reverse bits of a given 32 bits unsigned integer.

Example:

	Input: 43261596
	Output: 964176192
	Explanation: 43261596 represented in binary as 00000010100101000001111010011100, 
	             return 964176192 represented in binary as 00111001011110000010100101000000.

Follow up:

1. If this function is called many times, how would you optimize it?

## 解题方法

### 二进制字符串翻转

python真的好。bin()能求出二进制表示，ine(str,2)能把二进制转十进制表示。注意这个题目里面一定要是32位的二进制表示才行，因此一定要进行补全。

```python
class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        bins = bin(n)[2:][::-1]
        rev = (bins + '0' * (32 - len(bins)))
        return int(rev, 2)
```

### 位运算

二刷使用C++，进行位运算。每次看n的末尾数字是多少，然后拼接到res的最前面。这样循环32次，则把n的所有数字进行了逆序操作。

```cpp
class Solution {
public:
    uint32_t reverseBits(uint32_t n) {
        uint32_t res = 0;
        for (int i = 0; i < 32; ++i) {
            res = (res << 1) + (n & 1);
            n >>= 1;
        }
        return res;
    }
};
```

## 日期

2018 年 2 月 4 日 
2018 年 11 月 27 日 —— 最近的雾霾太可怕
