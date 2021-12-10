作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)

题目地址：https://leetcode.com/problems/reordered-power-of-2/description/

## 题目描述

Starting with a positive integer N, we reorder the digits in any order (including the original order) such that the leading digit is not zero.

Return true if and only if we can do this in a way such that the resulting number is a power of 2.

 

Example 1:

    Input: 1
    Output: true

Example 2:

    Input: 10
    Output: false

Example 3:

    Input: 16
    Output: true

Example 4:

    Input: 24
    Output: false

Example 5:

    Input: 46
    Output: true

Note:

1. 1 <= N <= 10^9

## 题目大意

判断一个数字经过重新组织各个数字的顺序后，能否组成2的幂。

## 解题方法

### 字典统计每位数字出现的次数

最初的想法是通过DFS的方式作组合，但是可能会超时。

想到N只有九位数字，那么在这个范围内的2的幂，应该不多。可以看N和这些2的幂是否拥有相同的数字就好了。使用Counter方法，判断N里的数字和2的幂数字是否相同。


python代码如下：

```python
class Solution(object):
    def reorderedPowerOf2(self, N):
        """
        :type N: int
        :rtype: bool
        """
        c = collections.Counter(str(N))
        return any(c == collections.Counter(str(1 << i)) for i in xrange(32))
```

C++里面的字典由于做了运算符重载，是可以直接进行==或者!=比较的，具体的比较方式是先比较字典的元素个数是否相等，如果相等再依次拿出每一个元素看在第二个字典中是否存在。代码如下：

```cpp
class Solution {
public:
    bool reorderedPowerOf2(int N) {
        unordered_map<char, int> c = count(N);
        for (int i = 0; i < 32; ++i) {
            auto counti = count(1 << i);
            if (counti == c)
                return true;
        }
        return false;
    }
    unordered_map<char, int> count(int N) {
        unordered_map<char, int> c;
        while (N != 0) {
            ++c[N % 10];
            N /= 10;
        }
        return c;
    }
};
```

参考资料：

https://leetcode.com/problems/reordered-power-of-2/discuss/149843/C++JavaPython-Straight-Forward

## 日期

2018 年 9 月 6 日 —— 作息逐渐规律。
2019 年 1 月 26 日 —— 周末加班
