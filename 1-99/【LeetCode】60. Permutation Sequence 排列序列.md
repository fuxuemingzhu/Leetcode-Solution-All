
作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)

题目地址：https://leetcode.com/problems/permutation-sequence/description/

## 题目描述

The set ``[1,2,3,...,n]`` contains a total of n! unique permutations.

By listing and labeling all of the permutations in order, we get the following sequence for n = 3:

    "123"
    "132"
    "213"
    "231"
    "312"
    "321"

Given n and k, return the kth permutation sequence.

Note:

- Given n will be between 1 and 9 inclusive.
- Given k will be between 1 and n! inclusive.

Example 1:

    Input: n = 3, k = 3
    Output: "213"

Example 2:

    Input: n = 4, k = 9
    Output: "2314"

## 题目大意

给出了一个数组[1,2,3,...,n]，求其全排列成一个数值，排序之后的第k个是多少。

## 解题方法

这个思路还是比较明朗的：我们先找出第一个数字是哪个，然后依次找其后的各个数字。写出来有点困难。。

完整的思路参考了[：\[LeetCode\] Permutation Sequence][1]这个博客。我没有想到可以直接求除法的结果以及余数，一直想着用减法，有点智障了。

同样先通过举例来获得更好的理解。以n = 4，k = 9为例：

    1234
    1243
    1324
    1342
    1423
    1432
    2134
    2143
    2314  <= k = 9
    2341
    2413
    2431
    3124
    3142
    3214
    3241
    3412
    3421
    4123
    4132
    4213
    4231
    4312
    4321

最高位可以取{1, 2, 3, 4}，而每个数重复3! = 6次。所以第k=9个permutation的s[0]为{1, 2, 3, 4}中的第9/6+1 = 2个数字s[0] = 2。

而对于以2开头的6个数字而言，k = 9是其中的第k' = 9%(3!) = 3个。而剩下的数字{1, 3, 4}的重复周期为2! = 2次。所以s[1]为{1, 3, 4}中的第k'/(2!)+1 = 2个，即s[1] = 3。

对于以23开头的2个数字而言，k = 9是其中的第k'' = k'%(2!) = 1个。剩下的数字{1, 4}的重复周期为1! = 1次。所以s[2] = 1.

对于以231开头的一个数字而言，k = 9是其中的第k''' = k''/(1!)+1 = 1个。s[3] = 4

那么我们就可以找出规律了:

a1 = k / (n - 1)!
k1 = k

a2 = k1 / (n - 2)!
k2 = k1 % (n - 2)!
...

an-1 = kn-2 / 1!
kn-1 = kn-2 % 1!

an = kn-1 / 0!
kn = kn-1 % 0!

代码如下：

```python
class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        ans = ''
        fact = [1] * n
        num = [str(i) for i in range(1, 10)]
        for i in range(1, n):
            fact[i] = fact[i - 1] * i
        k -= 1
        for i in range(n, 0, -1):
            first = k // fact[i - 1]
            k %= fact[i - 1]
            ans += num[first]
            num.pop(first)
        return ans
```

C++代码如下：

```cpp
class Solution {
public:
    string getPermutation(int n, int k) {
        string res;
        string num = "123456789";
        vector<int> f(n, 1);
        for (int i = 1; i < n; i++) f[i] = f[i - 1] * i;
        --k;
        for (int i = n; i >= 1; i--) {
            int j = k / f[i - 1];
            k %= f[i - 1];
            res.push_back(num[j]);
            num.erase(j, 1);
        }
        return res;
    }
};
```

参考资料：http://www.cnblogs.com/grandyang/p/4358678.html


## 日期

2018 年 6 月 11 日 —— 今天学科三在路上跑的飞快～
2018 年 12 月 22 日 —— 今天冬至

  [1]: http://bangbingsyb.blogspot.com/2014/11/leetcode-permutation-sequence.html
