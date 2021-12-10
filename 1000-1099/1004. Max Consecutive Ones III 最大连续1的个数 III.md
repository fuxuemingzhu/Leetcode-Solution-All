作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)


题目地址：https://leetcode.com/problems/max-consecutive-ones-iii/


## 题目描述

Given an array ``A`` of 0s and 1s, we may change up to ``K`` values from 0 to 1.

Return the length of the longest (contiguous) subarray that contains only 1s. 


Example 1:

    Input: A = [1,1,1,0,0,0,1,1,1,1,0], K = 2
    Output: 6
    Explanation: 
    [1,1,1,0,0,1,1,1,1,1,1]
    Bolded numbers were flipped from 0 to 1.  The longest subarray is underlined.

Example 2:

    Input: A = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], K = 3
    Output: 10
    Explanation: 
    [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
    Bolded numbers were flipped from 0 to 1.  The longest subarray is underlined.
 

Note:

1. ``1 <= A.length <= 20000``
1. ``0 <= K <= A.length``
1. ``A[i] is 0 or 1``


## 题目大意

数组A只包含有0和1，可以把其中的K个0翻转成1，问翻转之后最多能有多少个连续的1？


## 解题方法

### 虫取法/双指针

这个题最开始的想法是DP，但是没做出来。其实最简单的方法是虫取法或者叫做双指针。

[left, right]双闭区间表示一个经过一定次数的翻转后已经全部是1的区间。我们要求的长度就是这个区间的最大长度。我们需要把这个区间内的所有0都翻转成1，使用变量zero统计该区间内的被翻转的0的个数。易知，``zero <= K``.

我们把left和right的起始位置都设定为0，我们每次都向右移动一次right指针代表新判断一个元素。此时，如果right指向的数字是0，我们需要将zero+1，代表我们把这个0进行了翻转。然后我们就会想，如果翻转之后``zero > K``了怎么办？所以我们此时需要移动left指针啊！left有可能指向了1，所以需要一直移动直至``zero <= K``为止。

使用res保存最大区间长度即可。

那么为什么这个方法可行呢？

严格证明我不会，我只能说下我怎么理解这个方法。这个方法是常见的虫取法，这个虫取法的精髓是保证每次取到的区间是一个严格满足题目要求的区间。具体到这个题目来说就是维护了一个最多翻转K个0的全1区间。只要这个维护是有效的，那么我们就可以根据区间长度更新res。维护的过程我在上面已经讲解，核心是区间内统计0的个数，不过这个统计不是每次都遍历一次区间，而是使用一个变量，这个变量和区间同时维护即可。


C++代码如下：

```cpp
class Solution {
public:
    int longestOnes(vector<int>& A, int K) {
        int res = 0;
        int left = 0;
        int zero = 0;
        const int N = A.size();
        for (int right = 0; right < N; ++right) {
            if (A[right] == 0) 
                ++zero;
            while (zero > K) {
                if (A[left++] == 0)
                    --zero;
            }
            res = max(res, right - left + 1);
        }
        return res;
    }
};
```

## 日期

2019 年 3 月 3 日 —— 3月开始，春天到了


  [1]: https://blog.csdn.net/fuxuemingzhu/article/details/85227593
